# getting values from customer
subtotal = eval(input("Please enter the subtotal: "))
gratuity = eval(input("Please enter the tip amount (as a %): "))

# change the gratuity value into a percentage
gratrate = gratuity / 100

# getting the tip and total amount
tip = gratrate * subtotal
total = tip + subtotal

# printing the values
print("Subtotal: $", "{:,.2f}".format(subtotal))
print("Tip: $", "{:,.2f}".format(tip))
print("Total: $", "{:,.2f}".format(total))
