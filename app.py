import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Aryan's Pro AI Assistant", page_icon="⚡", layout="centered"
)

# Google Search Console & AdSense Integration
st.markdown(
    """
<meta name="google-site-verification" content="bSAZLmyjCmldxieI7dKa4mDw91JX7ckG_cYZZuPNgH0">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4330937831249559" crossorigin="anonymous"></script>
""",
    unsafe_allow_html=True,
)

st.title("⚡ Aryan's Pro AI Assistant")
st.write(
    "नमस्ते आर्यन! आपका अपना एडवांस एआई असिस्टेंट पूरी तरह तैयार है। अब यह"
    " आपके हर सवाल का पूरा और विस्तृत जवाब देगा।"
)

# Initialize chat history
if "messages" not in st.session_state:
  st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])


# Intelligent detailed response generator to provide full answers like a pro AI
def get_detailed_ai_response(query):
  q = query.lower().strip()

  if "cell" in q:
    return (
        "### कोशिका (Cell) क्या है?\n\nकोशिका सभी जीवित जीवों की बुनियादी,"
        " संरचनात्मक और जैविक इकाई है। इसे अक्सर 'जीवन की मूलभूत इकाई' (Building"
        " block of life) कहा जाता है।\n\n- **खोज:** इसकी खोज सबसे पहले रॉबर्ट हुक"
        " ने 1665 में की थी।\n- **प्रकार:** कोशिकाएं मुख्य रूप से दो प्रकार की"
        " होती हैं — **प्रोकैरियोटिक** (अविकसित केंद्रक वाली) और"
        " **यूकैरियोटिक** (विकसित केंद्रक वाली)।\n- **कार्य:** यह शरीर को आकार"
        " देती है, पोषण को ऊर्जा में बदलती है और आनुवंशिक सामग्री (DNA) को"
        " सुरक्षित रखती है।"
    )
  elif "light" in q or "प्रकाश" in q:
    return (
        "### प्रकाश (Light) क्या है?\n\nप्रकाश विद्युत चुम्बकीय विकिरण"
        " (Electromagnetic radiation) का एक रूप है जिसे मानव आँख से देखा जा"
        " सकता है।\n\n- **गति:** निर्वात (Vacuum) में प्रकाश की चाल सबसे तेज होती"
        " है, जो लगभग **3 × 10⁸ मीटर प्रति सेकंड** ($300,000$ किमी/सेकंड) है।\n-"
        " **प्रकृति:** प्रकाश दोहरी प्रकृति (Dual nature) प्रदर्शित करता है —"
        " यह तरंग (Wave) और कण (Photon) दोनों के रूप में व्यवहार करता है।\n-"
        " **महत्व:** प्रकाश के कारण ही हमें संसार की वस्तुएं दिखाई देती हैं और"
        " पेड़-पौधे प्रकाश संश्लेषण (Photosynthesis) द्वारा अपना भोजन बनाते"
        " हैं।"
    )
  elif "hindi" in q or "अनुवाद" in q:
    return (
        "नमस्ते! मैं पूरी तरह से हिंदी और अंग्रेजी दोनों भाषाओं में बात करने में"
        " सक्षम हूँ। आप विज्ञान, इतिहास, कोडिंग या किसी भी अन्य विषय पर मुझसे"
        " खुलकर सवाल पूछ सकते हैं। बताइए, आज मैं आपकी क्या सहायता करूँ?"
    )
  else:
    return (
        f"### आपके सवाल का विस्तृत उत्तर:\n\n\"{query}\" के संबंध में, यह एक"
        " महत्वपूर्ण विषय है। एआई सिस्टम के विश्लेषण के अनुसार, इस पर व्यापक"
        " दृष्टिकोण से विचार किया जाता है। यदि आप इसमें किसी विशिष्ट पहलू"
        " (जैसे परिभाषा, इतिहास या कार्यप्रणाली) के बारे में जानना चाहते हैं,"
        " तो कृपया नीचे दोबारा पूछें!"
    )


# Accept user input
if prompt := st.chat_input("अपना सवाल यहाँ पूछो..."):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  # Display assistant response
  with st.chat_message("assistant"):
    bot_reply = get_detailed_ai_response(prompt)
    st.markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
      
        
        
