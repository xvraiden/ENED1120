#!/usr/bin/env python3
from ev3dev2.motor import MoveDifferential, MediumMotor
from ev3dev2.sensor.lego import UltrasonicSensor, ColorSensor
from ev3dev2.button import Button
from time import sleep
import Constants
import Location
import Barcode
import Drivetrain




m_Drivetrain = MoveDifferential(Constants.leftDrive, Constants.rightDrive, Constants.MyTire, Constants.wheelOffset)

m_Ultrasonic = UltrasonicSensor()

m_Drivetrain.odometry_start(90, 0, 0)

Drivetrain.AvoidDrive(Constants.driveSpeed, -20 * 25.4, -12 * 25.4, True, m_Drivetrain, m_Ultrasonic)