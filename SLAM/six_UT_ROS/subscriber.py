from __future__ import print_function
import time
import threading
import RPi.GPIO as GPIO

def measure():
    while(1):
        file = open("test3.csv", "a")
        print("`a` to trigger or type exit() to exit")
        

        #-------------FRONT SENSOR-------------
        global GPIO_TRIGGER
        global GPIO_ECHO
        GPIO_TRIGGER=24
        GPIO_ECHO = 23

        GPIO.setup(GPIO_ECHO,GPIO.IN)
        GPIO.output(GPIO_TRIGGER,True)
        time.sleep(0.001)
        GPIO.output(GPIO_TRIGGER,False)
           
        while GPIO.input(GPIO_ECHO)==0:
            start=time.time()
    
        while GPIO.input(GPIO_ECHO)==1:
            stop=time.time()
        
        
        elapsed = (stop-start)*100000
        print ('Distance in cm ' , elapsed)
        file.write('%r,' % elapsed)    
            
            #--------------FRONT RIGHT SENSOR-------------

        GPIO_TRIGGER=7
        GPIO_ECHO = 21
        GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
        GPIO.output(GPIO_TRIGGER,True)
        time.sleep(0.001)
        GPIO.output(GPIO_TRIGGER,False)
        GPIO.setup(GPIO_ECHO,GPIO.IN)
        while GPIO.input(GPIO_ECHO)==0:
            start=time.time()
    
        while GPIO.input(GPIO_ECHO)==1:
            stop=time.time()
        
        
        elapsed = (stop-start)*100000
        print ('Distance in cm ' , elapsed)
        file.write('%r,' % elapsed)

            #---------------RIGHT SENSOR----------------

        GPIO_TRIGGER=11
        GPIO_ECHO = 26
        GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
        GPIO.output(GPIO_TRIGGER,True)
        time.sleep(0.001)
        GPIO.output(GPIO_TRIGGER,False)
        GPIO.setup(GPIO_ECHO,GPIO.IN)
            
        while GPIO.input(GPIO_ECHO)==0:
            start=time.time()
    
        while GPIO.input(GPIO_ECHO)==1:
            stop=time.time()
        
        
        elapsed = (stop-start)*100000
        print ('Distance in cm ' , elapsed)
        file.write('%r,' % elapsed)

            #--------------BACK SENSOR-------------

        GPIO_TRIGGER=7
        GPIO_ECHO = 19

        GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
        GPIO.output(GPIO_TRIGGER,True)
        time.sleep(0.001)
        GPIO.output(GPIO_TRIGGER,False)
        GPIO.setup(GPIO_ECHO,GPIO.IN)
            
        while GPIO.input(GPIO_ECHO)==0:
            start=time.time()
    
        while GPIO.input(GPIO_ECHO)==1:
            stop=time.time()
        
        
        elapsed = (stop-start)*100000
        print ('Distance in cm ' , elapsed)
        file.write('%r,' % elapsed)

            #--------------LEFT SENSOR-------------

        GPIO_TRIGGER=7
        GPIO_ECHO = 17

        GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
        GPIO.output(GPIO_TRIGGER,True)
        time.sleep(0.001)
        GPIO.output(GPIO_TRIGGER,False)
        GPIO.setup(GPIO_ECHO,GPIO.IN)
            
        while GPIO.input(GPIO_ECHO)==0:
            start=time.time()
    
        while GPIO.input(GPIO_ECHO)==1:
            stop=time.time()
        
        
        elapsed = (stop-start)*100000
        print ('Distance in cm ' , elapsed)
        file.write('%r,' % elapsed)

            #--------------FRONT LEFT SENSOR-------------

        GPIO_TRIGGER=7
        GPIO_ECHO = 18

        GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
        GPIO.output(GPIO_TRIGGER,True)
        time.sleep(0.001)
        GPIO.output(GPIO_TRIGGER,False)
        GPIO.setup(GPIO_ECHO,GPIO.IN)
            
           
        while GPIO.input(GPIO_ECHO)==0:
            start=time.time()
    
        while GPIO.input(GPIO_ECHO)==1:
            stop=time.time()
        
        
        elapsed = (stop-start)*100000
        print ('Distance in cm ' , elapsed)
        file.write('%r\n' % elapsed)
            
    return

#------------Main Program-------------

GPIO.setmode(GPIO.BCM)
temperature = 20
print("Ultrasonic Measurement")

GPIO_TRIGGER= 24
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.output(GPIO_TRIGGER,False)

#-------------FRONT SENSOR-------------

file = open("test3.csv", "a")


measure()
file.close()
print('program closing')
GPIO.cleanup
