T = int(input("Enter the number of test cases: "))

for i in range(T):
    K = int(input("Enter the number of cuts: "))

 
    vertical = K // 2
    horizontal= K - vertical

    max = vertical * horizontal

    print(max)
