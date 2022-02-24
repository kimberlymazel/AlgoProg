# importing math for the asin and degrees
import math

# getting the values for the formula
g = 9.8
mass = eval(input("Please enter the mass of the cart (in kg): "))
force = eval(input("Please enter the force to push the cart (in N): "))

# getting the angle from the formula and converting
formula = force/(mass*g)
sinangle = math.asin(formula)
degreeangle = math.degrees(sinangle)

# printing in one decimal place
print("The angle of the ramp is {:.1f}".format(degreeangle), "degrees")
