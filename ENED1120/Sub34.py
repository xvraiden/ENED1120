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

m_Claw = MediumMotor()

m_Ultrasonic = UltrasonicSensor()

m_Color = ColorSensor()

m_Button = Button()

m_Drivetrain.odometry_start(90, 6 * 25.4, -6 * 25.4)

Location.DetermineShelfLocation(2)

Drivetrain.AvoidDrive(Constants.driveSpeed, Location.LocationXShelf, Location.LocationYShelf, False, m_Drivetrain, m_Ultrasonic)

while (pos == False):
        if (m_Drivetrain.x_pos_mm >= Location.LocationXShelf):
            pos = True
        m_Drivetrain.on_for_distance(Constants.senseSpeed, (0.25 * 25.4))
        if (m_Color.reflected_light_intensity > 50):
            Barcode.colors[i] = 6
        else:
            Barcode.colors[i] = 0
        sleep(1)
        i = i + 1

Barcode.Interperate(2)

m_Button.wait_for_released("enter")

m_Drivetrain.on_for_distance(Constants.driveSpeed , -7 * 25.4)

Drivetrain.AvoidDrive(Constants.driveSpeed, 6 * 25.4, -6 * 25.4, False, m_Drivetrain, m_Ultrasonic)