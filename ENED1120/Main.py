from ev3dev2.motor import MoveDifferential
from ev3dev2.sensor.lego import UltrasonicSensor, ColorSensor
import Constants
import Location
import Barcode

pos = False
i = 0

m_Drivetrain = MoveDifferential(Constants.leftDrive, Constants.rightDrive, Constants.MyTire, Constants.wheelOffset)

m_Ultrasonic = UltrasonicSensor

m_Color = ColorSensor

m_Drivetrain.odometry_start(90, 6 * 25.4, -6 * 25.4)

#start
Location.DetermineLocation(1)

m_Drivetrain.on_to_coordinates(Constants.driveSpeed, Location.LocationX, Location.LocationY - 200)

while (pos == False):
    if (m_Drivetrain.x_pos_mm == Location.LocationX):
        pos = True
    m_Drivetrain.on_to_coordinates(Constants.senseSpeed, m_Drivetrain.x_pos_mm + (0.25 * 25.4), m_Drivetrain.y_pos_mm, True, False)
    Barcode.colors[i] = int(m_Color.color)
    i = i + 1