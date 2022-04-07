from ev3dev2.sound import Sound

m_Speaker = Sound()


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
            else:
                m_Speaker.play_file('GPWS.wav', 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)

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
                m_Speaker.play_file('GPWS.wav', 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)

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
            else:
                m_Speaker.play_file('GPWS.wav', 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)

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
            else:
                m_Speaker.play_file('GPWS.wav', 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)
