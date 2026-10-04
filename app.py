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
        with st.spinner("🧠 AI step-by-step aur saaf-suthra jawab taiyar kar raha hai..."):
            # Strict formatting prompt taaki equations aur steps bilkul clean aayein
            full_prompt = (
                f"You are an expert AI tutor. You MUST answer the following student query strictly in pure "
                f"Devanagari Hindi script (हिंदी में) in a very detailed, comprehensive, step-by-step long format. "
                f"CRITICAL FORMATTING RULES: "
                f"1. NEVER use square brackets like [...] for math equations. "
                f"2. ALWAYS use double dollar signs ($$ ... $$) for standalone display equations and single dollar signs ($ ... $) for inline variables. "
                f"3. Write each step clearly on a new line with proper spacing, bullet points, and clean explanations, just like a professional teacher. "
                f"Do not write explanations in English. Student Query: {query}"
            )
            encoded_prompt = urllib.parse.quote(full_prompt)
            
            # Alag-alag free AI models ki list
            models = ["openai", "mistral", "deepseek", "qwen"]
            response_text = None
            
            for model in models:
                url = f"https://text.pollinations.ai/{encoded_prompt}?model={model}"
                for attempt in range(2):
                    try:
                        res = requests.get(url, timeout=40)
                        if res.status_code == 200 and res.text.strip():
                            response_text = res.text
                            break
                    except Exception:
                        pass
                    time.sleep(2)
                if response_text:
                    break
            
            if response_text:
                st.markdown("### 📝 Step-by-Step Detailed Answer (Hindi):")
                st.markdown(response_text)
            else:
                st.error("⚠️ Abhi server par heavy load hai. Kripya 10 sekund intezaar karke dobara button par click karein!")
    else:
        st.warning("Kripya pehle apna sawal likhein!")
        
        
        
        
        
        
        
        
        
                    
                    
                    
                    
                    
