import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def import_data():
    '''
    Import CSV data of Bitcoin prices.
    '''
    uploaded_file = st.file_uploader('Upload your CSV file',
                                     type = 'csv',
                                     accept_multiple_files = False)
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file,
                         parse_dates = ['Date'],
                         index_col = ['Date'])
        return df
    return None

def eda_data(df):
    '''
    Perform exploratory data analysis on the imported data.
    '''
    # Make a plot of the closing price
    fig = plt.figure(figsize = (6, 3))
    ax = plt.axes()
    ax.plot(df.index, df['Close'])
    ax.set_title('Bitcoin price over time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (USD)')
    st.pyplot(fig)
    