#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# a = rospy.get_param('/bsn_handler/pre-condition/clear-C')
# rospy.set_param('/bsn_handler/pre-condition/clear-C', 1)


def add_list():
    print("")

def delete_list():
    print("")

def do_behavior():
    print("")


def callback(data):
    jsonDict = json.loads(data.data)
    jsonString = json.dumps(jsonDict, ensure_ascii=False, indent=4)
    pub.publish(jsonString)


def main():
    global pub
    rospy.init_node('bsn_handler22', anonymous=None)
    rospy.Subscriber("input22", String, callback)
    pub = rospy.Publisher('output22', String, queue_size=100)
    a = rospy.get_param('/bsn_handler/pre-condition/clear-C')
    print(a)
    rospy.spin()

main()