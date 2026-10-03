import streamlit as st
from google import genai
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Student Pro AI Assistant",
    page_icon="🚀",
    layout="centered"
)

# Custom Styling for Dark Theme & Mobile-Friendly UI
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

# Pre-configured API Key
API_KEY = "AQ.Ab8RN6JNWB6wPyrGKbZF6N4PTIrJ6OKgNtMVPsNduwhUGK419A"

try:
    client = genai.Client(api_key=API_KEY)
except Exception as e:
    st.error(f"API Key initialization error: {e}")
    st.stop()

# App Header
st.title("🌌 Student Pro AI Assistant")
st.markdown("### 📚 आपका स्मार्ट और आधुनिक एआई साथी (गणित, विज्ञान और हर सवाल का विस्तृत समाधान)")

st.markdown("---")

# Main Choice: Text Question or Photo Upload
option = st.radio(
    "👉 आप सवाल कैसे पूछना चाहते हैं?",
    ("✍️ लिखकर / टाइप करके सवाल पूछें", "📸 फोटो अपलोड करके सवाल हल करें")
)

st.markdown("---")

if option == "✍️ लिखकर / टाइप करके सवाल पूछें":
    st.subheader("🤖 गणित या किसी भी विषय का कठिन सवाल पूछें")
    st.markdown("यहाँ अपना सवाल लिखिए, आपको एकदम विस्तार से (Step-by-Step) लंबा और सटीक जवाब मिलेगा।")
    
    user_query = st.text_area(
        "अपना सवाल यहाँ टाइप करें:",
        placeholder="उदा. भौतिकी का नियम क्या है या समीकरण (x^2 + 5x + 6 = 0) को हल करें...",
        height=130
    )
    
    if st.button("🚀 विस्तृत जवाब प्राप्त करें (Solve)", type="primary"):
        if user_query.strip():
            with st.spinner("🧠 एआई ब्रह्मांडीय ज्ञान से उत्तर तैयार कर रहा है..."):
                try:
                    prompt_text = (
                        "You are an expert, friendly student tutor. "
                        "Provide a very detailed, comprehensive, step-by-step long answer in Hindi "
                        "for the following student query: " + user_query
                    )
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt_text
                    )
                    st.markdown("### 📝 विस्तृत उत्तर (Detailed Answer):")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"त्रुटि (Error): {e}")
        else:
            st.warning("कृपया पहले अपना सवाल दर्ज करें!")

else:
    st.subheader("📸 फोटो अपलोड करके सवाल हल करें")
    st.markdown("अपने सवाल या गणित के समीकरण की फोटो यहाँ अपलोड करें:")
    
    uploaded_file = st.file_uploader("सवाल की फोटो चुनें (JPG, PNG)", type=["jpg", "jpeg", "png"])
    
    image_prompt = st.text_input("फोटो से संबंधित कोई निर्देश (वैकल्पिक):", value="इस सवाल को हल करें और विस्तार से स्टेप-बाय-स्टेप समझाएं।")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="अपलोड की गई तस्वीर", use_column_width=True)
        
        if st.button("🔍 फोटो का विश्लेषण और समाधान करें", type="primary"):
            with st.spinner("👀 फोटो को पढ़ा जा रहा है और समाधान तैयार हो रहा है..."):
                try:
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[image, image_prompt]
                    )
                    st.markdown("### 📝 विस्तृत समाधान (Detailed Solution):")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"त्रुटि (Error): {e}")
                    
      
      
      
        
        
