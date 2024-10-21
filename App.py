import streamlit as st
import math

# Custom CSS for better visuals
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #00c6ff, #0072ff);
        font-family: 'Arial', sans-serif;
        color: white;
    }
    .title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: #fff;
        margin-bottom: 20px;
    }
    .calculator {
        background-color: #f0f0f0;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        margin: 0 auto;
        max-width: 600px;
        text-align: center;
    }
    .selectbox, .number-input {
        background-color: #f0f0f0;
        border: none;
        border-radius: 8px;
        padding: 10px;
        font-size: 18px;
        color: #333;
        width: 100%;
    }
    .calculate-btn {
        background-color: #0072ff;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 18px;
        font-weight: bold;
        transition: background-color 0.3s;
    }
    .calculate-btn:hover {
        background-color: #005bb5;
    }
    .result-box {
        background-color: #0072ff;
        color: white;
        padding: 20px;
        border-radius: 8px;
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True
)

# App Title
st.markdown('<div class="title">💻 Scientific Calculator</div>', unsafe_allow_html=True)

# Create calculator container
with st.container():
    st.markdown('<div class="calculator">', unsafe_allow_html=True)
    
    # Dropdown for selecting operation
    operation = st.selectbox(
        "Select an operation:",
        ("Add ➕", "Subtract ➖", "Multiply ✖️", "Divide ➗", "Power", "Square Root √", "Logarithm (base 10) log₁₀", 
         "Logarithm (custom base) logₐ", "Factorial !", "Sine sin(θ)", "Cosine cos(θ)", "Tangent tan(θ)"),
        format_func=lambda x: x.split()[0]  # Cleaner look by removing icons from dropdown when opened
    )

    # Input fields based on selected operation
    if operation in ["Add ➕", "Subtract ➖", "Multiply ✖️", "Divide ➗", "Power"]:
        num1 = st.number_input("Enter the first number:", value=0.0, key="num1", format="%.2f")
        num2 = st.number_input("Enter the second number:", value=0.0, key="num2", format="%.2f")
    
    elif operation == "Square Root √":
        num1 = st.number_input("Enter the number:", value=0.0, key="sqrt_num", format="%.2f")
    
    elif operation == "Logarithm (base 10) log₁₀":
        num1 = st.number_input("Enter the number:", value=0.0, key="log_num", format="%.2f")

    elif operation == "Logarithm (custom base) logₐ":
        num1 = st.number_input("Enter the number:", value=0.0, key="log_custom_num", format="%.2f")
        base = st.number_input("Enter the base:", value=10.0, key="log_custom_base", format="%.2f")

    elif operation == "Factorial !":
        num1 = st.number_input("Enter a number (positive integer):", min_value=0, step=1, value=0, key="factorial_num")

    elif operation in ["Sine sin(θ)", "Cosine cos(θ)", "Tangent tan(θ)"]:
        angle = st.number_input("Enter the angle (in degrees):", value=0.0, key="angle", format="%.2f")

    # Calculation button
    if st.button("Calculate", key="calculate_btn", help="Click to perform the operation"):
        if operation == "Add ➕":
            result = num1 + num2
        elif operation == "Subtract ➖":
            result = num1 - num2
        elif operation == "Multiply ✖️":
            result = num1 * num2
        elif operation == "Divide ➗":
            result = "Error: Division by zero" if num2 == 0 else num1 / num2
        elif operation == "Power":
            result = num1 ** num2
        elif operation == "Square Root √":
            result = "Error: Cannot calculate square root of a negative number" if num1 < 0 else math.sqrt(num1)
        elif operation == "Logarithm (base 10) log₁₀":
            result = "Error: Logarithm is undefined for zero or negative numbers" if num1 <= 0 else math.log10(num1)
        elif operation == "Logarithm (custom base) logₐ":
            result = "Error: Logarithm is undefined for zero or negative numbers" if num1 <= 0 else math.log(num1, base)
        elif operation == "Factorial !":
            result = math.factorial(int(num1))
        elif operation == "Sine sin(θ)":
            result = math.sin(math.radians(angle))
        elif operation == "Cosine cos(θ)":
            result = math.cos(math.radians(angle))
        elif operation == "Tangent tan(θ)":
            try:
                result = math.tan(math.radians(angle))
            except:
                result = "Error: Undefined for tan(90° + n*180°)."

        # Display result
        st.markdown(f'<div class="result-box">Result: {result}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close calculator div
