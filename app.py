import streamlit as st
from transformer import get_chatbot_answer  

st.title("Chatbot with Streamlit")


user_question = st.text_input("Ask a question about your data:")


if st.button("Get Answer"):
    
    answer = get_chatbot_answer(user_question)
    st.write("**Answer:**")
    st.write(answer)
