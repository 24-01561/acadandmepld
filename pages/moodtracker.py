import streamlit as st
import pandas as pd
from datetime import datetime
import sys
import os

# --- 1. IMPORT FIX ---
# This tells Python: "Look in the folder above this one to find tab.py"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tab 

# --- PAGE CONFIG ---
st.set_page_config(page_title="Mood Tracker", page_icon="😊", layout="wide")

# --- 2. INJECT LAYOUT ---
# This pulls the CSS, Theme, and Navbar from tab.py
# tab.render_css() handles the Background Image (Light) vs Solid Color (Dark)
tab.render_css() 
tab.render_top_buttons()
tab.render_navbar()

# --- 3. CUSTOM CSS ---
# Note: I removed the '.main' background override so tab.py can do its job.
st.markdown("""
<style>
    div.stButton > button {
        background: #2C2C2C;
        color: white;
        padding: 0.6rem 1rem;
        border-radius: 10px;
        border: none;
        transition: 0.2s;
    }
    div.stButton > button:hover {
        background: #7d6df2;
    }
    .card {
        padding: 20px;
        background: rgba(255,255,255,0.1); 
        border-radius: 15px;
        backdrop-filter: blur(5px);
        margin-bottom: 20px;
        border: 1px solid rgba(255,255,255,0.2);
    }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "mood_data" not in st.session_state:
    st.session_state.mood_data = []

# --- 4. LAYOUT FIX ---
# We use columns to create margins on the left and right ([1, 6, 1] ratio)
c1, c2, c3 = st.columns([1, 6, 1])

# All content goes inside the middle column (c2)
with c2:
    # --- TITLE ---
    st.markdown("<h1 style='text-align:center; margin-bottom: 30px;'>😊 Mood Tracker</h1>", unsafe_allow_html=True)

    # --- MOOD EMOJI LOGIC ---
    def mood_emoji(value):
        if value <= 2: return "😭"
        if value <= 4: return "😔"
        if value <= 6: return "😐"
        if value <= 8: return "🙂"
        return "🤩"

    # --- INPUT CARD ---
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("### How are you feeling today?")

    mood = st.slider("Rate your mood", 0, 10, 5)

    if st.button("Save Mood"):
        st.session_state.mood_data.append({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "mood": mood
        })
        st.success(f"Mood saved! {mood_emoji(mood)}", icon="💾")

    st.markdown("</div>", unsafe_allow_html=True)

    # --- HISTORY CHART ---
    st.write("## 📈 Mood History")

    if st.session_state.mood_data:
        df = pd.DataFrame(st.session_state.mood_data)

        # Display Line Chart
        st.line_chart(df["mood"])

        # Display Data Table
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No moods recorded yet. Start by rating your mood!")