from time import sleep
import math


def AvoidDrive(Speed, x, y, yFirst, m_Drivetrain, m_Ultrasonic):

    xTarget = x
    yTarget = y

    x = x - m_Drivetrain.x_pos_mm
    y = y - m_Drivetrain.y_pos_mm

    if (yFirst == False):
        if (x > 0):
            m_Drivetrain.turn_to_angle(Speed, 0)
        elif (x < 0):
            m_Drivetrain.turn_to_angle(Speed, 180)
        sleep(2)
        x = abs(x)
        while (x > 0):
            if (m_Ultrasonic.distance_centimeters > 20):
                if (x >= 10):
                    m_Drivetrain.on_for_distance(Speed,10,False)
                    x = x - 10
                else:
                    m_Drivetrain.on_for_distance(Speed,x)
                    x = 0
        sleep(2)
        if (y > 0):
            m_Drivetrain.turn_to_angle(Speed, 90)
        elif (y < 0):
            m_Drivetrain.turn_to_angle(Speed, 270)
        sleep(2)
        y = abs(y)
        while (y > 0):
            if (m_Ultrasonic.distance_centimeters > 10):
                if (y >= 10):
                    m_Drivetrain.on_for_distance(Speed,10,False)
                    y = y - 10
                else:
                    m_Drivetrain.on_for_distance(Speed,y)
                    y = 0
        sleep(2)
        m_Drivetrain.on_to_coordinates(Speed, xTarget, yTarget)
    else:
        if (y > 0):
            m_Drivetrain.turn_to_angle(Speed, 90)
        elif (y < 0):
            m_Drivetrain.turn_to_angle(Speed, 270)
        y = abs(y)
        sleep(2)
        while (y > 0):
            if (m_Ultrasonic.distance_centimeters > 10):
                if (y >= 10):
                    m_Drivetrain.on_for_distance(Speed,10,False)
                    y = y - 10
                else:
                    m_Drivetrain.on_for_distance(Speed,y)
                    y = 0

        sleep(2)
        if (x > 0):
            m_Drivetrain.turn_to_angle(Speed, 0)
        elif (x < 0):
            m_Drivetrain.turn_to_angle(Speed, 180)
        x = abs(x)
        sleep(2)
        while (x > 0):
            if (m_Ultrasonic.distance_centimeters > 10):
                if (x >= 10):
                    m_Drivetrain.on_for_distance(Speed,10,False)
                    x = x - 10
                else:
                    m_Drivetrain.on_for_distance(Speed,x)
                    x = 0
        sleep(2)
        m_Drivetrain.on_to_coordinates(Speed, xTarget, yTarget)
