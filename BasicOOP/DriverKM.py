# importing class module
from ClassDefKM import ShoppingListKM

# function that creates list of objects
def ItemListKM():
    li = []
    itemcount = 0

    # loop for if number of items is less than 1
    while itemcount < 1:
        itemcount = int(input("How many items will you order today? "))
        if itemcount < 1:
            print("Number of items must be at least 1.")

    for i in range(itemcount):
        print(f"Item #{i+1}-")  # item label (Item #1-)

        name = str(input("Enter food: "))

        # loop for if amount of pounds is less than or equal to 0
        amount = 0
        while amount <= 0:
            amount = eval(input("Enter amount of pounds: "))
            if amount <= 0:
                print("Amount of pounds must be greater than 0.")
        print()  # for spacing in between items
        li.append(ShoppingListKM(name, amount))
    return li

# function to display list
def ListDisplayKM(foodlist):
    print("Here's a summary of the items purchased:")
    print("---------------------------------------------")
    for ShoppingListKM in foodlist:  # for loop printing all items entered
        print(f"Item: {ShoppingListKM.getNameKM()}")
        print(f"Amount ordered: {ShoppingListKM.getAmountKM():.1f} pounds")
        print(f"Price per pound: ${ShoppingListKM.getPriceKM():.2f}")
        print(f"Price of order: ${ShoppingListKM.getCalcupriceKM():.2f}")
        print()  # spacing

# function for total price
def TotalPriceKM(foodlist):
    total = 0
    for i in foodlist:
        total = i.getCalcupriceKM() + total
    print("Total cost: ${:.2f}".format(total))  # printing total cost to 2 decimal places

# main function to call the functions
def main():
    foodlist = ItemListKM()  # variable for values from ItemListKM function
    ListDisplayKM(foodlist)  # displays list of items
    TotalPriceKM(foodlist)  # displays total price


main()  # runs main function

