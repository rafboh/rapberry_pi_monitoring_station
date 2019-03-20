from camera import Camera
import time



def make_photo(settings):
	camera = Camera(settings)
	camera.set_camera()
	time.sleep(2)
	for i in range(0, settings.number_photos):
		camera.make_photo()
		time.sleep(1)
	camera.close_camera()	
	

#def make_movie(camera):

def setup_sensors(sensors):
	for i in sensors:
		i.init_sensor()
		i.setup_channels()

def measure_distance(USsensor, settings):
	USsensor.set_line_out(settings.USsensor_line_out, True)
	time.sleep(0.00001)
	USsensor.set_line_out(settings.USsensor_line_out, False)
	
	
	while USsensor.read_line_in() == False:
		start_time = time.time()
	while USsensor.read_line_in() == True:
		stop_time = time.time()
	
	travel_time = stop_time - start_time
	distance = (travel_time*34300) / 2
	return distance

def check_time(start_time, settings, PIR_alert_no, in_range):
	
	if time.time()-start_time <= settings.cycle_photo_time:
		in_range = True
	elif time.time() - start_time > settings.time_with_no_action:
		in_range = True
		PIR_alert_no = 0		
	else:
		in_range = False
	return in_range, PIR_alert_no
	
