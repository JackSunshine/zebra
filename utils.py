import pandas as pd
import time
import numpy as np


def convert_to_float(series):
    return pd.to_numeric(series, downcast='float', errors='coerce')


def retry_after_sleep(method):
    def wrapper(*arg, **kwargs):
        try:
            return method(*arg, **kwargs)
        except Exception as e:
            time.sleep(10)
            print("Try again after sleep.")
            return method(*arg, **kwargs)
    return wrapper


def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


def trend_of_data(collection):
    return np.all(np.diff(moving_average(np.array(collection), n=4)) > 0)
