import numpy as np

def get_future_dates(start_date, into_future, offset = 1):
  '''
    Returns array of datetime values ranging from start_date to start_date+into_future.
  '''
  start_date = start_date + np.timedelta64(offset, 'D')
  end_date = start_date + np.timedelta64(into_future, 'D')
  return np.arange(start_date, end_date, dtype = 'datetime64[D]')