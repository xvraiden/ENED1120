import Constants
import OSD
import Location

# black - 1, white - 6
# list of intigers (6 or 1)
# four members of list colors
# colors is an array with infomation from the light sensor
colors = []
readAgain = false   # if the sensor does not get all data we want to read it again
b1 = 0
b2 = 0
b3 = 0
b4 = 0

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
        readAgain = true

    # checks if the barcode sensored is the same as desired one:
    match(unitNumber):
        # in first run
        case 1:
            if(barcode == Constants.barcode1):
                Location.DetermineDumpLocation(Constants.dump1)
                LocationX = Location.LocationXDump
                LocationY = Location.LocationYDump
                return True
            else:
                # display the location if the box does not match
                OSD.Draw("Box Type {0}".format(barcode))
                return False
        # in second run
        case 2:
            if(barcode == Constants.barcode2):
                Location.DetermineDumpLocation(Constants.dump2)
                LocationX = Location.LocationXDump
                LocationY = Location.LocationYDump
                return True
            else:
                # display the location if the box does not match
                OSD.Draw("Box Type {0}".format(barcode))
                return False








    


