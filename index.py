import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
from PIL import ImageChops

st.title('Comparison App')
st.write('This app allows you to submit two different URLs or images to get a comparison screenshot.')
# Greyscale conversion function
def convert_to_greyscale(uploaded_file):
    image = Image.open(uploaded_file)
    return image.convert("L")
  
def calculate_image_difference(img1, img2):
    diff = ImageChops.difference(img1, img2)
    return diff
  
option = st.radio(
    "Would you like to compare URLs or upload 2 files?",
    ["URL", "Upload"]
)

if option == "URL":
    url1 = st.text_input('Enter first URL')
    url2 = st.text_input('Enter second URL')
    

elif option == "Upload":
    uploaded_file1 = st.file_uploader("Upload the first image:", type=["jpeg", "jpg", "png"])
    uploaded_file2 = st.file_uploader("Upload the second image:", type=["jpeg", "jpg", "png"])
    
    if uploaded_file1 is not None and uploaded_file2 is not None:
        # Read uploaded files and convert to greyscale
        img1 = convert_to_greyscale(uploaded_file1)
        img2 = convert_to_greyscale(uploaded_file2)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(img1, caption="First Image (Greyscale)")
        with col2:
            st.image(img2, caption="Second Image (Greyscale)")
        
        diff_img = calculate_image_difference(img1, img2)
        st.image(diff_img, caption="Difference Image")
    else:
        st.write('Please upload both images.')
