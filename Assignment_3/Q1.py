def digitalroot(n):
    while n >= 10:
        digits = [int(digit) for digit in str(n)]
        n = sum(digits)
    return n

n = int(input().strip())
print(digitalroot(n))
