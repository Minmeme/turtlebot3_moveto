# Turtlebot3-Multi-Point-Navigation-Script
this package for turtlebot3 ros noetic.

## About Turlebot3 
 documentation  [Turlebot3](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#pc-setup)].

 > [!NOTE]
>  i use Raspberry Pi 4 4GB
>  Set up your turlebot3 for ros noeic

## About Pc
 install [Ros Noetic]((https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#pc-setup)](https://wiki.ros.org/noetic/Installation/Ubuntu)).
 
 Install Dependent ROS Packages
```
sudo apt-get install ros-noetic-joy ros-noetic-teleop-twist-joy \
  ros-noetic-teleop-twist-keyboard ros-noetic-laser-proc \
  ros-noetic-rgbd-launch ros-noetic-rosserial-arduino \
  ros-noetic-rosserial-python ros-noetic-rosserial-client \
  ros-noetic-rosserial-msgs ros-noetic-amcl ros-noetic-map-server \
  ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro \
  ros-noetic-compressed-image-transport ros-noetic-rqt* ros-noetic-rviz \
  ros-noetic-gmapping ros-noetic-navigation ros-noetic-interactive-markers
```

 > [!NOTE]
>  plz install ros-noetic-desktop-full

## install turtlebot3 packages
  Create a catkin workspace
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```
Add the workspace to your ROS environment
```
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
Install TurtleBot3 packages
```
git clone https://github.com/ROBOTIS-GIT/turtlebot3.git ~/catkin_ws/src/turtlebot3
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git ~/catkin_ws/src/turtlebot3_msgs
git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git ~/catkin_ws/src/turtlebot3_simulations
```
After cloning the repositories, don't forget to build your workspace:
```
cd ~/catkin_ws
catkin_make
source ~/catkin_ws/devel/setup.bash
```

## About ROS Network Configuration
### In PC
1 Chack your pi4 ip
```
ifconfig
```
2 Edit your .bashrc file
```
nano ~/.bashrc
```
3 Find the ROS_MASTER_URI and ROS_HOSTNAME setting section, then modify the IP adddresses accordingly
```
export ROS_MASTER_URI=http://{IP_ADDRESS_OF_REMOTE_PC}:11311
export ROS_HOSTNAME={IP_ADDRESS_OF_REMOTE_PC}
```
4 Save the file with Ctrl + S and exit the nano editor with Ctrl + X.
5 Apply changes with the command below.
```
 source ~/.bashrc
```
### In Pi4
make like pc
but chaing  ROS_HOSTNAM is Pi4 ip
```
export ROS_MASTER_URI=http://{IP_ADDRESS_OF_REMOTE_PC}:11311
export ROS_HOSTNAME={IP_ADDRESS_OF_PI4}
```
 > [!NOTE]
>  This is done so that the computer and robot are on the same network. and dont forget make PC and robot connect the same wifi.
