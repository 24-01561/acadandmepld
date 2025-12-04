import streamlit as st
from streamlit_calendar import calendar
import json, os
import sys

#Set page's configurations
st.set_page_config(page_title="Calendar To-Do", page_icon="📅", layout="wide", initial_sidebar_state="collapsed")

#Import tab
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tab 

#Inject tab layout styles
tab.render_css() 
tab.render_top_buttons()
tab.render_navbar()

#Custom CSS for calendar
st.markdown("""
<style>
    /* --- 1. BUTTONS: Dark Grey Base --- */
    div.stButton > button:first-child, 
    div.stFormSubmitButton > button:first-child {
        background-color: #2C2C2C !important; 
        color: #ffffff !important;            
        border: 1px solid #cccccc !important; 
        border-radius: 8px !important;
        font-weight: bold !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2) !important;
        
        /* This ensures the zoom happens smoothly */
        transition: transform 0.2s ease !important;
    }

    /* --- HOVER STATE: Zoom ONLY (No Color Change) --- */
    div.stButton > button:first-child:hover, 
    div.stFormSubmitButton > button:first-child:hover {
        /* Keep the color EXACTLY the same */
        background-color: #2C2C2C !important; 
        color: #ffffff !important;
        border-color: #cccccc !important;
        
        /* The Zoom Effect */
        transform: scale(1.05) !important;
    }
    
    /* Active/Click State */
    div.stButton > button:first-child:active, 
    div.stFormSubmitButton > button:first-child:active {
        background-color: #1a1a1a !important; /* Go slightly darker when actually clicking */
        transform: scale(0.98) !important;
    }

    /* --- 2. INPUT FIELDS --- */
    input[type="text"], input[type="date"] {
        background-color: #ffffff !important;
        color: #333333 !important;
        border: 1px solid #e0e0e0 !important;
        border-radius: 8px !important;
    }
    input[type="text"]:focus, input[type="date"]:focus {
        border: 1px solid #333333 !important;
        outline: none !important;
    }

    /* --- 3. FORM CONTAINER --- */
    [data-testid="stForm"] {
        background-color: #2c2c2c !important; 
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid #444444;
    }
    
    /* Text Labels inside Form */
    label, [data-testid="stMarkdownContainer"] p {
        color: #ffffff !important;
        font-weight: 500 !important;
    }

    /* --- 4. CALENDAR STYLE --- */
    .fc {
        background-color: #ffffff !important;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .fc-toolbar-title { color: #333333 !important; }
    .fc-col-header-cell-cushion, .fc-daygrid-day-number {
        color: #333333 !important; 
        text-decoration: none !important;
    }
    .fc-button {
        background-color: #ffffff !important;
        color: #333333 !important;
        border: 1px solid #cccccc !important;
    }
    .fc-button-active {
        background-color: #333333 !important;
        color: #ffffff !important;
    }

    /* Title Alignment */
    h1 {
        text-align: center;
        text-shadow: 0px 2px 4px rgba(0,0,0,0.3);
    }
</style>
""", unsafe_allow_html=True)

# --- 4. DATA LOADING ---
if os.path.exists("events.json"):
    with open("events.json", "r") as f:
        try:
            st.session_state["events"] = json.load(f)
        except json.JSONDecodeError:
            st.session_state["events"] = []

if "events" not in st.session_state:
    st.session_state["events"] = []
if "show_form" not in st.session_state:
    st.session_state["show_form"] = False
if "show_delete" not in st.session_state:
    st.session_state["show_delete"] = False


# --- 5. MAIN LAYOUT ---
# CHANGED: Ratios adjusted to make the center column much wider [0.1, 10, 0.1]
left_gap, main_col, right_gap = st.columns([0.1, 10, 0.1])

with main_col:
    
    st.title("Calendar To-Do Integration")

    # --- Buttons Row ---
    btn_col1, btn_col2 = st.columns(2)
    
    # CHANGED: Added logic to force the other variable to False when one is clicked
    with btn_col1:
        if st.button("Add a Task ➕"):
            st.session_state["show_form"] = not st.session_state["show_form"]
            st.session_state["show_delete"] = False  # Close delete if open

    with btn_col2:
        if st.button("Delete a Task ❌"):
            st.session_state["show_delete"] = not st.session_state["show_delete"]
            st.session_state["show_form"] = False  # Close add if open

    # --- Add Event Form ---
    if st.session_state["show_form"]:
        with st.form("date_form"):
            st.subheader("New Event Details")
            task_name = st.text_input("Enter the task name:")
            user_date = st.date_input("Event Date")
            
            submitted = st.form_submit_button("Save")

            if submitted and task_name:
                new_event = {
                    "title": task_name,
                    "start": user_date.strftime("%Y-%m-%d"),
                }
                st.session_state["events"].append(new_event) 
                with open("events.json", "w") as f:
                    json.dump(st.session_state["events"], f, indent=4)
                st.session_state["show_form"] = False 
                st.rerun()
                st.toast("Event added successfully!", icon="✅")
                    
    # --- Delete Event Form ---
    if st.session_state["show_delete"]:
        with st.form("delete_form"):
            st.subheader("Delete Event")
            titles = [e["title"] for e in st.session_state["events"]]

            if titles:
                selected = st.selectbox("Select event to delete:", titles)
                delete_submitted = st.form_submit_button("Delete")

                if delete_submitted:
                    st.session_state["events"] = [
                        e for e in st.session_state["events"] if e["title"] != selected
                    ]
                    with open("events.json", "w") as f:
                        json.dump(st.session_state["events"], f, indent=4)
                    st.session_state["show_delete"] = False
                    st.rerun()
                    st.toast("Event deleted successfully!", icon="🗑️")
            else:
                st.info("No events to delete.")

    # --- The Calendar ---
    calendar_options = {
        "initialView": "dayGridMonth",
        "selectable": True,
        "headerToolbar": {
            "left": "prev,next today",
            "center": "title",
            "right": "dayGridMonth,timeGridWeek,timeGridDay"
        },
        "eventColor": "#3788d8", 
        "height": "800px" # Optional: Added height to match the new width better
    }

    calendar(
        events=st.session_state["events"],
        options=calendar_options,
        key="my_calender"
    )
