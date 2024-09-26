import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Define scope for Google Sheets access
scope = ["https://spreadsheets.google.com/feeds", 
         "https://www.googleapis.com/auth/spreadsheets", 
         "https://www.googleapis.com/auth/drive.file", 
         "https://www.googleapis.com/auth/drive"]

# Authenticate and create a client to interact with the Google Sheets API
creds = Credentials.from_service_account_file("path_to_your_service_account.json", scopes=scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1gnDBXEZI98Ivic5GTrm930dUwsrBcFj1a3qsth610SM/edit?usp=sharing")

# Fetch all worksheets (tabs)
worksheet_stakeholder = sheet.get_worksheet(0)  # Worksheet index 0 for 'Stakeholder Analysis'
worksheet_user_factors = sheet.get_worksheet(1)  # Worksheet index 1 for 'User Factors'
worksheet_task_factors = sheet.get_worksheet(2)  # Worksheet index 2 for 'Task Factors'
worksheet_physical_env = sheet.get_worksheet(3)  # Worksheet index 3 for 'Physical Environment'
worksheet_org_social = sheet.get_worksheet(4)  # Worksheet index 4 for 'Organisational, Social Factors'

# Convert each worksheet to DataFrame
df_stakeholder = pd.DataFrame(worksheet_stakeholder.get_all_records())
df_user_factors = pd.DataFrame(worksheet_user_factors.get_all_records())
df_task_factors = pd.DataFrame(worksheet_task_factors.get_all_records())
df_physical_env = pd.DataFrame(worksheet_physical_env.get_all_records())
df_org_social = pd.DataFrame(worksheet_org_social.get_all_records())

# Define tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Stakeholder Analysis", "User Factors", "Task Factors", "Physical Environment", "Organisational, Social Factors"])

# Streamlit content: Display each DataFrame in its respective tab
with tab1:
    st.write("Stakeholder Analysis Data")
    st.write(df_stakeholder)

with tab2:
    st.write("User Factors Data")
    st.write(df_user_factors)

with tab3:
    st.write("Task Factors Data")
    st.write(df_task_factors)

with tab4:
    st.write("Physical Environment Data")
    st.write(df_physical_env)

with tab5:
    st.write("Organisational, Social Factors Data")
    st.write(df_org_social)
