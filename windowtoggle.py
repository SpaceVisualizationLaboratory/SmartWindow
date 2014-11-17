import RPi.GPIO as GPIO
import time
from subprocess import *
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(24,GPIO.IN)
pauseTime=10
movieList=['/home/pi/Movies/CosmicWeb_43.mov','/home/pi/Movies/Herschel_43.mov','/home/pi/Movies/CARMA_43.mov','/home/pi/Movies/Sundial_43.mov','/home/pi/Movies/Streams_43.mov']
iMovie=0
playingState = False
GPIO.output(25,GPIO.HIGH)
while True:
        while playingState:
		if (GPIO.input(24)==True):
			GPIO.output(25,GPIO.LOW)
			call(['omxplayer',movieList[iMovie]])
			iMovie=iMovie+1
			iMovie=iMovie % len(movieList)     
 			call('clear')
			playingState = False
		time.sleep(0.5)
        GPIO.output(25,GPIO.HIGH)
        call('clear')
        time.sleep(pauseTime)
	playingState=True
