import streamlit as st

st.title("Calulating PERIMETER and AREA")
length = st.number_input("input a length: ")
width = st.number_input("input a width: ")
click_button=st.button('calculate!!!')

if click_button:
    area = length * width
    perimeter = 2 * (length + width)
    st.write(f"area: {area}")
    st.write(f"perimeter: {perimeter}")
    st.write('YAYYYYYYY!!!')

