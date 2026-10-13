import streamlit as st
import ia

st.title("KhanesIA - Automation Center")
st.page_config(
    page_title="KhanesIA",
    page_icon="✨"
)

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for msg in st.session_state.mensagens:
    st.chat_message(msg["role"]).write(msg["content"])

prompt = st.chat_input("Digite algo...")

if prompt:
    st.session_state.mensagens.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.spinner("Pensando..."):
        resposta = ia.responder_stream(st.session_state.mensagens)
        st.session_state.mensagens.append({"role": "assistant", "content": resposta})
    st.chat_message("assistant").write(resposta) 