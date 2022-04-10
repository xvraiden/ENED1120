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

m_Claw = MediumMotor()

m_Ultrasonic = UltrasonicSensor()

m_Color = ColorSensor()

m_Button = Button()

#start at 27
m_Drivetrain.odometry_start(180, 27 * 25.4, 0)

#turn toward box
m_Drivetrain.turn_degrees(Constants.senseSpeed, -90)

pos = False

#get close to box
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

#drop box
m_Claw.on_for_degrees(Constants.clawSpeed, -120)