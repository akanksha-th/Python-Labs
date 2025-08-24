import streamlit as st
import imageio.v3 as iio
import numpy as np

st.title("Create your own GIFs")

# File uploader
uploaded_files = st.file_uploader("Upload images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images = [iio.imread(filename) for filename in uploaded_files]
    
    output_gif = 'new_gif.gif'
    iio.imwrite(output_gif, images, duration = 600, loop = 0)
    
    st.success("GIF successfully created!!")
    st.image(output_gif, use_container_width = True)
    
    st.download_button(label = 'Download GIF', data = output_gif, file_name="generated_gif.gif")

else:
    st.warning("Make sure the images are of same size and RETRY!!")
    
    