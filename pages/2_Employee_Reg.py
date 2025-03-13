import streamlit as st
from pymongo import MongoClient

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
    users_collection = db['users']
    # Debugging: Print success message
    print("Connected to MongoDB successfully")
except Exception as e:
    # Debugging: Print error message
    print(f"Error connecting to MongoDB: {e}")

# Set up the page title
st.set_page_config(page_title="Employee Registration", page_icon="📋")

st.markdown(
    """
        <style>div[data-testid="stToolbar"] { display: none;}</style>
    """,
    unsafe_allow_html=True,
)

st.title("📋 Employee Registration")

# Employee registration form
with st.form(key="employee_form"):
    name = st.text_input("Employee Name")
    email = st.text_input("Email")
    job_title = st.text_input("Job Title")
    department = st.text_input("Department")
    
    submit_button = st.form_submit_button(label="Register Employee")

# Check if the form is submitted
if submit_button:
    # Debugging: Print form data
    print(f"Form submitted with data: Name={name}, Email={email}, Job Title={job_title}, Department={department}")
    
    # Store the data in the users collection
    user_data = {
        "name": name,
        "email": email,
        "job_title": job_title,
        "department": department
    }
    try:
        # Check if the email already exists
        if users_collection.find_one({"email": email}):
            st.write(f"Error: An employee with the email {email} already exists.")
            print(f"Error: An employee with the email {email} already exists.")
        else:
            users_collection.insert_one(user_data)
            st.write("Employee Registration Successful!")
            st.write(f"**Name**: {name}")
            st.write(f"**Email**: {email}")
            st.write(f"**Job Title**: {job_title}")
            st.write(f"**Department**: {department}")

            # Debugging: Print success message
            print("Data inserted into MongoDB successfully")
    except Exception as e:
        st.write(f"Error inserting data into MongoDB: {e}")
        
        # Debugging: Print error message
        print(f"Error inserting data into MongoDB: {e}")