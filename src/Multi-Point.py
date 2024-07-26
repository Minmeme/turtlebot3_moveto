#!/usr/bin/env python

import rospy
import actionlib
import time
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Twist
from servo import ServoController

def move_to_goal(x, y, linear_speed=0.2, angular_speed=0.2):
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.w = 1.0

    client.send_goal(goal)

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    while not client.wait_for_result(rospy.Duration.from_sec(0.1)):
        twist = Twist()
        twist.linear.x = linear_speed
        twist.angular.z = angular_speed
        pub.publish(twist)
        rate.sleep()

    return client.get_result()

def point(x, y, linear_speed=0.2, angular_speed=0.2):
    result = move_to_goal(x, y, linear_speed, angular_speed)
    if result:
        rospy.loginfo(f"Reached goal at ({x}, {y})")
    else:
        rospy.loginfo(f"Failed to reach goal at ({x}, {y})")

if __name__ == '__main__':
    try:
        rospy.init_node('multi_point_navigation', anonymous=True)
        
        # Initialize servo controller
        servo_controller = ServoController()

        # Execute navigation points (uncomment to use)
        # point(5.0451, 0.1524)
        # point(5.0346, 0.5168)

        # Control the servo motor


        ######## Servo #########
        # set up
        # servo_controller.set_servo_angle(14, 10)
        # time.sleep(1)
        # servo_controller.set_servo_angle(15, 0)
        # time.sleep(2)

        # put
        # servo_controller.set_servo_angle(15, 150)
        # time.sleep(2)
        # servo_controller.set_servo_angle(14, 180)
        # time.sleep(1)
        ######## Servo #########

        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
    finally:
        # Deinitialize servo controller
        servo_controller.deinit()
