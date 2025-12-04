import streamlit as st
import tab  # Import tab module for layout components
import base64

#Set Page's Configuration
st.set_page_config(layout="wide", page_title="Acad&Me")

#Import tab 
tab.render_css()
tab.render_top_buttons()
tab.render_navbar()

#Setting main page's images 
comp_b64 = tab.get_base64_image("Other07.png")
abstract_b64 = tab.get_base64_image("Other12.png")
folder_b64 = tab.get_base64_image("Other18.png")

#Setting main page's images for the 4 members
img1_b64 = tab.get_base64_image("Card1.png")
img2_b64 = tab.get_base64_image("Card2.png")
img3_b64 = tab.get_base64_image("ricci.png")
img4_b64 = tab.get_base64_image("Card4.png")

#Defining the sources for the 3 main images
#If image file not found, use placeholder images
comp_src = f"data:image/png;base64,{comp_b64}" if comp_b64 else "https://placehold.co/600x500/png?text=3D+Computer" 
abstract_src = f"data:image/png;base64,{abstract_b64}" if abstract_b64 else "https://placehold.co/435x400/png?text=Abstract+Shapes"
folder_src = f"data:image/png;base64,{folder_b64}" if folder_b64 else "https://placehold.co/450x420/png?text=Folder+Graphic"

#Defining Sources for the 4 Team images
#If image file not found, use default Google profile pictures
src1 = f"data:image/png;base64,{img1_b64}" if img1_b64 else "https://lh3.googleusercontent.com/a-/ALV-UjVCiTyC465kcmoxoQ4yhCXfnoBGtyFJpa2YBFkMD4X6ijxtgJk=s330-p-k-rw-no"
src2 = f"data:image/png;base64,{img2_b64}" if img2_b64 else "https://lh3.googleusercontent.com/a/ACg8ocI1sH7REfpNRCEJqqfvFIOZFB95Z9zFfn1g-WCnSTxspJpb8WQ=s330-p-k-rw-no"
src3 = f"data:image/png;base64,{img3_b64}" if img3_b64 else "https://lh3.googleusercontent.com/a-/ALV-UjW6D_Y-drda3TbR6GLGq5mbugPOaQxq-dYfOnrCn8IwQlTMBnupQNKrwIVODVKrMTMhbNlkZh_cYIpfpez6n8s_HzQmgqc7bqoO70mt5_Y25f_9WWVggi_sCUlzMOjp-1vjcMOeKEnxG1z4eZUx2awChCHB2WkO66QdFBTbXibaBeAQfzpXMk3_H6fPb2jS21mWohfzKDClaU5eJbLqlsCej08xPj4c0utyYiM3IRwZ0mhfeIGw_XVgTOo7WuOEWRYPfhYzVc43GYFetLp14Ip67Bbp15gCv0WrPBg2Y_5E99OjJDj5zo2vCMNvHFmlK09vBOz6dSbfMelLgokCSa_cVg5GECYiMqRx4NqcJan8dGk_JAvqdXNMBDTLLKspLigr-wAhA-6d4Oc51597k6ETfNTXzvsKzZZSrIDHz-DdnGJUxcy0AIgXKM5bEhLshkMpTeIb_oFGEnrQeKdSq2UfcFqtY-BVnaXjlGm26ctCX9Lv99RHcTtFu1qEDd_556rvCevUw237SXFkykGmtqjLYnW2_pDpZPpRwUP44RgwiI3vcDLWP6oDSnhwlU2sEzVqownLFdTuasaYyWGxLYsVbI0Ye3tiLe2D-1XWGJQvhJpDpo4usnE86sTKvOV_K531DK3GANKiQMiXnMU1sD4ZBomijkcTHEDUHZD4QHzmhoC-SShg-1g87LE1heSr_W4SKESSXKa5GOXwb2Grd9uNBO38lUvKh5QGieuqYKU_Thrd32eQzi8bdLcFxYXSYAHFydxo1yfQVTDkNxW0IrOAuTWHmfVTKi9SSauXpZYz63fLH6QfRynEcjFRrSBmzvYQqG6xnrQNn9gz-CqXKYUhLGZb5ouzqRDzXViDfdAbDCafQmMMUAUHrRt-mzG02AOTMqifdd4de4gMdD9KsDlQAUnWL6uO9kadh4bx7cY8bBv1H_QgnsI0EPQ0Zp1V5rvSB4Jj9Kx3JAn2PHWr92fbjJfGXfoSRmNJP7NUATSH7-vVRMCqhdUlRzfghCwj5GJFfaO8Ryqi1P1qxHmeETDVnncCk4orsFb4P_YvaOjuUsZT9KjM=s330-p-k-rw-no"
src4 = f"data:image/png;base64,{img4_b64}" if img4_b64 else "https://lh3.googleusercontent.com/a-/ALV-UjURoXMPMWI54BvmFD7c9UJvyg0KSic3JIjU6R5iE8fAzNQZPic=s330-p-k-rw-no"

#HTML
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
<a href="calendartodo" class="cta-btn" style="background-color: #FFDB5B; color: black; text-decoration: none; padding: 15px 40px; font-size: 24px; font-weight: 700; border-radius: 8px; display: inline-block; box-shadow: 0px 4px 6px rgba(0,0,0,0.1);">Start now</a>
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
If you're ready to boost your focus, stay organized, and make studying feel lighter, Acad&Me is here for you. With tools built to keep you motivated and on track, it’s the perfect space for anyone wanting to be more productive.
<br><br>
<strong>Start your journey today—your future self will thank you!</strong>
</div>
</div>
<div class="visual-block" style="flex: 1; display: flex; justify-content: center;">
<img src="{folder_src}" alt="Folder Graphic" style="max-width: 80%;">
</div>
</div>

<div class="quote-box">
Get to be introduced to our developers 🚀
</div>

<div class="section" style="display: flex; justify-content: space-between; gap: 20px; margin-bottom: 60px; text-align: center; color: white;">

<div style="flex: 1;">
<img src="{src1}" alt="Card 1" style="width: 100%; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1); object-fit: cover;">
<div style="margin-top: 15px;">
<div style="font-size: 20px; font-weight: 700;">Johnearl Bobis</div>
<div style="font-size: 16px;">Project Analyst</div>
</div>
</div>

<div style="flex: 1;">
<img src="{src2}" alt="Card 2" style="width: 100%; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1); object-fit: cover;">
<div style="margin-top: 15px;">
<div style="font-size: 20px; font-weight: 700;">Joshua Garcia</div>
<div style="font-size: 16px;">Principal Developer</div>
</div>
</div>

<div style="flex: 1;">
<img src="{src3}" alt="Card 3" style="width: 100%; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1); object-fit: cover;">
<div style="margin-top: 15px;">
<div style="font-size: 20px; font-weight: 700;">Ricci Beatrice Gube</div>
<div style="font-size: 16px;">System Architect</div>
</div>
</div>

<div style="flex: 1;">
<img src="{src4}" alt="Card 4" style="width: 100%; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1); object-fit: cover;">
<div style="margin-top: 15px;">
<div style="font-size: 20px; font-weight: 700;">Ellaine Rae Villalobos</div>
<div style="font-size: 16px;">Solution Strategist</div>
</div>
</div>

</div>

<footer class="custom-footer" style="margin-top: 100px; padding: 60px 0; border-top: 1px solid rgba(255,255,255,0.3); display: flex; justify-content: space-between; font-family: 'Roboto Serif', serif; font-size: 16px; line-height: 2;">
<div class="footer-col">
</footer>
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

st.markdown(html_content, unsafe_allow_html=True) # Render the HTML content in Streamlit
