#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
import time
from simple_pid import PID
import ms5837
import smbus
import datetime
import threading


TOP_SWITCH = 21
ROTATE_SWITCH = 6
SERVO_OFF = 7
SERVO_UP = 10
SERVO_DOWN = 4

SYRINGE_NEUTRAL = 40
SYRINGE_MAX = 47

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(ROTATE_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(TOP_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
p = GPIO.PWM(12, 50) # channel 12, 50Hz
p.start(SERVO_OFF) #motor_off

sensor = ms5837.MS5837_02BA(1)

# Stop Servo
p.start(SERVO_OFF)
time.sleep(1)

def startup():
	sensor.init()
	time.sleep(1)
	sensor.read(ms5837.OSR_256)
	sensor.setFluidDensity(ms5837.DENSITY_FRESHWATER)

#NEED TO EDIT
def Go_To_Top():
#code to turn on servo and fill syringe w water and stop it when switch (pin 20) is activated
        global position
        print("GoToTop\n")
        count=0

        if (GPIO.input(TOP_SWITCH) == 0):
                p.ChangeDutyCycle(SERVO_OFF)
                position=0

        while (GPIO.input(TOP_SWITCH) == 1):
#               print("rotate switch: ", GPIO.input(21))
                p.ChangeDutyCycle(SERVO_UP) #syringe up
                if (GPIO.input(ROTATE_SWITCH) == 0):
                        count+=1
                        print("Count = ", count)
                        while(GPIO.input(ROTATE_SWITCH) == 0):
                                if (GPIO.input(TOP_SWITCH) == 0):
                                        break
                time.sleep(0.5)
        p.ChangeDutyCycle(SERVO_OFF)
        position = 0
        print("top reached")

def Go_To_Pos(target_position):
#code to turn on servo and fill syringe w water and stop it when switch (pin 20) is activated
        global position
        print("starting position = ", position)
        if target_position < 0:
               target_position = 0
        if target_position > SYRINGE_MAX:
                target_position = SYRING_MEX
        move_amount = target_position - position
        if target_position == 0:
                Go_To_Top()
                return
        if move_amount > 0:
                p.ChangeDutyCycle(SERVO_DOWN)
                while (move_amount > 0):
                        if (GPIO.input(ROTATE_SWITCH) == 0):  #wait for click
                                move_amount-=1 #reduce remaining amount to move by 1 rotation
                                position+=1
                                print("New Position = ", position, "Move Amount = ", move_amount)
                                while(GPIO.input(ROTATE_SWITCH) == 0): #wait for unclick
                                       time.sleep(0.1)
                        time.sleep(0.3)
                p.ChangeDutyCycle(SERVO_OFF)

        if move_amount < 0:
                p.ChangeDutyCycle(SERVO_UP)
                while (move_amount < 0):
                        if (GPIO.input(ROTATE_SWITCH) == 0):
                                move_amount += 1
                                position-=1
                                print("New Position = ", position, "Move Amount = ", move_amount)
                                while(GPIO.input(ROTATE_SWITCH) == 0):
                                        time.sleep(0.5)
                p.ChangeDutyCycle(SERVO_OFF)

        print("position reached")
        return

def Go_To_Depth(target_depth):
	pid = PID(-0.002, -0.005, 0, setpoint = target_depth*100)
	pid.sample_time = 1
	print("Going to ", target_depth, "M")
	# Read first depth
	sensor.read(ms5837.OSR_256)
	depth = sensor.depth() * 100
	print("Depth = ", depth)
	pid_d = pid(depth)
	print("p: ", pid_d)
	syr_position = round(pid_d + SYRINGE_NEUTRAL, 0)
	while (1):
		print("going to pos: ", syr_position)
		Go_To_Pos(syr_position)
		time.sleep(0.1)
		sensor.read(ms5837.OSR_256)
		depth = sensor.depth() * 100
		pid_d = pid(depth)
		print("pid_d = ", pid_d)
		syr_position = round(pid_d + SYRINGE_NEUTRAL, 0)
		print("depth = ", depth, "syr_pos = ", syr_position)

def init_html():

        #ORIGINAL CODE FROM 2023-24 below
        print("Content-type:text/html\r\n\r\n")
        print("")
        print("Hello everyone")
        print("""<p><a href="http://192.168.42.10/index.php">Go_Back_to_Data</a></p>"""
)


if __name__ == "__main__":
	init_html()
	startup()
	Go_To_Top()
	Go_To_Pos(SYRINGE_MAX)
	inp = input("Press Enter to Continue")
	Go_To_Pos(SYRINGE_NEUTRAL)
	Go_To_Depth(1.5)
	GPIO.cleanup()

