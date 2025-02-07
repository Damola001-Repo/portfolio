import streamlit as st
from send_email import  send_mail


st.title('Contact Me')

form = st.form(key='form')

with form:
    email = st.text_input(label='Your Email Address')
    raw_message = st.text_area(label='Write message')
    button = st.form_submit_button('Send')
    message = f"""\
Subject: New mail

From: {email}    
{raw_message}
    """


    if button:
        send_mail(message)
        st.info('Your email was sent successfully!')