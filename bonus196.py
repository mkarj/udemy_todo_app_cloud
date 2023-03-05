import streamlit as st
# pillow
from PIL import Image

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
