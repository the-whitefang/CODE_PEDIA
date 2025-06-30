import streamlit as st
from insights_chatbot_2 import end_process

st.set_page_config(page_title="Your Personal Insight Chatbot", layout="wide")
st.title("Your Personal Insight Chatbot ")
st.markdown("Fire away your question !")

question = st.text_input("Your Question",placeholder="e.g., Show the average property value for customers without previous loans")

if question:
    with st.spinner("Analyzing. . . ."):
        response, error = end_process(question)

    if error:
        st.error(f"Error: {error}")
    else:
        st.success("Insight: ")
        st.write(response)