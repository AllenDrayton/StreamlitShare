import streamlit as st
from PIL import Image

img = Image.open("Sage.png")

st.image(img, width = 500)

if st.checkbox("Show / Hide"):
    st.text("Showing the Widget")
    st.image(img, width = 250)

status = st.radio("Select Subjects : ", ('Computer', 'English', 'Social'))

st.success(status)