import streamlit as st
import google.generativeai as genai

# Configura tu clave aquí
genai.configure(api_key=AIzaSyD6hmTYL7x_gIyMdBlWI9JXwdpNhrmNgcg)
model = genai.GenerativeModel('gemini-1.5-flash')

# Instrucciones de personalidad (Personalización guardada)
SYS_PROMPT = "Eres una influencer fitness de rasgos finos, ojos claros, pelo oscuro con coleta alta. Vistes ropa deportiva corta y ajustada. Estás en tu habitación y respondes de forma motivadora."

st.set_page_config(page_title="Fitness AI", layout="centered")
st.image("url_de_tu_influencer.jpg") # Aquí pondremos la foto que generemos

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("¿Qué entrenamos hoy?"):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    response = model.generate_content(f"{SYS_PROMPT}\nUsuario: {prompt}")
    st.session_state.chat_history.append({"role": "assistant", "content": response.text})
    st.rerun()
