import streamlit as st
import pandas as pd
from src.app.st_functions import import_data, eda_data
import matplotlib.pyplot as plt


def page_home():
    st.title('Welcome to BitPredict')
    st.image('https://img.odcdn.com.br/wp-content/uploads/2023/04/Destaque-roubo-criptomoedas.jpg', use_column_width=True)
    st.write('This is a web app that allows you to forecast the price of Bitcoin using trained machine learning models. BitPredict is a tool designed for forecasting cryptocurrency prices using modern data analysis and predictive modeling techniques, like machine learning and deep learning models. It analyzes market data, historical prices, and halving events, and provides users with predictions of future price movements.')

def page_about():
    st.title('About me')
    st.write('My name is Kamil and I am a Data Scientist and PhD Candidate. With a passion for uncovering insights through data, I specialize in leveraging advanced analytical techniques and machine learning algorithms to solve complex problems and drive informed decision-making. My journey in data science is complemented by my PhD studies, where I focus on analyzing magnrtic resonance imaging images.')
    
def page_data():
    st.title('Exploratory Data Analysis')
    df = import_data()
    if df is not None:
        st.write('Data loaded successfully!')
        st.dataframe(df.head())
    else:
        st.write('Please upload a CSV file to get started.')
        
    st.write('This is our dataset, which contains prices of Bitcoin over time. Let\'s perform some exploratory data analysis to understand the data better.')
    if st.button('Perform EDA'):
        eda_data(df)