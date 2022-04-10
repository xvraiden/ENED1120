#!/usr/bin/env python3
from ev3dev2.motor import MoveDifferential, MediumMotor
from ev3dev2.sensor.lego import UltrasonicSensor, ColorSensor
from ev3dev2.button import Button
from time import sleep
import Constants
import Location
import Barcode
import Drivetrain

#create objects
m_Drivetrain = MoveDifferential(Constants.leftDrive, Constants.rightDrive, Constants.MyTire, Constants.wheelOffset)

m_Ultrasonic = UltrasonicSensor()

m_Button = Button()

#start at 102x -6y
m_Drivetrain.odometry_start(270, 102 * 25.4, -6 * 25.4)

#backup from b
m_Drivetrain.on_for_distance(Constants.driveSpeed , -10 * 25.4)

#go to a
Drivetrain.AvoidDrive(Constants.driveSpeed, 6 * 25.4, -6 * 25.4, False, m_Drivetrain, m_Ultrasonic)