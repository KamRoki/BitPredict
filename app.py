import streamlit as st

# App title
st.set_page_config(page_title = 'BitPredict',
                   layout = 'wide')

    
# Define the content for each page
def page_home():
    st.title('Welcome to BitPredict')
    st.image('https://img.odcdn.com.br/wp-content/uploads/2023/04/Destaque-roubo-criptomoedas.jpg', use_column_width=True)
    st.write('This is a web app that allows you to forecast the price of Bitcoin using trained machine learning models. BitPredict is a tool designed for forecasting cryptocurrency prices using modern data analysis and predictive modeling techniques, like machine learning and deep learning models. It analyzes market data, historical prices, and halving events, and provides users with predictions of future price movements.')

def page_about():
    st.title('About me')
    st.write('My name is Kamil and I am a Data Scientist and PhD Candidate. With a passion for uncovering insights through data, I specialize in leveraging advanced analytical techniques and machine learning algorithms to solve complex problems and drive informed decision-making. My journey in data science is complemented by my PhD studies, where I focus on analyzing magnrtic resonance imaging images.')
    
    
    
    
    

# Initialize session state for page selection
if 'page' not in st.session_state:
    st.session_state.page = 'Home'
    
    
    
    

# Sidebar for navigation
with st.sidebar:
    st.title('Menu')
    if st.button('Home'):
        st.session_state.page = 'Home'
    if st.button('About me'):
        st.session_state.page = 'About me'

# Display the selected page
if st.session_state.page == 'Home':
    page_home()
elif st.session_state.page == 'About me':
    page_about()