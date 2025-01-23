# PYTHON PROGRAM TO PRINT TABLE OF ANY NO.

# user input
num = int(input("Enter a number: "))

# using for loop to iterate and calculate table of the number
for i in range(1,11):
    result = num * i
    print(f"{num} x {i} = {result}")
