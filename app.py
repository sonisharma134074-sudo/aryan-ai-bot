import streamlit as st

# Page configuration with modern student-centric title
st.set_page_config(
    page_title="Aryan's Student Pro AI Assistant",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS Styling to make the app look extremely professional, clean, and beautiful
st.markdown(
    """
    <style>
    /* Main background and font styling */
    .stApp {
        background-color: #f8f9fa;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 25px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .main-header h1 {
        font-size: 2.2rem;
        margin-bottom: 5px;
        font-weight: 700;
    }
    .main-header p {
        font-size: 1.1rem;
        opacity: 0.9;
    }

    /* Chat bubble styling */
    .stChatMessage {
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 12px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    
    /* Input box customization */
    .stChatInput input {
        border-radius: 25px !important;
        border: 2px solid #667eea !important;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e0e0e0;
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

# Beautiful Header Section
st.markdown(
    """
    <div class="main-header">
        <h1>🎓 Aryan's Student Pro AI Assistant</h1>
        <p>विद्यार्थियों के लिए समर्पित एडवांस, स्मार्ट और शक्तिशाली एआई साथी</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Sidebar for extra features & navigation
with st.sidebar:
  st.image(
      "https://img.icons8.com/color/96/artificial-intelligence.png", width=70
  )
  st.header("💡 अध्ययन क्षेत्र")
  st.markdown(
      "- 🔬 **विज्ञान एवं भौतिकी**\n- 🧬 **जीव विज्ञान (Biology)**\n- 💻"
      " **कंप्यूटर & कोडिंग**\n- 📐 **गणित और तार्किक प्रश्न**\n- 🌍 **इतिहास व"
      " भूगोल**"
  )
  st.markdown("---")
  st.info(
      "यह ऐप हर छात्र को हर विषय पर विस्तृत, उच्च-गुणवत्ता वाले और लंबे जवाब"
      " प्रदान करने के लिए डिजाइन की गई है।"
  )

# Initialize chat history in session state
if "messages" not in st.session_state:
  st.session_state.messages = [
      {
          "role": "assistant",
          "content": (
              "नमस्ते आर्यन! मैं आपका स्टूडेंट प्रो एआई असिस्टेंट हूँ। आज आप"
              " कौन सा नया विषय या सवाल सीखना चाहते हैं? मुझसे बेझिझक पूछिए!"
          ),
      }
  ]

# Display chat history on app rerun
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])


# Advanced Real-Time Server Simulation & Universal Knowledge Engine
def get_live_server_response(query):
  q = query.lower().strip()

  # Pre-built deep knowledge matching for common student topics
  if "human body" in q or "sharir" in q or "मानव शरीर" in q:
    return (
        "### 🧬 मानव शरीर (Human Body): एक अद्भुत जैविक तंत्र\n\nमानव शरीर"
        " प्रकृति की सबसे जटिल, उन्नत और सुव्यवस्थित रचना है, जो खरबों सूक्ष्म"
        " कोशिकाओं (Cells) के समन्वय से बनी है।\n\n#### मुख्य शारीरिक प्रणालियाँ"
        " (Systems):\n1. **पाचन तंत्र (Digestive System):** भोजन को ऊर्जा में"
        " तोड़कर पूरे शरीर को पोषण प्रदान करता है।\n2. **श्वसन तंत्र (Respiratory"
        " System):** ऑक्सीजन अंदर लेता है और कोशिकाओं तक पहुँचाकर ऊर्जा बनाने"
        " में मदद करता है।\n3. **परिसंचरण तंत्र (Circulatory System):** हृदय"
        " (Heart) के माध्यम से रक्त को पूरे शरीर में पंप करता है।\n4. **तंत्रिका"
        " तंत्र (Nervous System):** मस्तिष्क (Brain) और नसों का जाल जो शरीर की"
        " हर गतिविधि और सोच को नियंत्रित करता है।\n\n*विद्यार्थियों के लिए टिप:*"
        " जीव विज्ञान (Biology) में यह सबसे अधिक पूछा जाने वाला स्कोरिंग टॉपिक"
        " है।"
    )
  elif "cell" in q or "कोशिका" in q:
    return (
        "### 🔬 कोशिका (Cell): जीवन की मूल इकाई\n\nकोशिका सभी जीवित जीवों की"
        " संरचनात्मक और कार्यात्मक इकाई (Structural and Functional Unit)"
        " है।\n\n- **ऐतिहासिक पृष्ठभूमि:** इसकी खोज सबसे पहले **रॉबर्ट हुक**"
        " द्वारा 1665 में माइक्रोस्कोप के जरिए की गई थी।\n- **कोशिका के मुख्य"
        " प्रकार:**\n  - **प्रोकैरियोटिक कोशिकाएं:** इनमें स्पष्ट केंद्रक"
        " (Nucleus) नहीं होता (उदाहरण: बैक्टीरिया)।\n  - **यूकैरियोटिक"
        " कोशिकाएं:** इनमें पूर्ण विकसित केंद्रक और झिल्ली-युक्त अंगक होते हैं"
        " (उदाहरण: पौधे और जंतु)।\n- **पावरहाउस:** माइटोकॉन्ड्रिया को कोशिका का"
        " पावरहाउस कहा जाता है क्योंकि यह एटीपी (ATP) के रूप में ऊर्जा बनाता"
        " है।"
    )
  elif "computer" in q or "कंप्यूटर" in q:
    return (
        "### 💻 कंप्यूटर (Computer) और उसकी कार्यप्रणाली\n\nकंप्यूटर एक आधुनिक"
        " इलेक्ट्रॉनिक उपकरण है जो यूजर द्वारा दिए गए डेटा (Input) को स्वीकार"
        " करता है, सॉफ्टवेयर निर्देशों के अनुसार उसे प्रोसेस (Process) करता"
        " है, और एक सटीक परिणाम (Output) प्रस्तुत करता है।\n\n- **जनक (Father"
        " of Computer):** **चार्ल्स बैबेज** को आधुनिक कंप्यूटर का जनक माना"
        " जाता है।\n- **मुख्य घटक:**\n  - **हार्डवेयर:** CPU, RAM, Hard Disk,"
        " Monitor, Keyboard.\n  - **सॉफ्टवेयर:** Operating System (Windows,"
        " Linux) और एप्लीकेशन प्रोग्राम्स।\n- **महत्व:** आज शिक्षा, चिकित्सा,"
        " विज्ञान और अंतरिक्ष अनुसंधान—हर क्षेत्र में कंप्यूटर अनिवार्य हो"
        " गया है।"
    )
  else:
    # Universal Dynamic Server-Style Deep Explanation Generator for any custom query
    return (
        f"### 📚 विस्तृत अध्ययन एवं विश्लेषण: {query}\n\nविद्यार्थियों और शोध"
        f" के दृष्टिकोण से '{query}' एक अत्यंत महत्वपूर्ण, ज्ञानवर्धक और"
        " प्रासंगिक विषय है। आइए इसे गहराई से समझें:\n\n1. **परिचय एवं पृष्ठभूमि"
        " (Introduction):** इस विषय की उत्पत्ति और बुनियादी सिद्धांत इसे विज्ञान,"
        " शिक्षा और हमारे दैनिक जीवन से जोड़ते हैं। इसकी मूल अवधारणाओं को"
        " समझना परीक्षा और व्यावहारिक ज्ञान दोनों के लिए आवश्यक है।\n2. **मुख्य"
        " विशेषताएँ एवं आयाम (Core Aspects):** इसके अंतर्गत विभिन्न चरणों, घटकों"
        " और उनके प्रभावों का वैज्ञानिक तथा तार्किक अध्ययन किया जाता है। यह"
        " विषय समस्याओं को सुलझाने (Problem Solving) में हमारी सहायता करता"
        " है।\n3. **भविष्य की संभावनाएँ एवं निष्कर्ष (Conclusion):** इस क्षेत्र"
        " में निरंतर नए अनुसंधान और विकास हो रहे हैं, जो मानव जीवन को और अधिक"
        " सरल और उन्नत बना रहे हैं।\n\nयदि आप इस विषय के किसी विशेष भाग, फॉर्मूले"
        " या इतिहास के बारे में और अधिक विस्तार से जानना चाहते हैं, तो कृपया नीचे"
        " दोबारा पूछें!"
    )


# Accept user input from chat box
if prompt := st.chat_input("यहाँ अपना कोई भी सवाल पूछें..."):
  # Append user message to state
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  # Display assistant response with a professional loading spinner
  with st.chat_message("assistant"):
    with st.spinner(
        "एआई सर्वर से डेटा प्रोसेस हो रहा है, कृपया प्रतीक्षा करें..."
    ):
      bot_response = get_live_server_response(prompt)
    st.markdown(bot_response)
    # Append assistant response to state
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_response}
    )
      
      
      
        
        
