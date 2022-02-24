# function convert_temp to prompt the user to input a fahrenheit temperature
def convert_temp():
    temperature = eval(input("Please enter a temperature in Fahrenheit: "))
    return temperature


# declaring a variable so that the value of convert_temp becomes a global variable
fahrenheit = convert_temp()


# function convert_to_celsius to calculate the temperature in celsius
def convert_to_celsius(fahrenheit):  # argument is the result from convert_temp
    celsius_temp = 5/9 * (fahrenheit - 32)
    return celsius_temp


# value of convert_to_celsius but made into a global variable
celsius = convert_to_celsius(fahrenheit)


# function convert_to_kelvin to calculate the temperature in kelvin
def convert_to_kelvin(celsius):  # argument is the global variable that has convert_to_celsius value
    kelvin_temp = celsius + 273.15
    return kelvin_temp


# global variable of result of convert_to_kelvin function
kelvin = convert_to_kelvin(celsius)


# printing the values of the temperature in fahrenheit, celsius and kelvin
print("The temperature in Fahrenheit is:", fahrenheit)
print("The temperature in Celsius is:", celsius)
print("The temperature in Kelvin is:", kelvin)
