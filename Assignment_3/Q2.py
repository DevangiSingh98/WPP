T = int(input().strip())
for i in range(T):
    N = int(input().strip())
    a, b = 0, 1
    while b < N:
        a, b = b, a + b
    if b == N or N == 0:
        print("IsFibo")
    else:
        print("IsNotFibo")
