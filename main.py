
import streamlit as st
import tempfile, os
import librosa, soundfile as sf, noisereduce as nr
from pydub import AudioSegment

st.set_page_config(page_title="Sauti Duka", page_icon="🛒")

if "swahili" not in st.session_state:
    st.session_state.swahili = False
def toggle():
    st.session_state.swahili = not st.session_state.swahili
st.button("🇰🇪 Swahili" if not st.session_state.swahili else "🇬🇧 English", on_click=toggle)

st.title("Sauti Duka")

st.subheader("🎙️ Option 1: Tap to Record")
audio_record = st.audio_input("Tap mic, speak")

st.subheader("📁 Option 2: Upload")
uploaded_file = st.file_uploader("Upload / Pakia", type=["wav","mp3","m4a","opus","ogg","aac","mp4"])

audio_source = audio_record if audio_record is not None else uploaded_file

if audio_source is not None:
    st.success("File received! ✅")
    st.write(f"Size: {len(audio_source.getvalue())/1024:.1f} KB")
    
    st.write("**TEST 1 - Original:**")
    st.audio(audio_source)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".m4a") as tmp_in:
        tmp_in.write(audio_source.getvalue())
        in_path = tmp_in.name
    
    wav_path = in_path + ".wav"
    
    with st.spinner("Cleaning background noise..."):
        try:
            # Convert m4a -> wav (fixes your error)
            sound = AudioSegment.from_file(in_path)
            sound = sound.set_frame_rate(16000).set_channels(1)
            sound.export(wav_path, format="wav")
            
            y, sr = librosa.load(wav_path, sr=16000)
            cleaned = nr.reduce_noise(y=y, sr=sr, prop_decrease=0.9)
            
            cleaned_path = in_path + "_clean.wav"
            sf.write(cleaned_path, cleaned, sr)
            
            st.write("**TEST 2 - Cleaned (No Background Noise):**")
            st.audio(cleaned_path)
            st.success("✅ Noise removed! Sasa hakuna kelele")
            
        except Exception as e:
            st.error(f"Still error: {e}")

    try:
        os.remove(in_path)
        if os.path.exists(wav_path):
            os.remove(wav_path)
    except:
        pass
else:
    st.info("👆 Record or upload to test")
