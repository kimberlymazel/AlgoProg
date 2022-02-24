# getting the number of the packages
package = int(input("Please enter the number of packages purchased: "))

# if statements for the discount
if 10 <= package <= 19:
    discount = 0.10
elif 20 <= package <= 49:
    discount = 0.20
elif 50 <= package <= 99:
    discount = 0.30
elif package >= 100:
    discount = 0.40
else:
    discount = 0.00

# getting the discount amount and package values
packageval = package * 99
discpercent = int(discount * 100)
discamount = discount * packageval
totalamount = packageval - discamount

# printing the values
print("Discount Amount @", discpercent, "% : $ {:.2f}".format(discamount))
print("Total Amount: $ {:.2f}".format(totalamount))
