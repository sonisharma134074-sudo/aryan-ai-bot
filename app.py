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

# Automatic API key configuration
p1 = "AQ.Ab8RN6KJg"
p2 = "HZNgTSOOcdMFIfc"
p3 = "CL_YJDcVM0oQ3qPh25FefjH5dA"
api_key = p1 + p2 + p3

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
      # Calling updated gemini-3.8-flash model
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
      error_msg = f"Kuchh error aaya: {e}"
      st.error(error_msg)
      st.session_state.messages.append(
          {"role": "assistant", "content": error_msg}
      )
        
        
