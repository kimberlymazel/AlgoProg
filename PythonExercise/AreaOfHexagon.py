# importing math for the sqrt and pow
import math

# getting the length of the side of the hexagon
length = eval(input("Please enter the side length of the hexagon: "))

# formula of area of the hexagon
top = 3 * math.sqrt(3)
formula = top/2
area = formula * math.pow(length, 2)

# printing the area of the hexagon
print("The area of a hexagon with side length", length, "is {:.3f}".format(area))
