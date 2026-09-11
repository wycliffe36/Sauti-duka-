import streamlit as st

st.set_page_config(page_title="Sauti Duka - Complete", page_icon="🛒")

# --- SAVE IN MEMORY ---
if "cart" not in st.session_state:
    st.session_state.cart = []
if "saved_voices" not in st.session_state:
    st.session_state.saved_voices = []
if "swahili" not in st.session_state:
    st.session_state.swahili = False

def toggle_lang():
    st.session_state.swahili = not st.session_state.swahili

# Products for shop
PRODUCTS = [
    {"name": "Sukari 1kg", "price": 150, "key": "sukari sugar"},
    {"name": "Mafuta 1L", "price": 250, "key": "mafuta oil"},
    {"name": "Mchele 1kg", "price": 180, "key": "mchele rice"},
    {"name": "Sabuni", "price": 50, "key": "sabuni soap"},
]

# UI Language
st.button("🇰🇪 Swahili" if not st.session_state.swahili else "🇬🇧 English", on_click=toggle_lang)
is_sw = st.session_state.swahili

st.title("Sauti Duka - Voice Shop" if not is_sw else "Sauti Duka - Duka la Sauti")

# --- 1. VOICE UPLOAD (your working part) ---
st.subheader("🎙️ Option 1: Tap to Record" if not is_sw else "🎙️ Chaguo 1: Gusa Kurekodi")
audio_record = st.audio_input("Tap mic to record" if not is_sw else "Gusa mic kurekodi")

st.subheader("📁 Option 2: Upload Voice" if not is_sw else "📁 Chaguo 2: Pakia Sauti")
uploaded = st.file_uploader("Shows ALL recordings - Voice 003.m4a etc", type=None)

audio = audio_record if audio_record else uploaded
transcript = ""

if audio:
    st.success("File received! ✅")
    st.audio(audio)
    
    # --- 2. VOICE TO TEXT (light version - no heavy library) ---
    st.divider()
    st.subheader("🗣️ Voice to Text / Sauti kwa Maandishi")
    st.write("What did customer say in this voice? (Andika alichosema)")
    
    # This is where voice becomes text - you type what you hear
    # Later we can add auto AI, but this works 100% today
    transcript = st.text_input(
        "Transcript:", 
        placeholder="Example: nataka sukari na mafuta",
        key=f"trans_{len(st.session_state.saved_voices)}"
    )
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💾 Save Voice + Text"):
            st.session_state.saved_voices.append({
                "name": audio.name if hasattr(audio, 'name') else f"Voice {len(st.session_state.saved_voices)+1}",
                "transcript": transcript,
                "data": audio.getvalue()
            })
            st.success("Saved!")
    with col2:
        if st.button("🔍 Search Shop with Voice"):
            st.session_state.search_query = transcript

# --- 3. SHOP ---
st.divider()
st.subheader("🛒 Shop / Bidhaa")

search = st.session_state.get("search_query", "") or transcript
if search:
    st.info(f"Searching for: '{search}'")
    # Filter products by voice transcript
    filtered = [p for p in PRODUCTS if any(word in p["key"] for word in search.lower().split())]
    display_products = filtered if filtered else PRODUCTS
    if filtered:
        st.success(f"Found {len(filtered)} from your voice!")
else:
    display_products = PRODUCTS

for p in display_products:
    c1, c2, c3 = st.columns([2,1,1])
    c1.write(f"**{p['name']}**")
    c2.write(f"KSh {p['price']}")
    if c3.button("Add", key=p['name']):
        st.session_state.cart.append(p)
        st.toast(f"Added {p['name']}")

# Cart
st.divider()
st.subheader(f"�asket Cart ({len(st.session_state.cart)})")
if st.session_state.cart:
    total = sum(item["price"] for item in st.session_state.cart)
    for item in st.session_state.cart:
        st.write(f"- {item['name']} - KSh {item['price']}")
    st.write(f"**Total: KSh {total}**")
    if st.button("Clear Cart"):
        st.session_state.cart = []
        st.rerun()
else:
    st.write("Cart empty / Mkokoteni mtupu")

# --- 4. SAVED VOICES HISTORY ---
st.divider()
st.subheader(f"📜 Saved Voices ({len(st.session_state.saved_voices)})")
if st.session_state.saved_voices:
    for i, v in enumerate(reversed(st.session_state.saved_voices)):
        st.write(f"**{v['name']}**: _{v['transcript']}_")
else:
    st.write("No saved voices yet")
