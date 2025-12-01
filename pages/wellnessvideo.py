import streamlit as st
import random
import sys
import os

# --- 1. IMPORT FIX ---
# This tells Python: "Look in the folder above this one to find tab.py"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tab 

# --- 2. PAGE CONFIG ---
st.set_page_config(layout="wide", page_title="Acad&Me - Wellness")

# --- 3. INJECT LAYOUT ---
# This pulls the CSS, Theme, and Navbar (with the clickable logo) from tab.py
tab.render_css()
tab.render_top_buttons()
tab.render_navbar()

# --- 4. VIDEO PAGE CONTENT ---
vids = [
    "https://www.youtube.com/watch?v=tybOi4hjZFQ",      
    "https://www.youtube.com/watch?v=WPPPFqsECz0",      
    "https://www.youtube.com/watch?v=h2aWYjSA1Jc",      
    "https://www.youtube.com/watch?v=oBu-pQG6sTY",      
    "https://www.youtube.com/watch?v=TXU591OYOHA",      
    "https://www.youtube.com/watch?v=mWdb6qg2IOc",      
    "https://www.youtube.com/watch?v=poZBpvLTHNw",      
    "https://www.youtube.com/watch?v=6p_yaNFSYao",      
    "https://www.youtube.com/watch?v=goqqLfrXzhI",      
    "https://www.youtube.com/watch?v=nJzWpHLGWlY",      
    "https://www.youtube.com/watch?v=WfPqlTRFnLU"       
]

if 'last_video' not in st.session_state:
    st.session_state.last_video = vids[0]

# Add spacing
st.write("")
st.write("")

col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    st.markdown("<h2 style='text-align: center;'>Wellness Corner 🌿</h2>", unsafe_allow_html=True)
    
    # Video Player
    st.video(st.session_state.last_video)
    
    st.write("")
    
    # Center the button
    b1, b2, b3 = st.columns([1, 1, 1])
    with b2:
        if st.button("New Motivation Video 🎥", use_container_width=True):
            randvid = random.choice(vids)
            # Try not to repeat the same video
            while len(vids) > 1 and randvid == st.session_state.last_video:
                randvid = random.choice(vids)
            st.session_state.last_video = randvid
            st.rerun()