import streamlit as st
import google.generativeai as genai
from PIL import Image

# पेज कॉन्फिगरेशन
st.set_page_config(
    page_title="Student Pro AI Assistant",
    page_icon="🚀",
    layout="centered"
)

# डार्क थीम और मोबाइल-फ्रेंडली डिज़ाइन के लिए स्टाइलिंग
st.markdown("""
    <style>
    .main {
        background-color: #0d1117;
        color: #ffffff;
    }
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: #21262d;
        color: white;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# सर्वर-साइड सिक्योर API कॉन्फिगरेशन (यूजर्स के लिए ज़ीरो-कॉन्फिग)
# ---------------------------------------------------------
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("सर्वर कॉन्फिगरेशन एरर! कृपया Streamlit Secrets में 'GOOGLE_API_KEY' सेट करें।")
    st.stop()

# ऐप का शीर्षक
st.title("🌌 Student Pro AI Assistant")
st.markdown("### 📚 पढ़ाई, गणित और अनुवाद के लिए आपका अल्टीमेट AI साथी")

st.markdown("---")

# फीचर चुनने का मेनू
app_mode = st.radio(
    "👉 कौन सा फीचर इस्तेमाल करना चाहते हैं?",
    ("🧠 AI स्टडी और मैथ सॉल्वर (विस्तृत उत्तर)", "🌐 क्विक ट्रांसलेटर (हिंदी ⇄ अंग्रेजी)", "📸 फोटो से सवाल हल करें")
)

st.markdown("---")

if app_mode == "🧠 AI स्टडी और मैथ सॉल्वर (विस्तृत उत्तर)":
    st.subheader("🤖 गणित, विज्ञान या सामान्य ज्ञान का कोई भी कठिन सवाल पूछें")
    st.markdown("हिंदी में एकदम विस्तृत, गहरे और स्टेप-बाय-स्टेप **लंबे जवाब** प्राप्त करें।")
    
    user_query = st.text_area(
        "यहाँ अपना सवाल लिखें:",
        placeholder="जैसे: प्रकाश संश्लेषण (Photosynthesis) को विस्तार से समझाएं या समीकरण x^2 + 5x + 6 = 0 को हल करें...",
        height=140
    )
    
    if st.button("🚀 विस्तृत उत्तर प्राप्त करें", type="primary"):
        if user_query.strip():
            with st.spinner("🧠 AI हिंदी में विस्तृत उत्तर तैयार कर रहा है..."):
                try:
                    prompt_text = (
                        "You are an expert, professional professor and tutor. "
                        "Provide a very detailed, comprehensive, deep, and step-by-step long answer in pure Devanagari Hindi script (हिंदी में) "
                        "covering all formulas, definitions, and explanations for the following query: " + user_query
                    )
                    response = model.generate_content(prompt_text)
                    st.markdown("### 📝 विस्तृत स्पष्टीकरण (Detailed Explanation):")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"एरर: {e}")
        else:
            st.warning("कृपया पहले अपना सवाल दर्ज करें!")

elif app_mode == "🌐 क्विक ट्रांसलेटर (हिंदी ⇄ अंग्रेजी)":
    st.subheader("🌐 AI भाषा अनुवादक (Translator)")
    st.markdown("किसी भी टेक्स्ट का हिंदी और अंग्रेजी के बीच तुरंत अनुवाद करें।")
    
    trans_direction = st.selectbox(
        "अनुवाद की दिशा चुनें:",
        ("English to Hindi (अंग्रेजी से हिंदी)", "Hindi to English (हिंदी से अंग्रेजी)")
    )
    
    trans_text = st.text_area(
        "अनुवाद करने के लिए यहाँ टेक्स्ट लिखें:",
        placeholder="अपना टेक्स्ट यहाँ टाइप या पेस्ट करें...",
        height=120
    )
    
    if st.button("🔄 अब अनुवाद करें", type="primary"):
        if trans_text.strip():
            with st.spinner("🔄 अनुवाद किया जा रहा है..."):
                try:
                    if "English to Hindi" in trans_direction:
                        t_prompt = f"Translate the following English text accurately into natural, fluent Devanagari Hindi: {trans_text}"
                    else:
                        t_prompt = f"Translate the following Hindi text accurately into fluent English: {trans_text}"
                    
                    response = model.generate_content(t_prompt)
                    st.markdown("### 📋 अनुवादित परिणाम (Translated Result):")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"एरर: {e}")
        else:
            st.warning("कृपया अनुवाद के लिए टेक्स्ट दर्ज करें!")

else:
    st.subheader("📸 हल करने के लिए फोटो अपलोड करें")
    st.markdown("अपने गणित के सवाल या विज्ञान के प्रश्न की फोटो अपलोड करें:")
    
    uploaded_file = st.file_uploader("सवाल की तस्वीर चुनें (JPG, PNG)", type=["jpg", "jpeg", "png"])
    img_prompt = st.text_input("निर्देश (वैकल्पिक):", value="हिंदी में स्टेप-बाय-स्टेप विस्तृत समाधान के साथ इसे पूरी तरह हल करें।")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="अपलोड की गई तस्वीर", use_column_width=True)
        
        if st.button("🔍 फोटो का विश्लेषण करें और हल करें", type="primary"):
            with st.spinner("👀 तस्वीर को पढ़ा जा रहा है और विस्तृत समाधान तैयार किया जा रहा है..."):
                try:
                    response = model.generate_content([image, img_prompt])
                    st.markdown("### 📝 विस्तृत समाधान (Detailed Solution):")
                    st.markdown(response.text)
                except Exception as ec:
                    st.error(f"एरर: {ec}")
                    
                    
                    
                    
                    
