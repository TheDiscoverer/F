import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN)
GPIO.setup(13,GPIO.OUT)
p=0
flag=1
while 1:
	
	if  GPIO.input(7)==0 and flag==1:
		print p,
		flag=0
	if GPIO.input(7)==0 and flag==0:
		p=p+1
	if GPIO.input(7)==1 and flag==0:
		print p
		flag=1
	'''
	if GPIO.input(7)==0:
		GPIO.output(13,GPIO.HIGH)
	else:
		GPIO.output(13,GPIO.LOW)

'''
	

