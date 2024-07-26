# Turtlebot3-Multi-Point-Navigation-Script
this package for turtlebot3 ros noetic.

## About Turlebot3 
 documentation  [Turlebot3](https://pages.github.com/](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#pc-setup)).

 > [!NOTE]
>  i use Raspberry Pi 4 4GB
>  Set up your turlebot3 for ros noeic

## About Pc
 install [Ros Noetic](https://pages.github.com/](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#pc-setup)](https://wiki.ros.org/noetic/Installation/Ubuntu)).
 > [!NOTE]
>  plz install ros-noetic-desktop-full
 
### Install Dependent ROS Packages
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
### Install TurtleBot3 Packages
```
sudo apt install ros-noetic-dynamixel-sdk
sudo apt install ros-noetic-turtlebot3-msgs
sudo apt install ros-noetic-turtlebot3
```

