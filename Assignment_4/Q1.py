T = int(input("Enter the number of test cases: "))
count = 0
for i in range(T):
    str = list(input())
    n = len(str)
    
    for j in range(n//2):
        if str[j] != str[n-j-1]:
            str[n-j-1]=str[j]
            count += 1
    
    print("".join(str))
    print(count)
    print("\n")