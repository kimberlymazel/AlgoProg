# getting the length of each edge of the triangle
edge1 = eval(input("Please enter the length of the first edge: "))
edge2 = eval(input("Please enter the length of the second edge: "))
edge3 = eval(input("Please enter the length of the third edge: "))

# formula for the perimeter
perimeter = edge1 + edge2 + edge3

# if statements to validate whether the two edges added are bigger than the last one
if edge1 + edge2 > edge3 and edge2 + edge3 > edge1 and edge1 + edge3 > edge2:
    print("The perimeter is", perimeter)
else:
    print("The perimeter cannot be calculated. The input is invalid.")
