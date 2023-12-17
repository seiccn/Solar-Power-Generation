# data_loading.py

import pandas as pd

def load_solar_data(file_path):
    # Load solar power generation data
    plant1_data = pd.read_csv(file_path)
    
    # Data cleaning and preprocessing (as in the notebook)
    # ...

    return plant1_data

def load_weather_data(file_path):
    # Load weather sensor data
    plant1_sensor = pd.read_csv(file_path)

    # Data cleaning and preprocessing (as in the notebook)
    # ...

    return plant1_sensor
