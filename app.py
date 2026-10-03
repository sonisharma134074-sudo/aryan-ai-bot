import streamlit as st
import requests
import urllib.parse

# Page Configuration
st.set_page_config(
    page_title="Student Pro AI Assistant",
    page_icon="🚀",
    layout="centered"
)

# Custom Styling for Clean, Fast UI
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
""", unsafe_allow_html=True,)

st.title("🚀 Student Pro AI Assistant")
st.markdown("Duniya ka koi bhi sawal yahan puchein — **Bina kisi API Key aur bina kisi login ke**, seedha vistarit jawab payein!")

st.markdown("---")

query = st.text_area(
    "Apna sawal yahan likhein:",
    placeholder="Jaise: Solve quadratic equation, photosynthesis, translation, ya koi bhi GK ka sawal...",
    height=140
)

if st.button("🚀 Vistarit Jawab Prapt Karein", type="primary"):
    if query.strip():
        with st.spinner("🧠 AI internet server se lamba aur vistarit jawab taiyar kar raha hai..."):
            try:
                # Hindi aur detail mein jawab mangne ke liye
                full_prompt = f"Answer the following student query in very detailed, comprehensive, step-by-step long format in pure Devanagari Hindi script (हिंदी में): {query}"
                encoded_prompt = urllib.parse.quote(full_prompt)
                
                # Free Public AI Server (No API Key required at all)
                url = f"https://text.pollinations.ai/{encoded_prompt}"
                response = requests.get(url, timeout=30)
                
                if response.status_code == 200 and response.text.strip():
                    st.markdown("### 📝 Vistarit Jawab (Detailed Answer):")
                    st.markdown(response.text)
                else:
                    st.error("Server thoda busy hai, kripya 1 minute baad dobara try karein!")
            except Exception as e:
                st.error(f"Connection Error: {e}")
    else:
        st.warning("Kripya pehle apna sawal likhein!")
        
        
        
                    
                    
                    
                    
                    
