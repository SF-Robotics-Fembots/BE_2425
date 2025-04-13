import Adafruit_MCP3008
from gpiozero import MCP3008

def get_battery():
	pot = MCP3008(0)
	new_val = pot.value*6.6
	print(new_val)
	return new_val


get_battery()


