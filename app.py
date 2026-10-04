import streamlit as st
import requests
import urllib.parse
import time
import re

# Page Configuration
st.set_page_config(
    page_title="Student Pro AI Assistant",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Ultra-Modern CSS Styling for Premium Look
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    .main {
        background-color: #0b0f19;
        color: #f3f4f6;
    }
    
    .stTextInput > div > div > input, .stTextArea > div > div > textarea, .stSelectbox > div > div > div {
        background-color: #111827 !important;
        color: #ffffff !important;
        border-radius: 10px !important;
        border: 1px solid #374151 !important;
    }
    
    .stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2) !important;
    }
    
    /* Custom Header Gradient */
    .gradient-title {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.3rem;
        font-weight: 700;
        margin-bottom: 0.1rem;
    }
    
    .subtitle {
        color: #9ca3af;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }
    
    /* Primary Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.6);
    }
    
    /* Sidebar Styling */
    sidebar .st-bb {
        background-color: #111827;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar UI
with st.sidebar:
    st.markdown("### 🌟 Student Pro Hub")
    st.markdown("Aapka apna advanced AI Tutor jo har mushkil sawal ko aasan banata hai.")
    st.markdown("---")
    st.markdown("💡 **Features:**")
    st.markdown("- 🧠 Step-by-Step Doubt Solver")
    st.markdown("- 📝 Practice Question Generator")
    st.markdown("- ⚡ Multi-Model Failover Support")
    st.markdown("- 📐 Clean LaTeX Math Rendering")
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #6b7280; font-size: 0.85rem;'>Designed with 🚀 for Soni Sharma</p>", unsafe_allow_html=True)

# Main App Header
st.markdown('<p class="gradient-title">🚀 Student Pro AI Assistant</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Duniya ka koi bhi kathin sawal puchein ya practice test generate karein — sabhi jawab shuddh Hindi aur professional format mein!</p>', unsafe_allow_html=True)

# Mode Selection
app_mode = st.radio(
    "Mode Chunein:",
    ["🔍 Sawal ka Step-by-Step Jawab", "📝 Practice Questions Generator"],
    horizontal=True
)

st.markdown("---")

# Shared AI fetch function with Multi-Model Failover & Math Cleaner
def ask_ai(prompt_text):
    encoded_prompt = urllib.parse.quote(prompt_text)
    models = ["openai", "mistral", "deepseek", "qwen"]
    response_text = None
    
    for model in models:
        url = f"https://text.pollinations.ai/{encoded_prompt}?model={model}"
        for attempt in range(2):
            try:
                res = requests.get(url, timeout=45)
                if res.status_code == 200 and res.text.strip():
                    response_text = res.text
                    break
            except Exception:
                pass
            time.sleep(1)
        if response_text:
            break
            
    if response_text:
        cleaned_response = re.sub(r'\[\s*(.*?)\s*\]', r'$$\1$$', response_text)
        return cleaned_response
    return None

if app_mode == "🔍 Sawal ka Step-by-Step Jawab":
    st.markdown("### 🧠 Doubt Solver Mode")
    query = st.text_area(
        "Apna sawal yahan likhein:",
        placeholder="Jaise: Integration, calculus, physics, GK, ya koi bhi translation...",
        height=130
    )
    
    if st.button("🚀 Vistarit Jawab Prapt Karein"):
        if query.strip():
            with st.spinner("🧠 AI ekdum saaf aur professional jawab taiyar kar raha hai..."):
                full_prompt = (
                    f"You are an expert AI tutor. You MUST answer the following student query strictly in pure "
                    f"Devanagari Hindi script (हिंदी में) in a very detailed, comprehensive, step-by-step long format. "
                    f"CRITICAL MATH FORMATTING: NEVER wrap math in square brackets [...]. ALWAYS use double dollar signs ($$ ... $$) "
                    f"for display equations and single dollar signs ($ ... $) for inline variables. "
                    f"Student Query: {query}"
                )
                ans = ask_ai(full_prompt)
                if ans:
                    st.markdown("### 📝 Step-by-Step Detailed Answer (Hindi):")
                    st.markdown(ans)
                else:
                    st.error("⚠️ Abhi server par heavy load hai. Kripya 10 sekund rukh kar dobara button dabayein!")
        else:
            st.warning("Kripya pehle apna sawal likhein!")

else:
    st.markdown("### 📝 Practice Question Generator Mode")
    col1, col2 = st.columns(2)
    with col1:
        subject = st.selectbox(
            "Subject Chunein:",
            ["Math (गणित)", "Science (विज्ञान)", "GK / General Knowledge", "English to Hindi Translation (अनुवाद)"]
        )
    with col2:
        num_q = st.slider("Kitne questions chahiye?", 3, 15, 5)
        
    topic = st.text_input(
        "Topic ya Chapter ka naam likhein:",
        placeholder="Jaise: Quadratic Equations, Solar System, Tenses Translation, etc."
    )
    
    if st.button("🚀 Questions Generate Karein"):
        if topic.strip():
            with st.spinner(f"🧠 AI {num_q} practice questions taiyar kar raha hai..."):
                full_prompt = (
                    f"You are an expert AI teacher. Generate exactly {num_q} high-quality practice questions for the subject '{subject}' "
                    f"on the topic '{topic}'. You MUST write everything strictly in pure Devanagari Hindi script (हिंदी में). "
                    f"Format each question clearly with numbers (1, 2, 3...) and provide answer keys or hints at the end of the list. "
                    f"For mathematical formulas, use standard double dollar signs ($$ ... $$) and single dollar signs ($ ... $). "
                    f"Never use square brackets for math equations. Make them very useful for student practice."
                )
                ans = ask_ai(full_prompt)
                if ans:
                    st.markdown(f"### 📋 Generated {num_q} Practice Questions ({subject} - {topic}):")
                    st.markdown(ans)
                else:
                    st.error("⚠️ Abhi server par heavy load hai. Kripya 10 sekund rukh kar dobara button dabayein!")
        else:
            st.warning("Kripya topic ya chapter ka naam likhein!")
            
        
        
        
        
        
        
        
        
        
                    
                    
                    
                    
                    
