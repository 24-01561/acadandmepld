import streamlit as st
import sys
import os


#Import tab
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tab 

#Set page's config
st.set_page_config(layout="wide", page_title="Acad&Me - Wellness")

#Import tab components
tab.render_css()
tab.render_top_buttons()
tab.render_navbar()

#Convert image to base64
cpe_b64 = tab.get_base64_image("image10.png")
#Set image source
cpe_src = f"data:image/png;base64,{cpe_b64}" if cpe_b64 else "https://placehold.co/600x500/png?text=3D+Computer"

html_content = f"""
<div class="main-content" style="max-width: 1440px; margin: 0 auto; padding: 0 40px;">

<div class="section" style="display: flex; align-items: center; justify-content: space-between; padding: 60px 0; gap: 60px;">
<div class="text-block" style="flex: 1;">
<div class="section-desc" style="font-size: 24px; line-height: 1.5; margin-bottom: 30px;">
A student-focused platform called Acad&Me was created to make learning easier, more structured, and more balanced. To help students stay on track, our website combines key productivity elements like an interactive calendar, Pomodoro timer, reminders, to-do lists, and motivational assistance. Additionally, we place a high priority on wellness by providing useful videos and mood tracking to encourage a healthy study-life balance. Acad&Me was founded with the single objective of assisting students in achieving their academic objectives while attending to their well-being.
</div>
<a href="calendartodo" style="color: black; text-decoration: none; font-size: 24px; font-weight: 700;">
</a>
</div>
<div class="visual-block" style="flex: 1; display: flex; justify-content: center;">
<img src="{cpe_src}" alt="Computer 3D" style="max-width: 100%; animation: float 6s ease-in-out infinite;">
</div>
</div>

<style>
.quote-box {{
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
max-width: 100%;
margin: 60px auto 40px auto;
}}

@keyframes float {{
0% {{ transform: translateY(0px); }}
50% {{ transform: translateY(-15px); }}
100% {{ transform: translateY(0px); }}
}}
</style>
"""

st.markdown(html_content, unsafe_allow_html=True) #Brings down the html content to the page
