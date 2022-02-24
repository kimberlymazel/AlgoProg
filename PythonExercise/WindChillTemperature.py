# getting the temperature
temp = eval(input("Enter a temperature between -58 degrees Fahrenheit and 41 degrees Fahrenheit: "))

# while loop for temperature
while -58 > temp or temp > 41:
    print("Input was not in range. Please re-enter a value between -58 degrees and 41 degrees Fahrenheit.")
    temp = eval(input("Re enter value: "))

# getting the wind speed
speed = eval(input("Enter wind speed that is greater or equal to 2mph: "))

# while loop for wind speed
while speed < 2:
    print("Input was not above or equal to 2mph.")
    speed = eval(input("Re-enter a value: "))

# formula for wind chill temperature
windchill = 35.74 + (0.6215 * temp) - (35.75 * (speed ** 0.16)) + (0.4275 * (temp * (speed ** 0.16)))

# printing the wind chill index to 3 decimal places
print("The wind chill index is {:.3f}".format(windchill))
