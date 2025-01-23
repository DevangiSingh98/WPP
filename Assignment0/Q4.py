# PYTHON PROGRAM TO SWAP TWO VARIABLES WITHOUT USING THIRD VARIABLE

# user input
x = int(input("Enter x: "))
y = int(input("Enter y: "))

print(f"you entered x = {x} and y = {y}")

# swapping
x = x + y
y = x - y
x = x - y

print("After swapping, ")

# printing the result.
print(f"x = {x} and y = {y}")
