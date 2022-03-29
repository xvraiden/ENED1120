import Constants

LocationX = 0
LocationY = 0

def DetermineLocation(UnitNumber):
    match UnitNumber:
        case 1:
            match Constants.shelf1:
                case "A1":
                    LocationX = 12 * 25.4
                    LocationY = 12 * 25.4
                case "A2":
                    LocationX = 12 * 25.4
                    LocationY = 36 * 25.4
                case "B1":
                    LocationX = 60 * 25.4
                    LocationY = 12 * 25.4
                case "B2":
                    LocationX = 60 * 25.4
                    LocationY = 36 * 25.4
                case "C1":
                    LocationX = 12 * 25.4
                    LocationY = 60 * 25.4
                case "C2":
                    LocationX = 12 * 25.4
                    LocationY = 84 * 25.4
                case "D1":
                    LocationX = 60 * 25.4
                    LocationY = 60 * 25.4
                case "D2":
                    LocationX = 60 * 25.4
                    LocationY = 84 * 25.4

            match Constants.package1:
                case 1:
                    LocationX = LocationX + (3 * 25.4)
                case 2:
                    LocationX = LocationX + (9 * 25.4)
                case 3:
                    LocationX = LocationX + (15 * 25.4)
                case 4:
                    LocationX = LocationX + (21 * 25.4)
                case 5:
                    LocationX = LocationX + (27 * 25.4)
                case 6:
                    LocationX = LocationX + (33 * 25.4)
                case 7:
                    LocationX = LocationX + (3 * 25.4)
                    LocationY = LocationY + (12 * 25.4)
                case 8:
                    LocationX = LocationX + (9 * 25.4)
                    LocationY = LocationY + (12 * 25.4)
                case 9:
                    LocationX = LocationX + (15 * 25.4)
                    LocationY = LocationY + (12 * 25.4)
                case 10:
                    LocationX = LocationX + (21 * 25.4)
                    LocationY = LocationY + (12 * 25.4)
                case 11:
                    LocationX = LocationX + (27 * 25.4)
                    LocationY = LocationY + (12 * 25.4)
                case 12:
                    LocationX = LocationX + (33 * 25.4)
                    LocationY = LocationY + (12 * 25.4)
        case 2:
            match Constants.shelf2:
                case "A1":
                    LocationX = 12 * 25.4
                    LocationY = 12 * 25.4
                case "A2":
                    LocationX = 12 * 25.4
                    LocationY = 36 * 25.4
                case "B1":
                    LocationX = 60 * 25.4
                    LocationY = 12 * 25.4
                case "B2":
                    LocationX = 60 * 25.4
                    LocationY = 36 * 25.4
                case "C1":
                    LocationX = 12 * 25.4
                    LocationY = 60 * 25.4
                case "C2":
                    LocationX = 12 * 25.4
                    LocationY = 84 * 25.4
                case "D1":
                    LocationX = 60 * 25.4
                    LocationY = 60 * 25.4
                case "D2":
                    LocationX = 60 * 25.4
                    LocationY = 84 * 25.4

            match Constants.package2:
                case 1:
                    LocationX = LocationX + (3 * 25.4)
                case 2:
                    LocationX = LocationX + (9 * 25.4)
                case 3:
                    LocationX = LocationX + (15 * 25.4)
                case 4:
                    LocationX = LocationX + (21 * 25.4)
                case 5:
                    LocationX = LocationX + (27 * 25.4)
                case 6:
                    LocationX = LocationX + (33 * 25.4)
                case 7:
                    LocationX = LocationX + (3 * 25.4)
                    LocationY = LocationY + (12 * 25.4)
                case 8:
                    LocationX = LocationX + (9 * 25.4)
                    LocationY = LocationY + (12 * 25.4)
                case 9:
                    LocationX = LocationX + (15 * 25.4)
                    LocationY = LocationY + (12 * 25.4)
                case 10:
                    LocationX = LocationX + (21 * 25.4)
                    LocationY = LocationY + (12 * 25.4)
                case 11:
                    LocationX = LocationX + (27 * 25.4)
                    LocationY = LocationY + (12 * 25.4)
                case 12:
                    LocationX = LocationX + (33 * 25.4)
                    LocationY = LocationY + (12 * 25.4)
    