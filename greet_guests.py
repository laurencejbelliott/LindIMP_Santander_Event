#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from mary_tts.msg import maryttsActionGoal


speakPub = rospy.Publisher("speak/goal", maryttsActionGoal, queue_size=1)


def callback(data):
    greetStr = "Hello, and welcome to the Santanderr celebratory event!"
    greetMsg = maryttsActionGoal()
    greetMsg.goal.text = greetStr
    speakPub.publish(greetMsg)
    print("Nearby person greeted with: \"" + greetStr + "\"")
    # time until another greeting allowed, in seconds
    wait_time = 7
    print("Waiting for " + str(wait_time) + " seconds before next greeting allowed...\n")
    rospy.sleep(wait_time)


def listener():
    rospy.init_node('greet_guests', anonymous=False)

    rospy.Subscriber("people_tracker/pose", PoseStamped, callback, queue_size=1)

    rospy.spin()


if __name__ == "__main__":
    listener()
