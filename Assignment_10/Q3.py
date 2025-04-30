import numpy as np

def odd_magic(n):
    sq = np.zeros((n, n), dtype=int)
    r, c = 0, n // 2  

    for num in range(1, n * n + 1):
        sq[r, c] = num
        nr, nc = (r - 1) % n, (c + 1) % n  

        if sq[nr, nc]:  
            r += 1
        else:
            r, c = nr, nc

    return sq

def even_magic(n):
    sq = np.arange(1, n * n + 1).reshape(n, n)
    mask = np.zeros((n, n), dtype=bool)

    for r in range(n):
        for c in range(n):
            if (r % 4 == c % 4) or ((r % 4 + c % 4) == 3):  
                mask[r, c] = True

    sq[mask] = n * n + 1 - sq[mask]  
    return sq

def magic_square(n):
    if n % 2 == 1:
        return odd_magic(n)
    elif n % 4 == 0:
        return even_magic(n)
    else:
        return f"Single even magic squares (e.g., {n}) need a different method."

for N in [4, 5, 7, 8]:
    print(f"\nMagic Square for N={N}:\n", magic_square(N))
