#!/usr/bin/python3
import rospy
import bsn_core.functions as fc
from std_msgs.msg import String


def callback(data):
    print("callback test", data.data)


def main():
    global pub
    rospy.init_node("bsn_handler", anonymous=None)
    rospy.Subscriber("input", String, callback)
    pub = rospy.Publisher("output", String, queue_size=100)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        print("==============================START==============================")
        pre_condition = fc.check_param("/pre_condition")
        print("Pre_condition :", pre_condition)
        completion = fc.check_goal(pre_condition)
        print("Completion :", completion)
        if completion is True:
            rospy.signal_shutdown("Goal Complete")
            print("===============================END===============================")

        behavior = fc.do_behavior(pre_condition)
        print("Behavior :", behavior)
        fc.add_list(behavior)
        fc.delete_list(behavior)

        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
