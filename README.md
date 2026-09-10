# Sauti Duka 🛒 - Voice Shop Assistant

Built for AMD Developer Hackathon.

Problem: Small shopkeepers in Kenya get noisy voice notes in Swahili/English.

Solution: We clean noise and transcribe on AMD Cloud GPUs.

Features:
- Noise reduction with noisereduce
- Speech-to-text with Whisper (base)
- English / Swahili toggle button
- Runs on AMD GPUs (no local hardware needed)

How to run:
pip install -r requirements.txt
streamlit run main.py
