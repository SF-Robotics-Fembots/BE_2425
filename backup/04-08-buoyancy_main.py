#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
import time


p = GPIO.PWM(12, 50) # channel 12, 50Hz
p.start(SERVO_OFF) #motor_off

#switched
Pin_Top_Sensor=6
Pin_Rotation_Sensor=21
Pin_Servo=12

Servo_Stop = 7
Servo_Up = 10
Servo_Down = 4

Position_Max = 27

#Setup GPIOs and PWM
GPIO.setmode(GPIO.BCM)
GPIO.setup(Pin_Top_Sensor, GPIO.IN)

GPIO.setup(Pin_Servo, GPIO.OUT)
GPIO.setup(Pin_Rotation_Sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Pin_Top_Sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
p = GPIO.PWM(Pin_Servo, 50) # channel 12, 50Hz

# Stop Servo
p.start(Servo_Stop)
time.sleep(1)

#NEED TO EDIT
def godive():
#code to turn on servo and fill syringe w water and stop it when switch (pin 20) is activated
	#4 -> godive, 7=stop, 
	p.ChangeDutyCycle(6)
	count = 0	
	while (1):
		x = GPIO.input(Pin_Top_Sensor)
#		print("godive x = ", x)
		#s = GPIO.input(Pin_Rotation_Sensor)
		#count =+1
		#s = 0
		#print("count:", count)
		if (x == 0):
			p.ChangeDutyCycle(7)
			print("top reached")
			break  # Exit the loop to prevent continuous execution


def read_rotations():
	p.ChangeDutyCycle(4)
	while (1):
		y = GPIO.input(7)
		if (y == 0):
			print("rotation completed")
			break

def dive_test():
#code to turn on servo and fill syringe w water and stop it when switch (pin 20) is activated
	val=input();
	print("Value: ", val);
	duty = float(angle) / 18 + 2
	print ("duty", duty)
	p.ChangeDutyCycle(duty)
	while (1):
		x = GPIO.input(21)
		print("x = ", x)
		if (x == 0):
			angle = 90
		else:
			angle = 180 
		print("Angle", angle)
		duty = float(angle) / 18 + 2
		print ("duty", duty)
		p.ChangeDutyCycle(duty)
		time.sleep(1)



def goup():
#code to turn on servo and expel water and stop it when switch (pin 20) is activated
        angle = 50
        print("Angle", angle)
        duty = float(angle) / 18 + 2
        print ("duty", duty)
        p.ChangeDutyCycle(duty)
        while (1):
                x = GPIO.input(21)
                print("go up x = ", x)
                if (x == 0):
                        angle = 90
                else:
                        angle = 50
                print("Angle", angle)
                duty = float(angle) / 18 + 2
                print ("duty", duty)
                p.ChangeDutyCycle(duty)
                time.sleep(1)

def init_html():

        #ORIGINAL CODE FROM 2023-24 below
        print("Content-type:text/html\r\n\r\n")
        print("")
        print("Hello everyone")
        print("""<p><a href="http://192.168.42.10/index.php">Go_Back_to_Data</a></p>"""
)


if __name__ == "__main__":
	init_html()
	godive()
	#read_rotations()
	p.stop()
	GPIO.cleanup()

