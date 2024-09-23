import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

# Configure api
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input, image):
    if input:
        response=model.generate_content([input,image], stream=True)
        response.resolve()
    else:
        response=model.generate_content([image])
    return response.text
    
##initialize streamlit app
st.set_page_config(page_title="PicQuery")

# App name
st.markdown("<h4 style='text-align: center;'>PicQuery</h4>", unsafe_allow_html=True)

# Upload image
uploaded_file= st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
image=''
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Input and Submit button
input=st.text_input(" ", key="input", placeholder="Ask about the image")
submit=st.button("Submit")

## if submit is clicked
if submit:
    response=get_gemini_response(input,image)
    st.write(response)
    
    

