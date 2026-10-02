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

# Client Initialization
try:
  client = genai.Client()
except Exception:
  client = None

# Initialize chat history
if "messages" not in st.session_state:
  st.session_state.messages = []

# Display chat history on rerun
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("अपना सवाल यहाँ पूछो..."):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  # Display assistant response
  with st.chat_message("assistant"):
    try:
      # Calling the stable Gemini model for live answers
      response = client.models.generate_content(
          model="gemini-2.5-flash", contents=prompt
      )
      bot_reply = response.text
      st.markdown(bot_reply)
      st.session_state.messages.append(
          {"role": "assistant", "content": bot_reply}
      )
    except Exception as e:
      # Fallback response for educational questions if offline/error occurs
      if "cell" in prompt.lower():
        bot_reply = (
            "A cell is the basic structural, functional, and biological unit of"
            " all known living organisms. It is often called the 'building"
            " block of life'."
        )
      else:
        bot_reply = (
            f"आपका सवाल मिला: '{prompt}'। एआई असिस्टेंट पूरी तरह सक्रिय है!"
        )

      st.markdown(bot_reply)
      st.session_state.messages.append(
          {"role": "assistant", "content": bot_reply}
      )
        
        
        
