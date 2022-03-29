import Constants

# black - 1, white - 6
# list of intigers (6 or 1)
# four members of  list colors
colors = []
b1 = 0
b2 = 0
b3 = 0
b4 = 0

# this part of the code needs to figure out which types is barcode:

boxType1 = [0,6,6,6]
boxType2 = [0,6,0,6]
boxType3 = [0,0,6,6]
boxType4 = [0,6,6,0]

bar1 = 0
bar2 = 0


for i in range(4):
    if(colors[i] == boxType1[i]):
        b1 = b1 + 1
    if(colors[i] == boxType2[i]):
        b2 = b2 + 1
    if(colors[i] == boxType3[i]):
        b3 = b3 + 1
    if(colors[i] == boxType4[i]):
        b4 = b4 + 1
    if(colors[i] == Constants.barcode1):
        bar1 = bar1 + 1
    if(colors[i] == Constants.barcode2):
        bar2 = bar2 + 1

if(bar1 == 4):
    
    # something
    # it is barcode 1
elif(bar2 == 4):
    # it is barcode 2
    
else:
    # move to another one

    


