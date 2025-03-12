import os
import streamlit as st
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import random

# Load environment variables
load_dotenv()
uri = os.getenv('MONGO_URI')

# MongoDB connection
try:
    client = MongoClient(uri)
    db = client['gophishdb']
    clicks_collection = db['clicks']
    # Debugging: Print success message
    print("Connected to MongoDB successfully")
except Exception as e:
    # Debugging: Print error message
    print(f"Error connecting to MongoDB: {e}")

# Page config
st.set_page_config(page_title="GoPhish Dashboard", layout="wide")

# Title
st.title("📊 GoPhish Dashboard")
st.write("Monitor the performance of phishing simulations in real-time.")

# Metrics Section
col1, col2, col3 = st.columns(3)

# Query MongoDB for metrics
total_emails = clicks_collection.count_documents({})
total_clicks = clicks_collection.count_documents({"clicked": "Yes"})
unique_compromised_users = len(clicks_collection.distinct("user_id", {"clicked": "Yes"}))

# Calculate click rate
click_rate = (total_clicks / total_emails) * 100 if total_emails > 0 else 0

col1.metric("Total Emails Sent", total_emails)
col2.metric("Click Rate", f"{click_rate:.2f}%")
col3.metric("Compromised Users", unique_compromised_users)

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