import streamlit as st
import ia
import uuid
from supabase import create_client

st.set_page_config(
    page_title="KhanesIA",
    page_icon="✨"
)
st.title("KhanesIA - Automation Center")

@st.cache_resource
def get_supabase():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = get_supabase()

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "mensagens" not in st.session_state:
    resp = (
        supabase.table("chats")
        .select("role, content")
        .eq("session_id", st.session_state.session_id)
        .order("created_at")
        .execute
    )

    st.session_state.mensagens = resp.data if resp.data else []

for msg in st.session_state.mensagens:
    st.chat_message(msg["role"]).write(msg["content"])

prompt = st.chat_input("Digite algo...")

if prompt:
    st.session_state.mensagens.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    supabase.table("chats").insert({
    "session_id": st.session_state.session_id,
    "role": "user",
    "content": prompt
    }).execute()

    with st.spinner("Pensando..."):
        resposta = ia.responder_stream(st.session_state.mensagens)
    
    st.session_state.mensagens.append({"role": "assistant", "content": resposta})
    st.chat_message("assistant").write(resposta)

    supabase.table("chats").insert({
        "session_id": st.session_state.session_id,
        "role": "assistant",
        "content": resposta
    }).execute()