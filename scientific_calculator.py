import streamlit as st
import math

# Streamlit app
st.title("Scientific Calculator")

# User input
num1 = st.number_input("Enter first number:", format="%.4f")
operation = st.selectbox("Select operation:", [
    "Add", "Subtract", "Multiply", "Divide", 
    "Square Root", "Power (x^y)"
])

if operation == "Square Root":
    if st.button("Calculate"):
        if num1 < 0:
            st.write("Cannot take the square root of a negative number!")
        else:
            result = math.sqrt(num1)
            st.write(f"√{num1} = {result}")

elif operation == "Power (x^y)":
    num2 = st.number_input("Enter second number:", format="%.4f")
    if st.button("Calculate"):
        result = math.pow(num1, num2)
        st.write(f"{num1} ^ {num2} = {result}")

else:
    num2 = st.number_input("Enter second number:", format="%.4f")
    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                result = "Cannot divide by zero!"
            else:
                result = num1 / num2
        
        st.write(f"The result is: {result}")
