from openai import OpenAI

API_KEY = st.secrets["OPENROUTER_API_KEY"]
base_orl = "https://openrouter.ai/api/v1"

def responder(mensagens):
    resposta = client.chat.completions.create(
        model = "nvidia/nemotron-3-ultra-550b-a55b:free",
        messages = mensagens
    )
    return resposta.choices[0].message.content