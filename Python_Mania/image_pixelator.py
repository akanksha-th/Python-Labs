import streamlit as st
import numpy as np
import cv2
from PIL import Image
import io

st.title("🟦 Pixelate Your Image! 🎨")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Pixelation intensity slider
pixel_size = st.slider("Select pixelation intensity", 
                       min_value=5, max_value=50, value=10)

if uploaded_file:
    image = np.array(Image.open(uploaded_file))
    h, w = image.shape[:2]
    
    small = cv2.resize(image, (w//pixel_size, h//pixel_size), interpolation = cv2.INTER_LINEAR)
    pixelated_arr = cv2.resize(small, (w, h), interpolation = cv2.INTER_NEAREST)
    
    pixelated_img = Image.fromarray(pixelated_arr)
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption='Original Image', use_container_width = True)
    with col2:
        st.image(pixelated_img, caption='Pixelated Image', use_container_width = True)
    
    img_bytes = io.BytesIO()  # Create an in-memory byte buffer
    pixelated_img.save(img_bytes, format="PNG")  # Save the pixelated image into this buffer
    img_bytes.seek(0) 
    
    st.download_button(
        label="Download Pixelated Image",
        data=img_bytes,
        file_name="pixelated_image.png",
        mime="image/png"
    )