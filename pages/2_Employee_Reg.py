import streamlit as st

# Set up the page title
st.set_page_config(page_title="Employee Registration", page_icon="📋")

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
    
    st.write("Employee Registration Successful!")
    st.write(f"**Name**: {name}")
    st.write(f"**Email**: {email}")
    st.write(f"**Job Title**: {job_title}")
    st.write(f"**Department**: {department}")
