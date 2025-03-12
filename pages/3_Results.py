import os
import streamlit as st
import pandas as pd
import plotly.express as px
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
uri = os.getenv('MONGO_URI')

# MongoDB connection
try:
    client = MongoClient(uri)
    db = client['gophishdb']
    users_collection = db['users']
    clicks_collection = db['clicks']
    # Debugging: Print success message
    print("Connected to MongoDB successfully")
except Exception as e:
    # Debugging: Print error message
    print(f"Error connecting to MongoDB: {e}")

# Page Config
st.set_page_config(page_title="Phishing Results", layout="wide")

# Title
st.title("📈 Phishing Simulation Results")
st.write("Track email clicks and user interactions.")

# Query MongoDB for data
clicks = list(clicks_collection.find())
user_ids = [click['user_id'] for click in clicks]
users = list(users_collection.find({"_id": {"$in": user_ids}}))

# Create a dictionary to map user_id to email
user_id_to_name = {str(user['_id']): user['name'] for user in users}

# Populate sample_data
sample_data = {
    "User": [user_id_to_name.get(str(click['user_id']), 'Unknown') for click in clicks],
    "Clicked": [click['clicked'] for click in clicks],
    "Timestamp": [click['timestamp'] for click in clicks]
}

# Convert to DataFrame
df = pd.DataFrame(sample_data)
st.dataframe(df)

# Convert timestamp to datetime and extract month
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df["Month"] = df["Timestamp"].dt.strftime("%Y-%m")

# Count "Yes" vs "No"
yes_count = df[df["Clicked"] == "Yes"].shape[0]
no_count = df[df["Clicked"] == "No"].shape[0]

# Pie Chart: Yes vs No
st.subheader("📊 Summary of Click Responses")
fig_pie = px.pie(
    values=[yes_count, no_count], 
    names=["Clicked (Yes)", "Did Not Click (No)"],
    title="Phishing Click Rate",
    color_discrete_sequence=["red", "green"]
)
st.plotly_chart(fig_pie)

# Monthly Summary of Clicks
monthly_summary = df.groupby(["Month", "Clicked"]).size().unstack(fill_value=0)

st.subheader("📅 Monthly Click Trends")
fig_bar = px.bar(
    monthly_summary,
    x=monthly_summary.index,
    y=["Yes", "No"],
    title="Phishing Clicks by Month",
    labels={"value": "Number of Clicks", "Month": "Month"},
    barmode="group",
    color_discrete_map={"Yes": "red", "No": "green"}
)
st.plotly_chart(fig_bar)

# Identify Top 3 Users Who Clicked "Yes" the Most
top_users = df[df["Clicked"] == "Yes"]["User"].value_counts().head(3)

st.subheader("⚠️ Most in Need of Cyber Training")
st.write("These users clicked on phishing emails the most times this month:")

# Display as a DataFrame
top_users_df = pd.DataFrame({"User": top_users.index, "Clicks": top_users.values})
st.dataframe(top_users_df, hide_index=True)