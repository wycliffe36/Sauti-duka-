import streamlit as st
import io

st.set_page_config(page_title="Sauti Duka", layout="centered")

# Language toggle
if "swahili" not in st.session_state:
    st.session_state.swahili = False

def toggle_lang():
    st.session_state.swahili = not st.session_state.swahili

st.button(
    "🇰🇪 Switch to Swahili" if not st.session_state.swahili else "🇬🇧 Switch to English",
    on_click=toggle_lang
)

# Title
if not st.session_state.swahili:
    st.title("Sauti Duka - Voice Shop Assistant")
    st.write("Upload any voice note (WhatsApp, Samsung Recorder) - m4a, opus, mp3, wav all work.")
else:
    st.title("Sauti Duka - Msaidizi wa Duka kwa Sauti")
    st.write("Pakia sauti yoyote (WhatsApp, Samsung) - m4a, opus, mp3, wav zote zinafanya kazi.")

# THE FIX: Accept ALL Samsung formats
uploaded_file = st.file_uploader(
    "Upload Voice Note / Pakia Sauti" if not st.session_state.swahili else "Pakia Sauti Yako",
    type=["wav", "mp3", "m4a", "opus", "ogg", "aac", "w4a", "mp4"],
    accept_multiple_files=False
)

if uploaded_file is not None:
    st.success("File received! ✅" if not st.session_state.swahili else "Faili limepokelewa! ✅")
    
    # Show audio player - this will play your Samsung recording
    st.audio(uploaded_file, format='audio/m4a')
    
    st.info("Cleaning background noise..." if not st.session_state.swahili else "Inasafisha kelele...")
    
    # Demo for now - your AMD Whisper will go here
    st.warning("Transcribing on AMD GPU..." if not st.session_state.swahili else "Inatafsiri kwenye AMD GPU...")
    
    # Simulated result - you will replace with real transcription later
    if not st.session_state.swahili:
        st.write("### Transcription:")
        st.write("> 'Habari, nataka mchele kilo mbili'")
        st.write("### Detected Intent: Order Rice 2kg")
    else:
        st.write("### Unukuzi:")
        st.write("> 'Habari, nataka mchele kilo mbili'")
        st.write("### Nia: Kuagiza Mchele kilo 2")

else:
    if not st.session_state.swahili:
        st.info("👆 Tap 'Browse files' above and select your recording from Samsung folder")
    else:
        st.info("👆 Bonyeza 'Browse files' hapo juu na chagua rekodi yako")
