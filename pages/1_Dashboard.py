import streamlit as st
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

# Load secrets
try:
    MONGO_URI = st.secrets["MONGO"]["MONGO_URI"]
    print("Mongo URI loaded from secrets")
except KeyError as e:
    st.error(f"Error accessing Mongo URI from secrets: {e}. Please set up your .streamlit/secrets.toml file.")
    st.stop()

# MongoDB connection
try:
    client = MongoClient(MONGO_URI)
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

# Query MongoDB for daily data
clicks = list(clicks_collection.find())
df = pd.DataFrame(clicks)

# Convert timestamp to datetime and extract day of the week
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["day_of_week"] = df["timestamp"].dt.day_name()

# Set the categorical order for the days of the week
days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
df["day_of_week"] = pd.Categorical(df["day_of_week"], categories=days_order, ordered=True)

# Group by day of the week and count emails sent and clicks
emails_sent = df.groupby("day_of_week").size()
clicks = df[df["clicked"] == "Yes"].groupby("day_of_week").size()

# Ensure all days are present in the index
emails_sent = emails_sent.reindex(days_order, fill_value=0)
clicks = clicks.reindex(days_order, fill_value=0)

# DataFrame for visualization
df_vis = pd.DataFrame({"Emails Sent": emails_sent, "Clicks": clicks}, index=days_order)

# Visualization Section
st.subheader("📈 Phishing Engagement Trends")

col4, col5 = st.columns(2)

with col4:
    st.bar_chart(df_vis)

with col5:
    st.line_chart(df_vis)

# Expandable Section for Details
with st.expander("🔍 View Detailed Stats"):
    st.write(df_vis)