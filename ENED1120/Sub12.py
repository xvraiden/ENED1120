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

#begin at 6x -6y
m_Drivetrain.odometry_start(90, 6 * 25.4, -6 * 25.4)

#determine position of stop
locationShelf = Location.DetermineShelfLocation(1)

#go to location
Drivetrain.AvoidDrive(Constants.driveSpeed, locationShelf[0] - 50, locationShelf[1], True, m_Drivetrain, m_Ultrasonic)

sleep(5)

#determine position of home b
locationDump = Location.DetermineDumpLocation("B")

#go to b
Drivetrain.AvoidDrive(Constants.driveSpeed, locationDump[0], locationDump[1], False, m_Drivetrain, m_Ultrasonic)

#task 2
m_Button.wait_for_released("enter")

#backup from b
m_Drivetrain.on_for_distance(Constants.driveSpeed , -10 * 25.4)

#go home a
Drivetrain.AvoidDrive(Constants.driveSpeed, 6 * 25.4, -6 * 25.4, False, m_Drivetrain, m_Ultrasonic)