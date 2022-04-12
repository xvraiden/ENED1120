from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedRPM
from ev3dev2.wheel import Wheel
from ev3dev2.sensor import INPUT_1, INPUT_2

#drive motor ports
leftDrive = OUTPUT_B
rightDrive = OUTPUT_C

topColor = INPUT_1
bottomColor = INPUT_2

#speeds for moving
#driveSpeed = SpeedRPM(60)
driveSpeed = SpeedRPM(20)
senseSpeed = SpeedRPM(10)

#claw speed
clawSpeed = SpeedRPM(120)

#wheel offset on center mm
wheelOffset = 134.0 

# sensing distance in cm
sensingDistance = 7

#package location[shelf,package,barcode,dropoff]
Packages = [["A1",7,1,"C"],["A1",9,2,"B"]]

hitCount = 3

#tire with diameter and width in mm
class MyTire(Wheel):
    """
    part number 56145
    comes in set 31313
    """
    def __init__(self):
        Wheel.__init__(self, 70.4, 36.2)
