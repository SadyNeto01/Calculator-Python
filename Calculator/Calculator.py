import math  # Import the math module for mathematical functions

# Define a function to add two numbers
def add(x, y):
    return x + y

# Define a function to subtract two numbers
def subtract(x, y):
    return x - y

# Define a function to multiply two numbers
def multiply(x, y):
    return x * y

# Define a function to divide two numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Error: Cannot divide by zero.")
        return None

# Define a function for square root
def square_root(x):
    return math.sqrt(x)

# Define a function for sine
def sine(x):
    return math.sin(math.radians(x))  # Convert degrees to radians

# Define a function for cosine
def cosine(x):
    return math.cos(math.radians(x))  # Convert degrees to radians

# Define a function for tangent
def tangent(x):
    return math.tan(math.radians(x))  # Convert degrees to radians

# Main function to take user input and perform calculations
def calculator():
    # Display the calculator menu
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Sine")
    print("7. Cosine")
    print("8. Tangent")

    # Get user input for operation
    choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

    # Check if the selected operation requires one or two numbers
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
    else:
        num1 = None

    if choice in ('1', '2', '3', '4'):
        num2 = float(input("Enter second number: "))
    else:
        num2 = None

    # Perform the selected operation
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    elif choice == '5':
        result = square_root(num1)
    elif choice == '6':
        result = sine(num1)
    elif choice == '7':
        result = cosine(num1)
    elif choice == '8':
        result = tangent(num1)
    else:
        print("Invalid input. Please enter a valid operation.")
        return

    # Display the result
    print("Result:", result)

# Call the calculator function
calculator()
