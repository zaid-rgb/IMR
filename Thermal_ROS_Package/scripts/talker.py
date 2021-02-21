#!/usr/bin/env python

import sys
import numpy as np
import cv2
from pylepton import Lepton

import roslib
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import threading

def capture(flip_v = False, device = "/dev/spidev0.0"):
  threading.Timer(5,capture).start();
  with Lepton(device) as l:
    a,_ = l.capture()
  if flip_v:
    cv2.flip(a,0,a)
  cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX)
  np.right_shift(a, 8, a)
  image_captured = np.uint8(a)z

  pub=rospy.Publisher("chatter", Image , queue_size=10)
  rospy.init_node("talker", anonymous=True)
  rate = rospy.Rate(2)

  birdge=CvBridge();
  cv_image = birdge.cv2_to_imgmsg(image_captured, 'passthrough' );

  pub.publish(cv_image)
  rate.sleep()

image = capture()
