#!/usr/bin/python3

import rospy
import actionlib
import time
from actionlib_msgs.msg import GoalStatus
from geometry_msgs.msg import PoseWithCovarianceStamped, Pose, Point, Quaternion
from move_base_msgs.msg import MoveBaseGoal, MoveBaseAction
import tf.transformations

import board
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo


class MoveBaseActionClient:
    def __init__(self):
        rospy.loginfo("Wait for amcl")
        rospy.wait_for_message('/amcl_pose', PoseWithCovarianceStamped)
        rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, self.amcl_callback)
        self.move_base_action = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
        self.move_base_action.wait_for_server(rospy.Duration(5))

    def amcl_callback(self, msg):
        robot_pose = msg.pose.pose
        robot_theta = tf.transformations.euler_from_quaternion(
            (robot_pose.orientation.x, robot_pose.orientation.y, robot_pose.orientation.z, robot_pose.orientation.w)
        )
        rospy.loginfo(f"Robot Pose=> x:{robot_pose.position.x} y:{robot_pose.position.y} theta:{robot_theta[2]}")

    def create_goal(self, x: float, y: float, theta: float):
        quat = tf.transformations.quaternion_from_euler(0, 0, theta)
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = Pose(Point(x, y, 0.0), Quaternion(quat[0], quat[1], quat[2], quat[3]))

        return goal

    def move_to_point(self, x: float, y: float, theta: float):
        target_point = self.create_goal(x, y, theta)
        self.move_to_goal(target_point)

    def move_to_goal(self, goal):
        self.move_base_action.send_goal(goal)
        success = self.move_base_action.wait_for_result()
        state = self.move_base_action.get_state()
        quat = goal.target_pose.pose.orientation
        theta = tf.transformations.euler_from_quaternion((quat.x, quat.y, quat.z, quat.w))
        rospy.loginfo(f"Move to x: {goal.target_pose.pose.position.x} y: {goal.target_pose.pose.position.y} theta: {theta[2]}")
        if success and state == GoalStatus.SUCCEEDED:
            print(" Complete")
            return True
        else:
            print(" Fail")
            self.move_base_action.cancel_goal()
            return False


class ServoController:
    def __init__(self, frequency=50):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.pca = PCA9685(self.i2c)
        self.pca.frequency = frequency

    def set_servo_angle(self, channel, angle):
        servo_motor = servo.Servo(self.pca.channels[channel])
        servo_motor.angle = angle
        print("Servo => channels:", channel, "angle:", angle)

    def deinit(self):
        self.pca.deinit()


class Servo:
    def __init__(self):
        self.servo_controller = ServoController()

    def collect(self):
        self.servo_controller.set_servo_angle(14, 10)
        time.sleep(0.5)
        self.servo_controller.set_servo_angle(15, 0)
        time.sleep(2)

    def push(self):
        self.servo_controller.set_servo_angle(15, 153)
        time.sleep(0.5)
        self.servo_controller.set_servo_angle(14, 180)
        time.sleep(2)


def move_to_points(points):
    mba = MoveBaseActionClient()
    servo_control = Servo()

    for point in points:
        if point == 's':
            mba.move_to_point(1.7406722757359785, 0.039618379174469975, 1.57)  # s
            rospy.sleep(1)
        elif point == '1':
            mba.move_to_point(1.7543447659149112, 0.4134949092410032, 3.1)  # B1
            rospy.sleep(1)
            servo_control.push()
            servo_control.collect()
        elif point == '2':
            mba.move_to_point(1.3127463207760863, 0.43556666051057735, 3.14)  # B2
            rospy.sleep(1)
            servo_control.push()
            servo_control.collect()
        elif point == '3':
            mba.move_to_point(0.8032692734446746, 0.45076580952000417, 3.14)  # B3
            rospy.sleep(1)
            servo_control.push()
            servo_control.collect()
        elif point == '4':
            mba.move_to_point(0.38294635587964737, 0.43010144124774297, 3.14)  # B4
            rospy.sleep(1)
            servo_control.push()
            servo_control.collect()
        elif point == '5':
            mba.move_to_point(-0.1112575970497414, 0.4462328548883487, 3.14)  # B5
            rospy.sleep(1)
            servo_control.push()
            servo_control.collect()
        elif point == 'b':
            mba.move_to_point(1.6951648264777233, 0.36882977992174476, -1.57)  # BUR
            rospy.sleep(1)
            mba.move_to_point(1.6860229175321546, 0.02478249739312485, 3.14)  # BUL
            rospy.sleep(1)
            mba.move_to_point(-0.1840515285973654, -0.015136595886307145, 3.14)  # Back S
            rospy.sleep(1)





def main():
    rospy.init_node('movetogoal_node')
    a = str(input("Enter your P1:"))
    b = str(input("Enter your P2:"))
    c = str(input("Enter your P3:"))
    d = str(input("Enter your P4:"))
    e = str(input("Enter your P5:"))

    points = ['s', e, d, c, b, a, 'b']
    print("your pos:", points)

    move_to_points(points)


    # while not rospy.is_shutdown():

    #------------------------------FN


    ######## Servo #########
    # set up
    # servo_control.collect()
    # servo_control.push()
    ######## Servo #########
        

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
