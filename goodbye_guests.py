#!/usr/bin/env python
import rospy, random
from geometry_msgs.msg import PoseStamped
from mary_tts.msg import maryttsActionGoal


speakPub = rospy.Publisher("speak/goal", maryttsActionGoal, queue_size=1)


def callback(data):
    goodbyeStrs = [
        "Thank you for attending! We hope you have enjoyed the celebration!",
        "Goodbye! Thank you for coming!"
    ]
    goodbyeMsg = maryttsActionGoal()
    goodbyeStr = goodbyeStrs[random.randrange(0, len(goodbyeStrs))]
    goodbyeMsg.goal.text = goodbyeStr
    speakPub.publish(goodbyeMsg)
    print("Nearby person greeted with: \"" + goodbyeStr + "\"")
    # time until another greeting allowed, in seconds
    wait_time = 7
    print("Waiting for " + str(wait_time) + " seconds before next greeting allowed...\n")
    rospy.sleep(wait_time)


def listener():
    rospy.init_node('goodbye_guests', anonymous=False)

    rospy.Subscriber("people_tracker/pose", PoseStamped, callback, queue_size=1)

    rospy.spin()


if __name__ == "__main__":
    listener()
