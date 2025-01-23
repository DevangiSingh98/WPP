# PYTHON PROGRAM TO CALCULATE FACTORIAL OF A NO.

# user input
num = int(input("Enter a number: "))


f = 1
for i in range(1, num + 1):          # iterating using for loop
    f *= i                           # Calculating factorial

# printing the result.
print(f"Factorial of entered number = {f}")
