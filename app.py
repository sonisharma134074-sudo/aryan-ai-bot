import streamlit as st
from google import genai

# पेज कॉन्फ़िगरेशन
st.set_page_config(page_title="Aryan's Real AI Pro", page_icon="⚡")
st.title("⚡ Aryan's Pro AI Assistant")

# साइडबार एपीआई की के लिए
with st.sidebar:
  st.subheader("Configuration")
  api_key = st.text_input("अपनी जेमिनी एपीआई की यहाँ डालें:", type="password")
  st.markdown(
      "[एपीआई की यहाँ से फ्री में लें]"
      "(https://aistudio.google.com/app/apikey)"
  )

if api_key:
  # क्लाइंट इनिशियलाइज करें
  client = genai.Client(api_key=api_key)

  # चैट हिस्ट्री मैनेज करने के लिए
  if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

  # पुराने मैसेज स्क्रीन पर दिखाने के लिए
  for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])

  # यूजर इनपुट बॉक्स
  if user_input := st.chat_input("अपना सवाल यहाँ पूछो..."):
    st.session_state.chat_history.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
      st.markdown(user_input)

    # असली एआई से जवाब लेना
    with st.chat_message("assistant"):
      with st.spinner("एआई सोच रहा है..."):
        try:
          response = client.models.generate_content(
              model="gemini-2.5-flash", contents=user_input
          )
          ai_reply = response.text
          st.markdown(ai_reply)
          st.session_state.chat_history.append(
              {"role": "assistant", "content": ai_reply}
          )
        except Exception as e:
          st.error(f"कुछ एरर आया: {e}")
else:
  st.info("कृपया पहले साइडबार में अपनी जेमिनी एपीआई की दर्ज करें।")
  
