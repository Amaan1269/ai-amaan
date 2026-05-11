import streamlit as st

st.title("AI Demo Project")
st.write("This is my deployed AI/ML project")

user_input = st.text_input("Enter text")

if user_input:
    st.success(f"You entered: {user_input}")
