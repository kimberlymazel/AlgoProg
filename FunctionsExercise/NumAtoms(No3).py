# asking the user for the inputted values
element_amount = eval(input("Please enter the amount of the element in grams: "))
weight_optional = input("Do you want to enter the atomic weight of the element? Yes/No: ")

# if function for the optional second argument
if weight_optional == "Yes" or weight_optional == "yes":
    atomic_weight = eval(input("Please enter the atomic weight of the element: "))
    # allowing the user to input their own atomic weight
else:
    atomic_weight = 196.97  # default atomic weight of gold


# function that calculates the number of atoms present in the sample
def num_atoms(element_amount, atomic_weight):
    AVOGADRO = 6.022 * 10**23  # all capitals to show that it is a constant (avogadro's number)
    numatoms = (element_amount/atomic_weight) * AVOGADRO  # formula to calculate the number of atoms
    return numatoms


# printing the number of atoms present in the sample
print(num_atoms(element_amount, atomic_weight))
