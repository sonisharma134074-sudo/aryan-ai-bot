from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
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


# Function to generate PDF notes from chat history
def create_pdf(messages):
  buffer = BytesIO()
  p = canvas.Canvas(buffer, pagesize=letter)
  width, height = letter

  p.setFont("Helvetica-Bold", 16)
  p.drawString(50, height - 50, "Aryan's Student Pro AI - Galaxy Study Notes")

  p.setFont("Helvetica", 10)
  p.drawString(50, height - 70, "Generated automatically for students & explorers.")

  y = height - 100
  p.setFont("Helvetica", 11)

  for msg in messages:
    role = "Student" if msg["role"] == "user" else "AI Assistant"
    text = f"{role}: {msg['content']}"

    lines = text.split("\n")
    for line in lines:
      if y < 50:
        p.showPage()
        y = height - 50
        p.setFont("Helvetica", 11)
      p.drawString(50, y, line[:90])
      y -= 18
    y -= 10

  p.save()
  buffer.seek(0)
  return buffer


# Sidebar with Tools & PDF Download
with st.sidebar:
  st.image("https://img.icons8.com/color/96/experimental-rocket.png", width=70)
  st.header("🌌 गैलेक्सी टूल्स")
  st.markdown(
      "- 🎤 **वॉइस टाइपिंग:** बोलकर अपना सवाल पूछें\n- 📥 **PDF नोट्स:** अपनी चैट"
      " को तुरंत डाउनलोड करें"
  )
  st.markdown("---")

  if "messages" in st.session_state and len(st.session_state.messages) > 1:
    pdf_data = create_pdf(st.session_state.messages)
    st.download_button(
        label="📥 चैट नोट्स PDF डाउनलोड करें",
        data=pdf_data,
        file_name="Aryan_Galaxy_Study_Notes.pdf",
        mime="application/pdf",
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
              " हूँ। आज ब्रह्मांड के किस रहस्य या विषय पर चर्चा करनी है? बेझिझक"
              " पूछिए!"
          ),
      }
  ]

# Display chat history
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])


# Universal Knowledge & Server Engine
def get_ai_response(query):
  q = query.lower().strip()

  if "milky way" in q or "galaxy" in q or "आकाशगंगा" in q:
    return (
        "### 🌌 मिल्की वे (Milky Way) आकाशगंगा\n\nमिल्की वे वह आकाशगंगा है"
        " जिसमें हमारा सौर मंडल (Solar System) स्थित है।\n\n- **आकार (Shape):**"
        " यह एक **सर्पिल (Spiral)** आकाशगंगा है।\n- **तारे और ग्रह:** इसमें अरबों"
        " तारे, गैस के बादल और धूलकण हैं। हमारे सौर मंडल में पृथ्वी, चंद्रमा"
        " और सूर्य इसी का हिस्सा हैं।"
    )
  elif "space" in q or "universe" in q or "ब्रह्मांड" in q:
    return (
        "### 🌠 ब्रह्मांड (Universe) का रहस्य\n\nब्रह्मांड में सभी समय,"
        " अंतरिक्ष, ऊर्जा, ग्रह, तारे, आकाशगंगाएँ और सभी जीवित पदार्थ शामिल"
        " हैं। इसकी उत्पत्ति लगभग 13.8 अरब साल पहले **बिग बैंग (Big Bang)**"
        " महाविस्फोट से हुई थी।"
    )
  elif "human body" in q or "sharir" in q or "मानव शरीर" in q:
    return (
        "### 🧬 मानव शरीर (Human Body): एक अद्भुत जैविक तंत्र\n\nमानव शरीर"
        " प्रकृति की सबसे जटिल रचना है, जो खरबों सूक्ष्म कोशिकाओं से मिलकर"
        " बनी है। पाचन, श्वसन, परिसंचरण और तंत्रिका तंत्र इसके मुख्य स्तंभ हैं।"
    )
  elif "computer" in q or "कंप्यूटर" in q:
    return (
        "### 💻 कंप्यूटर (Computer) और उसकी कार्यप्रणाली\n\nकंप्यूटर एक आधुनिक"
        " इलेक्ट्रॉनिक उपकरण है जो डेटा को प्रोसेस करके सटीक परिणाम देता है।"
        " इसके जनक **चार्ल्स बैबेज** हैं।"
    )
  else:
    return (
        f"### 📚 विस्तृत अध्ययन एवं विश्लेषण: {query}\n\nविद्यार्थियों के"
        f" दृष्टिकोण से '{query}' एक अत्यंत महत्वपूर्ण विषय है:\n\n1. **परिचय:**"
        " इस विषय के बुनियादी सिद्धांतों को समझना परीक्षा और ज्ञान दोनों के लिए"
        " आवश्यक है。\n2. **वैज्ञानिक महत्व:** यह हमारे ब्रह्मांड और दैनिक जीवन"
        " से गहराई से जुड़ा हुआ है。\n3. **निष्कर्ष:** इसके निरंतर अध्ययन से"
        " हमारी तार्किक क्षमता में वृद्धि होती है।"
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

# Chat input box
if prompt := st.chat_input("अपना सवाल गैलेक्सी में पूछें..."):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  with st.chat_message("assistant"):
    with st.spinner("गैलेक्सी सर्वर से उत्तर आ रहा है..."):
      bot_response = get_ai_response(prompt)
    st.markdown(bot_response)
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_response}
    )
      
      
      
      
        
        
