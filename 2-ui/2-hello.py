import streamlit as st

st.title("Saying Hello!!!!")
name = st.text_input("And you are?")
age = st.number_input("How old are you?", min_value=0, max_value=120, step=1)

st.write(f"Hello,{name}!")
st.write(f"You are {age} years old.")

#TO COMPLETLEY RERUN STREAMLIT APP, USE THE "RERUN" BUTTON IN THE TOP RIGHT CORNER OF THE WEBSITE
#LINK TO THIS IS NUMBER 18501 AND HOMEWORK IS 28501
#CAN ONLY RUN ONE STREAMLIT APP AT A TIME, SO IF YOU ARE RUNNING ANOTHER APP, PLEASE CLOSE IT FIRST

button_state = st.button("Submit")
if button_state:
    st.write(f"hello, {name}!")
    st.write(f"Your age is {age} years old.")
