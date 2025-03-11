import streamlit as st
import pandas as pd
import random

# Page config
st.set_page_config(page_title="GoPhish Dashboard", layout="wide")

# Title
st.title("📊 GoPhish Dashboard")
st.write("Monitor the performance of phishing simulations in real-time.")

# Metrics Section
 # Placeholders, replace with database value
col1, col2, col3 = st.columns(3)
total_emails = 48 
click_rate = 33  
compromised_users = 5  

col1.metric("Total Emails Sent", total_emails)
col2.metric("Click Rate", f"{click_rate}%")
col3.metric("Compromised Users", compromised_users)

# Simulated Data (Replace with database query)
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
emails_sent = [random.randint(40, 60) for _ in days]
clicks = [random.randint(10, 30) for _ in days]

# DataFrame for visualization
df = pd.DataFrame({"Day": days, "Emails Sent": emails_sent, "Clicks": clicks})
df.set_index("Day", inplace=True)

# Visualization Section
st.subheader("📈 Phishing Engagement Trends")

col4, col5 = st.columns(2)

with col4:
    st.bar_chart(df)

with col5:
    st.line_chart(df)

# Expandable Section for Details
with st.expander("🔍 View Detailed Stats"):
    st.write(df)

