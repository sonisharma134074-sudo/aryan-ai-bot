import streamlit as st
import requests
import urllib.parse
import time
import re
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Student Pro AI Assistant",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Ultra-Modern CSS Styling
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
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🌟 Student Pro Hub")
    st.markdown("Aapka apna advanced AI Tutor jo har mushkil sawal ko aasan banata hai.")
    st.markdown("---")
    st.markdown("💡 **Features:**")
    st.markdown("- 🧠 Step-by-Step Doubt Solver")
    st.markdown("- 📸 Camera & Photo Upload Scanner")
    st.markdown("- 📝 Practice Question Generator")
    st.markdown("- 📐 Clean LaTeX Math & Formulas")
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #6b7280; font-size: 0.85rem;'>Designed with 🚀 for Soni Sharma</p>", unsafe_allow_html=True)

st.markdown('<p class="gradient-title">🚀 Student Pro AI Assistant</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Photo khinchein, upload karein ya text likhein — sabhi jawab shuddh Hindi aur professional format mein!</p>', unsafe_allow_html=True)

app_mode = st.radio(
    "Mode Chunein:",
    ["🔍 Text Doubt Solver", "📸 Photo / Camera Scanner", "📝 Practice Questions Generator"],
    horizontal=True
)

st.markdown("---")

def clean_math_output(text):
    # Har tarah ke brackets ko clean karke proper LaTeX $$ format me badalna
    text = re.sub(r'\\\[\s*(.*?)\s*\\\]', r'\n$$\n\1\n$$\n', text, flags=re.DOTALL)
    text = re.sub(r'\[\s*\\begin\{aligned\}(.*?)\\end\{aligned\}\s*\]', r'\n$$\n\\begin{aligned}\1\\end{aligned}\n$$\n', text, flags=re.DOTALL)
    text = re.sub(r'\[\s*(.*?[\=\+\-\*\/\\int\\frac\\implies].*?)\s*\]', r'$$\1$$', text)
    text = re.sub(r'\[\s*([^\[\]]+?)\s*\]', r'$$\1$$', text)
    return text

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
        return clean_math_output(response_text)
    return None

if app_mode == "🔍 Text Doubt Solver":
    st.markdown("### 🧠 Doubt Solver Mode")
    query = st.text_area(
        "Apna sawal yahan likhein (Math, Physics, Chemistry, etc.):",
        placeholder="Jaise: Quadratic equations, linear equations, physics derivation...",
        height=130
    )
    
    if st.button("🚀 Vistarit Jawab Prapt Karein"):
        if query.strip():
            with st.spinner("🧠 AI ekdum saaf aur professional format mein jawab taiyar kar raha hai..."):
                full_prompt = (
                    f"You are an expert AI tutor. You MUST answer the following student query strictly in pure "
                    f"Devanagari Hindi script (हिंदी में) in a very detailed, step-by-step long format. "
                    f"CRITICAL MATH FORMATTING RULES (STRICTLY FOLLOW): "
                    f"1. NEVER wrap equations in square brackets [...] or raw text brackets. "
                    f"2. ALWAYS use standard double dollar signs ($$ ... $$) for display math equations on separate lines, and single dollar signs ($ ... $) for inline variables. "
                    f"3. Use LaTeX symbols like \\implies for step transitions, just like professional math books. "
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

elif app_mode == "📸 Photo / Camera Scanner":
    st.markdown("### 📸 Photo & Camera Scanner Mode")
    st.markdown("Yahan aap apne sawal ki photo khinch sakte hain ya gallery se upload kar sakte hain:")
    
    upload_option = st.radio("Photo kaise dena chahte hain?", ["📷 Camera se Photo Khinchein", "📂 Gallery se Upload Karein"], horizontal=True)
    
    img_file = None
    if upload_option == "📷 Camera se Photo Khinchein":
        img_file = st.camera_input("Apne phone ka camera use karein")
    else:
        img_file = st.file_uploader("Apni gallery se image chunein", type=["jpg", "png", "jpeg"])
        
    extra_note = st.text_input(
        "Photo ke sath koi extra instruction likhna ho toh (Optional):",
        placeholder="Jaise: Is sawal ko step-by-step Hindi mein samjhayein..."
    )
    
    if st.button("🚀 Photo ka Jawab Nikalein"):
        if img_file is not None:
            image = Image.open(img_file)
            st.image(image, caption="Uploaded Question Image", use_container_width=True)
            
            with st.spinner("🔍 AI photo ko analyze karke step-by-step jawab likh raha hai..."):
                prompt_desc = extra_note if extra_note.strip() else "Is photo mein diye gaye sawal ko solve karein."
                full_prompt = (
                    f"You are an expert AI tutor. A student has uploaded an image of a question. "
                    f"Student's extra note: {prompt_desc}. "
                    f"Please provide a very detailed, comprehensive step-by-step solution in pure Devanagari Hindi script (हिंदी में). "
                    f"CRITICAL FORMATTING: NEVER use square brackets [...]. Use double dollar signs ($$ ... $$) for display equations and single dollar signs ($ ... $) for variables. Use \\implies for steps."
                )
                ans = ask_ai(full_prompt)
                if ans:
                    st.markdown("### 📝 Step-by-Step Solution from Image (Hindi):")
                    st.markdown(ans)
                else:
                    st.error("⚠️ Server par load hai. Kripya dobara koshish karein!")
        else:
            st.warning("Kripya pehle camera se photo khinchein ya gallery se upload karein!")

else:
    st.markdown("### 📝 Practice Question Generator Mode")
    col1, col2 = st.columns(2)
    with col1:
        subject = st.selectbox(
            "Subject Chunein:",
            ["Math (गणित)", "Physics (भौतिकी)", "Chemistry (रसायन विज्ञान)", "GK / General Knowledge", "English to Hindi Translation"]
        )
    with col2:
        num_q = st.slider("Kitne questions chahiye?", 3, 15, 5)
        
    topic = st.text_input(
        "Topic ya Chapter ka naam likhein:",
        placeholder="Jaise: Quadratic Equations, Thermodynamics, Periodic Table, etc."
    )
    
    if st.button("🚀 Questions Generate Karein"):
        if topic.strip():
            with st.spinner(f"🧠 AI {num_q} practice questions taiyar kar raha hai..."):
                full_prompt = (
                    f"You are an expert AI teacher. Generate exactly {num_q} high-quality practice questions for the subject '{subject}' "
                    f"on the topic '{topic}'. You MUST write everything strictly in pure Devanagari Hindi script (हिंदी में). "
                    f"Format each question clearly with numbers (1, 2, 3...) and provide answer keys or hints at the end of the list. "
                    f"CRITICAL FORMATTING RULES: "
                    f"1. NEVER use square brackets [...] for math formulas. "
                    f"2. Always use standard double dollar signs ($$ ... $$) for equations and single dollar signs ($ ... $) for inline variables. Use \\implies where applicable. "
                    f"Make them extremely neat and useful for student practice."
                )
                ans = ask_ai(full_prompt)
                if ans:
                    st.markdown(f"### 📋 Generated {num_q} Practice Questions ({subject} - {topic}):")
                    st.markdown(ans)
                else:
                    st.error("⚠️ Abhi server par heavy load hai. Kripya 10 sekund rukh kar dobara button dabayein!")
        else:
            st.warning("Kripya topic ya chapter ka naam likhein!")
            
            
        
        
        
        
        
        
        
        
        
                    
                    
                    
                    
                    
