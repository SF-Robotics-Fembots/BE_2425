#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(21, GPIO.IN)
GPIO.setup(7, GPIO.IN)
p = GPIO.PWM(12, 50) # channel 12, 50Hz
p.start(7)
time.sleep(1)
#things to remember: 90 stops, 120 is dive and fill w water, 30 is resurface! 


def init_html():

        #ORIGINAL CODE FROM 2023-24 below
        print("Content-type:text/html\r\n\r\n")
        print("")
        print("Hello everyone")
        print("""<p><a href="http://192.168.42.10/index.php">Go_Back_to_Data</a></p>"""
)


if __name__ == "__main__":
#	init_html()
	inval=7
	while(inval!=999):
		inval=int(input())
		p.ChangeDutyCycle(inval)
	p.stop()
	GPIO.cleanup()

