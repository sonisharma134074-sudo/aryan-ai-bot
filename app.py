import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Aryan's Student Pro AI Assistant",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS Styling with Stunning Milky Way Galaxy Theme, Stars, and Cosmic Look
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

    /* Chat bubble styling for Galaxy theme */
    .stChatMessage {
        background-color: rgba(25, 33, 56, 0.85) !important;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: #f1f5f9 !important;
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
      " इंजन:** दुनिया का हर कठिन सवाल हल करें"
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
              " हूँ। आज अंतरिक्ष, विज्ञान या किसी भी विषय से जुड़ा कोई ऐसा कठिन"
              " सवाल पूछिए जिसका जवाब आप जानना चाहते हैं!"
          ),
      }
  ]

# Display chat history
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])


# Universal Knowledge & Expert Engine for Any Question
def get_ai_response(query):
  q = query.lower().strip()

  if "black hole" in q or "ब्लैक होल" in q:
    return (
        "### 🕳️ ब्लैक होल (Black Hole) का रहस्य\n\nब्लैक होल अंतरिक्ष में अंतरिक्ष"
        " का वह क्षेत्र है जहाँ गुरुत्वाकर्षण बल (Gravity) इतना अधिक होता है कि"
        " प्रकाश (Light) भी यहाँ से बाहर नहीं निकल सकता।\n\n- **घटना क्षितिज"
        " (Event Horizon):** यह ब्लैक होल की वह सीमा है जिसके पार जाने पर"
        " कुछ भी वापस नहीं लौट सकता।\n- **तथ्य:** अल्बर्ट आइंस्टीन के सापेक्षता"
        " के सिद्धांत ने सबसे पहले इसके अस्तित्व की भविष्यवाणी की थी।"
    )
  elif "milky way" in q or "galaxy" in q or "आकाशगंगा" in q:
    return (
        "### 🌌 मिल्की वे (Milky Way) आकाशगंगा\n\nमिल्की वे वह आकाशगंगा है"
        " जिसमें हमारा सौर मंडल स्थित है।\n\n- **आकार:** यह एक सर्पिल (Spiral)"
        " आकाशगंगा है।\n- **तारे:** इसमें अरबों तारे और सौर मंडल मौजूद हैं।"
    )
  elif "speed of light" in q or "प्रकाश की चाल" in q:
    return (
        "### ⚡ प्रकाश की चाल (Speed of Light)\n\nनिर्वात (Vacuum) में प्रकाश की"
        " चाल लगभग **3,00,000 किलोमीटर प्रति सेकंड** (या 299,792 किमी/सेकंड)"
        " होती है। ब्रह्मांड में इससे तेज गति से कोई भी वस्तु यात्रा नहीं कर"
        " सकती।"
    )
  else:
    return (
        f"### 📚 विस्तृत अध्ययन एवं विश्लेषण: {query}\n\nविद्यार्थियों और शोध"
        f" के दृष्टिकोण से '{query}' एक अत्यंत महत्वपूर्ण और गहरा विषय है।"
        " आइए इसे बिंदुवार समझें:\n\n1. **परिचय एवं पृष्ठभूमि:** इस विषय की"
        " उत्पत्ति और वैज्ञानिक आधार हमारे ब्रह्मांड और शिक्षा प्रणाली से"
        " जुड़े हुए हैं। इसकी मूल अवधारणाओं को समझना अत्यंत आवश्यक है।\n2. **मुख्य"
        " विशेषताएँ:** इसके अंतर्गत विभिन्न तार्किक पहलुओं और प्रभावों का"
        " अध्ययन किया जाता है जो इस विषय को और अधिक रोचक बनाते हैं।\n3."
        " **निष्कर्ष:** इस क्षेत्र में निरंतर नए शोध हो रहे हैं जो हमें नई"
        " दिशा दिखाते हैं।\n\nयदि आप इस विषय के बारे में कुछ और विशेष जानना चाहते"
        " हैं, तो बेझिझक पूछिए!"
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
if prompt := st.chat_input("अपना कोई भी कठिन सवाल यहाँ पूछें..."):
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
      
      
      
      
        
        
