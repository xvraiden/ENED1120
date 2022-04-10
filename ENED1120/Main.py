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

m_Color = ColorSensor()

colors = []

# begin odometry at start location a in mm
m_Drivetrain.odometry_start(90, 6 * 25.4, -6 * 25.4)

#create loop that runs number of times based on boxes to be fulfilled
for q in range(1, len(Constants.Packages), 1):
    #get location of shelf at index q in file Location.py
    locationShelf = Location.DetermineShelfLocation(q)

    #drive to start of desired shelf
    Drivetrain.AvoidDrive(Constants.driveSpeed, locationShelf[0], locationShelf[1], True, m_Drivetrain, m_Ultrasonic)

    sleep(1)

    #sense the barcode until we are at location
    #while (pos == False):
       #if (((m_Drivetrain.x_pos_mm >= locationShelf[0] + 15) or (m_Drivetrain.x_pos_mm <= locationShelf[0] - 15)) and i > 3):
        #    pos = True
        #m_Drivetrain.on_for_distance(Constants.senseSpeed, (0.25 * 25.4))
        #if (m_Color.reflected_light_intensity > 10):
         #   colors.append(6)
        #else:
         #   colors.append(0)
        #sleep(1)
        #i = i + 1

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

    #interpret the barcode and proceed if proper barcode detected otherwise return to home
    if (Barcode.Interperate(q, colors) == True):
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