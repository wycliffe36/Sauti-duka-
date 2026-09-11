
import streamlit as st

st.set_page_config(page_title="Sauti Duka", page_icon="🛒")

# Language toggle
if "swahili" not in st.session_state:
    st.session_state.swahili = False
def toggle():
    st.session_state.swahili = not st.session_state.swahili
st.button("🇰🇪 Swahili" if not st.session_state.swahili else "🇬🇧 English", on_click=toggle)

st.title("Sauti Duka - Voice Shop")

# Both options you asked for
st.subheader("🎙️ Option 1: Tap to Record")
audio_record = st.audio_input("Tap mic to record")

st.subheader("📁 Option 2: Upload Voice")
uploaded = st.file_uploader("Upload / Pakia sauti", type=["wav","mp3","m4a","ogg","opus"])

audio = audio_record if audio_record else uploaded

if audio:
    st.success("File received! ✅")
    st.write(f"Size: {len(audio.getvalue())/1024:.1f} KB")
    st.write("**Tap to test your uploaded voice:**")
    st.audio(audio)
    st.success("✅ Ready for shop!")
else:
    st.info("👆 Record or upload to test")
