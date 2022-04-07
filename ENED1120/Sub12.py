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

m_Button = Button()

m_Drivetrain.odometry_start(90, 6 * 25.4, -6 * 25.4)

locationShelf = Location.DetermineShelfLocation(1)

Drivetrain.AvoidDrive(Constants.driveSpeed, locationShelf[0] - 75, locationShelf[1], True, m_Drivetrain, m_Ultrasonic)

sleep(5)

locationDump = Location.DetermineDumpLocation("B")

Drivetrain.AvoidDrive(Constants.driveSpeed, locationDump[0], locationDump[1], False, m_Drivetrain, m_Ultrasonic)

m_Button.wait_for_released("enter")

m_Drivetrain.on_for_distance(Constants.driveSpeed , -7 * 25.4)

Drivetrain.AvoidDrive(Constants.driveSpeed, 6 * 25.4, -6 * 25.4, False, m_Drivetrain, m_Ultrasonic)