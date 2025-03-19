#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(21, GPIO.IN)
p = GPIO.PWM(12, 50) # channel 12, 50Hz
p.start(2.1)
time.sleep(1)
#things to remember: 90 stops, 120 is dive and fill w water, 30 is resurface! 


def godive():
#code to turn on servo and fill syringe w water and stop it when switch (pin 20) is activated
	angle = 120
	print("Angle", angle)
	duty = float(angle) / 18 + 2
	print ("duty", duty)
	print("Duty", duty)
	p.ChangeDutyCycle(duty)
	while (1):
		#value=int(input('Enter_an_integer')
		#p = GPIO.PWM(12, value)
		x = GPIO.input(21)
		print("godive x = ", x)
		if (x == 0):
			angle = 90
			print("i was pressed!")
			break  # Exit the loop to prevent continuous execution
			time.sleep(3)
'''
		print("Angle", angle)
		#duty = float(angle) / 18 + 2
		duty=2
		print ("******8 duty = ", duty)
		p.ChangeDutyCycle(duty)
		time.sleep(1)
'''

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

def trythree():
#simple code to run servo one direction, stop, and reverse
# angie's changes: keeps going bcuz of the loop
	'''while(True):
		angle = 120
		print("Angle", angle)
		duty = float(angle) / 18 + 2
		print ("duty", duty)
		p.ChangeDutyCycle(duty)
		time.sleep(30)
		print ("1")	
	
	#reverse
	'''
	angle = 90
	print("Angle", angle)
	duty = float(angle) / 18 + 2
	print ("duty", duty)
	p.ChangeDutyCycle(duty)
	time.sleep(2)
	print ("3")

	angle = 120
	print("Angle", angle)
	duty = float(angle) / 18 + 2
	print ("duty", duty)
	p.ChangeDutyCycle(duty)
	time.sleep(60)
	print ("3")

	angle = 90
	print("Angle", angle)
	duty = float(angle) / 18 + 2
	print ("duty", duty)
	p.ChangeDutyCycle(duty)
	time.sleep(2)
	print ("4")

def tryzero():
	print("1")
	for angle in range (2, 180):
                print("Angle", angle)
                duty = float(angle) / 18 + 2
                print ("duty", duty)
                p.ChangeDutyCycle(duty)
                time.sleep(3)

def tryone(val):
	print("2")
	print("Val ", val)
	duty = (float(val) / 18) + 2
	p.ChangeDutyCycle(duty)

if(0):
	print("3")
	p.ChangeDutyCycle(0)

def spinme():
	print("4")
	for duty in range (0,180):
		print(duty)
		p.ChangeDutyCycle(duty)
		time.sleep(2)

try:
	print("Starting")
	while(1):
		value=int(input("Duty Cycle"))
		print(value)
		p.ChangeDutyCycle(value)

finally:
        p.stop()
        GPIO.cleanup()

if __name__ == "__main__":
	3 > 2
	godive()
	#goup()
	if(0):
		print("6")
		time.sleep(3)
		p.ChangeDutyCycle(0)
		GPIO.cleanup()
