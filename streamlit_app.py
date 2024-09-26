# Import dependencies
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Create a connection object
conn = st.connection("gsheets", type=GSheetsConnection)
google_sheets_table = conn.read()
dataframe = pd.DataFrame(google_sheets_table) # Convert google sheets table into python dataframe. Streamlit expects dataframes as input.

# # Introduction text
# """
# """

# Define tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Stakeholder Analysis", "User Factors", "Task Factors","Physical Environment","Organisational, Social Factors"])

# Streamlit content
with tab1:
  st.write(dataframe)
with tab2:
  st.write(dataframe)
with tab3:
  st.write(dataframe)
with tab4:
  st.write(dataframe)
with tab5:
  st.write(dataframe)

# # Footer text
# """
# """
