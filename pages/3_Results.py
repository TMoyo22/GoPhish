import streamlit as st
import pandas as pd
import plotly.express as px

# Page Config
st.set_page_config(page_title="Phishing Results", layout="wide")

# Title
st.title("📈 Phishing Simulation Results")
st.write("Track email clicks and user interactions.")

# Placeholder Data (Replace with database queries)
sample_data = {
    "User": [
        "alice@example.com", "bob@example.com", "charlie@example.com",
        "dave@example.com", "eve@example.com", "frank@example.com",
        "alice@example.com", "bob@example.com", "alice@example.com"
    ],
    "Clicked": ["Yes", "No", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "No"],
    "Timestamp": [
        "2025-03-01 14:30", "2025-03-02 15:15", "2025-03-03 16:05",
        "2025-03-04 12:00", "2025-03-05 13:45", "2025-03-06 10:30",
        "2025-03-06 11:15", "2025-03-07 09:20", "2025-03-07 17:40"
    ]
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

