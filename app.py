import streamlit as st
import requests
import time
from fast_api import brand_image_report, vector_search


# Set page title and favicon
st.set_page_config(page_title="ChhaviAI", page_icon=":robot_face:")

# Set page header
st.title(":robot_face: ChhaviAI")

# Brand Image Report Section
st.header("Brand Image Report")

openai_key = st.text_input("Enter OpenAI Key:")
# User input for Twitter username
username = st.text_input("Enter Twitter username:")

# Generate report button
if st.button("Generate Report") and username != "":
    try:
        with st.spinner("Generating report..."):
            response = brand_image_report(username, openai_key)
            st.write(response["response"])
    except Exception as e:
        st.error("Error occurred during report generation. Please check your OpenAI key and try again.")

# Product Evaluation Section
st.header("Product Evaluation")

# User input for product query
query = st.text_input("Enter a product query:")

# Ask button
if st.button("Ask") and query != "":
    try:
        with st.spinner("Fetching product evaluation..."):
            response = vector_search(query, openai_key)
            st.write(response["response"])
    except Exception as e:
        st.error("Error occurred during product evaluation. Please check your OpenAI key and try again.")
