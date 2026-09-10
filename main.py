import streamlit as st
import tempfile, os
import librosa, soundfile as sf, noisereduce as nr

st.set_page_config(page_title="Sauti Duka")
st.title("Sauti Duka - Final")

audio = st.audio_input("🎙️ Tap mic")

if audio is not None:
    st.success("File received! ✅")
    st.audio(audio)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".m4a") as f:
        f.write(audio.getvalue())
        p = f.name

    y, sr = librosa.load(p, sr=16000)
    clean = nr.reduce_noise(y=y, sr=sr)
    
    out = p + "_clean.wav"
    sf.write(out, clean, sr)
    
    st.write("Cleaned - No noise:")
    st.audio(out)
