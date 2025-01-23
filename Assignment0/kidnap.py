# Codedocs admin Kidnap

T = int(input("Enter the number of test cases: "))


for i in range(T):
    N = int(input("Enter the number of boxes: ")) # No. of test cases
    X = int(input("Enter the current position of gold coin: ")) # current position of the gold coin
    S = int(input("Enter the number of swaps: ")) # No. of swaps
    
    for j in range(S):
        A = int(input("Enter the first box to swap: "))
        B = int(input("Enter the second box to swap: "))
        if X == A:
            X = B
        elif X == B:
            x = A
print(f"Current position of gold coin is : {X} ")
    