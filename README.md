# BitPredict

## Table of Contents
- [Description](#description)
- [Models](#models)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)

## Description
BitPredict is an advanced cryptocurrency price prediction tool that leverages machine learning and data analysis algorithms to provide accurate market forecasts. With innovative analytical methods, BitPredict enables investors to make more informed decisions in the cryptocurrency market.

## Models
All of the trained models are available in text file, in models folder. In this project some models were trained with following mean absolute error values:
* Model 0: Naive Model (MAE = 530.38)
* Model 1: Dense Neural Network with window 7 and horizon 1 (MAE = 529.55)
* Model 2: Dense Neural Network with window 30 and horizon 1 (MAE = 562.82)
* Model 3: Dense Neural Network with window 30 and horizon 7 (MAE = 1153.65)
* Model 4: Convolutional Neural Network 1D (MAE = 535.69)
* Model 5: Recurrent Neural Network LSTM (MAE = 546.80)
* Model 6: Multivariate Dense Neural Network (MAE = 531.09)
* Model 7: N-BEATS Algorithm (MAE = 527.22)
* Model 8: Ensemble Model (MAE = 528.52)
* Model 9: Dense Neural Network on full historical data

## Requirements
To run BitPredict, you need to have the following dependencies installed:
- Python 3.11
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Tensorflow
- Streamlit

You can install the required packages using `pip`.

## Installation ()
1. Clone the repository:
```
git clone https://github.com/KamRoki/BitPredict.git
```
2. Navigate to the project directory:
```
cd BitPredict
```
3. Install the required packages
```
pip install -r requirements.txt
```
4. Run the Streamlit app
```
streamlit run app.py
```

## Usage
After installing BitPredict, you can start using the application by Streamlit app. Here are the basic steps:
1. **Import Data**: Load market and historical data into the system
2. **Configurate the Model**: Select the appropriate machine learning model and adjust its parameters
3. **Run Forecasting**: Perform predictions
4. **Analyze Results**: Review and interpret the forecast results. 

## Contributing 
I welcome contributions to BitPredict! If you have ideas, suggestions, or would like to fix bugs, please follow these steps:
1. Fork the repository
2. Create a new branch
3. Make changes
4. Commit your changes
5. Push to the branch
6. Open a pull request.

## Contact
For questions or support, please reach out to *kami.stachurski@gmail.com*.