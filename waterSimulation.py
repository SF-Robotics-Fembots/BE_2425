import random
import time

print("simulating water movement: ")

def randomPressure():
	num = random.uniform(19, 22)
	print("", num, "kPa")

while True:
	randomPressure()
	time.sleep(1)
