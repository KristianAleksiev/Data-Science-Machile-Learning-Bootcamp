"""
Symbolic Computations:

Batch gradient descent using SymPy

from sympy import symbols, diff

# Setup - Resource intense!
multiplier = 0.1
max_iter = 500
params = np.array([1.8, 1.0]) # Initial guess

for n in range(max_iter):
    gradient_x = diff(f(a, b), a).evalf(subs={a:params[0], b:params[1]})
    gradient_y = diff(f(a, b), b).evalf(subs={a:params[0], b:params[1]})
    gradients = np.array([gradient_x, gradient_y])

    params = params - multiplier * gradients

print(f"Values in gradient array: {gradients}")
print(f"Minimum occurs at x value of: {params[0]}")
print(f"Minimum occurs at y value of: {params[1]}")
print(f"The cost is: {f(params[0], params[1])}")
"""