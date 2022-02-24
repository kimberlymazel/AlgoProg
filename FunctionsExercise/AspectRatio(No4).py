# prompting the users to input the current height and width and desired width
current_width = eval(input("Please enter the current width of the image: "))
current_height = eval(input("Please enter the current height of the image: "))
desired_width = eval(input("Please enter the desired width of the image: "))


# calc_new_height function to calculate the new height using the aspect ratio
def calc_new_height():
    aspect_ratio = current_height/current_width  # calculating the aspect ratio from the height and width
    new_height = aspect_ratio * desired_width  # calculating the new height by multiplying the width and aspect ratio
    return new_height


# printing the corresponding height
print("The corresponding height is:", calc_new_height())
