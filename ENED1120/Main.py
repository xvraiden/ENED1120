from ev3dev2.motor import MoveDifferential, MediumMotor
from ev3dev2.sensor.lego import UltrasonicSensor, ColorSensor
import Constants
import Location
import Barcode

#create position flag and barcode scan number
pos = False
i = 0

#create objects for sensors, motors, drivetrain
m_Drivetrain = MoveDifferential(Constants.leftDrive, Constants.rightDrive, Constants.MyTire, Constants.wheelOffset)

m_Claw = MediumMotor()

m_Ultrasonic = UltrasonicSensor

m_Color = ColorSensor


# begin odometry at start location a in mm
m_Drivetrain.odometry_start(90, 6 * 25.4, -6 * 25.4)

#create loop that runs number of times based on boxes to be fulfilled
for q in range(1, Constants.quantity, 1):
    #get location of shelf at index q in file Location.py
    Location.DetermineShelfLocation(q)

    #drive to start of desired shelf
    m_Drivetrain.on_to_coordinates(Constants.driveSpeed, Location.LocationXShelf, Location.LocationYShelf - 200)

    #sense the barcode until we are at location
    while (pos == False):
        if (m_Drivetrain.x_pos_mm >= Location.LocationXShelf):
            pos = True
        m_Drivetrain.on_to_coordinates(Constants.senseSpeed, m_Drivetrain.x_pos_mm + (0.25 * 25.4), m_Drivetrain.y_pos_mm, True, False)
        Barcode.colors[i] = int(m_Color.color)
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
            m_Drivetrain.on_for_distance(Constants.senseSpeed, 10)

        #pickup box
        m_Claw.on_for_degrees(Constants.clawSpeed, m_Claw.position + 30)

        #backup from shelf
        m_Drivetrain.on_for_distance(Constants.senseSpeed, -180)

        #go to dump location location
        m_Drivetrain.on_to_coordinates(Constants.driveSpeed, Barcode.LocationX, Barcode.LocationY)

        #go home
        m_Drivetrain.on_to_coordinates(Constants.driveSpeed, 6 * 25.4, -6 * 25.4)
    else:
        #go home
        m_Drivetrain.on_to_coordinates(Constants.driveSpeed, 6 * 25.4, -6 * 25.4)