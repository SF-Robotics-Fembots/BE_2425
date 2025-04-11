#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
import time
from simple_pid import PID

TOP_SWITCH = 6
ROTATE_SWITCH = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
p = GPIO.PWM(12, 50) # channel 12, 50Hz
p.start(7)
time.sleep(1)
#things to remember: 90 stops, 120 is dive and fill w water, 30 is resurface! 

position = 9999

#k values respective to p, i, and d
#setpoint=target
pid = PID(1, 0.1, 0.05, setpoint=250)
#system we want to control (motor)
#depth = goTo() #0 should be neutrally bouyant

def goToTop():
	global position
	count=0
	if (GPIO.input(TOP_SWITCH) == 1):
		p.ChangeDutyCycle(10)
		position=0
	while (GPIO.input(TOP_SWITCH) == 1):
		if (GPIO.input(ROTATE_SWITCH) == 0):
			count+=1
			print("Count = ", count)
			while(GPIO.input(ROTATE_SWITCH) == 0):
				time.sleep(0.05)
	p.ChangeDutyCycle(7)
	position = 0
	print("top reached")


def goTo():
	#global position
	target_position = 10
	current_position = 6
	print("current_position = ", current_position, " target_position=", target_position)
	if target_position < 0:
		print("Can not move to position less than zero")
		return
	move_amount = target_position - current_position
	if target_position == 0:
		goToTop()
		return
	if move_amount > 0:
		p.ChangeDutyCycle(4)
		while (move_amount > 0):
			if (GPIO.input(ROTATE_SWITCH) == 0):  #wait for click
				move_amount -= 1 #reduce remaining amount to move by 1 rotation
				#current_position +=1
				current_position = input("current position?")
				move_amount = target_position - int(current_position)
				print("current_position = ", current_position, "Move Amount = ", move_amount)
				if move_amount == 0:
					break

				'''while(GPIO.input(ROTATE_SWITCH) == 0): #wait for unclick
					time.sleep(0.05)
		'''
		p.ChangeDutyCycle(7)

	if move_amount < 0:
		p.ChangeDutyCycle(10)
		while (move_amount < 0):
			if (GPIO.input(ROTATE_SWITCH) == 0):
				move_amount += 1
				position-=1
				print("Position = ", position, "Move Amount = ", move_amount)
				while(GPIO.input(ROTATE_SWITCH) == 0):
					time.sleep(0.05)
		p.ChangeDutyCycle(7)

	print("position reached")


while True:
#	#compute new output from PID according to the systems current value
	depth = goTo()
	control = pid(depth)
	
	#feed pid output to system and get its current value
	depth = goTo(control, target_position)

#if __name__ == "__main__":
	#goToTop()
	#input current_position
	#goTo(int(input()))
#	goTo()
