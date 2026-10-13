import streamlit as st
from openai import OpenAI

client = OpenAI(
    base_url = "https://openrouter.ai/api/v1",
    api_key = st.secrets["OPENROUTER_API_KEY"],
)

def responder(mensagens):
    resposta = client.chat.completions.create(
        model = "nvidia/nemotron-3-ultra-550b-a55b:free",
        messages = mensagens
    )
    return resposta.choices[0].message.content