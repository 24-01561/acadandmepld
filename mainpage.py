import streamlit as st
import tab  # Import the layout file
import base64

# 1. Page Setup
st.set_page_config(layout="wide", page_title="Acad&Me")

# 2. Inject Layout (CSS, Buttons, Navbar)
tab.render_css()
tab.render_top_buttons()
tab.render_navbar()

# --- PAGE SPECIFIC IMAGES ---
comp_b64 = tab.get_base64_image("other07.png")
abstract_b64 = tab.get_base64_image("other12.png")
folder_b64 = tab.get_base64_image("other18.png")

comp_src = f"data:image/png;base64,{comp_b64}" if comp_b64 else "https://placehold.co/600x500/png?text=3D+Computer"
abstract_src = f"data:image/png;base64,{abstract_b64}" if abstract_b64 else "https://placehold.co/435x400/png?text=Abstract+Shapes"
folder_src = f"data:image/png;base64,{folder_b64}" if folder_b64 else "https://placehold.co/450x420/png?text=Folder+Graphic"

# --- HTML CONTENT ---
# IMPORTANT: Do not add indentation to the lines below. 
# Keep them touching the left side of the screen.
html_content = f"""
<div class="main-content" style="max-width: 1440px; margin: 0 auto; padding: 0 40px;">
<div class="section" style="display: flex; align-items: center; justify-content: space-between; padding: 60px 0; gap: 60px;">
<div class="text-block" style="flex: 1;">
<div class="section-title" style="font-size: 42px; font-weight: 700; margin-bottom: 25px; line-height: 1.2;">
Welcome to Acad&Me—your companion for staying focused, organized, and motivated.
</div>
<div class="section-desc" style="font-size: 24px; line-height: 1.5; margin-bottom: 30px;">
From timers to task trackers and wellness tools, everything here is designed 
to support your learning journey. We're glad you're here!
</div>
<a href="#" class="cta-btn" style="background-color: #FFDB5B; color: black; text-decoration: none; padding: 15px 40px; font-size: 24px; font-weight: 700; border-radius: 8px; display: inline-block; box-shadow: 0px 4px 6px rgba(0,0,0,0.1);">Start now</a>
</div>
<div class="visual-block" style="flex: 1; display: flex; justify-content: center;">
<img src="{comp_src}" alt="Computer 3D" style="max-width: 100%; animation: float 6s ease-in-out infinite;">
</div>
</div>
<div class="section" style="display: flex; align-items: center; justify-content: space-between; padding: 60px 0; gap: 60px;">
<div class="visual-block" style="flex: 1; display: flex; justify-content: center;">
<img src="{abstract_src}" alt="Abstract Shapes" style="max-width: 80%;">
</div>
<div class="text-block" style="flex: 1;">
<div class="section-desc" style="font-size: 24px; line-height: 1.5;">
We created Acad&Me to help students manage their academic responsibilities without feeling overwhelmed. 
Many struggle with focus, organization, and maintaining their well-being.
<br><br>
Acad&Me was built to make studying easier, healthier, and more manageable for every student.
</div>
</div>
</div>
<div class="section" style="display: flex; align-items: center; justify-content: space-between; padding: 60px 0; gap: 60px;">
<div class="text-block" style="flex: 1;">
<div class="section-desc" style="font-size: 24px; line-height: 1.5;">
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
</div>
</div>
<div class="visual-block" style="flex: 1; display: flex; justify-content: center;">
<img src="{folder_src}" alt="Folder Graphic" style="max-width: 80%;">
</div>
</div>
<div class="cards-grid">
<div class="grey-card"></div>
<div class="grey-card"></div>
<div class="grey-card"></div>
<div class="grey-card"></div>
</div>
<footer class="custom-footer" style="margin-top: 100px; padding: 60px 0; border-top: 1px solid rgba(255,255,255,0.3); display: flex; justify-content: space-between; font-family: 'Roboto Serif', serif; font-size: 16px; line-height: 2;">
<div class="footer-col">
<h4>Acad&me</h4>
</div>
<div class="footer-col">
<div>Home</div>
<div>About</div>
</div>
<div class="footer-col">
<div>Contact</div>
<div>Email: acadnme@gmail.com</div>
<div>Instagram: acad&me</div>
<div>Twitter: acad&me</div>
</div>
<div class="footer-col">
<div>Join our newsletter</div>
<div>Email Address ____________</div>
<div style="font-size: 14px; margin-top: 10px; text-align: right;">Submit</div>
</div>
</footer>
</div>
<style>
@keyframes float {{
0% {{ transform: translateY(0px); }}
50% {{ transform: translateY(-15px); }}
100% {{ transform: translateY(0px); }}
}}
</style>
"""

st.markdown(html_content, unsafe_allow_html=True)