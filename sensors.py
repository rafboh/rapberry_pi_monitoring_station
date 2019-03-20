import sys

class Sensor():
	def __init__(self, io, line_in, line_out, gpio_mode = 'BCM', state = 'low'):
		self.line_in = line_in
		self.line_out = line_out
		self.io = io
		self.gpio_mode = gpio_mode
		self.state = state
		
	def init_sensor(self):
		self.io.setwarnings(False)
		if self.gpio_mode == 'BCM':
			self.io.setmode(self.io.BCM)
		elif self.gpio_mode == 'BOARD':
			self.io.setmode(self.io.BOARD)
		else:
			print('mode can be "BOARD" or "BCM"')
			sys.exit(0)
		print('sensor initiatlized: '+ str(self.line_in) + ' ; ' + str(self.line_out))
	
	def setup_channels(self):
		self.io.setup(self.line_in, self.io.IN)
		if self.state == 'high':
			self.io.setup(self.line_out, self.io.OUT, initial = self.io.HIGH)
		elif self.state == 'low':
			self.io.setup(self.line_out, self.io.OUT, initial = self.io.LOW)
		else:
			print ('sensor ' + str(self.line_in) + ' ; ' + str(self.line_out) + ' not initialized, state can be high or low, exiting')
			sys.exit(0)
		print(self.line_in, self.line_out)
		
	def cleanup_channels(self):
		self.io.cleanup()
		
	def read_line_in(self):
		return self.io.input(self.line_in)
	
	def set_line_out(self, channel, state):
		self.channel = channel
		self.state = state
		#print(channel, state)
		self.io.output(channel,state)
		
	def reset_channels_low(self):
		self.io.output(self.line_out, self.io.LOW)
	def reset_channels_high(self):
		self.io.output(self.line_out, self.io.HIGH)
		
class TemperatureSensor():
	def __init__(self, temperature_sensor):
		self.temperature_sensor = temperature_sensor
	
	def get_temp(self):
		print(self.temperature_sensor.get_temperature())
		

		
