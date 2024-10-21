import streamlit as st
import math

# Define the calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Error: Cannot calculate square root of a negative number."
    return math.sqrt(x)

def log(x, base=10):
    if x <= 0:
        return "Error: Logarithm is undefined for zero or negative numbers."
    return math.log(x, base)

def factorial(x):
    if x < 0:
        return "Error: Factorial of a negative number is undefined."
    return math.factorial(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    try:
        return math.tan(math.radians(x))
    except:
        return "Error: Undefined for tan(90° + n*180°)."

# Streamlit app structure
st.title("Scientific Calculator")

# Create a dropdown for operation selection
operation = st.selectbox(
    "Select an operation:",
    ("Add", "Subtract", "Multiply", "Divide", "Power", "Square Root", "Logarithm (base 10)", 
     "Logarithm (custom base)", "Factorial", "Sine", "Cosine", "Tangent")
)

# Input fields based on selected operation
if operation in ["Add", "Subtract", "Multiply", "Divide", "Power"]:
    num1 = st.number_input("Enter the first number:", value=0.0)
    num2 = st.number_input("Enter the second number:", value=0.0)
    
elif operation == "Square Root":
    num1 = st.number_input("Enter the number:", value=0.0)
    
elif operation == "Logarithm (base 10)":
    num1 = st.number_input("Enter the number:", value=0.0)

elif operation == "Logarithm (custom base)":
    num1 = st.number_input("Enter the number:", value=0.0)
    base = st.number_input("Enter the base:", value=10.0)

elif operation == "Factorial":
    num1 = st.number_input("Enter a number (positive integer):", min_value=0, step=1, value=0)

elif operation in ["Sine", "Cosine", "Tangent"]:
    angle = st.number_input("Enter the angle (in degrees):", value=0.0)

# Perform the operation when the button is clicked
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    elif operation == "Power":
        result = power(num1, num2)
    elif operation == "Square Root":
        result = sqrt(num1)
    elif operation == "Logarithm (base 10)":
        result = log(num1)
    elif operation == "Logarithm (custom base)":
        result = log(num1, base)
    elif operation == "Factorial":
        result = factorial(int(num1))
    elif operation == "Sine":
        result = sin(angle)
    elif operation == "Cosine":
        result = cos(angle)
    elif operation == "Tangent":
        result = tan(angle)

    # Display the result
    st.write(f"Result: {result}")
