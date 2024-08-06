import streamlit as st
import pandas as pd
from src.app.st_functions import import_data


# ---
# App title
st.set_page_config(page_title = 'BitPredict',
                   layout = 'wide')

# ---    
# Define the content for each page
from src.app.pages import page_home, page_about, page_data
        
# ---
# Initialize session state for page selection
if 'page' not in st.session_state:
    st.session_state.page = 'Home'
    
    
# ---
# Sidebar for navigation
with st.sidebar:
    st.title('Menu')
    if st.button('Home'):
        st.session_state.page = 'Home'
    if st.button('Load data'):
        st.session_state.page = 'Load data'
    if st.button('About me'):
        st.session_state.page = 'About me'

# Display the selected page
if st.session_state.page == 'Home':
    page_home()
elif st.session_state.page == 'About me':
    page_about()
elif st.session_state.page == 'Load data':
    page_data()