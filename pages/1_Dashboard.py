import streamlit as st

st.title("📊 GoPhish Dashboard")
st.write("Monitor the performance of GoPhish.")

col1, col2, col3 = st.columns(3)
col1.metric("Total Emails Sent", "48")
col2.metric("Click Rate", "33%")
col3.metric("Compromised Users", "5")
