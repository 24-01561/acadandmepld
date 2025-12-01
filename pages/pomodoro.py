import streamlit as st
import time
import sys
import os

# --- 1. CONFIG: WIDE MODE ---
st.set_page_config(page_title="Pomodoro", page_icon="🍅", layout="wide")

# --- 2. IMPORT LAYOUT ---
try:
    import tab
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    import tab 

# --- 3. INJECT LAYOUT ---
tab.render_css() 
tab.render_top_buttons()
tab.render_navbar()

# --- Constants ---
W = 25 * 60
S = 5 * 60
L = 15 * 60
CYCLES = 4

# --- Utility Functions ---
def format_time(s):
    return f"{int(s // 60):02d}:{int(s % 60):02d}"

def get_time(phase):
    if phase == "work":
        return W
    if phase == "short_break":
        return S
    return L

# --- Control Functions ---
def start_pause():
    st.session_state.running = not st.session_state.running

def set_phase(new_phase):
    st.session_state.phase = new_phase
    new_time = get_time(new_phase)
    st.session_state.time_remaining = new_time
    st.session_state.total_duration = new_time
    st.session_state.running = False

def move_next():
    current = st.session_state.phase
    cycles = st.session_state.cycles

    if current == "work":
        cycles += 1
        st.session_state.cycles = cycles
        next_p = "long_break" if cycles % CYCLES == 0 else "short_break"
    else:
        next_p = "work"
    
    set_phase(next_p)

# --- CSS Styling ---
def local_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@700&display=swap');

        /* Hide Streamlit default UI */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Motivational Banner */
        .quote-box {
            background-color: white;
            border: 1px solid black;
            box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
            padding: 15px;
            text-align: center;
            border-radius: 10px;
            margin-bottom: 20px;
            font-size: 20px;
            font-weight: 700;
            color: black;
            max-width: 600px;
            margin: 0 auto 20px auto;
        }
        
        /* Main Card */
        .main-card {
            background-color: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            max-width: 600px;
            margin: 0 auto 20px auto;
        }

        /* Status Bar Styles */
        .status-bar {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 10px;
        }
        
        .status-item {
            font-size: 14px;
            color: #aaa;
            font-weight: 700;
            padding: 8px 16px;
            border-radius: 20px;
            background-color: #f0f0f0;
        }
        
        /* Active Status Highlight */
        .status-active {
            color: #0D2F64;
            background-color: #FFDB5B; 
            border: 1px solid #0D2F64;
        }

        /* Typography */
        .phase-title {
            color: #020030;
            font-size: 48px;
            font-weight: 700;
            margin-bottom: 0px;
            margin-top: 0px;
        }
        
        .timer-display {
            color: #0D2F64;
            font-size: 96px;
            font-weight: 700;
            line-height: 1;
            margin-top: 10px;
        }

        /* --- TIMER BUTTONS FIX (Targeted) --- */
        /* We now target buttons ONLY inside the .timer-controls container */
        .timer-controls div[data-testid="stButton"] {
            display: flex;
            justify-content: center;
        }

        .timer-controls div[data-testid="stButton"] > button {
            width: 100%;
            max-width: 600px !important; 
            
            /* Ensure buttons are tall and chunky */
            min-height: 55px !important; 
            padding-top: 10px !important;
            padding-bottom: 10px !important;
            
            border-radius: 12px !important;
            font-family: 'Quicksand', sans-serif !important;
            font-weight: 700 !important;
            font-size: 20px !important; 
            
            /* Visual Styles: Light Grey + Black Border */
            border: 2px solid #000000 !important;
            box-shadow: 0px 4px 0px rgba(0, 0, 0, 0.2) !important;
            background-color: #D9D9D9 !important; 
            color: #0D2F64 !important;             
            transition: all 0.1s;
            margin-bottom: 10px;
        }
        
        .timer-controls div[data-testid="stButton"] > button:hover {
            transform: translateY(-2px);
            background-color: #e6e6e6 !important;
            box-shadow: 0px 6px 0px rgba(0, 0, 0, 0.2) !important;
        }
        
        .timer-controls div[data-testid="stButton"] > button:active {
            transform: translateY(2px);
            box-shadow: 0px 2px 0px rgba(0, 0, 0, 0.2) !important;
        }
    </style>
    """, unsafe_allow_html=True)

# --- Main App ---

def pomodoro_app():
    if "phase" not in st.session_state:
        st.session_state.phase = "work"
        st.session_state.time_remaining = W
        st.session_state.total_duration = W
        st.session_state.running = False
        st.session_state.cycles = 0

    local_css()

    st.write("##")

    # --- LAYOUT WITH COLUMNS ---
    left_col, center_col, right_col = st.columns([1, 1.5, 1])

    with center_col:
        # Banner
        st.markdown('<div class="quote-box">✨ Keep going, you got this. ✨</div>', unsafe_allow_html=True)

        # --- Status Bar ---
        current = st.session_state.phase
        phases = [("work", "Focus"), ("short_break", "Short Break"), ("long_break", "Long Break")]
        
        status_html = '<div class="status-bar">'
        for p_key, p_name in phases:
            active_class = "status-active" if p_key == current else ""
            status_html += f'<div class="status-item {active_class}">{p_name}</div>'
        status_html += '</div>'

        # --- Main Card ---
        phase_label = "Study Now" if current == "work" else current.replace("_", " ").title()
        time_str = format_time(st.session_state.time_remaining)

        st.markdown(f"""
            <div class="main-card">
                {status_html}
                <div class="phase-title">{phase_label}</div>
                <div class="timer-display">{time_str}</div>
            </div>
        """, unsafe_allow_html=True)

        # Progress Bar
        progress = (st.session_state.total_duration - st.session_state.time_remaining) / st.session_state.total_duration
        st.progress(progress)
        
        st.write("---")

        # --- CONTROLS (Wrapped in a specific container) ---
        st.markdown('<div class="timer-controls">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            label = "PAUSE" if st.session_state.running else "START"
            st.button(label, on_click=start_pause, use_container_width=True)
        with col2:
            st.button("NEXT ⏭", on_click=move_next, use_container_width=True)

        col3, col4 = st.columns(2)
        with col3:
            st.button("Short Break ☕", on_click=set_phase, args=("short_break",), use_container_width=True)
        with col4:
            st.button("Long Break 🛌", on_click=set_phase, args=("long_break",), use_container_width=True)
            
        st.markdown('</div>', unsafe_allow_html=True) # End timer-controls container

    # Timer Logic
    if st.session_state.running and st.session_state.time_remaining > 0:
        time.sleep(1)
        st.session_state.time_remaining -= 1
        st.rerun()

    if st.session_state.running and st.session_state.time_remaining <= 0:
        st.session_state.running = False
        st.balloons()
        move_next()
        st.rerun()

if __name__ == "__main__":
    pomodoro_app()