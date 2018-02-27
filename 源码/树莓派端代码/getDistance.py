import RPi.GPIO as GPIO
import time
def checkdist():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(38,GPIO.OUT,initial=GPIO.LOW)

	GPIO.setup(40,GPIO.IN)
        
        GPIO.output(38,GPIO.HIGH)
        
        time.sleep(0.000015)
        GPIO.output(38,GPIO.LOW)
        while not GPIO.input(40):
                pass
        
        t1 = time.time()
        while GPIO.input(40):
                pass
        
        t2 = time.time()
        
        return (t2-t1)*340/2
