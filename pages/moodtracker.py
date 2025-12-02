import streamlit as st
import pandas as pd
from datetime import datetime
import sys
import os

# --- 1. IMPORT FIX ---
# We keep this logic to ensure we find tab.py in the parent folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
try:
    import tab
except ImportError:
    st.error("Error: Could not find 'tab.py'. Please check your folder structure.")
    st.stop()

# --- PAGE CONFIG ---
st.set_page_config(page_title="Mood Tracker", page_icon="😊", layout="wide")

# --- 2. INJECT LAYOUT (Restored to prevent errors) ---
# We MUST call these to ensure the page structure loads correctly
tab.render_css() 
tab.render_top_buttons()
tab.render_navbar()

# --- 3. THE OVERRIDE (This removes the binary background) ---
st.markdown("""
<style>
    /* --- 1. REMOVE BINARY BACKGROUND IMAGE & FORCE DARK --- */
    .stApp {
        background-image: none !important;    /* Hides the binary pattern */
        background-color: #0E1117 !important; /* Sets the dark background */
        background-attachment: fixed;
        background-size: cover;
    }
    
    /* --- 2. FORCE TEXT TO WHITE --- */
    /* We use !important to override whatever tab.render_css() set */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, div, span, li {
        color: #FAFAFA !important;
    }

    /* --- 3. CUSTOM CARD & BUTTON STYLES --- */
    div.stButton > button {
        background: #2C2C2C !important;
        color: white !important;
        padding: 0.6rem 1rem;
        border-radius: 10px;
        border: none;
        transition: 0.2s;
    }
    div.stButton > button:hover {
        background: #44444 !important;
        color: white !important;
        border: 1px solid white !important;
    }

    .card {
        padding: 20px;
        background: rgba(255,255,255,0.05); /* Dark mode semi-transparent */
        border-radius: 15px;
        backdrop-filter: blur(5px);
        margin-bottom: 20px;
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    /* Fix for Chart Text Color */
    g.infolayer g.g-gtitle text {
        fill: white !important;
    }
    g.xtick text, g.ytick text {
        fill: white !important; 
    }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "mood_data" not in st.session_state:
    st.session_state.mood_data = []

# --- 4. PAGE CONTENT ---
c1, c2, c3 = st.columns([1, 6, 1])

with c2:
    # Title
    st.markdown("<h1 style='text-align:center; margin-bottom: 30px;'>😊 Mood Tracker</h1>", unsafe_allow_html=True)

    # Emoji Logic
    def mood_emoji(value):
        if value <= 2: return "😭"
        if value <= 4: return "😔"
        if value <= 6: return "😐"
        if value <= 8: return "🙂"
        return "🤩"

    # Input Card
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

    # History Section
    st.write("## 📈 Mood History")

    if st.session_state.mood_data:
        df = pd.DataFrame(st.session_state.mood_data)
        
        # Display Chart
        st.line_chart(df["mood"])

        # Display Data Table (Styled to ensure visibility)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No moods recorded yet. Start by rating your mood!")