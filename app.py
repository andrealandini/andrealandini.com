# Importing necessary libraries
import streamlit as st
import pandas as pd

# Title of the web app
st.title('Sample Streamlit App')

# Subheader
st.subheader('Upload a CSV file')

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read data from uploaded CSV file
    data = pd.read_csv(uploaded_file)

    # Display the raw data
    st.write('Raw data:')
    st.write(data)

    # Perform some analysis (example: show summary statistics)
    st.subheader('Summary statistics:')
    st.write(data.describe())

    # Visualize data (example: simple line chart)
    st.subheader('Line chart:')
    st.line_chart(data)

# Adding a footer
st.text('Made with Streamlit')

