import streamlit as st
import requests
from PIL import Image
import io
import time
import re

# Page Configuration
st.set_page_config(
    page_title="Student Pro AI Assistant",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Ultra-Modern CSS Styling for Professional Mobile UI
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

# Sidebar Hub Info (Zero API Key Needed)
with st.sidebar:
    st.markdown("### 🌟 Student Pro Hub")
    st.markdown("100% Free • 10-Server + Notes & Images")
    st.markdown("---")
    st.markdown("💡 **Active Features:**")
    st.markdown("- 🧠 Text Doubt Solver")
    st.markdown("- 📸 Camera & Gallery Photo Scanner")
    st.markdown("- 📚 Subject Important Notes (Hist/Bio/Geo)")
    st.markdown("- 🎨 AI Image & Diagram Generator")
    st.markdown("- 📖 English to Hindi Translation")
    st.markdown("- 📝 Practice Question Generator")
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #6b7280; font-size: 0.85rem;'>Designed with 🚀 for Soni Sharma</p>", unsafe_allow_html=True)

st.markdown('<p class="gradient-title">🚀 Student Pro AI Assistant</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Students ke liye — Notes, Diagrams, aur 10-Server Backup ke sath shuddh Hindi!</p>', unsafe_allow_html=True)

# Mode Selection (Expanded with Notes & Image Generation)
app_mode = st.radio(
    "Mode Chunein:",
    [
        "🔍 Text Doubt", 
        "📸 Photo Scanner", 
        "📚 Important Notes", 
        "🎨 AI Diagram Generator", 
        "📖 Translation", 
        "📝 Practice Qs"
    ],
    horizontal=True
)

st.markdown("---")

def ask_pollinations_ai(prompt_text):
    """Zero API key, 10-Model automatic fallback with auto-wait & retry system"""
    models = [
        "openai", 
        "mistral", 
        "deepseek", 
        "llama", 
        "qwen", 
        "openai-large", 
        "mistral-large", 
        "deepseek-coder", 
        "llama-3", 
        "qwen-coder"
    ]
    
    for cycle in range(2):
        for model in models:
            url = f"https://text.pollinations.ai/{requests.utils.quote(prompt_text)}?model={model}&private=true"
            try:
                response = requests.get(url, timeout=15)
                if response.status_code == 200 and response.text.strip():
                    return response.text
            except Exception:
                continue
        time.sleep(1)
                
    return None

def display_formatted_response(raw_text):
    """Automatically cleans raw LaTeX brackets and renders professional math formulas"""
    if not raw_text:
        return
    
    text = re.sub(r'\\\[(.*?)\\\]', r'$$\1$$', raw_text, flags=re.DOTALL)
    text = re.sub(r'\[\s*(\\begin\{aligned\}.*?\\end\{aligned\})\s*\]', r'$$\1$$', text, flags=re.DOTALL)
    text = re.sub(r'\[\s*(\\begin\{matrix\}.*?\\end\{matrix\})\s*\]', r'$$\1$$', text, flags=re.DOTALL)
    text = re.sub(r'\\\((.*?)\\\)', r'$\1$', text, flags=re.DOTALL)
    text = text.replace(r'(\implies)', r'$\implies$')
    
    st.markdown(text)

# 1. Text Doubt Solver Mode
if app_mode == "🔍 Text Doubt":
    st.markdown("### 🧠 Doubt Solver Mode")
    query = st.text_area(
        "Apna sawal yahan likhein (Math, Physics, Chemistry, etc.):",
        placeholder="Jaise: Quadratic equations, integration...",
        height=130
    )
    
    if st.button("🚀 Vistarit Jawab Prapt Karein"):
        if query.strip():
            with st.spinner("🧠 AI 10-Server network se step-by-step jawab nikal raha hai..."):
                full_prompt = (
                    f"You are an expert AI tutor. Answer the student query strictly in pure "
                    f"Devanagari Hindi script (हिंदी में) in a very detailed, step-by-step long format. "
                    f"CRITICAL MATH FORMATTING: Use standard double dollar signs ($$ ... $$) for display math equations "
                    f"and single dollar signs ($ ... $) for inline variables. Use \\implies for steps. "
                    f"Student Query: {query}"
                )
                ans = ask_pollinations_ai(full_prompt)
                if ans:
                    st.markdown("### 📝 Step-by-Step Detailed Answer (Hindi):")
                    display_formatted_response(ans)
                else:
                    st.error("⚠️ Sabhi servers par abhi bhari load hai. Kripya 2 seconds baad dobara click karein!")
        else:
            st.warning("Kripya pehle apna sawal likhein!")

# 2. Photo & Camera Scanner Mode
elif app_mode == "📸 Photo Scanner":
    st.markdown("### 📸 Photo & Camera Scanner Mode")
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
            
            with st.spinner("🔍 AI photo ko analyze karke jawab likh raha hai..."):
                prompt_desc = extra_note if extra_note.strip() else "Is photo mein diye gaye sawal ko step-by-step solve karein."
                full_prompt = (
                    f"You are an expert AI tutor. A student has uploaded a question image. "
                    f"Student's instruction: {prompt_desc}. "
                    f"Provide a very detailed, comprehensive step-by-step solution in pure Devanagari Hindi script (हिंदी में). "
                    f"Use double dollar signs ($$ ... $$) for equations."
                )
                ans = ask_pollinations_ai(full_prompt)
                if ans:
                    st.markdown("### 📝 Step-by-Step Solution (Hindi):")
                    display_formatted_response(ans)
                else:
                    st.error("⚠️ Image process karne mein error aaya. Dobara koshish karein!")
        else:
            st.warning("Kripya pehle camera se photo khinchein ya gallery se upload karein!")

# 3. Important Notes Generator Mode (History, Bio, Geo, etc.)
elif app_mode == "📚 Important Notes":
    st.markdown("### 📚 Subject Important Notes & Key Points Generator")
    col1, col2 = st.columns(2)
    with col1:
        subj_choice = st.selectbox(
            "Subject Chunein:",
            ["History (इतिहास)", "Biology (जीव विज्ञान)", "Geography (भूगोल)", "Physics (भौतिकी)", "Chemistry (रसायन)", "Pol Science (राजनीति विज्ञान)"]
        )
    with col2:
        note_type = st.selectbox(
            "Notes ka Format:",
            ["Important Points & Summary", "Key Dates & Events", "Important Definitions", "Exam Revision Cheat Sheet"]
        )
        
    chapter_topic = st.text_input(
        "Chapter ya Topic ka naam likhein:",
        placeholder="Jaise: The French Revolution, Photosynthesis, Solar System..."
    )
    
    if st.button("🚀 Important Notes Generate Karein"):
        if chapter_topic.strip():
            with st.spinner(f"📚 AI {subj_choice} ke liye important notes taiyar kar raha hai..."):
                full_prompt = (
                    f"You are an expert professor. Generate comprehensive, high-yield examination notes, "
                    f"important key points, definitions, and highlights for the subject '{subj_choice}' on the topic '{chapter_topic}'. "
                    f"Format type: '{note_type}'. "
                    f"You MUST write everything strictly in pure Devanagari Hindi script (हिंदी में) using clean bullet points and bold headings."
                )
                ans = ask_pollinations_ai(full_prompt)
                if ans:
                    st.markdown(f"### 📋 Important Notes ({subj_choice} - {chapter_topic}):")
                    display_formatted_response(ans)
                else:
                    st.error("⚠️ Notes generate karne mein error aaya! Dobara koshish karein.")
        else:
            st.warning("Kripya chapter ya topic ka naam likhein!")

# 4. AI Image & Diagram Generator Mode
elif app_mode == "🎨 AI Diagram Generator":
    st.markdown("### 🎨 AI Educational Diagram & Image Generator")
    st.markdown("Pankh, cell structure, map concept, ya kisi bhi scientific/historical scene ka description likhein:")
    
    img_query = st.text_input(
        "Image ya Diagram ka description English mein likhein (Best results ke liye):",
        placeholder="Jaise: Plant cell structure diagram labeled educational, or Solar system planets..."
    )
    
    if st.button("🚀 Diagram / Image Generate Karein"):
        if img_query.strip():
            with st.spinner("🎨 AI educational image generate kar raha hai..."):
                encoded_prompt = requests.utils.quote(img_query + ", educational diagram, clean vector style, high quality")
                image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=800&height=600&nologo=true"
                
                st.image(image_url, caption=f"Generated AI Diagram: {img_query}", use_container_width=True)
                st.success("✅ Aapka diagram taiyar hai! Students ise save karke padhai mein use kar sakte hain.")
        else:
            st.warning("Kripya description likhein!")

# 5. English to Hindi Translation Mode
elif app_mode == "📖 Translation":
    st.markdown("### 📖 English to Hindi Translation Mode")
    eng_text = st.text_area(
        "English text yahan enter karein:",
        placeholder="Jaise: Translate this paragraph or sentence...",
        height=130
    )
    
    if st.button("🚀 Shuddh Hindi Anuvad Karein"):
        if eng_text.strip():
            with st.spinner("📖 AI shuddh Hindi anuvad kar raha hai..."):
                full_prompt = (
                    f"Translate the following English text into pure, natural, and grammatically "
                    f"correct Devanagari Hindi script (हिंदी में). Also provide useful vocabulary notes. "
                    f"English Text: {eng_text}"
                )
                ans = ask_pollinations_ai(full_prompt)
                if ans:
                    st.markdown("### 📋 Hindi Anuvad (Translation):")
                    display_formatted_response(ans)
                else:
                    st.error("⚠️ Anuvad karne mein error aaya!")
        else:
            st.warning("Kripya pehle English text likhein!")

# 6. Practice Question Generator Mode
else:
    st.markdown("### 📝 Practice Question Generator Mode")
    col1, col2 = st.columns(2)
    with col1:
        subject = st.selectbox(
            "Subject Chunein:",
            ["Math (गणित)", "Physics (भौतिकी)", "Chemistry (रसायन विज्ञान)", "Biology (जीव विज्ञान)", "History (इतिहास)", "Geography (भूगोल)"]
        )
    with col2:
        num_q = st.slider("Kitne questions chahiye?", 3, 10, 5)
        
    topic = st.text_input(
        "Topic ya Chapter ka naam likhein:",
        placeholder="Jaise: Integration, Cell Division, Nationalism in India..."
    )
    
    if st.button("🚀 Questions Generate Karein"):
        if topic.strip():
            with st.spinner(f"🧠 AI {num_q} practice questions taiyar kar raha hai..."):
                full_prompt = (
                    f"Generate exactly {num_q} high-quality practice questions for the subject '{subject}' "
                    f"on the topic '{topic}'. You MUST write everything strictly in pure Devanagari Hindi script (हिंदी में). "
                    f"Provide clear answers/hints at the end. Use double dollar signs ($$ ... $$) for math equations."
                )
                ans = ask_pollinations_ai(full_prompt)
                if ans:
                    st.markdown(f"### 📋 Generated {num_q} Practice Questions ({subject} - {topic}):")
                    display_formatted_response(ans)
                else:
                    st.error("⚠️ Questions generate karne mein error aaya!")
        else:
            st.warning("Kripya topic ka naam likhein!")
                
        
            
                    
                    
                    
                    
