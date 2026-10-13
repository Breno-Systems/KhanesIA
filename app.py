import streamlit as st

st.title("KhanesIA - Automation Center")

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for msg in st.session_state.mensagens:
    st.chat_message(msg["role"]).write(msg["content"])

prompt = st.chat_input("Figite algo...")

if prompt:
    st.session_state.mensagens.append({"role": "user", "content": prompt})
    st.session_state.mensagens.append({"role": "assistant", "content": "echo: " + prompt})
    st.chat_message("user").write(prompt)
    st.chat_message("assistant").write("echo: " + prompt)