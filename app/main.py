import streamlit as st  # Import Streamlit
import os
import sys

# Get the project root directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add project directory to Python path
sys.path.append(BASE_DIR)

# Import database initialization function
from db.database import init_db
init_db()

# Configure Streamlit page
st.set_page_config(page_title="DocManager", layout="wide")

# Initialize database
init_db()

# Display application title
st.title("Smart PDF Document Manager")

st.divider()

# Create three tabs
tabs = st.tabs(["Upload", "Search & View", "Analytics"])

with tabs[0]:
    pass

with tabs[1]:
    pass

with tabs[2]:
    pass