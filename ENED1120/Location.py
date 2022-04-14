import Constants

#all units in mm

#determine shelf location based on package number, shelf number, and package number
def DetermineShelfLocation(unitNumber):

    LocationXShelf = 0
    LocationYShelf = 0

    if (Constants.Packages[unitNumber - 1][0] == "A1"):
        LocationXShelf = 12 * 25.4
        LocationYShelf = 12 * 25.4
    elif (Constants.Packages[unitNumber - 1][0] == "A2"):
        LocationXShelf = 12 * 25.4
        LocationYShelf = 36 * 25.4
    elif (Constants.Packages[unitNumber - 1][0] == "B1"):
        LocationXShelf = 60 * 25.4
        LocationYShelf = 12 * 25.4
    elif (Constants.Packages[unitNumber - 1][0] == "B2"):
        LocationXShelf = 60 * 25.4
        LocationYShelf = 36 * 25.4
    elif (Constants.Packages[unitNumber - 1][0] == "C1"):
        LocationXShelf = 12 * 25.4
        LocationYShelf = 60 * 25.4
    elif (Constants.Packages[unitNumber - 1][0] == "C2"):
        LocationXShelf = 12 * 25.4
        LocationYShelf = 84 * 25.4
    elif (Constants.Packages[unitNumber - 1][0] == "D1"):
        LocationXShelf = 60 * 25.4
        LocationYShelf = 60 * 25.4
    elif (Constants.Packages[unitNumber - 1][0] == "D2"):
        LocationXShelf = 60 * 25.4
        LocationYShelf = 84 * 25.4
            
    if (Constants.Packages[unitNumber - 1][1] == 1):
        LocationXShelf = LocationXShelf + (0 * 25.4)
        LocationYShelf = LocationYShelf - (6 * 25.4)
    elif (Constants.Packages[unitNumber - 1][1] == 2):
        LocationXShelf = LocationXShelf + (6 * 25.4)
        LocationYShelf = LocationYShelf - (6 * 25.4)
    elif (Constants.Packages[unitNumber - 1][1] == 3):
        LocationXShelf = LocationXShelf + (12 * 25.4)
        LocationYShelf = LocationYShelf - (6 * 25.4)
    elif (Constants.Packages[unitNumber - 1][1] == 4):
        LocationXShelf = LocationXShelf + (18 * 25.4)
        LocationYShelf = LocationYShelf - (6 * 25.4)
    elif (Constants.Packages[unitNumber - 1][1] == 5):
        LocationXShelf = LocationXShelf + (24 * 25.4)
        LocationYShelf = LocationYShelf - (6 * 25.4)
    elif (Constants.Packages[unitNumber - 1][1] == 6):
        LocationXShelf = LocationXShelf + (30 * 25.4)
        LocationYShelf = LocationYShelf - (6 * 25.4)
    elif (Constants.Packages[unitNumber - 1][1] == 7):
        LocationXShelf = LocationXShelf + (7 * 25.4)
        LocationYShelf = LocationYShelf + (18 * 25.4)
    elif (Constants.Packages[unitNumber - 1][1] == 8):
        LocationXShelf = LocationXShelf + (13 * 25.4)
        LocationYShelf = LocationYShelf + (18 * 25.4)
    elif (Constants.Packages[unitNumber - 1][1] == 9):
        LocationXShelf = LocationXShelf + (19 * 25.4)
        LocationYShelf = LocationYShelf + (18 * 25.4)
    elif (Constants.Packages[unitNumber - 1][1] == 10):
        LocationXShelf = LocationXShelf + (25 * 25.4)
        LocationYShelf = LocationYShelf + (18 * 25.4)
    elif (Constants.Packages[unitNumber - 1][1] == 11):
        LocationXShelf = LocationXShelf + (31 * 25.4)
        LocationYShelf = LocationYShelf + (18 * 25.4)
    elif (Constants.Packages[unitNumber - 1][1] == 12):
        LocationXShelf = LocationXShelf + (37 * 25.4)
        LocationYShelf = LocationYShelf + (18 * 25.4)
    return LocationXShelf, LocationYShelf

#determine the location of the home position in mm
def DetermineDumpLocation(dumpLocation):

    LocationXDump = 0
    LocationYDump = 0

    if(dumpLocation == "B"):
        LocationXDump = 102 * 25.4
        LocationYDump = -6 * 25.4
    elif(dumpLocation == "C"):
        LocationXDump = 6 * 25.4
        LocationYDump = 114 * 25.4
    elif(dumpLocation == "D"):
        LocationXDump = 102 * 25.4
        LocationYDump = 114 * 25.4
    return LocationXDump, LocationYDump