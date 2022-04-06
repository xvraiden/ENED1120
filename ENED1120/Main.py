#!/usr/bin/env python3
from ev3dev2.motor import MoveDifferential, MediumMotor
from ev3dev2.sensor.lego import UltrasonicSensor, ColorSensor
from time import sleep
import Constants
import Location
import Barcode

#create position flag and barcode scan number
pos = False
i = 0
    
#create objects for sensors, motors, drivetrain
m_Drivetrain = MoveDifferential(Constants.leftDrive, Constants.rightDrive, Constants.MyTire, Constants.wheelOffset)

m_Claw = MediumMotor()

m_Ultrasonic = UltrasonicSensor()

m_Color = ColorSensor()

def AvoidDrive(Speed, x, y, yFirst):
    xtemp = x
    ytemp = y

    if (yFirst == False):
        m_Drivetrain.turn_to_angle(Speed, 0)

        while (x > 180):
            if (m_Ultrasonic.distance_centimeters > 10):
                if (x >= 10):
                    m_Drivetrain.on_for_distance(Speed,10,False)
                    x = x - 10
                else:
                    m_Drivetrain.on_for_distance(Speed,x)
                    x = 0

        if (xtemp != m_Drivetrain.x_pos_mm):
            m_Drivetrain.on_to_coordinates(Speed, xtemp, m_Drivetrain.y_pos_mm)

        m_Drivetrain.turn_to_angle(Speed, 90)

        while (y > 0):
            if (m_Ultrasonic.distance_centimeters > 10):
                if (y >= 10):
                    m_Drivetrain.on_for_distance(Speed,10,False)
                    y = y - 10
                else:
                    m_Drivetrain.on_for_distance(Speed,y)
                    y = 0

        if (ytemp != m_Drivetrain.y_pos_mm):
            m_Drivetrain.on_to_coordinates(Speed, m_Drivetrain.x_pos_mm, ytemp)
    else:
        m_Drivetrain.turn_to_angle(Speed, 90)

        while (y > 0):
            if (m_Ultrasonic.distance_centimeters > 10):
                if (y >= 10):
                    m_Drivetrain.on_for_distance(Speed,10,False)
                    y = y - 10
                else:
                    m_Drivetrain.on_for_distance(Speed,y)
                    x = 0

        if (ytemp != m_Drivetrain.y_pos_mm):
            m_Drivetrain.on_to_coordinates(Speed, m_Drivetrain.x_pos_mm, ytemp)

        m_Drivetrain.turn_to_angle(Speed, 180)

        while (x > 0):
            if (m_Ultrasonic.distance_centimeters > 10):
                if (x >= 10):
                    m_Drivetrain.on_for_distance(Speed,10,False)
                    x = x - 10
                else:
                    m_Drivetrain.on_for_distance(Speed,x)
                    x = 0

        if (xtemp != m_Drivetrain.x_pos_mm):
            m_Drivetrain.on_to_coordinates(Speed, xtemp, m_Drivetrain.y_pos_mm)

# begin odometry at start location a in mm
m_Drivetrain.odometry_start(90, 6 * 25.4, -6 * 25.4)

#create loop that runs number of times based on boxes to be fulfilled
for q in range(1, len(Constants.Packages), 1):
    #get location of shelf at index q in file Location.py
    Location.DetermineShelfLocation(q)

    #drive to start of desired shelf
    #m_Drivetrain.on_to_coordinates(Constants.driveSpeed, Location.LocationXShelf, Location.LocationYShelf)
    AvoidDrive(Constants.driveSpeed, Location.LocationXShelf, Location.LocationYShelf, True)

    sleep(1)

    #sense the barcode until we are at location
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

    #interpret the barcode and proceed if proper barcode detected otherwise return to home
    if (Barcode.Interperate(q) == True):
        #turn to face box
        m_Drivetrain.turn_degrees(Constants.senseSpeed, -90)

        pos = False

        #get close to box and prep for pickup
        while (pos == False):
            if (m_Ultrasonic.distance_centimeters <= Constants.sensingDistance):
                pos = True
            m_Drivetrain.on_for_distance(Constants.senseSpeed, 10, False)

        #pickup box
        m_Claw.on_for_degrees(Constants.clawSpeed, m_Claw.position + 30)

        sleep(1)

        #backup from shelf
        m_Drivetrain.on_for_distance(Constants.senseSpeed, -180)

        #go to dump location location
        #m_Drivetrain.on_to_coordinates(Constants.driveSpeed, Barcode.LocationX, Barcode.LocationY)
        AvoidDrive(Constants.driveSpeed, Barcode.LocationX, Barcode.LocationY, False)

        #dump box
        m_Claw.on_for_degrees(Constants.clawSpeed, m_Claw.position + 30)
        m_Drivetrain.on_for_distance(Constants.senseSpeed, -180)

        #go home
        #m_Drivetrain.on_to_coordinates(Constants.driveSpeed, 6 * 25.4, -6 * 25.4)
        AvoidDrive(Constants.driveSpeed, 6 * 25.4, -6 * 25.4, False)
        sleep(5)
    else:
        #go home
        #m_Drivetrain.on_to_coordinates(Constants.driveSpeed, 6 * 25.4, -6 * 25.4)
        AvoidDrive(Constants.driveSpeed, 6 * 25.4, -6 * 25.4, False)
        sleep(5)