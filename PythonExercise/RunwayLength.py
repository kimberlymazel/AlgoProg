# getting the values for speed and acceleration
v = eval(input("Please enter the plane's take off speed in m/s: "))
a = eval(input("Please enter the plane's acceleration in m/s**2: "))

# getting the values for the formula
v2 = v ** 2
aa = 2 * a

# formula for the runway length
runway = v2/aa

# printing the runway length
print("The minimum runway length needed for this airplane is {:.4f}".format(runway), "meters.")