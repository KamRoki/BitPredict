import streamlit as st

# App title
st.set_page_config(page_title = 'BitPredict',
                   layout = 'wide')

# Sidebar
sidebar_options = ['Home', 'Forecasting', 'Results', 'About me']
selection = st.sidebar.radio('Menu', sidebar_options)

if selection == 'Home':
    st.title('Welcome to BitPredict')
    st.image('https://img.odcdn.com.br/wp-content/uploads/2023/04/Destaque-roubo-criptomoedas.jpg', use_column_width = True)
    st.write('This is a web app that allows you to forecast the price of Bitcoin using a trained machine learning models. BitPredict is a tool designed for forecasting cryptocurrency prices using modern data analysis and predictive modeling techniques, like machine learning and deep learning models. It analyzes market data, historical prices, and halving events, provide users with predictions of future price movements.')
    