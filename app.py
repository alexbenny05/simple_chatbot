import streamlit as st
st.set_page_config(page_title="PICO")
st.title("PICO")
def chat_response(user_input):
    user_input=user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return"Hello i am PICO" 
    elif "your name" in user_input:
        return "I am a simple bot for fun"
    elif "joke" in user_input:
        return "why 6 is afraid of 7 because 7 8 9"
    elif "bye" in user_input:
        return "good bye"
    else:
        return "sorry doesnot understand"
user_input=st.text_input("You:")
if user_input:
    response=chat_response(user_input)
    st.text_area("Bot:",value=response,height=100)
