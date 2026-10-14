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

    except Exception as e:
        raise RuntimeError(f"Erro na API/Streaming: {e}") from e