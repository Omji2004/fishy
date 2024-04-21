import streamlit as st

num1 = st.number_input('Enter first number')
num2 = st.number_input('Enter second number')
num3 = st.number_input('Enter third number')

largest_num = max(num1, num2, num3)

st.write('The largest number is', largest_num)
