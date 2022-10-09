""""
How a machine learns:
- Relationship in the data
1. Predict -> Theta Zero, Theta One
2. Calculate Error -> Measuring the quality of the prediction
3. Learn -> Adjusting the prediction
4. Go back to the Prediction based on the result of the process and repeat

Gradient descent - Steepest descent - Optimisation algo -> Min(f(x))
Cost functions (Loss functions, Objective functions):

"""


def gradient_descent(derivative_func, initial_guess, multiplier=0.02, precision=0.001):
    new_x = initial_guess
    x_values = [new_x]
    slope_values = [derivative_func(new_x)]

    for n in range(500):
        previous_x = new_x
        gradient = derivative_func(previous_x)
        new_x = previous_x - multiplier * gradient

        step_size = abs(new_x - previous_x)

        x_values.append(new_x)
        slope_values.append(derivative_func(new_x))

        if step_size < precision:
            break

    return new_x, x_values, slope_values


"""The plot:
local_min, list_x, deriv_list = gradient_descent(derivative_func=deriv_g, initial_guess=0)
plt.figure(figsize=[15, 5])

plt.subplot(1, 2, 1)

plt.xlim(-2, 2)
plt.ylim(0.5, 5.5)
plt.title("Cost function", fontsize=17)
plt.xlabel("X", fontsize=16)
plt.ylabel("g(x)", fontsize=16)
plt.plot(x_2, g(x_2), color="blue", linewidth=3, alpha=0.6)


plt.scatter(list_x, g(np.array(list_x)), color="red", s=100, alpha=0.6)

plt.subplot(1, 2, 2)
plt.title("Slope of the cost function", fontsize=17)
plt.xlabel("X", fontsize=16)
plt.ylabel("g' (x)'", fontsize=16)
plt.grid()
plt.xlim(-2, 2)
plt.ylim(-6, 8)

plt.plot(x_2, deriv_g(x_2), color="skyblue", linewidth=5, alpha=0.6)
plt.scatter(list_x, deriv_list, color="red", s=100, alpha=0.6)            
plt.show()

print(f"Local min occurs at: {local_min}")
print(f"Cost at this minimum is: {g(local_min)}")
print(f"Number of steps: {len(list_x)}")
"""
