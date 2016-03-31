#!/usr/bin/python2.7

import picamera
import time
import datetime

camera=picamera.PiCamera()
camera.resolution=(1920, 1080)
print "hellowworld"
camera.start_preview(fullscreen=False, window=(100,100,1000,1000))
while True:
	command = raw_input("")
	if command.rstrip() == "a":
		camera.hflip = not camera.hflip
	elif command.rstrip() == "q":
		camera.vflip = not camera.vflip
	elif command.rstrip() == "":
		name = "/home/pi/picture/%s.jpg" % datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%s")
		camera.capture(name)
