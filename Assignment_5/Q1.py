L = int(input())  
R = int(input())  

max = 0  

for A in range(L, R + 1):  
    for B in range(A, R + 1):  
        result = A ^ B  
        if result > max:  
            max = result  

print(max)
