import streamlit as st

st.set_page_config(page_title="Sauti Duka", page_icon="🛒")

# Language
if "swahili" not in st.session_state:
    st.session_state.swahili = False

def toggle_lang():
    st.session_state.swahili = not st.session_state.swahili

st.button("🇰🇪 Swahili" if not st.session_state.swahili else "🇬🇧 English", on_click=toggle_lang)

if st.session_state.swahili:
    title = "Sauti Duka - Duka la Sauti"
    rec_text = "🎙️ Chaguo 1: Gusa Kurekodi"
    up_text = "📁 Chaguo 2: Pakia Rekodi"
    hint_rec = "Gusa mic kurekodi sauti mpya"
    hint_up = "Chagua sauti kutoka simu - itaonyesha rekodi ZOTE"
    success = "Faili imepokewa! ✅"
    test = "Gusa kucheza sauti yako:"
    ready = "✅ Tayari kwa duka!"
    info = "👆 Rekodi au pakia ili kujaribu"
else:
    title = "Sauti Duka - Voice Shop"
    rec_text = "🎙️ Option 1: Tap to Record"
    up_text = "📁 Option 2: Upload Voice"
    hint_rec = "Tap mic to record new voice"
    hint_up = "Choose from phone - shows ALL recordings"
    success = "File received! ✅"
    test = "Tap to test your uploaded voice:"
    ready = "✅ Ready for shop!"
    info = "👆 Record or upload to test"

st.title(title)

# OPTION 1
st.subheader(rec_text)
audio_record = st.audio_input(hint_rec)

# OPTION 2 - FIXED: type=None shows ALL Samsung recordings
st.subheader(up_text)
uploaded = st.file_uploader(hint_up, type=None)

# Show audio
audio = audio_record if audio_record else uploaded

if audio:
    st.success(success)
    st.write(f"Size: {len(audio.getvalue())/1024:.1f} KB | Name: {audio.name if hasattr(audio, 'name') else 'recorded voice'}")
    st.write(f"**{test}**")
    st.audio(audio)
    st.success(ready)
    st.balloons()
else:
    st.info(info)
    st.write("If you can't see Voice 002.m4a: Tap Upload -> Browse files -> ☰ -> Audio -> Recordings")
