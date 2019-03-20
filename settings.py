class Settings():
	def __init__(self):
		self.camera_resolution = (1280,720)
		self.camera_mode = ('photo','movie')
		self.PIRsensor_line_out =(27)
		self.PIRsensor_line_in = 17
		self.USsensor_line_out =(18) #trigger
		self.USsensor_line_in = 24 #echo
		self.gpio_mode = 'BCM'
		self.number_photos = 2 #number of photos done in one series
		self.ultrasound_distance_trigger = 10 #distance triggering action in cm
		self.cycle_photo_time = 15 #cycle time during which photos are done in seconds
		self.time_with_no_action = 60
