#!/usr/bin/env python3
from turtle import color
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

m_Color = ColorSensor(Constants.topColor)

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
Drivetrain.AvoidDrive(Constants.driveSpeed, locationShelf[0], 0, False, m_Drivetrain, m_Ultrasonic)

#turn around to scan box
m_Drivetrain.turn_degrees(Constants.driveSpeed, 180)

#while (pos == False):
#        if (((m_Drivetrain.x_pos_mm >= locationShelf[0] + 15) or (m_Drivetrain.x_pos_mm <= locationShelf[0] - 15)) and i > 3):
#            pos = True
#        m_Drivetrain.on_for_distance(Constants.senseSpeed, (0.25 * 25.4))
#       if (m_Color.reflected_light_intensity > 10):
#            colors.append(1)
#        else:
#            colors.append(0)
#        sleep(1)
#        i = i + 1

#search for start of box
while (pos == False):
    if (not((m_Color.color == 1) or (m_Color.color == 6))):
        m_Drivetrain.on_for_distance(Constants.senseSpeed, 5)
    else:
        pos = True

pos = False

#get staring location
xtemp = m_Drivetrain.x_pos_mm
ytemp = m_Drivetrain.y_pos_mm

codePos = 1

m_Drivetrain.on_for_distance(Constants.senseSpeed, 2.5 * 25.4, True, False)

while (pos == False):
    #determine distance scanned
    x = abs(xtemp - m_Drivetrain.x_pos_mm)
    y = abs(ytemp - m_Drivetrain.y_pos_mm)

    #determine if we are believed to pass the next bar
    if (x >=  1.5 * 25.4):
            codePos = 4
    elif (x >=  1 * 25.4):
            codePos = 3
    elif (x >=  0.5 * 25.4):
            codePos = 2
    elif (x >=  0 * 25.4):
            codePos = 1

    #read the sensor and determine color
    if (m_Color.color == 6):
        colors.append([1,codePos])
    elif (m_Color.color == 1):
        colors.append([0,codePos])

    #determine if we are finished scanning
    if ((x > (3 * 25.4) - 15) or (x < (3 * 25.4) + 15)):
            pos = True

m_Drivetrain.off()

#determine the scanned barcode
Barcode.Interperate(2, colors)

#begin task 4
m_Button.wait_for_released("enter")

#turn to face box
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

m_Claw.on_for_degrees(Constants.clawSpeed, -120)