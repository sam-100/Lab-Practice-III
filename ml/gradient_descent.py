# Problem Statement: 
# Implement Gradient Descent Algorithm to find the local minima of a function.
# For example, find the local minima of the function y=(x+3)² starting from the point x=2.

import numpy as np

def func(x):
    return (x-3)**2

def derivative(x):
    return 2*(x-3)

learning_rate = 0.1
max_iterations = 100
precision = 0.0001

x = 2

converged = False
for i in range(max_iterations):
    x_old = x
    gradient = derivative(x_old)
    x = x - gradient*learning_rate
    print(f"iteration {i}: x = {x} and f(x) = {func(x)}")
    print(f"absolute difference = {abs(func(x)-func(x_old))}")
    if abs(func(x)-func(x_old)) < precision:
        converged = True
        break    

if converged == True:
    print(f"We found convergence at x = {x} where value of function is {func(x)}")
else:
    print(f"No convergence found in {max_iterations} iterations!")

# Plot the function
import matplotlib.pyplot as plt

x_values = np.linspace(-2, 8, 100)
y_values = func(x_values)

plt.plot(x_values, y_values, label = '$(x-3)^2$')
plt.
plt.xlabel = 'x'
plt.ylabel = 'f(x)'
plt.title = 'Plot of the function f(x) = $(x-3)^2$'
plt.legend()
plt.grid(True)
plt.show()

help(np.linspace)

