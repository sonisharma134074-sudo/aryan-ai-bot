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
        with st.spinner("🧠 Server par traffic hai, AI connect hone ki koshish kar raha hai..."):
            full_prompt = (
                f"You are an expert AI tutor. You MUST answer the following student query strictly in pure "
                f"Devanagari Hindi script (हिंदी में) in a very detailed, comprehensive, step-by-step long format. "
                f"CRITICAL REQUIREMENT for Math/Science: For all mathematical equations, formulas, and variables, "
                f"use standard Markdown math notation with double dollar signs ($$ ... $$) for standalone display "
                f"equations and single dollar signs ($ ... $) for inline equations so they render correctly. "
                f"Do not write explanations in English. Student Query: {query}"
            )
            encoded_prompt = urllib.parse.quote(full_prompt)
            
            # Alag-alag free AI models ki list
            models = ["openai", "mistral", "deepseek", "qwen"]
            response_text = None
            
            for model in models:
                url = f"https://text.pollinations.ai/{encoded_prompt}?model={model}"
                for attempt in range(2): # Har model par 2 baar try karega
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
                st.error("⚠️ Abhi server par kafi heavy load hai. Kripya 10-15 sekund intezaar karke dobara button par click karein!")
    else:
        st.warning("Kripya pehle apna sawal likhein!")
        
        
        
        
        
        
        
        
                    
                    
                    
                    
                    
