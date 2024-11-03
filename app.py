import os
from PIL import Image
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import PyPDF2


# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY") 

# Configure the Generative AI model
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

# Define function to generate model response
def get_response(input_text, content):
    """Generates a response from the generative model based on input text and content."""
    if input_text:
        response = model.generate_content([input_text, content])
    else:
        response = model.generate_content(content)
    return response.text

# Streamlit page configuration and styling
st.set_page_config(page_title="Gemini Decode", page_icon=":crystal_ball:", layout="wide")

# Custom CSS for background, text styling, and font loading
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Cantora+One&display=swap" rel="stylesheet">
    <style>
        
        .main-header {
            font-family: 'Cantora One', sans-serif;
            font-size: 30px;
            font-weight: bold;
            color: #a7a9be;
            text-align: center;
            margin-top: 20px;
            text-transform: uppercase;
            margin-bottom: 25px;
        }
        
        .stTextInput, .stButton {
            border-radius: 5px;
        }
            
        .stButton > button {
            background-color: #6c63ff;
            color: white;
            font-weight: bold;

    </style>
""", unsafe_allow_html=True)

# Main header with Cantora One font
st.markdown('<div class="main-header">Gemini Decode: Multilanguage Document Extraction by Gemini Pro</div>', unsafe_allow_html=True)

# Sidebar for instructions and settings
with st.sidebar:
    st.header("Instructions")
    st.write("""
        1. Enter your query or prompt in the text input.
        2. Upload an image or PDF document of the content you want to extract.
        3. Click 'Submit' to get a response.
    """)

    st.write("Customize your extraction settings if needed.")
    
    
# Main input fields for user prompt and file upload
st.subheader("Chat with Gemini-Pro")
input_prompt = st.text_input("Input your query or prompt:")
uploaded_file = st.file_uploader("Upload an image or PDF document:", type=["jpg", "jpeg", "png", "pdf"])

content = None  

# File processing
if uploaded_file is not None:
    file_type = uploaded_file.type
    if file_type in ["image/jpeg", "image/png"]:
        # Display and set content for image files
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        content = image
    elif file_type == "application/pdf":
        # Extract and display text from PDF files
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        pdf_text = "".join(page.extract_text() for page in pdf_reader.pages)
        st.text_area("Extracted PDF Text:", pdf_text, height=200)
        content = pdf_text

# Generate response upon submission
if st.button("Submit") and content is not None:
    with st.spinner("Processing..."):
        response = get_response(input_prompt, content)
    st.subheader("Bot Response:")
    st.write(response)
