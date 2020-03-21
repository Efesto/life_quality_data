import Adafruit_CCS811
import RPi.GPIO as GPIO

class CCS811:
	def read(self):
		ccs =  Adafruit_CCS811()
		temp = ccs.calculateTemperature()
		ccs.tempOffset = temp - 25.0

		if not ccs.readData():
			return [ccs.geteCO2(), ccs.getTVOC(), temp]
		else:
			return [-1, -1, temp]