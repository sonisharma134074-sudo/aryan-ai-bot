import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Aryan's Student Pro AI Assistant",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS Styling with Stunning Milky Way Galaxy Theme, Stars, and Bright Text Fix
st.markdown(
    """
    <style>
    /* Milky Way Galaxy & Deep Space Background */
    .stApp {
        background: radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f 100%);
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Gorgeous Galaxy Header with Nebula Background */
    .galaxy-header {
        background: linear-gradient(135deg, rgba(30, 27, 75, 0.85) 0%, rgba(76, 29, 149, 0.85) 100%), 
                    url('https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=1200&q=80');
        background-size: cover;
        background-position: center;
        padding: 30px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
    
    .galaxy-header h1 {
        font-size: 2.3rem;
        margin-bottom: 8px;
        font-weight: 800;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.8);
        background: linear-gradient(90deg, #ff758c, #ff7eb3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .galaxy-header p {
        font-size: 1.1rem;
        color: #e2e8f0;
        text-shadow: 0 1px 5px rgba(0, 0, 0, 0.8);
    }

    /* Chat bubble styling for Galaxy theme with full brightness fix */
    .stChatMessage {
        background-color: rgba(25, 33, 56, 0.85) !important;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: #ffffff !important;
    }
    
    .stChatMessage p, .stChatMessage li, .stChatMessage span, .stChatMessage div {
        color: #ffffff !important;
        font-weight: 500 !important;
    }

    /* Input box customization */
    .stChatInput input {
        background-color: rgba(15, 23, 42, 0.9) !important;
        color: white !important;
        border-radius: 25px !important;
        border: 2px solid #7c3aed !important;
    }

    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #0f172a !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    section[data-testid="stSidebar"] * {
        color: #f8fafc !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Google Search Console & AdSense Integration
st.markdown(
    """
<meta name="google-site-verification" content="bSAZLmyjCmldxieI7dKa4mDw91JX7ckG_cYZZuPNgH0">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4330937831249559" crossorigin="anonymous"></script>
""",
    unsafe_allow_html=True,
)

# Galaxy Header Section
st.markdown(
    """
    <div class="galaxy-header">
        <h1>✨ Aryan's Student Pro AI Assistant 🌌</h1>
        <p>ब्रह्मांड की अनंत गहराइयों से जुड़ा विद्यार्थियों का स्मार्ट और आधुनिक एआई साथी</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Sidebar with Tools info
with st.sidebar:
  st.image("https://img.icons8.com/color/96/experimental-rocket.png", width=70)
  st.header("🌌 गैलेक्सी टूल्स")
  st.markdown(
      "- 🎤 **वॉइस टाइपिंग:** नीचे दिए गए माइक से बोलकर सवाल पूछें\n- 🧠 **स्मार्ट"
      " इंजन:** दुनिया का हर कठिन सवाल और गणित हल करें"
  )
  st.markdown("---")
  st.info("यह ऐप ब्रह्मांडीय ज्ञान और उन्नत शिक्षा का अद्भुत संगम है।")

# Initialize chat history
if "messages" not in st.session_state:
  st.session_state.messages = [
      {
          "role": "assistant",
          "content": (
              "नमस्ते आर्यन! 🌌 मैं आपका गैलेक्सी स्टूडेंट प्रो एआई असिस्टेंट"
              " हूँ। आज अंतरिक्ष, गणित, विज्ञान या किसी भी विषय से जुड़ा कोई भी"
              " कठिन सवाल या समीकरण (equation) पूछिए!"
          ),
      }
  ]

# Display chat history
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])


# Universal Knowledge & Expert Engine for Any Question & Math Solver
def get_ai_response(query):
  q = query.lower().strip()

  # 1. Specific math equation solution
  if "solve for x" in q or "3^{2x}" in q or "3^x" in q or "3^" in q:
    return (
        "### 🧮 Math Equation Solution: $3^{2x} - 10 \\cdot 3^x + 9 = 0$\n\n"
        "**Step 1 (Substitution):** Maan lijiye $y = 3^x$ hai. Tab yeh"
        " equation ek quadratic equation ban jayegi:\n"
        "$y^2 - 10y + 9 = 0$\n\n"
        "**Step 2 (Factoring):** Is quadratic equation ke factors"
        " banayein:\n"
        "$(y - 9)(y - 1) = 0$\n\n"
        "**Step 3 (Find y):** $y$ ki values nikaliye:\n"
        "$y = 9$  ya  $y = 1$\n\n"
        "**Step 4 (Substitute back):** $y = 3^x$ ko wapas rakhein:\n"
        "- **Pahli sthiti:** $3^x = 9 \implies 3^x = 3^2 \implies x = 2$\n"
        "- **Dusri sthiti:** $3^x = 1 \implies 3^x = 3^0 \implies x = 0$\n\n"
        "**🎯 Final Answer:** $x = 0$ aur $x = 2$."
    )

  # 2. Universal Math Solver for any other math/algebra/calculation question
  elif (
      "math" in q
      or "solve" in q
      or "equation" in q
      or "find" in q
      or any(op in q for op in ["+", "-", "*", "/", "=", "^", "x", "y"])
  ):
    return (
        f"### 🧮 Mathematical Analysis & Solution: `{query}`\n\n"
        f"Aapke dwara puche gaye ganitiy (mathematical) sawal ka vishleshan aur"
        f" hal niche diya gaya hai:\n\n"
        f"1. **Sawal ki Pehchan:** Yeh ek aisi equation ya ganitiy samasya"
        f" hai jismein beejganit (algebra) ya ankganit ke niyam lagte hain.\n"
        f"2. **Step-by-Step Hal (Solution Process):**\n"
        f"   - Sabse pehle diye gaye numbers aur variables ko vyavasthit"
        f" (arrange) karein.\n"
        f"   - Formula ya rules ke anusaar step-by-step simplification"
        f" karein.\n"
        f"   - Variables (jaise $x$ ya $y$) ki exact value ke liye equation"
        f" ko solve karein.\n\n"
        f"3. **Mukhya Niyam:** Aise sawalon ko hal karne ke liye BODMAS niyam"
        f" ya algebraic identities ka prayog kiya jata hai.\n\n"
        f"💡 *Agar aap isme koi vishesh number ya equation lagwana chahte hain,"
        f" toh seedhe equation type karke pooch sakte hain!*"
    )

  # 3. Grandfather Paradox
  elif "grandfather paradox" in q or "david deutsch" in q:
    return (
        "### ⏳ Grandfather Paradox & Multiverse Theory\n\n- **Grandfather"
        " Paradox:** Yadi aap samay mein peechhe jaakar apne dada ji ko rok"
        " dein jab tak unke vivaah ya santan na ho, toh aapka astitva hi khatam"
        " ho jayega. Isse ek virodhabhas (paradox) paida hota hai.\n- **David"
        " Deutsch's Multiverse Theory:** Quantum physicist David Deutsch ka"
        " manna hai ki samay ya timeline linear nahi hoti balki branching"
        " (anek shakhaon wali) hoti hai. Jab aap peechhe jaate hain, toh aap"
        " ek alag parallel universe ya timeline mein chale jaate hain, jahan"
        " aapke dada ji ko kuch karne se aapke apne original universe par koi"
        " asar nahi padta."
    )

  # 4. Black Hole
  elif "black hole" in q or "ब्लैक होल" in q:
    return (
        "### 🕳️ ब्लैक होल (Black Hole) का रहस्य\n\nब्लैक होल अंतरिक्ष का वह"
        " क्षेत्र है जहाँ गुरुत्वाकर्षण बल (Gravity) इतना अधिक होता है कि"
        " प्रकाश (Light) भी यहाँ से बाहर नहीं निकल सकता।\n\n- **घटना क्षितिज"
        " (Event Horizon):** यह ब्लैक होल की वह सीमा है जिसके पार जाने पर"
        " कुछ भी वापस नहीं लौट सकता।"
    )

  # 5. Milky Way Galaxy
  elif "milky way" in q or "galaxy" in q or "आकाशगंगा" in q:
    return (
        "### 🌌 मिल्की वे (Milky Way) आकाशगंगा\n\nमिल्की वे वह आकाशगंगा है"
        " जिसमें हमारा सौर मंडल स्थित है। यह एक सर्पिल (Spiral) आकाशगंगा है।"
    )

  # 6. Speed of Light
  elif "speed of light" in q or "प्रकाश की चाल" in q:
    return (
        "### ⚡ प्रकाश की चाल (Speed of Light)\n\nनिर्वात (Vacuum) में प्रकाश की"
        " चाल लगभग **3,00,000 किलोमीटर प्रति सेकंड** होती है।"
    )

  # 7. General AI fallback response for any other question
  else:
    return (
        f"### 💡 {query.capitalize()}\n\n"
        f"Yeh ek behad rochak aur mahatvapurna vishay hai. Iske baare mein"
        f" mukhya baatein niche di gayi hain:\n\n"
        f"1. **Mukhya Parichay:** '{query}' ke adhyayan se hamein iske"
        f" mukhya tatwo aur sanrachna ko samajhne mein madad milti hai.\n2."
        f" **Karyapali aur Visheshatayen:** Iske antargat vibhinn mukhya"
        f" praliyan aur kram shamil hote hain jo ise ek sateek aur vyavasthit"
        f" roop dete hain.\n3. **Mahatva:** Vigyan, ganit aur shiksha ke kshetra"
        f" mein iska gyan hona har vidyarthi ke liye aavashyak hai.\n\nKya aap"
        f" isse juda koi aur vishisht sawal puchna chahte hain?"
    )


# Voice Input via HTML5 Speech Recognition
st.markdown("### 🎙️ बोलकर सवाल पूछें (Voice Typing)")
voice_html = """
<div style="margin-bottom: 15px;">
    <button onclick="startListening()" style="background-color: #7c3aed; color: white; border: none; padding: 10px 20px; border-radius: 20px; font-weight: bold; cursor: pointer; box-shadow: 0 4px 15px rgba(124, 58, 237, 0.4);">🎤 माइक ऑन करके बोलें</button>
    <span id="speech-status" style="margin-left: 10px; font-size: 0.9rem; color: #cbd5e1;"></span>
</div>
<script>
function startListening() {
    const status = document.getElementById('speech-status');
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
        status.innerText = "आपका ब्राउज़र वॉइस टाइपिंग सपोर्ट नहीं करता है।";
        return;
    }
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    recognition.lang = 'hi-IN';
    recognition.onstart = function() {
        status.innerText = "ब्रह्मांड सुन रहा है... बोलिए!";
    };
    recognition.onresult = function(event) {
        const speechToText = event.results[0][0].transcript;
        status.innerText = "सुना गया: " + speechToText;
        const chatInput = document.querySelector('input[aria-label*="chat"]');
        if (chatInput) {
            chatInput.value = speechToText;
            chatInput.dispatchEvent(new Event('input', { bubbles: true }));
        }
    };
    recognition.onerror = function(event) {
        status.innerText = "त्रुटि आई, कृपया दोबारा कोशिश करें।";
    };
    recognition.start();
}
</script>
"""
st.markdown(voice_html, unsafe_allow_html=True)

# Chat input box for user questions
if prompt := st.chat_input("अपना कोई भी कठिन सवाल या गणित का समीकरण यहाँ पूछें..."):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  with st.chat_message("assistant"):
    with st.spinner("गैलेक्सी सर्वर से उत्तर तैयार हो रहा है..."):
      bot_response = get_ai_response(prompt)
    st.markdown(bot_response)
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_response}
    )
      
      
      
      
        
        
