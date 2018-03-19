import pandas as pd
import time


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
