import streamlit as st
import requests
import urllib.parse
import time

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
""", unsafe_allow_html=True)

st.title("🚀 Student Pro AI Assistant")
st.markdown("Duniya ka koi bhi sawal yahan puchein — **Step-by-step aur vistarit jawab Hindi mein payein!**")

st.markdown("---")

query = st.text_area(
    "Apna sawal yahan likhein:",
    placeholder="Jaise: Integration, calculus, physics, ya koi bhi kathin sawal...",
    height=140
)

if st.button("🚀 Vistarit Jawab Prapt Karein", type="primary"):
    if query.strip():
        with st.spinner("🧠 AI server se connect ho raha hai, kripya thoda intezaar karein..."):
            try:
                full_prompt = (
                    f"You are an expert AI tutor. You MUST answer the following student query strictly in pure "
                    f"Devanagari Hindi script (हिंदी में) in a very detailed, comprehensive, step-by-step long format. "
                    f"CRITICAL REQUIREMENT for Math/Science: For all mathematical equations, formulas, and variables, "
                    f"use standard Markdown math notation with double dollar signs ($$ ... $$) for standalone display "
                    f"equations and single dollar signs ($ ... $) for inline equations so they render correctly. "
                    f"Do not write explanations in English. Student Query: {query}"
                )
                encoded_prompt = urllib.parse.quote(full_prompt)
                url = f"https://text.pollinations.ai/{encoded_prompt}"
                
                # Auto-retry loop (3 koshishein agar server busy ho)
                response = None
                for attempt in range(3):
                    try:
                        response = requests.get(url, timeout=40)
                        if response.status_code == 200 and response.text.strip():
                            break
                    except requests.exceptions.RequestException:
                        pass
                    time.sleep(2) # 2 second wait karke dobara try karega
                
                if response and response.status_code == 200 and response.text.strip():
                    st.markdown("### 📝 Step-by-Step Detailed Answer (Hindi):")
                    st.markdown(response.text)
                else:
                    st.error("Server abhi bohot zyada busy hai. Kripya 10-15 sekund baad dobara button dabayein!")
            except Exception as e:
                st.error(f"Connection Error: {e}")
    else:
        st.warning("Kripya pehle apna sawal likhein!")
        
        
        
        
        
        
                    
                    
                    
                    
                    
