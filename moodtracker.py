import streamlit as st

st.title("😊Mood Tracker")

st.write("Rate your mood today (0 = Sad, 10 = Happy):")

mood = st.slider("Mood", 0, 10)

if "moods" not in st.session_state:
    st.session_state.moods = []

if st.button("Save Mood"):
    st.session_state.moods.append(mood)
    st.success("Mood saved!")

st.write("### Mood History:")

if st.session_state.moods:
    st.line_chart(st.session_state.moods)
    st.write(st.session_state.moods)
else:
    st.write("No mood saved yet.")
