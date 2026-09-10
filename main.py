
import streamlit as st
import tempfile, os
import librosa, soundfile as sf, noisereduce as nr

st.set_page_config(page_title="Sauti Duka", page_icon="🛒")
st.title("Sauti Duka - Final Version")

# One recorder that works on Samsung Note 20 Chrome
audio = st.audio_input("🎙️ Tap mic and speak: 'Habari nataka mchele'")

if audio is not None:
    st.success("File received! ✅")
    st.write(f"File size: {len(audio.getvalue())/1000:.1f} KB")
    
    st.write("**1. Original:**")
    st.audio(audio)
    
    # Save temp
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio.getvalue())
        tmp_path = tmp.name

    # Clean noise
    with st.spinner("Removing background noise..."):
        y, sr = librosa.load(tmp_path, sr=16000)
        cleaned = nr.reduce_noise(y=y, sr=sr, prop_decrease=0.9)
        cleaned_path = tmp_path.replace(".wav", "_clean.wav")
        sf.write(cleaned_path, cleaned, sr)

    st.write("**2. Cleaned (No Noise):**")
    st.audio(cleaned_path)
    st.success("Done! Noise removed ✅")

    os.remove(tmp_path)
else:
    st.info("👆 Tap the mic above to record")
