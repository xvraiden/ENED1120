#!/usr/bin/env python3
from ev3dev2.motor import MoveDifferential, MediumMotor
from ev3dev2.sensor.lego import UltrasonicSensor, ColorSensor
from time import sleep
import Constants
import Location
import Barcode
import Drivetrain

#create position flag and barcode scan number
pos = False
i = 0
    
#create objects for sensors, motors, drivetrain
m_Drivetrain = MoveDifferential(Constants.leftDrive, Constants.rightDrive, Constants.MyTire, Constants.wheelOffset)

m_Claw = MediumMotor()

m_Ultrasonic = UltrasonicSensor()

m_ColorTop = ColorSensor(Constants.topColor)
m_ColorBottom = ColorSensor(Constants.bottomColor)

colors = []

# begin odometry at start location a in mm
m_Drivetrain.odometry_start(90, 6 * 25.4, -6 * 25.4)

#create loop that runs number of times based on boxes to be fulfilled
for q in range(2, len(Constants.Packages) + 1, 1):
    #get location of shelf at index q in file Location.py
    locationShelf = Location.DetermineShelfLocation(q)

    #drive to start of desired shelf
    Drivetrain.AvoidDrive(Constants.driveSpeed, locationShelf[0], locationShelf[1], True, m_Drivetrain, m_Ultrasonic)

    sleep(1)


    pos = False


    while (pos == False):
        if (not((m_ColorTop.color == 1) or (m_ColorTop.color == 6))):
            m_Drivetrain.on_for_distance(Constants.senseSpeed, 5)
            
        else:
            pos = True

        m_Drivetrain.on_for_distance(Constants.senseSpeed, 7)

        if (m_ColorTop.reflected_light_intensity > 10):
            colors.append(2)
            print(m_ColorTop.reflected_light_intensity)
        else:
            colors.append(0)
            print(m_ColorTop.reflected_light_intensity)

        if (m_ColorBottom.reflected_light_intensity > 25):
            colors.append(2)
            print(m_ColorBottom.reflected_light_intensity)
        elif (m_ColorBottom.reflected_light_intensity > 10):
            colors.append(1)
            print(m_ColorBottom.reflected_light_intensity)
        else:
            colors.append(0)
            print(m_ColorBottom.reflected_light_intensity)
        
    m_Drivetrain.off()


    #interpret the barcode and proceed if proper barcode detected otherwise return to home
    if (Barcode.NewInterperate(2, colors) == True):
        #turn to face box

        locationDump = Location.DetermineDumpLocation(Constants.Packages[q][3])

        m_Drivetrain.turn_degrees(Constants.senseSpeed, -90)

        pos = False

        #get close to box and prep for pickup
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
        Drivetrain.AvoidDrive(Constants.driveSpeed, locationDump[0], locationDump[1], False, m_Drivetrain, m_Ultrasonic)

        #dump box
        m_Claw.on_for_degrees(Constants.clawSpeed, -120)
        m_Drivetrain.on_for_distance(Constants.senseSpeed, -254)

        #go home
        Drivetrain.AvoidDrive(Constants.driveSpeed, 6 * 25.4, -6 * 25.4, False, m_Drivetrain, m_Ultrasonic)
        sleep(5)
    else:
        #go home
        Drivetrain.AvoidDrive(Constants.driveSpeed, 6 * 25.4, -6 * 25.4, False, m_Drivetrain, m_Ultrasonic)
        sleep(5)