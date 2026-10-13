import streamlit as st

st.title("KhanesIA - Automation Center")

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for msg in st.session_state.mensagens:
    st.chat_message(msg["role"].write(msg["content"]))

prompt = st.chat_input()

if prompt:
    st.session_state.mensagens.append({"role": "user", "content": prompt})