# PYTHON PROGRAM TO REVERSE A GIVEN NO.

# user input
num = int(input("Enter a number: "))

sum = 0    # initializing sum as zero

while num != 0:
    digit = num % 10        # retreiving the last digit
    sum = sum*10 + digit    # adding the digit to the sum
    num = num // 10         # removing the last digit from the original number

print(sum)   #printing the result.
