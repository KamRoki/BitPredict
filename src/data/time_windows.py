import numpy as np

def get_labelled_windows(x, horizon):
    return x[:, :-horizon], x[:, -horizon:]

def make_windows(x, window_size, horizon):
    """
    Turns a 1D array into a 2D array of sequential windows of window_size.
    """
    window_step = np.expand_dims(np.arange(window_size + horizon), axis = 0)
    window_indexes = window_step + np.expand_dims(np.arange(len(x) - (window_size + horizon - 1)), axis = 0).T
    windowed_array = x[window_indexes]
    windows, labels = get_labelled_windows(windowed_array, horizon = horizon)
    return windows, labels