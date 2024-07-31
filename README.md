# BitPredict
BitPredict is an advanced cryptocurrency price prediction tool that leverages machine learning and data analysis algorithms to provide accurate market forecasts. With innovative analytical methods, BitPredict enables investors to make more informed decisions in the cryptocurrency market.

## Table of Contents
- [Description](#description)
- [Models](#models)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Description
BitPredict is a tool designed for forecasting cryptocurrency prices using modern data analysis and predictive modeling techniques, like machine learning and deep learning models. It analyzes market data, historical prices, and halving events, provide users with predictions of future price movements.

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

You can install the required packages using `pip`.

## Installation (in progress)
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
...