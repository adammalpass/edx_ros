#!/usr/bin/env python  
import rospy

from std_msgs.msg import Int16
from project1_solution.msg import TwoInts

pub = rospy.Publisher('sum', Int16, queue_size = 20)        

def callback(data):
   # rospy.loginfo(str(rospy.get_caller_id()) + " Received: "+ str(data.a) + " " + str(data.b))
    pub.publish(data.a + data.b)

def listener_talker():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("two_ints", TwoInts, callback)
   
    rospy.spin()


if __name__ == '__main__':
    listener_talker()
