import board
import busio
import adafruit_ccs811

class CCS811:
	def read(self):
		i2c = busio.I2C(board.SCL, board.SDA)
		ccs811 = adafruit_ccs811.CCS811(i2c)

		if not ccs811.data_ready:
			return None
		return [ccs811.eco2, ccs811.tvoc]