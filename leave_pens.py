#!/usr/bin/env python
import rospy, actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


def leave_pens():
    client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    client.wait_for_server()
    print("Move_base server ready!")

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = 5.70100021362
    goal.target_pose.pose.position.y = -2.89500021935

    goal.target_pose.pose.orientation.z = -0.966442346438
    goal.target_pose.pose.orientation.w = 0.256883613747

    client.send_goal(goal)
    print("Goal sent")
    client.wait_for_result()
    result = client.get_goal_status_text()
    print(result)


if __name__ == "__main__":
    rospy.init_node("leave_pens")
    leave_pens()
