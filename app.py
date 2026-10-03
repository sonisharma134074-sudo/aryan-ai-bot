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
""", unsafe_allow_html=True)

st.title("🚀 Student Pro AI Assistant")
st.markdown("Duniya ka koi bhi sawal yahan puchein — **Step-by-step aur vistarit jawab payein!**")

st.markdown("---")

query = st.text_area(
    "Apna sawal yahan likhein:",
    placeholder="Jaise: Integration, calculus, physics, ya koi bhi kathin sawal...",
    height=140
)

if st.button("🚀 Vistarit Jawab Prapt Karein", type="primary"):
    if query.strip():
        with st.spinner("🧠 AI step-by-step lamba aur vistarit jawab taiyar kar raha hai..."):
            try:
                # Math aur science formulas ko proper Markdown Math ($$...$$ aur $...$) mein format karne ke liye prompt
                full_prompt = (
                    f"You are an expert AI tutor. Answer the following student query in a very detailed, "
                    f"comprehensive, step-by-step long format. CRITICAL REQUIREMENT: For all mathematical equations, "
                    f"formulas, and variables, use standard Markdown math notation with double dollar signs ($$ ... $$) "
                    f"for standalone display equations and single dollar signs ($ ... $) for inline equations so they "
                    f"render correctly. Query: {query}"
                )
                encoded_prompt = urllib.parse.quote(full_prompt)
                
                url = f"https://text.pollinations.ai/{encoded_prompt}"
                response = requests.get(url, timeout=30)
                
                if response.status_code == 200 and response.text.strip():
                    st.markdown("### 📝 Step-by-Step Detailed Answer:")
                    st.markdown(response.text)
                else:
                    st.error("Server thoda busy hai, kripya dobara try karein!")
            except Exception as e:
                st.error(f"Connection Error: {e}")
    else:
        st.warning("Kripya pehle apna sawal likhein!")
        
        
        
        
                    
                    
                    
                    
                    
