import streamlit as st
import google.generativeai as genai
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Student Pro AI Assistant",
    page_icon="🚀",
    layout="centered"
)

# Custom Styling for Dark Theme & Mobile-Friendly UI
st.markdown("""
    <style>
    .main {
        background-color: #0d1117;
        color: #ffffff;
    }
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: #21262d;
        color: white;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# =========================================================
# YAHAN APNI ASLI GOOGLE API KEY DAL DENI HAI
# (Inverted commas "" ke andar apni key paste kar dena)
# Iske baad kisi bhi dost ko API key nahi dalni padegi!
# =========================================================
API_KEY = "AQ.Ab8RN6ISW4swL1LeC5LYXwjjxweFV18lFpDKJfR_Cve6UQWAzg"

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Configuration Error: {e}")

# App Header (English UI)
st.title("🌌 Student Pro AI Assistant")
st.markdown("### 📚 Your Smart AI Companion for Math, Science & All Subjects")

st.markdown("---")

# Main Choice: Text Question or Photo Upload
option = st.radio(
    "👉 How would you like to ask your question?",
    ("✍️ Type your question", "📸 Upload a photo of the question")
)

st.markdown("---")

if option == "✍️ Type your question":
    st.subheader("🤖 Ask any difficult question in Math or Science")
    st.markdown("Type your question below, and you will get a detailed, step-by-step answer in **Hindi**.")
    
    user_query = st.text_area(
        "Enter your question here:",
        placeholder="e.g., Solve the equation x^2 + 5x + 6 = 0 or explain Newton's laws...",
        height=130
    )
    
    if st.button("🚀 Get Detailed Answer (Solve)", type="primary"):
        if user_query.strip():
            with st.spinner("🧠 AI is generating a detailed answer in Hindi..."):
                try:
                    prompt_text = (
                        "You are an expert, friendly student tutor. "
                        "Provide a very detailed, comprehensive, step-by-step long answer in pure Devanagari Hindi script (हिंदी में) "
                        "for the following student query: " + user_query
                    )
                    response = model.generate_content(prompt_text)
                    st.markdown("### 📝 Detailed Answer (विस्तृत उत्तर):")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter your question first!")

else:
    st.subheader("📸 Upload Photo to Solve Question")
    st.markdown("Upload a photo of your question or math equation below:")
    
    uploaded_file = st.file_uploader("Choose question photo (JPG, PNG)", type=["jpg", "jpeg", "png"])
    
    image_prompt = st.text_input("Instructions for photo (Optional):", value="Solve this question and explain step-by-step in Hindi.")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        if st.button("🔍 Analyze and Solve Photo", type="primary"):
            with st.spinner("👀 Reading photo and generating solution in Hindi..."):
                try:
                    response = model.generate_content([image, image_prompt])
                    st.markdown("### 📝 Detailed Solution (विस्तृत समाधान):")
                    st.markdown(response.text)
                except Exception as ec:
                    st.error(f"Error: {ec}")
                    
                    
                    
