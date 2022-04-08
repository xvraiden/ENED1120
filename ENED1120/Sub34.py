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

pos = False
i = 0

colors = []

m_Drivetrain.odometry_start(0, 11 * 25.4, 0)

locationShelf = Location.DetermineShelfLocation(2)

Drivetrain.AvoidDrive(Constants.driveSpeed, locationShelf[0], 0, False, m_Drivetrain, m_Ultrasonic)

m_Drivetrain.turn_degrees(Constants.driveSpeed, 180)

while (pos == False):
        if (((m_Drivetrain.x_pos_mm >= locationShelf[0] + 15) or (m_Drivetrain.x_pos_mm <= locationShelf[0] - 15)) and i > 3):
            pos = True
        m_Drivetrain.on_for_distance(Constants.senseSpeed, (0.25 * 25.4))
        if (m_Color.reflected_light_intensity > 10):
            colors.append(6)
        else:
            colors.append(0)
        sleep(1)
        i = i + 1

Barcode.Interperate(2, colors)

m_Button.wait_for_released("enter")

m_Drivetrain.turn_degrees(Constants.senseSpeed, -90)

pos = False

while (pos == False):
    if (m_Ultrasonic.distance_centimeters <= Constants.sensingDistance):
        pos = True
    m_Drivetrain.on_for_distance(Constants.senseSpeed, 10, False)

#pickup box
m_Claw.on_for_degrees(Constants.clawSpeed, 120)

sleep(1)

#backup from shelf
m_Drivetrain.on_for_distance(Constants.senseSpeed, -75)

#go to dump location location
Drivetrain.AvoidDrive(Constants.driveSpeed, 48 * 25.4 , m_Drivetrain.y_pos_mm, True, m_Drivetrain, m_Ultrasonic)

m_Claw.on_for_degrees(Constants.clawSpeed, -120)