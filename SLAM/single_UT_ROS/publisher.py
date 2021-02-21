#!/usr/bin/env python
from __future__ import print_function
import time
import RPi.GPIO as GPIO

import sys
import rospy
import roslib
from std_msgs.msg import Float64

def measure():
    while(1):
        print("`a` to trigger or type exit() to exit")
        a = input()
        if( a== 'a'):
            
            GPIO.output(GPIO_TRIGGER,True)
            time.sleep(0.001)
            GPIO.output(GPIO_TRIGGER,False)
           

            while GPIO.input(GPIO_ECHO)==0:
                start=time.time()
    
            while GPIO.input(GPIO_ECHO)==1:
                stop=time.time()

            pub=rospy.Publisher("distance",Float64, queue_size=10)
            rospy.init_node("ultranode", anonymous=True)
            
        
            elapsed = (stop-start)*100000
            print ('Distance in cm ' , elapsed)
            
            pub.publish(distance)
            
        elif(a=='exit()'):
            break
        else:
            print('you entered an invalid number')
    
    return

    

#------------Main Program-------------

GPIO.setmode(GPIO.BCM)
temperature = 20

print("Ultrasonic Measurement")


#-------------FRONT SENSOR-------------
GPIO_TRIGGER=24
GPIO_ECHO = 23

GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)

GPIO.output(GPIO_TRIGGER,False)

measure()
GPIO.cleanup
