from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedRPM
from ev3dev2.wheel import Wheel

#drive motor ports
leftDrive = OUTPUT_A
rightDrive = OUTPUT_D

#speeds for moving
driveSpeed = SpeedRPM(60)
senseSpeed = SpeedRPM(30)

#claw speed
clawSpeed = SpeedRPM(30)

#wheel offset on center mm
wheelOffset = 136.0 

# sensing distance in cm
sensingDistance = 7

#box quantity
quantity = 2

#package locations OLD
shelf1 = "A1"
package1 = 1
barcode1 = 1
dump1 = "C"

shelf2 = "A2"
package2 = 2
barcode2 = 1
dump2 = "B"

#package location[shelf,package,barcode,dropoff]
Packages = [["A1",1,1,"C"],["A1",1,1,"C"]]


#tire with diameter and width in mm
class MyTire(Wheel):
    """
    part number 56145
    comes in set 31313
    """
    def __init__(self):
        Wheel.__init__(self, 70.3, 36.2)