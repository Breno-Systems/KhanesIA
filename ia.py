import streamlit as st
from openai import OpenAI

@st.cache_resource
def get_client():
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=st.secrets["OPENROUTER_API_KEY"],
        default_headers={
            "HTTP-Referer": "https://khanesia-dev.streamlit.app", # Coloque sua URL real depois
            "X-Title": "KhanesIA Automation Center",
        }
    )

client = get_client()

def responder_stream(mensagens):
    resposta = client.chat.completions.create(
        model = "nvidia/nemotron-3-ultra-550b-a55b:free",
        messages = mensagens
    )

        # --- DIAGNÓSTICO ---
    print("=== RESPOSTA BRUTA DA API ===")
    print(resposta)          # Mostra o objeto todo no terminal/logs do Streamlit Cloud
    print("=============================")
    
    return resposta.choices[0].message.content