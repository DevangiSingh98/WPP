import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**3 - 6*x**2 + 11*x - 6

def bisection(f, a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    midpoints = []

    for _ in range(max_iter):
        c = (a + b) / 2
        midpoints.append(c)

        if abs(f(c)) < tol:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return np.array(midpoints)


np.random.seed(0)
x_vals = np.linspace(0, 5, 500)
f_vals = f(x_vals)

a, b = None, None
for i in range(len(x_vals)-1):
    if f_vals[i] * f_vals[i+1] < 0:
        a, b = x_vals[i], x_vals[i+1]
        break


midpoints = bisection(f, a, b)


x_plot = np.linspace(a-1, b+1, 400)
plt.plot(x_plot, f(x_plot), label='f(x)')
plt.axhline(0, color='gray', linestyle='--')
plt.plot(midpoints, f(midpoints), 'ro-', label='Bisection Steps')
plt.title('Bisection Method Root Finding')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
