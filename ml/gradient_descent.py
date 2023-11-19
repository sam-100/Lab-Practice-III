# Gradient Descent Algorithm

def gradient_descent(x, learning_rate, epochs):
    # Function to minimize: y = (x + 3)^2
    def function_to_minimize(x):
        return (x + 3)**2
    
    # Initialize variables
    x_values = [x]
    y_values = [function_to_minimize(x)]
    
    # Gradient Descent iterations
    for epoch in range(epochs):
        gradient = 2 * (x + 3)  # Gradient of the function
        x = x - learning_rate * gradient  # Update x using the gradient descent formula
        
        # Save current values for plotting
        x_values.append(x)
        y_values.append(function_to_minimize(x))
        
    return x_values, y_values

# Set initial parameters
initial_x = 2
learning_rate = 0.1
epochs = 50

# Run gradient descent
x_values, y_values = gradient_descent(initial_x, learning_rate, epochs)

# Print the result
print("Local Minimum:", x_values[-1])

# Plot the function and the steps taken by the gradient descent algorithm
import matplotlib.pyplot as plt

x_values_plot = [i for i in range(-8, 4)]
y_values_plot = [(x + 3)**2 for x in x_values_plot]

plt.plot(x_values_plot, y_values_plot, label='Function: y=(x + 3)^2')
plt.scatter(x_values, y_values, color='red', label='Gradient Descent Steps')
plt.title('Gradient Descent to Find Local Minimum')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
