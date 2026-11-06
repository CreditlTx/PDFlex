import streamlit as st  # Import Streamlit
import os
import sys

# Get the project root directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add project directory to Python path
sys.path.append(BASE_DIR)

# Import database initialization function
from db.database import init_db

from core.services import DocumentService

# Configure Streamlit page
st.set_page_config(page_title="PDFlex", layout="wide")

# Initialize database and creating the object of class document_service
init_db()

service=DocumentService()


# Display application title
st.title("Smart PDF Document Manager")

st.divider()

# Create three tabs
tabs = st.tabs(["Upload", "Search & View", "Analytics"])

with tabs[0]:
    st.header("Upload PDF")
    uploaded_file=st.file_uploader("UPLOAD PDF",type=["PDF"])
    tags=st.text_input("tags (comma separated)")
    description=st.text_area("description")
    lecture_date=st.date_input("lecture date(optional)",value=None)

    if st.button("upload",type='primary'):
        if uploaded_file and tags and description:
            service.upload_document(uploaded_file,tags,description,lecture_date)
        else:
            st.error("please fill the blank field")

with tabs[1]:
    # logic of search and view
    pass

with tabs[2]:
    pass