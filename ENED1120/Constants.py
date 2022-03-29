from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedRPM
from ev3dev2.wheel import Wheel

leftDrive = OUTPUT_A
rightDrive = OUTPUT_D

driveSpeed = SpeedRPM(60)
senseSpeed = SpeedRPM(30)

wheelOffset = 136.0 

sensingDistance = 7

#shelf locations
shelf1X = 5
shelf1Y = 5

shelf2X = 5
shelf2Y = 5

#package locations
package1X = 10
package1Y = 10

package2X = 10
package2Y = 10

class MyTire(Wheel):
    """
    part number 56145
    comes in set 31313
    """
    def __init__(self):
        Wheel.__init__(self, 70.3, 36.2)