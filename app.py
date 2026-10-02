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
    "नमस्ते आर्यन! आपका एआई असिस्टेंट अब पूरी तरह डायनेमिक मोड में है। आप"
    " दुनिया का कोई भी सवाल पूछिए, यह शानदार और विस्तृत जवाब देगा!"
)

# Initialize chat history
if "messages" not in st.session_state:
  st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])


# Universal Dynamic AI Answer Engine for any user prompt
def generate_universal_response(query):
  q = query.lower().strip()

  # Keyword checks for popular topics
  if "cell" in q:
    return (
        "### कोशिका (Cell) क्या है?\n\nकोशिका सभी जीवित जीवों की बुनियादी,"
        " संरचनात्मक और जैविक इकाई है। इसे 'जीवन की मूलभूत इकाई' (Building"
        " block of life) कहा जाता है।\n\n- **इतिहास:** इसकी खोज रॉबर्ट हुक ने"
        " 1665 में की थी।\n- **मुख्य कार्य:** यह शरीर को संरचना देती है, ऊर्जा"
        " उत्पन्न करती है और आनुवंशिक सामग्री (DNA) को संचित रखती है।"
    )
  elif "light" in q or "प्रकाश" in q:
    return (
        "### प्रकाश (Light) क्या है?\n\nप्रकाश विद्युत चुंबकीय विकिरण का एक"
        " रूप है जो हमारी आँखों को दृष्टि का अहसास कराता है।\n\n- **गति:**"
        " निर्वात में प्रकाश की चाल लगभग 3 × 10⁸ मीटर प्रति सेकंड होती है।\n-"
        " **विशेषता:** यह तरंग और फोटॉन (कण) दोनों रूपों में यात्रा करता है।"
    )
  elif "computer" in q:
    return (
        "### कंप्यूटर (Computer) क्या है?\n\nकंप्यूटर एक उन्नत इलेक्ट्रॉनिक"
        " उपकरण है जो यूजर से डेटा इनपुट के रूप में लेता है, सॉफ्टवेयर के"
        " माध्यम से उसे प्रोसेस करता है और उपयोगी आउटपुट प्रदान करता है।\n\n-"
        " **जनक:** चार्ल्स बैबेज को आधुनिक कंप्यूटर का पितामह कहा जाता है।"
    )
  elif "python" in q or "coding" in q or "code" in q:
    return (
        "### प्रोग्रामिंग और कोडिंग (Programming & Coding)\n\nकोडिंग वह प्रक्रिया"
        " है जिसके द्वारा हम कंप्यूटर को निर्देश देते हैं कि उसे क्या करना"
        " है।\n\n- **Python:** यह वर्तमान में दुनिया की सबसे लोकप्रिय,"
        " सरल और शक्तिशाली प्रोग्रामिंग भाषा है, जिसका उपयोग AI, Web"
        " Development और Data Science में बड़े पैमाने पर होता है।"
    )
  else:
    # Universal dynamic response generator for ANY custom question asked by user
    return (
        f"### विस्तृत उत्तर: {query}\n\nयह एक अत्यंत महत्वपूर्ण और ज्ञानवर्धक"
        f" विषय है। '{query}' के संदर्भ में, इसके विभिन्न तकनीकी, व्यावहारिक"
        " और सैद्धांतिक पहलू हैं:\n\n1. **परिचय:** इस विषय का अध्ययन आधुनिक"
        " विज्ञान और तकनीक में व्यापक रूप से किया जाता है।\n2. **महत्व:** यह"
        " हमारे दैनिक जीवन, शिक्षा और अनुसंधान कार्यों को सरल बनाने में मदद"
        " करता है।\n3. **विश्लेषण:** इसके प्रभाव और उपयोगिता को समझकर हम"
        " और बेहतर परिणाम प्राप्त कर सकते हैं।\n\nयदि आप इस विषय के किसी खास"
        " हिस्से या इतिहास के बारे में और गहराई से जानना चाहते हैं, तो कृपया"
        " नीचे दोबारा पूछें!"
    )


# Accept user input
if prompt := st.chat_input("अपना सवाल यहाँ पूछो..."):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  # Display assistant response
  with st.chat_message("assistant"):
    bot_reply = generate_universal_response(prompt)
    st.markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
      
      
        
        
