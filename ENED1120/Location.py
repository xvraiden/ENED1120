import Constants

#all units in mm

#create locations for shelf and drop off locations
LocationXShelf = 0
LocationYShelf = 0

LocationXDump = 0
LocationYDump = 0

#determine shelf location based on package number, shelf number, and package number
def DetermineShelfLocation(unitNumber):
    match(Constants.Packages(unitNumber - 1, 0)):
        case "A1":
            LocationXShelf = 12 * 25.4
            LocationYShelf = 12 * 25.4
        case "A2":
            LocationXShelf = 12 * 25.4
            LocationYShelf = 36 * 25.4
        case "B1":
            LocationXShelf = 60 * 25.4
            LocationYShelf = 12 * 25.4
        case "B2":
            LocationXShelf = 60 * 25.4
            LocationYShelf = 36 * 25.4
        case "C1":
            LocationXShelf = 12 * 25.4
            LocationYShelf = 60 * 25.4
        case "C2":
            LocationXShelf = 12 * 25.4
            LocationYShelf = 84 * 25.4
        case "D1":
            LocationXShelf = 60 * 25.4
            LocationYShelf = 60 * 25.4
        case "D2":
            LocationX = 60 * 25.4
            LocationY = 84 * 25.4

    match(Constants.Packages(unitNumber - 1, 1)):
        case 1:
            LocationXShelf = LocationXShelf + (0 * 25.4)
            LocationYShelf = LocationYShelf - (6 * 25.4)
        case 2:
            LocationXShelf = LocationXShelf + (6 * 25.4)
            LocationYShelf = LocationYShelf - (6 * 25.4)
        case 3:
            LocationXShelf = LocationXShelf + (12 * 25.4)
            LocationYShelf = LocationYShelf - (6 * 25.4)
        case 4:
            LocationXShelf = LocationXShelf + (18 * 25.4)
            LocationYShelf = LocationYShelf - (6 * 25.4)
        case 5:
            LocationXShelf = LocationXShelf + (24 * 25.4)
            LocationYShelf = LocationYShelf - (6 * 25.4)
        case 6:
            LocationXShelf = LocationXShelf + (30 * 25.4)
            LocationYShelf = LocationYShelf - (6 * 25.4)
        case 7:
            LocationXShelf = LocationXShelf + (0 * 25.4)
            LocationYShelf = LocationYShelf + (18 * 25.4)
        case 8:
            LocationXShelf = LocationXShelf + (6 * 25.4)
            LocationYShelf = LocationYShelf + (18 * 25.4)
        case 9:
            LocationXShelf = LocationXShelf + (12 * 25.4)
            LocationYShelf = LocationYShelf + (18 * 25.4)
        case 10:
            LocationXShelf = LocationXShelf + (18 * 25.4)
            LocationYShelf = LocationYShelf + (18 * 25.4)
        case 11:
            LocationXShelf = LocationXShelf + (24 * 25.4)
            LocationYShelf = LocationYShelf + (18 * 25.4)
        case 12:
            LocationXShelf = LocationXShelf + (30 * 25.4)
            LocationYShelf = LocationYShelf + (18 * 25.4)



#determine the location of the home position in mm
def DetermineDumpLocation(dumpLocation):
    match(dumpLocation):
        case "B":
            LocationXDump = 102 * 25.4
            LocationYDump = -6 * 25.4
        case "C":
            LocationXDump = 6 * 25.4
            LocationYDump = 114 * 25.4
        case "D":
            LocationXDump = 102 * 25.4
            LocationYDump = 114 * 25.4