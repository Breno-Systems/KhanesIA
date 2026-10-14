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
    try:
        stream = client.chat.completions.create(model = "nvidia/nemotron-3-ultra-550b-a55b:free",
            messages = mensagens,
            stream=True
        )

        for chunk in stream:
            if not chunk.choices:
                continue

            delta = chunk.choices[0].delta
            conteudo = getattr(delta, "content", None)

            if conteudo:
                yield conteudo

        if hasattr(conteudo, "error") and conteudo.error:
            msg = conteudo.error.get("message", "Erro desconhecido da API")
            code = conteudo.error.get("code", "N/A")
            raise RuntimeError (f"Erro da API ({code}): {msg}")

        if not conteudo.choices:
            raise RuntimeError("Resposta da API vazia: 'choices' não encontrado ou nulo") 

        return stream.choices[0].message.content
    
    except Exception as e: raise RuntimeError(f"Erro de conexão com a API: {e}")