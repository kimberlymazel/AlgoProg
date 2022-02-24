# importing math module to calculate gcd and fraction module to display in fraction format
import math
import fractions

# asking the user to input a positive numerator and denominator
numerator = eval(input("Please enter a positive numerator: "))
while numerator < 1:  # while loop to ensure that the numerator entered is more than 0
    print("The numerator inputted is not positive.")
    numerator = eval(input("Please enter a numerator that is positive: "))

denominator = eval(input("Please enter a positive denominator: "))
while denominator < 1:  # while loop to ensure that the denominator entered is more than 0
    print("The denominator inputted is not positive.")
    denominator = eval(input("Please enter a denominator that is positive: "))

# calculating the gdc using the function from the math module
gcd = math.gcd(numerator, denominator)

# converting the inputted numerator and denominator into reduced fraction form
rednumerator = numerator//gcd
reddenominator = denominator//gcd

# getting the mixed fraction for the improper fractions
first = int(numerator//denominator)  # whole number of mixed fraction
top = numerator % denominator  # the numerator of the mixed fraction which is the modulus
second = fractions.Fraction(top, denominator)  # the modulus over the denominator of the mixed fraction

# if else statements to check if the fraction is proper/improper and to reduce it into mixed or whole number
if numerator < denominator:  # if statement for proper fractions
    print("The fraction", numerator, "/", denominator, "is a proper fraction.")
    if gcd != 1:  # if statement that reduces the proper fraction if the gcd is not 1
        print("This proper fraction can be reduced into", rednumerator, "/", reddenominator)
    else:
        print("This proper fraction cannot be reduced any further.")
else:  # else statement for improper fractions
    print("The fraction", numerator, "/", denominator, "is an improper fraction.")
    if gcd != 1:  # if statement to reduce the improper fraction if the gcd is not 1
        print("This improper fraction can be reduced to", rednumerator, "/", reddenominator)
    else:
        print("This improper fraction cannot be reduced any further.")
    if second == 0:  # checks if the fraction is a whole number, if modulus/denominator is 0, it is a whole number.
        print("The whole number is", first)
    else:
        print("The mixed fraction is", first, "and", second)
