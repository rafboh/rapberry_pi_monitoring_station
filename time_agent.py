import time

class TimeAgent():
	def __init__(self, settings):
		self.PIR_alert_no = 0
		self.settings = settings
		
	def start_series(self):
		if self.PIR_alert_no == 1:
			self.start_time = time.time()
		
	def increment_alert_no(self):
		self.PIR_alert_no += 1
		
	def check_range(self):
		if time.time()-self.start_time <= self.settings.cycle_photo_time:
			self.in_range = True
		elif time.time() - self.start_time > self.settings.time_with_no_action:
			self.in_range = True
			self.PIR_alert_no = 0		
		else:
			self.in_range = False
	
