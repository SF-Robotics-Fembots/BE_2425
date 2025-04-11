#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
import time

TOP_SWITCH = 6
ROTATE_SWITCH = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
p = GPIO.PWM(12, 50) # channel 12, 50Hz
p.start(7)

#time.sleep(1)
#things to remember: 90 stops, 120 is dive and fill w water, 30 is resurface! 
#7 is stop, 6 the syring goes down, 11 syringe goes up

#position = 9999

'''def read_rotations():
	p.ChangeDutyCycle(3)
	counter = 0
	while (1):
		#y = GPIO.input(6)
		#x = GPIO.input(21)

#		print("switch value: ", y, " ", x)
		if (GPIO.input(ROTATE_SWITCH) == 0):
			time.sleep(0.05)
			counter += 1
			print("rotation: ", counter)
#			y = 1
#			break
			while (GPIO.input(6) == 0):
				time.sleep(0.05)
'''
'''
def test():
	global position
	print("123")
	p.ChangeDutyCycle(11)
	print("222")
'''
def goAng():
	global position
	position = 999
	print("GoToTop\n")
	count=0
	print("count=", count)
	print("1111")
	while(1):
		p.ChangeDutyCycle(6)
		print("333")
	if(0):	
		while(GPIO.input(ROTATE_SWITCH) == 0):
                        print("222")
                        p.ChangeDutyCycle(6)
                      
 
		if(GPIO.input(ROTATE_SWITCH) == 1):
			count+=1
			print("count=", count)

		if (GPIO.input(TOP_SWITCH) == 1):
			p.ChangeDutyCycle(6)
			position=0

def goToTop():
	global position
#	print("GoToTop\n")
#	p.ChangeDutyCycle(11)
	p.ChangeDutyCycle(4)
	count=0
	if(GPIO.input(ROTATE_SWITCH) == 1):
		count+=1
#		print("count=", count)

	if (GPIO.input(TOP_SWITCH) == 0):
		p.ChangeDutyCycle(7)
		position=0

	while (GPIO.input(TOP_SWITCH) == 1):
#		print("rotate switch: ", GPIO.input(21))
		if (GPIO.input(ROTATE_SWITCH) == 0):
			count+=1
#			print("Count = ", count)
			while(GPIO.input(ROTATE_SWITCH) == 0):
				time.sleep(0.05)
	
	position = 0
	print("current_position = ", position)
	p.ChangeDutyCycle(7)

#changed from position to current_position - 3/22

def goTo(target_position):
	global current_position
	#goToTop()
	while True: 
		global current_position
		global position
		print("111")
		position = input()
		print(type(position))
		position = int(position)
		print(type(position))
		print("222")
		move_amount = target_position - position
		if target_position < 0:
			print("Can not move to position less than zero")
			return
		if target_position == 0:
			goToTop()
			current_position = 0
			return
		if move_amount > position: #was 0
			p.ChangeDutyCycle(4)
			if (move_amount > position): #was 0
				if (GPIO.input(ROTATE_SWITCH) == 0):  #wait for click
					move_amount-=1 #reduce remaining amount to move by 1 rotation
					position+=1
					print("New Position = ", position, "Move Amount = ", move_amount)
					while(GPIO.input(ROTATE_SWITCH) == 0): #wait for unclick
						time.sleep(0.05)
			return position
			p.ChangeDutyCycle(7)

		if move_amount < position: #was 0
			p.ChangeDutyCycle(10)
			if (move_amount < position): #was 0
				if (GPIO.input(ROTATE_SWITCH) == 0):
					move_amount += 1
					position-=1
					print("New Position = ", position, "Move Amount = ", move_amount)
					while(GPIO.input(ROTATE_SWITCH) == 0):
						time.sleep(0.05)
			return position
			p.ChangeDutyCycle(7)
		
		#print("position reached")

if __name__ == "__main__":
	#print("333")
#	read_rotations()	
	goToTop()
	#target_position = 40
	#position = 50
#	target_position = int(input())
#	goTo(target_position)
