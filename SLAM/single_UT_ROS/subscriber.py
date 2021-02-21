#!/usr/bin/env python
from __future__ import print_function
import time
import RPi.GPIO as GPIO

import sys
import rospy
import roslib
from std_msgs.msg import Float64



def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    file = open("test3.txt", "a")
    elapsed=data.data
    file.write('%r\n' % (elapsed))
    file.close()

#------------Main Program-------------
rospy.init('ultranode_list', anonymous = True)
rospy.Subscriber("distance",Float64, callback)
rospy.spin()
