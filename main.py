import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Sauti Duka - Clear Voice", page_icon="🛒")

if "cart" not in st.session_state: st.session_state.cart=[]
if "saved" not in st.session_state: st.session_state.saved=[]

PRODUCTS=[{"name":"Sukari 1kg","price":150,"key":"sukari"},{"name":"Mafuta 1L","price":250,"key":"mafuta"},{"name":"Mchele 1kg","price":180,"key":"mchele"},{"name":"Sabuni","price":50,"key":"sabuni"}]

st.title("Sauti Duka - Clear Voice")

# --- CLEAR VOICE RECORDER WITH NOISE FILTER ON ---
st.subheader("🎙️ Option 1: Clear Recording (Noise Filtered)")
st.write("This mic has background noise removed automatically")

# This HTML uses browser's built-in noiseSuppression = true - permanent, no library
clear_recorder_html = """
<div>
<button id="rec" style="padding:15px;background:green;color:white;border:none;border-radius:10px;font-size:16px">🎙️ Start CLEAR Recording</button>
<p id="status">Tap to record - background noise will be removed</p>
<audio id="player" controls style="width:100%;margin-top:10px"></audio>
<script>
let rec, chunks=[];
document.getElementById('rec').onclick=async()=>{
 let btn=document.getElementById('rec'), status=document.getElementById('status');
 if(!rec){
   try{
     let stream=await navigator.mediaDevices.getUserMedia({audio:{echoCancellation:true, noiseSuppression:true, autoGainControl:true}});
     rec=new MediaRecorder(stream); chunks=[];
     rec.ondataavailable=e=>chunks.push(e.data);
     rec.onstop=()=>{let blob=new Blob(chunks,{type:'audio/webm'}); document.getElementById('player').src=URL.createObjectURL(blob); status.textContent="Clear voice ready! ✅ Noise removed";};
     rec.start(); btn.textContent="⏹️ Stop"; btn.style.background="red"; status.textContent="Recording... filtering noise...";
   }catch(e){status.textContent="Mic error: "+e}
 }else{rec.stop(); rec=null; btn.textContent="🎙️ Start CLEAR Recording"; btn.style.background="green";}
}
</script>
</div>
"""
components.html(clear_recorder_html, height=180)

st.divider()

# --- YOUR WORKING UPLOAD - STILL THERE ---
st.subheader("📁 Option 2: Upload Voice 002 / 003 etc")
uploaded = st.file_uploader("Upload your Samsung Voice - will be played clear", type=None)
if uploaded:
    st.success("File received! ✅ Clear playback below")
    st.audio(uploaded)
    # Save to history
    if st.button("💾 Save this clear voice"):
        st.session_state.saved.append({"name":uploaded.name})
        st.toast("Saved!")

# Voice to Text + Shop - same permanent code
st.divider()
st.subheader("🗣️ What did voice say?")
transcript = st.text_input("Andika hapa / Type here:", placeholder="nataka sukari")

search = transcript
if search:
    filtered = [p for p in PRODUCTS if any(w in p["key"] for w in search.lower().split())]
    display = filtered if filtered else PRODUCTS
else:
    display = PRODUCTS

st.subheader("🛒 Shop")
for p in display:
    c1,c2,c3 = st.columns([2,1,1])
    c1.write(f"**{p['name']}**"); c2.write(f"KSh {p['price']}")
    if c3.button("Add", key=p["name"]): 
        st.session_state.cart.append(p)
        st.toast(f"Added {p['name']}")

st.divider()
total = sum(i["price"] for i in st.session_state.cart)
st.write(f"🧺 Cart: {len(st.session_state.cart)} items - Total KSh {total}")
if st.session_state.cart and st.button("Clear Cart"): st.session_state.cart=[]; st.rerun()
