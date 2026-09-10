import streamlit as st
import librosa
import soundfile as sf
import noisereduce as nr
import tempfile
import os

st.set_page_config(page_title="Sauti Duka", layout="centered")

if "swahili" not in st.session_state:
    st.session_state.swahili = False
def toggle_lang():
    st.session_state.swahili = not st.session_state.swahili
st.button("🇰🇪 Switch to Swahili" if not st.session_state.swahili else "🇬🇧 Switch to English", on_click=toggle_lang)

st.title("Sauti Duka - Voice Shop Assistant" if not st.session_state.swahili else "Sauti Duka - Msaidizi wa Duka")

uploaded_file = st.file_uploader(
    "Upload Voice Note / Pakia Sauti",
    type=["wav","mp3","m4a","opus","ogg","aac","mp4"],
)

if uploaded_file is not None:
    st.success("File received! ✅")
    
    # Save uploaded file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".m4a") as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name

    # Load audio
    y, sr = librosa.load(tmp_path, sr=16000)
    
    st.write("**Original (with noise):**")
    st.audio(uploaded_file)
    
    with st.spinner("Cleaning background noise for real..."):
        # Real noise reduction
        cleaned = nr.reduce_noise(y=y, sr=sr, prop_decrease=0.9)
        
        # Save cleaned
        cleaned_path = tmp_path.replace(".m4a", "_cleaned.wav")
        sf.write(cleaned_path, cleaned, sr)
    
    st.write("**Cleaned (noise removed):**")
    st.audio(cleaned_path)
    st.success("Noise removed! Kelele imeondolewa!" if not st.session_state.swahili else "Kelele imeondolewa!")
    
    # Transcription placeholder - you will add Whisper here
    st.write("**Ready for AMD Whisper transcription**")

    # Cleanup
    os.remove(tmp_path)
    if os.path.exists(cleaned_path):
        os.remove(cleaned_path)
