#!/usr/bin/env python
# -*- coding: utf-8 -*-
#code for python2
import serial
import time
import Kondo_B3M_functions_forsampleprogram as Kondo_B3M

ser = serial.Serial('/dev/Kondo_USB-RS485_converter', 1500000)
time.sleep(1)

Kondo_B3M.resetServo(4)
Kondo_B3M.enFreeServo(4)
Kondo_B3M.change_servocontrol_mode(4, 0) #mode : 00>positionCTRL, 04>velocityCTRL, 08>current(torque)CTRL, 12>feedforwardCTRL
Kondo_B3M.set_servo_trajectory_to_5Poly(4)
Kondo_B3M.set_servo_gain_to_presets(4, 0)
Kondo_B3M.change_servocontrol_mode(4, 0) #mode : 00>positionCTRL, 04>velocityCTRL, 08>current(torque)CTRL, 12>feedforwardCTRL
"""
Kondo_B3M.control_servo_by_position_with_time(4, 9000, 500)
Kondo_B3M.read_servo_Position(4)

Kondo_B3M.control_servo_by_position_with_time(4, 0, 500)
Kondo_B3M.read_servo_Position(4)

Kondo_B3M.control_servo_by_position_with_time(4, 9000, 500)
Kondo_B3M.read_servo_Position(4)

Kondo_B3M.control_servo_by_position_with_time(4, 0, 500)
Kondo_B3M.read_servo_Position(4)
"""

Kondo_B3M.change_servocontrol_mode(4, 8) #mode : 00>positionCTRL, 04>velocityCTRL, 08>current(torque)CTRL, 12>feedforwardCTRL

Kondo_B3M.control_servo_by_Torque(4, 500)
time.sleep(0.5)
Kondo_B3M.control_servo_by_Torque(4, 1000)
time.sleep(0.5)
Kondo_B3M.control_servo_by_Torque(4, 1500)
time.sleep(0.5)
Kondo_B3M.control_servo_by_Torque(4, 2000)
time.sleep(0.5)
Kondo_B3M.control_servo_by_Torque(4, 2500)
time.sleep(0.5)
Kondo_B3M.control_servo_by_Torque(4, -1000)
time.sleep(1)
Kondo_B3M.enFreeServo(4)


ser.close()
time.sleep(2)