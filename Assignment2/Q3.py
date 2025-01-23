T = int(input("Enter the number of test cases:"))

while T!=0:
    num = int(input("Enter a number:"))
    
    count = 0

    digits =[]
    for i in str(num):
        digits.append(int(i))

    for i in digits:
        if i!=0:
            if num % i == 0 :
                count+=1

    print(count)
    T-=1
