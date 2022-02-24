# asking the users for the values
earth_weight = eval(input("Please input your weight in pounds: "))  # weight on earth value
gravityOptional = input("Do you want to input a surface gravity? Yes/No: ")  # optional second argument

# if statement to determine the value for the second argument
if gravityOptional == "Yes" or gravityOptional == "yes":
    gravity = eval(input("Please input your gravity in m/s^2: "))
else:
    gravity = 23.1  # default gravity


# calc weight on planet function to calculate the new weight
def calc_weight_on_planet(earth_weight, gravity):
    mass = earth_weight / 9.8
    new_weight = mass * gravity
    return new_weight


# printing the new weight
print("Your weight on that planet is", calc_weight_on_planet(earth_weight, gravity))
