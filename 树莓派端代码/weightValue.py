'''
import RPi.GPIO as GPIO
import time
def getweightValue():
	GPIO.setwarnings(False) 
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(31,GPIO.IN)
#	GPIO.output(11,GPIO.HIGH)
	GPIO.setup(29,GPIO.OUT)		#DT   ADD0
	GPIO.output(29,GPIO.LOW)	#SCK
	count=0
	while GPIO.input(31):
		pass
	for i in range(24):
		GPIO.output(29,GPIO.HIGH)
		count=count<<1
		GPIO.output(29,GPIO.LOW)
		if GPIO.input(31):
			count=count+1
	GPIO.output(29,GPIO.HIGH)
	count=count^0x800000
	GPIO.output(29,GPIO.LOW)
	return (count/100-83221)*113/454-25
'''
import RPi.GPIO as GPIO
import time
import urllib
import urllib2
def getweightValue():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(31,GPIO.IN)
#       GPIO.output(11,GPIO.HIGH)
        GPIO.setup(29,GPIO.OUT)         #DT   ADD0
        GPIO.output(29,GPIO.LOW)        #SCK
        count=0
        while GPIO.input(31):
                pass
        for i in range(24):
                GPIO.output(29,GPIO.HIGH)
                count=count<<1
                GPIO.output(29,GPIO.LOW)
                if GPIO.input(31):
                        count=count+1
        GPIO.output(29,GPIO.HIGH)
        count=count^0x800000
        GPIO.output(29,GPIO.LOW)
       # w=(count/100-83221)*113/454;
        w=(count/100-83309)*113/458-25+16
	return w
