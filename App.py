import streamlit as st
import math

# Custom CSS for styling the app
st.markdown(
    """
    <style>
    .title {
        font-size:48px;
        font-weight:bold;
        color:#4CAF50;
        text-align:center;
    }
    .calculator {
        background-color:#f0f0f0;
        padding:30px;
        border-radius:10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .button {
        background-color:#4CAF50;
        color:white;
        padding:10px 20px;
        border:none;
        border-radius:5px;
        cursor:pointer;
        font-size:16px;
        font-weight:bold;
    }
    .button:hover {
        background-color:#45a049;
    }
    </style>
    """, unsafe_allow_html=True
)

# App title
st.markdown('<div class="title">Scientific Calculator</div>', unsafe_allow_html=True)

# Create a container for the calculator with padding and background
with st.container():
    st.markdown('<div class="calculator">', unsafe_allow_html=True)
    
    # Create columns for better layout
    col1, col2 = st.columns(2)

    # Dropdown for selecting operation
    operation = st.selectbox(
        "Select an operation:",
        ("Add", "Subtract", "Multiply", "Divide", "Power", "Square Root", "Logarithm (base 10)", 
         "Logarithm (custom base)", "Factorial", "Sine", "Cosine", "Tangent")
    )

    # Input fields based on selected operation
    with col1:
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

    # Button to trigger the calculation
    with col2:
        if st.button("Calculate", key="calculate_button"):
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

            # Display the result in a nice box
            st.success(f"Result: {result}")

    st.markdown('</div>', unsafe_allow_html=True)  # Close calculator div

# Calculator functions
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

