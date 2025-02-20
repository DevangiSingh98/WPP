t = int(input("Enter the number of test cases: "))

for _ in range(t):
    w = list(input("Enter the word: "))

    i = len(w) - 2
    while i >= 0 and w[i] >= w[i + 1]:
        i -= 1

    if i == -1:
        print("no answer")
    else:
        j = len(w) - 1
        while w[j] <= w[i]:
            j -= 1

        w[i], w[j] = w[j], w[i]     #swap
        
        w = w[:i + 1] + sorted(w[i + 1:])
        print("".join(w))
