# PYTHON PROGRAM TO FIND THE FACTORIAL OF A NUMBER.

# user input
num = int(input("Enter a number: "))


f = 1
for i in range(1, num + 1):          # iterating using for loop
    f *= i                           # Calculating factorial

# printing the result.
print(f"Factorial of entered number = {f}")

