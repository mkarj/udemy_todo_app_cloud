import streamlit as st
# pillow
from PIL import Image

st.subheader("Color to Grayscale Converter")

# load picture
uploaded_image = st.file_uploader("Upload Image")

# start web cam
with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")
    print(camera_image)

if camera_image:
    # create pillow image instance
    img = Image.open(camera_image)
    # convert the pillow image to grayscale
    gray_img = img.convert("L")
    # render/display grayscale image on the webpage
    st.image(gray_img)

if uploaded_image:
    img = Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.image(gray_img)
