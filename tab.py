import streamlit as st
import base64
import random

#Convert images to base64
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return ""

#CSS Styles
def render_css():
    if "theme" not in st.session_state:
        st.session_state["theme"] = "dark"  # Default to dark theme

    #Load BG Image
    bg_b64 = get_base64_image("image13.png") 

    #Sets for light and dark mode
    if st.session_state["theme"] == "light": #If light mode is pressed
        text_color = "#ffffff"
        
        # Button Colors
        btn_bg = "#2C2C2C"        
        btn_hover = "#444444"     
        btn_text = "#ffffff"
        
        card_bg = "#D9D9D9"
        
        #Light mode background with image
        app_bg_style = "background-color: #5DA2D5;"
        
        #Light mode bg opacity changer
        bg_opacity = 0.4  

        #Image overlay
        bg_overlay_css = f"""
        .stApp::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-image: url("data:image/png;base64,{bg_b64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            opacity: {bg_opacity}; 
            z-index: -1;
        }}
        """

    else: #Dark mode
        text_color = "#ffffff"
        
        #Button Colors
        btn_bg = "#374151"
        btn_hover = "#4B5563"
        btn_text = "#ffffff"
        
        card_bg = "rgba(255, 255, 255, 0.05)"
        
        #Dark mode
        app_bg_style = "background-color: #0b1220;"
        bg_overlay_css = "" #No image overlay

    #Custom CSS for tab
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;700&family=Lilita+One&family=Roboto+Serif:wght@400&family=Roboto:wght@500&display=swap');

    [data-testid="stHeader"], footer {{ display: none; }}

    /*Apply  Image Overlay*/
    {bg_overlay_css}

    .stApp {{
        {app_bg_style} !important;
        color: {text_color} !important;
        font-family: 'Quicksand', sans-serif;
        transition: background 0.5s ease;
        z-index: 1; 
    }}

    .block-container {{
        padding: 0 !important;
    }}

    /*Navigation bar*/
    .navbar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 40px;
        height: 100px;
        max-width: 1440px;
        margin: 0 auto;
    }}

    .nav-links {{
        display: flex;
        gap: 30px;
        align-items: center;
        font-family: 'Lilita One', cursive;
        font-size: 24px;
        text-shadow: 0px 2px 4px rgba(0,0,0,0.1);
    }}
    
    .nav-item a {{
        text-decoration: none;
        color: inherit;
        transition: 0.2s;
    }}
    .nav-item a:hover {{ transform: scale(1.05); color: #FFDB5B; }}

    /*Buttons*/
    div[data-testid="stButton"] button {{
        background-color: {btn_bg};
        color: {btn_text};
        border: none;
        width: 100%;
        transition: transform 0.2s, background-color 0.2s;
    }}
    
    div[data-testid="stButton"] button:hover {{
        transform: scale(1.02);
        background-color: {btn_hover} !important; 
        color: {btn_text} !important;
        border: none !important;
    }}
    
    /*Cards*/
    .cards-grid {{
        display: flex;
        justify-content: space-between;
        gap: 20px;
        margin: 100px 0;
    }}
    .grey-card {{
        flex: 1;
        height: 250px;
        background-color: {card_bg};
        border-radius: 4px;
        transition: background-color 0.5s ease;
    }}
    </style>
    """, unsafe_allow_html=True)

#Light/Dark Mode Toggle and Motivational Button
def render_top_buttons():
    motivational_quotes = [
        "Believe you can and you're halfway there.",
        "The only way to do great work is to love what you do.",
        "It always seems impossible until it's done."
    ]
    
    spacer, dark_col, motiv_col = st.columns([8, 1, 1.5])

    with dark_col:
        btn_label = "☀️ Light" if st.session_state["theme"] == "dark" else "🌙 Dark"
        
        if st.button(btn_label, key="theme_toggle"):
            st.session_state["theme"] = "light" if st.session_state["theme"] == "dark" else "dark"
            st.rerun()

    with motiv_col:
        if st.button("💡 Stay Motivated!", key="motiv_btn"):
            st.toast(random.choice(motivational_quotes), icon="✨")

#Navigation bar
def render_navbar():
    logo_b64 = get_base64_image("logo.png") 
    logo_src = f"data:image/png;base64,{logo_b64}" if logo_b64 else "https://placehold.co/200x80/png?text=Acad%26Me"
    
    st.markdown(f"""
    <div class="navbar">
        <div class="logo">
            <a href="/" target="_self">
                <img src="{logo_src}" style="height: 90px;" alt="Acad&Me">
            </a>
        </div>
        <div class="nav-links">
            <span class="nav-item"><a href="pomodoro" target="_self">Pomodoro</a></span>
            <span class="nav-item"><a href="calendartodo" target="_self">Calendar</a></span>
            <span class="nav-item"><a href="wellnessvideo" target="_self">Wellness video</a></span>
            <span class="nav-item"><a href="moodtracker" target="_self">Track your mood</a></span>
            <span class="nav-item"><a href="about" target="_self">About</a></span>
        </div>
    </div>
    """, unsafe_allow_html=True)
