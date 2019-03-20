import RPi.GPIO as io
from sensors import *
import time
import w1thermsensor as ts
import picamera as cam
from settings import Settings
from sensor_functions import *
from time_agent import TimeAgent

settings = Settings()
scans_active = True

PIRsensor = Sensor(io, settings.PIRsensor_line_in, settings.PIRsensor_line_out, settings.gpio_mode, 'low')
USsensor = Sensor(io, settings.USsensor_line_in, settings.USsensor_line_out, settings.gpio_mode, 'low')
sensors = (PIRsensor, USsensor)
setup_sensors(sensors)
temp_sensor = TemperatureSensor(ts.W1ThermSensor())
timeagent = TimeAgent(settings)



while scans_active:
	try:
		#body sensor scan
		if PIRsensor.read_line_in():
			timeagent.increment_alert_no()
			timeagent.start_series()
			PIRsensor.set_line_out(settings.PIRsensor_line_out, True)
			timeagent.check_range()
			if timeagent.in_range:
				make_photo(settings)
			else:
				time.sleep(1)
			PIRsensor.set_line_out(settings.PIRsensor_line_out, False)		
		
		#print temperature
		temp_sensor.get_temp()
		print('distance = %.1f cm' % measure_distance(USsensor, settings))
		if measure_distance(USsensor, settings) < settings.ultrasound_distance_trigger:
			make_photo(settings)
			
		
			
	
	
	
	
	
	
	
	
	
	
	except KeyboardInterrupt:
		scans_active = False
		io.cleanup()
		break





#temperature sensor scan

#door contact scan


#voice scan

#if presence detected camera scan

#if camera registers motion alert message

"""
	IFsensor.set_line_out(2, True)
	#IFsensor.set_line_out_on()
	IFsensor.set_line_out(3, 0)
	print(IFsensor.read_line_in())
	if IFsensor.read_line_in():
		print('motion')
	#print(i)
	temp_sensor.get_temp()
	time.sleep(0.3)
	IFsensor.set_line_out(2, False)
	#IFsensor.set_line_out_off()
	IFsensor.set_line_out(3, 1)
	time.sleep(0.3)
#IFsensor.set_line_out(2, 0)
IFsensor.cleanup_channels()
"""
