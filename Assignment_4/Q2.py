import math

T = int(input("Enter no. of test cases: " ))


for i in range(T):
    a, b = map(int, input("Enter two numbers: ").split())  
    count = 0
    for num in range(a,b+1):
        if math.isqrt(num) ** 2 == num:
            count+=1

    if count>1:
        print(count)
    else:
        print("There are no perfect squares present in the range provided.")