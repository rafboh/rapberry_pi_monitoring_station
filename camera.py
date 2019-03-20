import picamera
import time

class Camera():
	def __init__(self,settings):
		self.settings = settings
		self.camera = picamera.PiCamera()
		
	def set_camera(self):
		self.camera.resolution = self.settings.camera_resolution
	def make_photo (self):
		self.file_name = 'images/img-'+time.strftime("%Y%m%d-%H%M%S")+'.jpg'
		self.camera.capture(self.file_name)
	def close_camera(self):
		self.camera.close()
