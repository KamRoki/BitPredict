import tensorflow as tf

def mean_absolute_scaled_error(y_true, y_pred):
  """
  Implement MASE (Mean Absolute Scaled Error) formula.
  """
  mae = tf.reduce_mean(tf.abs(y_true - y_pred))

  # Naive forecast
  mae_naive_no_season = tf.reduce_mean(tf.abs(y_true[1:] - y_true[:-1])) # naive forecast without seasonality

  return mae / mae_naive_no_season

def evaluate_preds(y_true, y_pred):
    y_true = tf.cast(y_true, dtype = tf.float32)
    y_pred = tf.cast(y_pred, dtype = tf.float32)

    # Calculate various metrics
    mae = tf.keras.metrics.mean_absolute_error(y_true, y_pred)
    mse = tf.keras.metrics.mean_squared_error(y_true, y_pred)
    rmse = tf.sqrt(mse)
    mape = tf.keras.metrics.mean_absolute_percentage_error(y_true, y_pred)
    mase = mean_absolute_scaled_error(y_true, y_pred)

    if mae.ndim > 0:
        mae = tf.reduce_mean(mae)
        mse = tf.reduce_mean(mse)
        rmse = tf.reduce_mean(rmse)
        mape = tf.reduce_mean(mape)
        mase = tf.reduce_mean(mase)

    return {
        "Mean Absolute Error": mae.numpy(),
        "Mean Squared Error": mse.numpy(),
        "Root Mean Squared Error": rmse.numpy(),
        "Mean Absolute Percentage Error": mape.numpy(),
        "Mean Absolute Scaled Error": mase.numpy()
    }