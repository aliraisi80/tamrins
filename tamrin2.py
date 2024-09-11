# from PIL import Image
#
# img=Image.open('logo.ipg')
# bw=img.convert("L")
# bw=save("new-logo.png")
# bw.show()

import streamlit as st
from PIL import Image
st.subheader("Color to Grayscale Converter")
with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")
    uploaded_image = st.file_uploader
if camera_image:
    img = Image.open(camera_image)
    gray_camera_img = img.convert('L')
    st.image(gray_camera_img)
