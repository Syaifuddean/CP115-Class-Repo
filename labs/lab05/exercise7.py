import math
one_number = float(input("Enter one number: "))
square_root = math.hypot(one_number, 2)
square = one_number ** 2
cube = one_number ** 3
sine = math.sin(one_number)

print("The square root of " + str(one_number) + " is: " + str(square_root))
print("The square of " + str(one_number) + " is: " + str(square))
print("The cube of " + str(one_number) + " is: " + str(cube))
print("The sine of " + str(one_number) + " is: " + str(sine))