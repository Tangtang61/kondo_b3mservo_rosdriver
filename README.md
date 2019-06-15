# kondo-b3mservo-rosdriver
　　
## Overview
ROS package for control of servo motor by ***Kondo Kagaku Inc***.  
<br>
<br>
<br>
## Description
This package is for control of serial servo (B3Mseries) by ***Kondo Kagaku Inc*** via ROS.  
It includes nodes for send/receive commands to/from servos and pub/sub them, an additional file to wrap functions to generate commands to servos, and peripherals.(a sample file to control by a joystick, etc.)  
<br>
<br>
<br>
## Demo
sorry, still in prepare
<br>
<br>
<br>
## Requirements
confirmed environment is as follows:
  * Ubuntu16.04  
  * python2.7.12  
  * ROS kinetic kame  
<br>
<br>
<br>

## Install
`cd ~/NAME_OF_YOUR_ROS_WORKSPACE(e.g catkin_ws)/src`  
`git clone git@github.com:k24koba/kondo-b3mservo-rosdriver.git`  
`cd ~/catkin_ws`  
`catkin_make`  
<br>
<br>
<br>
## Before use
Confirm that you have connected your B3M servo to your PC via [RS485-USB adapter](https://kondo-robot.com/product/02133)  
First, you have to go through several process to use serial servos by ***Kondo Kagaku Inc***.<br>
You can consult official website about this process(https://kondo-robot.com/faq/usb_adapter_for_linux_2019)
<br>
<br>
<br>
## How to use
in directory ***scripts***, you have several files:
  * ***generate_command_autodetect_joy.py***  : command generator to your servo from ROS joystick package
  * ***Kondo_B3M_functions.py***  :  collection of functions to generate servo command
  * ***Kondo_B3M_functions.pyc*** : file generated by byte compile of ***Kondo_B3M_functions.py***
  * ***position_control_autodetect.py***  : node to control servos by its position (angle)
  * ***torque_control_autodetect.py***  : node to control servos by its velocity
  * ***torque_control_autodetect_multicast.py*** : node to control servos by its torque (using multi-cast mode to send torque command)
  * ***velocity_control_autodetect.py*** : node to control servos by its torque
<br>
As simple way to use, execute arbitrary node file (position, velocity, or torque control)<br>
e.g :<br>
`catkin_make`  
You may have an error such as ***serial.serialutil.SerialException: [Errno 2] could not open port /dev/Kondo_USB-RS485_converter: [Errno 2] No such file or directory: '/dev/Kondo_USB-RS485_converter'***  
To solve this you can take two ways : <br>
  * change device name in ***<node file>.py*** and ***Kondo_B3M_functions.py*** to appropriate name such as ***/dev/ttyUSB0***  
  * change recognized device name in your PC by using symbolic link
