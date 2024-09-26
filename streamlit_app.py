# Import dependencies
import streamlit as st
import pandas as pd
from st_gsheets_connection import GSheetsConnection

# Set up the Google Sheets connection using the streamlit secrets
conn = st.connection("gsheets", type=GSheetsConnection)

# Read the data from the Google Sheets
google_sheets_table = conn.read()

# Convert the Google Sheets data into a pandas DataFrame
dataframe = pd.DataFrame(google_sheets_table)

# Define tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Stakeholder Analysis", "User Factors", "Task Factors", "Physical Environment", "Organizational, Social Factors"])

# Streamlit content
with tab1:
    st.write("## Stakeholder Analysis")
    st.write(dataframe)  # Display the dataframe or specific parts of it

with tab2:
    st.write("## User Factors")
    st.write(dataframe)  # Display the dataframe or specific parts of it

with tab3:
    st.write("## Task Factors")
    st.write(dataframe)  # Display the dataframe or specific parts of it

with tab4:
    st.write("## Physical Environment")
    st.write(dataframe)  # Display the dataframe or specific parts of it

with tab5:
    st.write("## Organizational, Social Factors")
    st.write(dataframe)  # Display the dataframe or specific parts of it
