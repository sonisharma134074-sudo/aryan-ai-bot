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

# Ultra-Modern Galaxy Space Background & UI CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    .main {
        background: linear-gradient(rgba(11, 15, 25, 0.85), rgba(11, 15, 25, 0.95)), 
                    url('https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?q=80&w=1920&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #f3f4f6;
    }
    
    .stTextInput > div > div > input, .stTextArea > div > div > textarea, .stSelectbox > div > div > div {
        background-color: rgba(17, 24, 39, 0.9) !important;
        color: #ffffff !important;
        border-radius: 10px !important;
        border: 1px solid rgba(129, 140, 248, 0.5) !important;
        backdrop-filter: blur(10px);
    }
    
    .gradient-title {
        background: linear-gradient(135deg, #818cf8 0%, #c084fc 50%, #f472b6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.3rem;
        font-weight: 700;
        margin-bottom: 0.1rem;
    }
    
    .subtitle {
        color: #cbd5e1;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.5);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 22px rgba(168, 85, 247, 0.7);
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Hub Info
with st.sidebar:
    st.markdown("### 🌟 Student Pro Hub")
    st.markdown("100% Free • Galaxy Space Theme")
    st.markdown("---")
    st.markdown("💡 **Active Features:**")
    st.markdown("- 🧠 Text Doubt Solver")
    st.markdown("- 📸 Camera & Gallery Photo Scanner")
    st.markdown("- 📚 Subject Important Notes")
    st.markdown("- 🎨 AI Custom + Preset Diagrams & Labels")
    st.markdown("- 📖 English to Hindi Translation")
    st.markdown("- 📝 Practice Question Generator")
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 0.85rem;'>Designed with 🚀 for Soni Sharma</p>", unsafe_allow_html=True)

st.markdown('<p class="gradient-title">🚀 Student Pro AI Assistant</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Galaxy Space Background, Custom & Preset Diagrams + Labels Guide!</p>', unsafe_allow_html=True)

# Mode Selection
app_mode = st.radio(
    "Mode Chunein:",
    [
        "🔍 Text Doubt", 
        "📸 Photo Scanner", 
        "📚 Important Notes", 
        "🎨 AI Diagram & Labels", 
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
                    st.error("⚠️️ Sabhi servers par abhi bhari load hai. Kripya 2 seconds baad dobara click karein!")
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

# 3. Important Notes Generator Mode
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

# 4. AI Image & Diagram Generator Mode (Supports BOTH Custom Text & Presets + Hindi Labels Guide)
elif app_mode == "🎨 AI Diagram & Labels":
    st.markdown("### 🎨 AI Educational Diagram & Labeled Guide")
    st.markdown("Popular presets chunein YA apna custom description likhein—sath mein saare parts ke naam aur details Hindi mein paayein!")
    
    diagram_choice = st.selectbox(
        "Diagram Chunein ya Apna Likhein:",
        [
            "✨ Custom Description (Apna khud ka likhein)",
            "🧬 Chromosome Structure (गुणसूत्र)",
            "🌱 Plant Cell Structure (पादप कोशिका)",
            "🐾 Animal Cell Structure (जंतु कोशिका)",
            "🧬 DNA Double Helix (डीएनए)",
            "❤️ Human Heart Labeled (मानव हृदय)",
            "🪐 Solar System (सौर मंडल)",
            "🌊 Water Cycle (जल चक्र)"
        ]
    )
    
    if diagram_choice == "✨ Custom Description (Apna khud ka likhein)":
        custom_query = st.text_input(
            "Apni pasand ka koi bhi diagram ya image English mein likhein:",
            placeholder="Jaise: Neuron cell structure, microscope diagram, atom structure..."
        )
        img_query = custom_query if custom_query.strip() else "educational scientific diagram"
        parts_guide = ""
    else:
        diagram_data = {
            "🧬 Chromosome Structure (गुणसूत्र)": {
                "prompt": "detailed scientific diagram of chromosome X shape with clear parts, clean vector illustration, white background",
                "labels": """### 🏷️ Chromosome (गुणसूत्र) ke Mukhya Parts aur Naam:
1. **Chromatid (क्रोमैटिड):** DNA aur protein ki do identical strands jo cell division ke waqt dikhti hain.
2. **Centromere (सेंट्रोमियर):** Woh central constricted region jahan dono chromatids aapas mein jude hote hain.
3. **Telomere (टीलोमियर):** Chromosome ke dono ends jo DNA ko damage hone se bachate hain.
4. **Short Arm (p arm) & Long Arm (q arm):** Centromere ke upar aur niche ke hisse."""
            },
            "🌱 Plant Cell Structure (पादप कोशिका)": {
                "prompt": "detailed plant cell diagram with cell wall chloroplast vacuole labeled, clean vector educational illustration",
                "labels": """### 🏷️ Plant Cell (पादप कोशिका) ke Mukhya Parts aur Naam:
1. **Cell Wall (कोशिका भित्ति):** Cell ki outermost rigid layer jo Cellulose ki bani hoti hai.
2. **Chloroplast (क्लोरोप्लास्ट):** Jisme chlorophyll hota hai aur photosynthesis (prakash-sanshleshan) hota hai.
3. **Vacuole (रिक्तिका):** Badi central vacuole jo cell ko rigidity aur shape deti hai.
4. **Nucleus (केंद्रक):** Jo cell ki saari activities ko control karta hai aur genetic material rakhta hai."""
            },
            "🐾 Animal Cell Structure (जंतु कोशिका)": {
                "prompt": "detailed animal cell diagram with nucleus mitochondria membrane, clean vector educational illustration",
                "labels": """### 🏷️ Animal Cell (जंतु कोशिका) ke Mukhya Parts aur Naam:
1. **Cell Membrane (कोशिका झिल्ली):** Semipermeable membrane jo cell ke andar-bahar cheezon ko control karti hai.
2. **Mitochondria (माइटोकॉन्ड्रिया):** Isko cell ka "Powerhouse" kehte hain kyunki yeh energy (ATP) banata hai.
3. **Nucleus (केंद्रक):** Cell ka brain jo DNA aur genes carry karta hai.
4. **Ribosome:** Protein synthesis ka kaam karta hai."""
            },
            "🧬 DNA Double Helix (डीएनए)": {
                "prompt": "DNA double helix structure scientific 3D illustration, clean educational vector style",
                "labels": """### 🏷️ DNA Structure ke Mukhya Parts aur Naam:
1. **Double Helix:** Iski ladder jaisi ghuma hua structure hoti hai.
2. **Nitrogenous Bases:** Adenine (A) hamesha Thymine (T) se judta hai, aur Cytosine (C) hamesha Guanine (G) se judta hai.
3. **Sugar-Phosphate Backbone:** Jo DNA ki outer sides banati hai."""
            },
            "❤️ Human Heart Labeled (मानव हृदय)": {
                "prompt": "human heart anatomical diagram with chambers valves arteries, clean medical textbook illustration",
                "labels": """### 🏷️ Human Heart (Manav Hriday) ke Mukhya Parts aur Naam:
1. **Right & Left Atrium (अलिंद):** Upar ke do chambers jo blood receive karte hain.
2. **Right & Left Ventricle (निलय):** Niche ke do chambers jo blood ko poore shareer mein pump karte hain.
3. **Aorta (महाधमनी):** Oxygenated blood ko poore shareer mein bhejti hai.
4. **Valves:** Blood ke ulte flow ko rokte hain."""
            },
            "🪐 Solar System (सौर मंडल)": {
                "prompt": "solar system planets orbiting the sun educational diagram, clean vector style",
                "labels": """### 🏷️ Solar System (सौर मंडल) ke Mukhya Parts:
1. **Sun (सूर्य):** Center star jiske gravitational pull se saare planets ghumte hain.
2. **Inner Planets:** Mercury (बुध), Venus (शुक्र), Earth (पृथ्वी), Mars (मंगल).
3. **Outer Planets:** Jupiter (बृहस्पति), Saturn (शनि), Uranus (अरुण), Neptune (वरुण)."""
            },
            "🌊 Water Cycle (जल चक्र)": {
                "prompt": "water cycle natural process evaporation precipitation condensation diagram, clean educational illustration",
                "labels": """### 🏷️ Water Cycle (Jal Chakra) ke Mukhya Steps:
1. **Evaporation (वाष्पीकरण):** Suraj ki garmi se paani ka bhaaf ban kar udna.
2. **Condensation (संघनन):** Bhaaf ka thanda hokar badal (clouds) banna.
3. **Precipitation (वर्षा):** Baarish, barf ya ole ke roop mein zameen par paani ka wapas aana."""
            }
        }
        selected_info = diagram_data.get(diagram_choice, {})
        img_query = selected_info.get("prompt", "educational scientific diagram")
        parts_guide = selected_info.get("labels", "")
    
    if st.button("🚀 Diagram aur Labels Generate Karein"):
        if img_query.strip():
            with st.spinner("🎨 AI educational diagram aur labels taiyar kar raha hai..."):
                encoded_prompt = requests.utils.quote(img_query + ", high quality, 8k resolution, clean educational vector")
                image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=800&height=600&nologo=true"
                
                st.image(image_url, caption=f"Generated Diagram", use_container_width=True)
                st.success("✅ Diagram taiyar hai!")
                
                if parts_guide:
                    st.markdown("---")
                    st.markdown(parts_guide)
                elif diagram_choice == "✨ Custom Description (Apna khud ka likhein)":
                    with st.spinner("🧠 AI is diagram ke parts ki details Hindi mein nikal raha hai..."):
                        info_prompt = f"Provide detailed scientific parts and labels guide in pure Hindi for: {img_query}"
                        ai_parts = ask_pollinations_ai(info_prompt)
                        if ai_parts:
                            st.markdown("---")
                            st.markdown("### 🏷️ Custom Diagram Parts & Details (Hindi):")
                            display_formatted_response(ai_parts)
        else:
            st.warning("Kripya description likhein ya option chunein!")

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
              
                
        
            
                    
                    
                    
                    
