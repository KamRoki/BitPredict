import matplotlib.pyplot as plt
import tensorflow as tf

def plot_time_series(timesteps, values, format = '.', start = 0, end = None, label = None):
  """
  Plots a timesteps (a series of points in time) against values (a series of values across timesteps).

  Parameters
  ---------
  timesteps : array of timesteps
  values : array of values across time
  format : style of plot, default "."
  start : where to start the plot (setting a value will index from start of timesteps & values)
  end : where to end the plot (setting a value will index from end of timesteps & values)
  label : label to show on plot of values
  """
  # Plot the series
  plt.plot(timesteps[start:end], values[start:end], format, label = label)
  plt.xlabel("Time")
  plt.ylabel("BTC Price (USD)")
  if label:
    plt.legend(fontsize = 14) # make label bigger
  plt.grid(True);
  
  
  def get_upper_lower(preds):
    std = tf.math.reduce_std(preds, axis = 0)
    interval = 1.96 * std
    preds_mean = tf.reduce_mean(preds, axis = 0)
    lower, upper = preds_mean - interval, preds_mean + interval
    return lower, upper
  
  