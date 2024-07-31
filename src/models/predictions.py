import tensorflow as tf
import numpy as np

def make_preds(model, input_data):
    forecast = model.predict(input_data)
    return tf.squeeze(forecast)


def make_future_forecast(values, model, into_future, window_size) -> list:
  '''
  Make future forecasts into_future steps after values ends.

  Returns future forecasts as a list of floats.
  '''
  # Create an empty list
  future_forecast = []
  last_window = values[-window_size:]

  for _ in range(into_future):
    future_pred = model.predict(tf.expand_dims(last_window, axis = 0))
    print(f'Predicting on:\n {last_window} -> Prediction: {tf.squeeze(future_pred).numpy()}\n')

    future_forecast.append(tf.squeeze(future_pred).numpy())

    # Update last window
    last_window = np.append(last_window, future_pred)[-window_size:]

  return future_forecast