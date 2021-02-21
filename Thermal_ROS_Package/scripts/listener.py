#!/usr/bin/env python

import sys
import numpy as np
import cv2
from pylepton import Lepton

import datetime

import roslib

import rospy


from std_msgs.msg import UInt8MultiArray
from rospy.numpy_msg import numpy_msg
from sensor_msgs.msg import Image

from cv_bridge import CvBridge



def callback(data):
    print('murad')
    g=CvBridge()
    current_date_time=str(datetime.datetime.now())
    current_date_time=current_date_time.split(' ');
    current_date=current_date_time[0].split('-');
    current_time=current_date_time[1].split(':');
    current_hours=current_time[0];
    current_minutes=current_time[1];
    current_seconds= str(round(float(current_time[2])));
    cv_image = g.imgmsg_to_cv2(data, "passthrough")
	

    cv2.imwrite(current_hours+ current_minutes +current_seconds+'.png', cv_image)
    cv2.imshow("Image window",cv_image)
    
#----------------Main Program-------------------
def listener():
    rospy.init_node('listener', anonymous=True)
    image_sub = rospy.Subscriber("chatter",Image,callback)
    rospy.spin()


listener()




