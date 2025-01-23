import random

lst = []

count = 0 

for i in range(100):
    lst.append(random.randint(0,100))

    if lst[i]==0:
        count+=1
print(lst)
print("\n Number of zeroes present=",count)