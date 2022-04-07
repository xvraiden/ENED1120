
def AvoidDrive(Speed, x, y, yFirst, m_Drivetrain, m_Ultrasonic):

    x = x - m_Drivetrain.x_pos_mm
    y = y - m_Drivetrain.y_pos_mm

    if (yFirst == False):
        if (x > 0):
            m_Drivetrain.turn_to_angle(Speed, 0)
        elif (x < 0):
            m_Drivetrain.turn_to_angle(Speed, 180)
        x = abs(x)
        while (x > 0):
            if (m_Ultrasonic.distance_centimeters > 20):
                if (x >= 10):
                    m_Drivetrain.on_for_distance(Speed,10,False)
                    x = x - 10
                else:
                    m_Drivetrain.on_for_distance(Speed,x)
                    x = 0
        if (y > 0):
            m_Drivetrain.turn_to_angle(Speed, 90)
        elif (y < 0):
            m_Drivetrain.turn_to_angle(Speed, 270)
        y = abs(y)
        while (y > 0):
            if (m_Ultrasonic.distance_centimeters > 10):
                if (y >= 10):
                    m_Drivetrain.on_for_distance(Speed,10,False)
                    y = y - 10
                else:
                    m_Drivetrain.on_for_distance(Speed,y)
                    y = 0

    else:
        if (y > 0):
            m_Drivetrain.turn_to_angle(Speed, 90)
        elif (y < 0):
            m_Drivetrain.turn_to_angle(Speed, 270)
        y = abs(y)
        while (y > 0):
            if (m_Ultrasonic.distance_centimeters > 10):
                if (y >= 10):
                    m_Drivetrain.on_for_distance(Speed,10,False)
                    y = y - 10
                else:
                    m_Drivetrain.on_for_distance(Speed,y)
                    y = 0

        if (x > 0):
            m_Drivetrain.turn_to_angle(Speed, 0)
        elif (x < 0):
            m_Drivetrain.turn_to_angle(Speed, 180)
        x = abs(x)
        while (x > 0):
            if (m_Ultrasonic.distance_centimeters > 10):
                if (x >= 10):
                    m_Drivetrain.on_for_distance(Speed,10,False)
                    x = x - 10
                else:
                    m_Drivetrain.on_for_distance(Speed,x)
                    x = 0
