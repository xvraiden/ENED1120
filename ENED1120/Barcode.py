import Constants
import OSD
import Location

# black - 1, white - 6
# list of intigers (6 or 1)
# four members of list colors
# colors is an array with infomation from the light sensor
colors = []
readAgain = False   # if the sensor does not get all data we want to read it again


LocationX = 0
LocationY = 0

barcode = 0; # type of barcode that sensor identified. It can be 1,2,3 or 4 based on which box type we are reading

# all barcodes of box types that were given to us
boxType1 = [0,6,6,6]
boxType2 = [0,6,0,6]
boxType3 = [0,0,6,6]
boxType4 = [0,6,6,0]

# this part of the code needs to figure out which types is barcode:

def Interperate(unitNumber):
    
    b1 = 0
    b2 = 0
    b3 = 0
    b4 = 0

    for i in range(4):
        if(colors[i] == boxType1[i]):
            b1 = b1 + 1
        if(colors[i] == boxType2[i]):
            b2 = b2 + 1
        if(colors[i] == boxType3[i]):
            b3 = b3 + 1
        if(colors[i] == boxType4[i]):
            b4 = b4 + 1

    if(b1 == 4):
        barcode = 1
    elif(b2 == 4):
        barcode = 2
    elif(b3 == 4):
        barcode = 3
    elif(b4 == 4):
        barcode = 4
    else:
        readAgain = True

    # checks if the barcode sensored is the same as desired one:
    if (barcode == Constants.Packages[unitNumber - 1][ 2]):
        Location.DetermineDumpLocation(Constants.Packages[unitNumber - 1][3])
        OSD.Draw("Box Type {0}; Correct Barcode Scanned".format(barcode))
        LocationX = Location.LocationXDump
        LocationY = Location.LocationYDump
        return True
    else:
        # display the location if the box does not match
        OSD.Draw("Box Type {0}; Incorrect Barcode Scanned".format(barcode))
        return False









    


