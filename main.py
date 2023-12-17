# main.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy.stats import normaltest

from data_loading import load_solar_data, load_weather_data
from visualization import plot_dc_power, plot_daily_yield, plot_ambient_temperature

def main():
    # Load data
    plant1_data = load_solar_data('/kaggle/input/solar-power-generation-data/Plant_1_Generation_Data.csv')
    plant1_sensor = load_weather_data('/kaggle/input/solar-power-generation-data/Plant_1_Weather_Sensor_Data.csv')

    # Visualization
    plot_dc_power(plant1_data)
    plot_daily_yield(plant1_data)
    plot_ambient_temperature(plant1_sensor)

if __name__ == "__main__":
    main()
