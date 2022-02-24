# getting the coordinates
x1 = eval(input("Please enter the x value of the first coordinate: "))
y1 = eval(input("Please enter the y value of the first coordinate: "))

x2 = eval(input("Please enter the x value of the second coordinate: "))
y2 = eval(input("Please enter the y value of the second coordinate: "))

# formula for the slope
ycoord = y2-y1
xcoord = x2-x1

slopeformula = ycoord/xcoord

# coordinates put together
firstcoord = x1, y1
secondcoord = x2, y2

# printing the slope and coordinates
# formatting to 5 decimal places

print("The slope for the line that connects", firstcoord, "and", secondcoord, "is {:.5f}".format(slopeformula))
