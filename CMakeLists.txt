cmake_minimum_required(VERSION 3.0.2)
project(turtlebot3_moveto)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

################################################
## Declare ROS messages, services and actions ##
################################################

################################################
## Declare ROS dynamic reconfigure parameters ##
################################################

###################################
## catkin specific configuration ##
###################################

catkin_package(
 CATKIN_DEPENDS rospy std_msgs
)

###########
## Build ##
###########

#############
## Install ##
#############

catkin_install_python(PROGRAMS
  scripts/move2goal.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

#############
## Testing ##
#############
