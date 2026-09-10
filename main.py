import streamlit as st
import whisper
from audio_cleaner import clean_audio

st.set_page_config(page_title="Sauti Duka", page_icon="🛒")

LANG = {
    "EN": {
        "title": "Sauti Duka - Voice Shop Assistant",
        "subtitle": "Helping small shopkeepers sell with voice",
        "upload": "Upload customer voice note",
        "clean": "Cleaning noise...",
        "transcribe": "Transcribing on AMD GPU...",
        "result": "Customer wants:",
        "button": "Switch to Swahili"
    },
    "SW": {
        "title": "Sauti Duka - Msaidizi wa Sauti Dukani",
        "subtitle": "Kusaidia wajasiriamali wadogo kuuza kwa sauti",
        "upload": "Pakia sauti ya mteja",
        "clean": "Inasafisha kelele...",
        "transcribe": "Inatafsiri kwa AMD GPU...",
        "result": "Mteja anataka:",
        "button": "Badilisha kwa Kiingereza"
    }
}

if "lang" not in st.session_state:
    st.session_state.lang = "EN"

def toggle_lang():
    st.session_state.lang = "SW" if st.session_state.lang == "EN" else "EN"

t = LANG[st.session_state.lang]

st.button(t["button"], on_click=toggle_lang)
st.title(t["title"])
st.caption(t["subtitle"])

audio = st.file_uploader(t["upload"], type=["wav","mp3","m4a"])

if audio:
    with open("temp.wav","wb") as f:
        f.write(audio.getbuffer())
    
    st.info(t["clean"])
    clean_audio("temp.wav","clean.wav")
    
    st.info(t["transcribe"])
    model = whisper.load_model("base")
    lang_code = "sw" if st.session_state.lang == "SW" else "en"
    result = model.transcribe("clean.wav", language=lang_code)
    
    st.success(f'{t["result"]} {result["text"]}')
