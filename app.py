import streamlit as st
from google import genai

# Page configuration
st.set_page_config(page_title="Aryan's Pro AI Assistant")

# Google Search Console & AdSense Integration
st.markdown(
    """
<meta name="google-site-verification" content="bSAZLmyjCmldxieI7dKa4mDw91JX7ckG_cYZZuPNgH0">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4330937831249559" crossorigin="anonymous"></script>
""",
    unsafe_allow_html=True,
)

st.title("⚡ Aryan's Pro AI Assistant")

# Sidebar API Key configuration
with st.sidebar:
  st.subheader("Configuration")
  api_key = st.text_input("अपनी जेमिनी एपीआई की यहाँ डालें:", type="password")
  st.markdown("[एपीआई की यहाँ से फ्री में लें](https://aistudio.google.com)")

if not api_key:
  st.warning(
      "कृपया आगे बात करने के लिए साइडबार में अपनी Gemini API Key दर्ज करें।"
  )
else:
  # Client initialization with updated model gemini-3.8-flash
  client = genai.Client(api_key=api_key)

  # Initialize chat history
  if "messages" not in st.session_state:
    st.session_state.messages = []

  # Display chat messages from history on app rerun
  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])

  # Accept user input
  if prompt := st.chat_input("अपना सवाल यहाँ पूछो..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
      st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
      try:
        # Calling gemini-3.8-flash model
        response = client.models.generate_content(
            model="gemini-3.8-flash", contents=prompt
        )
        bot_reply = response.text
        st.markdown(bot_reply)
        # Add assistant response to chat history
        st.session_state.messages.append(
            {"role": "assistant", "content": bot_reply}
        )
      except Exception as e:
        error_msg = f"कुछ एरर आया: {e}"
        st.error(error_msg)
        st.session_state.messages.append(
            {"role": "assistant", "content": error_msg}
        )
        
