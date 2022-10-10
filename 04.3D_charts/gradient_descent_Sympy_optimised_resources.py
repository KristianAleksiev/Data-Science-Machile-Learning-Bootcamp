"""
# Partial derivative functions
# With regard to X
def fpx(x, y):
    r = 3 ** (-x ** 2 - y ** 2)
    return 2 * x * log(3) * r / (r + 1) ** 2

# With regard to Y
def fpy(x, y):
    r = 3 ** (-x ** 2 - y ** 2)
    return 2 * y * log(3) * r / (r + 1) ** 2


# Setup
multiplier = 0.1
max_iter = 500
params = np.array([1.8, 1.0]) # Initial guess

for n in range(max_iter):
    gradient_x = fpx(params[0], params[1])
    gradient_y = fpy(params[0], params[1])
    gradients = np.array([gradient_x, gradient_y])

    params = params - multiplier * gradients

print(f"Values in gradient array: {gradients}")
print(f"Minimum occurs at x value of: {params[0]}")
print(f"Minimum occurs at y value of: {params[1]}")
print(f"The cost is: {f(params[0], params[1])}")



"""