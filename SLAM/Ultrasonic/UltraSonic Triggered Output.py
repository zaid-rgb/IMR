from __future__ import print_function
import time
import RPi.GPIO as GPIO

def measure():
    while(1):
     
        GPIO.output(GPIO_TRIGGER,True)
        time.sleep(0.001)
        GPIO.output(GPIO_TRIGGER,False)
           

        while GPIO.input(GPIO_ECHO)==0:
            start=time.time()
    
        while GPIO.input(GPIO_ECHO)==1:
            stop=time.time()
        
        
        elapsed = (stop-start)*100000
        print ('Distance in cm ' , elapsed)
        elapsed = str(elapsed)
        a= type(elapsed)
        print (a)
        file.write('%r\n' % (elapsed))
    return

    

#------------Main Program-------------

GPIO.setmode(GPIO.BCM)
temperature = 20
speedSound = (33100)+(0.6*temperature)
print("Ultrasonic Measurement")
print(speedSound)

#-------------FRONT SENSOR-------------
GPIO_TRIGGER=24
GPIO_ECHO = 23

GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)

GPIO.output(GPIO_TRIGGER,False)
file = open("test3.txt", "a")


measure()
file.close()
GPIO.cleanup
