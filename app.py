import streamlit as st

def student_info(name,age):
    st.write(f"student's name: {name}")
    st.write(f"student's age: {age}")

# Title of the app
st.title("Student Information")

#widgets
name=st.text_input("Enter the student's name", value="")
age=st.slider("Enter the student's age", min_value=0, max_value=122, value=25)
if st.button("Display information"):
    student_info(name,age)
