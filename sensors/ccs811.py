from Adafruit_CCS811 import Adafruit_CCS811

class CCS811:
	def read(self):
		try:
			ccs = Adafruit_CCS811()

			while not ccs.available():
				pass

			if ccs.available() and not ccs.readData():
				return [ccs.geteCO2(), ccs.getTVOC()]
			else:
				return [None, None]
		except OSError:
			return [None, None]
