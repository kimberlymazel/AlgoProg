class ShoppingListKM:
# initializer method
    def __init__(self, name, amount):  # parameters corresponding to name and amount of food
        self.__name = name  # name of item
        self.__amount = amount  # amount of items in pounds
        self.__price = self.__PriceListKM()  # price for respective items updated by private method
        self.__calcuprice = self.CostCalculateKM()  # calculated price for each item updated by public method


# private method storing list of items and respective price
    def __PriceListKM(self):
        if self.__name == "Dry Cured Iberian Ham":
            self.__price = 177.80
        elif self.__name == "Wagyu Steaks":
            self.__price = 450.00
        elif self.__name == "Matsutake Mushrooms":
            self.__price = 272.00
        elif self.__name == "Kopi Luwak Coffee":
            self.__price = 306.50
        elif self.__name == "Moose Cheese":
            self.__price = 487.20
        elif self.__name == "White Truffles":
            self.__price = 3600.00
        elif self.__name == "Blue Fin Tuna":
            self.__price = 3603.00
        elif self.__name == "Le Bonnotte Potatoes":
            self.__price = 270.81
        else:  # trailing else for items not on the list
            self.__price = 0.00

        return self.__price

# public method to calculate the cost
    def CostCalculateKM(self):
        self.__calcuprice = self.__amount * self.__price
        return self.__calcuprice

# accessor methods
    def getNameKM(self):
        return self.__name

    def getAmountKM(self):
        return self.__amount

    def getPriceKM(self):
        return self.__price

    def getCalcupriceKM(self):
        return self.__calcuprice
