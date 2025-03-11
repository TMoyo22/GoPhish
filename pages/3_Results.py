import streamlit as st
import pandas as pd

st.title("📈 Results & Analytics")
st.write("Track email clicks and user interactions.")

# Placeholder Data (To be replaced with real database queries)
sample_data = {
    "User": ["bob1@example.com", "bob2@example.com", "bob3@example.com"],
    "Clicked": ["Yes", "No", "Yes"],
    "Timestamp": ["2025-03-11 14:30", "2025-03-11 15:15", "2025-03-11 16:05"]
}
df = pd.DataFrame(sample_data)

st.dataframe(df)
