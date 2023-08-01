import streamlit as st 

st.header("Contact Me")

with st.form(key="email_form"):
    user_name = st.text_input("Your Name")
    user_email = st.text_input("Your email address:")
    message = st.text_area("Your messagem")
    button = st.form_submit_button("Submit")
    if button: 
        print("I was pressed")