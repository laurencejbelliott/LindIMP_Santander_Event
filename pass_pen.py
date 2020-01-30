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
    goal.target_pose.pose.position.x = 3.36976957321
    goal.target_pose.pose.position.y = 4.25985527039

    goal.target_pose.pose.orientation.z = 0.296989783605
    goal.target_pose.pose.orientation.w = 0.954880656645

    client.send_goal(goal)
    print("Goal sent")
    client.wait_for_result()
    result = client.get_goal_status_text()
    print(result)
    if result == "Goal reached.":
        speakPub.publish(goodbyeMsg)
        print(goodbyeText)


if __name__ == "__main__":
    rospy.init_node("pass_pen")
    pass_pen()
