#!/usr/bin/env python3
from ev3dev2.motor import MoveDifferential, MediumMotor
from ev3dev2.sensor.lego import UltrasonicSensor, ColorSensor
from ev3dev2.button import Button
from time import sleep
import Constants
import Location
import Barcode
import Drivetrain

#creates objects for ev3
m_Drivetrain = MoveDifferential(Constants.leftDrive, Constants.rightDrive, Constants.MyTire, Constants.wheelOffset)

m_Claw = MediumMotor()

m_Ultrasonic = UltrasonicSensor()

m_ColorTop = ColorSensor(Constants.topColor)
m_ColorBottom = ColorSensor(Constants.bottomColor)

m_Button = Button()

#creates position and inex
pos = False
i = 0

colors = []

#begin at 11x 0y
m_Drivetrain.odometry_start(0, 11 * 25.4, 0)

#determine location of package 9
locationShelf = Location.DetermineShelfLocation(2)

#go to location 9
#Drivetrain.AvoidDrive(Constants.driveSpeed, locationShelf[0], 0, False, m_Drivetrain, m_Ultrasonic)

#turn around to scan box
#m_Drivetrain.turn_degrees(Constants.driveSpeed, 180)

while (pos == False):
    if (not((m_ColorTop.color == 1) or (m_ColorTop.color == 6))):
        #m_Drivetrain.on_for_distance(Constants.senseSpeed, 5)
        pos = True
    else:
        pos = True


if (m_ColorTop.reflected_light_intensity > 15):
    colors.append(2)
else:
    colors.append(0)

if (m_ColorBottom.reflected_light_intensity > 35):
    colors.append(2)
elif (m_ColorBottom.reflected_light_intensity > 15):
    colors.append(1)
else:
    colors.append(0)


m_Drivetrain.off()

#determine the scanned barcode
Barcode.NewInterperate(2, colors)

#begin task 4
m_Button.wait_for_released("enter")

#drive forward a bit
m_Drivetrain.on_for_distance(Constants.driveSpeed, 40)

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