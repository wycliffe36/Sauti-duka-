
import streamlit as st
import tempfile, os
import librosa, soundfile as sf, noisereduce as nr

st.set_page_config(page_title="Sauti Duka", page_icon="🛒")

# Keep Swahili button
if "swahili" not in st.session_state:
    st.session_state.swahili = False
def toggle():
    st.session_state.swahili = not st.session_state.swahili
st.button("🇰🇪 Swahili" if not st.session_state.swahili else "🇬🇧 English", on_click=toggle)

st.title("Sauti Duka - Voice Shop Assistant")

# 1. DIRECT RECORD
st.subheader("🎙️ Option 1: Tap to Record")
audio_record = st.audio_input("Tap mic, speak, then tap stop")

# 2. UPLOAD BUTTON
st.subheader("📁 Option 2: Upload Voice Note")
uploaded_file = st.file_uploader(
    "Upload / Pakia",
    type=["wav","mp3","m4a","opus","ogg","aac","mp4","w4a"]
)

# Use whichever is used
audio_source = audio_record if audio_record is not None else uploaded_file

if audio_source is not None:
    st.success("File received! ✅")
    st.write(f"Size: {len(audio_source.getvalue())/1024:.1f} KB")
    
    st.write("**TEST 1 - Original (Tap to play and test):**")
    st.audio(audio_source)

    # Save
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_source.getvalue())
        tmp_path = tmp.name

    with st.spinner("Cleaning background noise..."):
        y, sr = librosa.load(tmp_path, sr=16000)
        cleaned = nr.reduce_noise(y=y, sr=sr, prop_decrease=0.9)
        cleaned_path = tmp_path.replace(".wav", "_clean.wav")
        sf.write(cleaned_path, cleaned, sr)

    st.write("**TEST 2 - Cleaned (No Background Noise - Tap to test):**")
    st.audio(cleaned_path)
    st.success("✅ Noise removed! Test both players above")

    # Cleanup
    try:
        os.remove(tmp_path)
    except:
        pass
else:
    st.info("👆 Record with mic OR upload a file from Download folder to test")
