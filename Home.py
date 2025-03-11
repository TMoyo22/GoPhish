import streamlit as st

st.set_page_config(page_title="GoPhish", layout="wide")

st.markdown(
    """
    # 🎣 Welcome to <span style="color:turquoise;">Go</span>Phish!
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    GoPhish is your interactive phishing simulation tool designed to train employees on cybersecurity awareness.  
    Track phishing engagement, register employees, and analyze results—all in one platform.  

    🔹 **Dashboard** - View click rates and key stats  
    🔹 **Employee Registration** - Add new employees to the system  
    🔹 **Results** - See who passed or failed the phishing drill  
    🔹 **Chatbot** - Get real-time guidance on cybersecurity threats  

    Use the **sidebar** to navigate between pages.
    """
)