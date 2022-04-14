import Constants
import OSD
import Location

# black - 0, white - 1
# list of intigers (0 or 1)
# four members of list colors
# colors is an array with infomation from the light sensor
readAgain = False   # if the sensor does not get all data we want to read it again

# all barcodes of box types that were given to us
boxType1 = [0,1,1,1]
boxType2 = [0,1,0,1]
boxType3 = [0,0,1,1]
boxType4 = [0,1,1,0]

# this part of the code needs to figure out which types is barcode:

def Filter(data):
    colors = []
    c = 0
    counterState = 0
    counterDist = 0
    colors.append(data[0][0])

    for i in range(len(data)):
        if (colors[c] != data[i][0]):
            counterState = counterState + 1
        else:
            counterState = 0

        if (data[i - 1][0] == data[i][0]):
            counterDist = counterDist + 1
        else:
            counterDist = 0

        if ((counterState >= Constants.hitCount) or ((data[i][1] == c + 2) and(counterDist >= Constants.hitCount))):
            print(data[i][0])
            print(c)
            print(i)
            print('')
            c = c + 1
            counterState = 0
            counterDist = 0
            colors.append(data[i][0])
            
    return colors

def Interperate(unitNumber, data):

    colors = Filter(data)
    
    barcode = 0
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
        OSD.Draw("Box Type {0}\nCorrect\nBarcode\nScanned".format(barcode))
        return True
    else:
        # display the location if the box does not match
        OSD.Draw("Box Type {0}\nIncorrect\nBarcode\nScanned".format(barcode))
        return False

def NewInterperate(unitNumber, colors):

    barcode = 0

    if (colors[0] == 0):
        barcode = 3
    elif (colors[1] == 1):
        barcode = 2
    elif (colors[1] == 2):
        barcode = 1
    elif (colors[1] == 0):
        barcode = 4

    if (barcode == Constants.Packages[unitNumber - 1][ 2]):
        OSD.Draw("Box Type {0}\nCorrect\nBarcode\nScanned".format(barcode))
        return True
    else:
        # display the location if the box does not match
        OSD.Draw("Box Type {0}\nIncorrect\nBarcode\nScanned".format(barcode))
        return False
