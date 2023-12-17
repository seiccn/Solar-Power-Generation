# data_loading.py

import pandas as pd

def load_solar_data(file_path):
    # Load solar generation data
    solar_data = pd.read_csv(file_path, parse_dates=['DATE_TIME'])
    return solar_data

def load_weather_data(file_path):
    # Load weather sensor data
    weather_data = pd.read_csv(file_path, parse_dates=['DATE_TIME'])
    return weather_data

def load_irradiance_data(file_path):
    # Load irradiance data
    irradiance_data = pd.read_csv(file_path, parse_dates=['DATE_TIME'])
    return irradiance_data

def load_module_temperature_data(file_path):
    # Load module temperature data
    module_temp_data = pd.read_csv(file_path, parse_dates=['DATE_TIME'])
    return module_temp_data

def load_solar_data_plant2(file_path):
    # Load solar generation data for Plant 2
    solar_data_plant2 = pd.read_csv(file_path, parse_dates=['DATE_TIME'])
    return solar_data_plant2

def load_weather_data_plant2(file_path):
    # Load weather sensor data for Plant 2
    weather_data_plant2 = pd.read_csv(file_path, parse_dates=['DATE_TIME'])
    return weather_data_plant2

def load_irradiance_data_plant2(file_path):
    # Load irradiance data for Plant 2
    irradiance_data_plant2 = pd.read_csv(file_path, parse_dates=['DATE_TIME'])
    return irradiance_data_plant2

def load_module_temperature_data_plant2(file_path):
    # Load module temperature data for Plant 2
    module_temp_data_plant2 = pd.read_csv(file_path, parse_dates=['DATE_TIME'])
    return module_temp_data_plant2
