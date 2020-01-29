#!/usr/bin/env python
import rospy, actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from mary_tts.msg import maryttsActionGoal


speakPub = rospy.Publisher("speak/goal", maryttsActionGoal, queue_size=1)
goodbyeMsg = maryttsActionGoal()
goodbyeText = "Please take a pen to sign the Santanderr contract!"
goodbyeMsg.goal.text = goodbyeText


def pass_pen():
    client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    client.wait_for_server()
    print("Move_base server ready!")

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = -8.39071083069
    goal.target_pose.pose.position.y = 9.36499023438

    goal.target_pose.pose.orientation.z = 0.464598051694
    goal.target_pose.pose.orientation.z = 0.885521682604

    client.send_goal(goal)
    print("Goal sent")
    client.wait_for_result()
    result = client.get_goal_status_text()
    print(result)
    if result == "Goal reached.":
        speakPub.publish(goodbyeMsg)
        print(goodbyeText)

    rospy.spin()


if __name__ == "__main__":
    rospy.init_node("pass_pen")
    pass_pen()
