# visualization.py
import matplotlib.pyplot as plt

def plot_solar_generation(data, title="Solar Generation"):
    # Plot solar generation data
    plt.figure(figsize=(10, 6))
    plt.plot(data['DATE_TIME'], data['AC_POWER'], label='AC Power')
    plt.title(title)
    plt.xlabel('Date and Time')
    plt.ylabel('AC Power (kW)')
    plt.legend()
    plt.show()

def plot_weather_data(data, title="Weather Sensor Data"):
    # Plot weather sensor data
    plt.figure(figsize=(10, 6))
    plt.plot(data['DATE_TIME'], data['AMBIENT_TEMPERATURE'], label='Ambient Temperature')
    plt.plot(data['DATE_TIME'], data['MODULE_TEMPERATURE'], label='Module Temperature')
    plt.title(title)
    plt.xlabel('Date and Time')
    plt.ylabel('Temperature (Celsius)')
    plt.legend()
    plt.show()

def plot_irradiance_data(data, title="Irradiance Data"):
    # Plot irradiance data
    plt.figure(figsize=(10, 6))
    plt.plot(data['DATE_TIME'], data['IRRADIATION'], label='Irradiance')
    plt.title(title)
    plt.xlabel('Date and Time')
    plt.ylabel('Irradiance (W/m^2)')
    plt.legend()
    plt.show()

def plot_module_temperature_data(data, title="Module Temperature Data"):
    # Plot module temperature data
    plt.figure(figsize=(10, 6))
    plt.plot(data['DATE_TIME'], data['MODULE_TEMPERATURE'], label='Module Temperature')
    plt.title(title)
    plt.xlabel('Date and Time')
    plt.ylabel('Temperature (Celsius)')
    plt.legend()
    plt.show()

def plot_solar_generation_plant2(data, title="Solar Generation - Plant 2"):
    # Plot solar generation data for Plant 2
    plt.figure(figsize=(10, 6))
    plt.plot(data['DATE_TIME'], data['AC_POWER'], label='AC Power - Plant 2')
    plt.title(title)
    plt.xlabel('Date and Time')
    plt.ylabel('AC Power (kW)')
    plt.legend()
    plt.show()

def plot_weather_data_plant2(data, title="Weather Sensor Data - Plant 2"):
    # Plot weather sensor data for Plant 2
    plt.figure(figsize=(10, 6))
    plt.plot(data['DATE_TIME'], data['AMBIENT_TEMPERATURE'], label='Ambient Temperature - Plant 2')
    plt.plot(data['DATE_TIME'], data['MODULE_TEMPERATURE'], label='Module Temperature - Plant 2')
    plt.title(title)
    plt.xlabel('Date and Time')
    plt.ylabel('Temperature (Celsius)')
    plt.legend()
    plt.show()

def plot_irradiance_data_plant2(data, title="Irradiance Data - Plant 2"):
    # Plot irradiance data for Plant 2
    plt.figure(figsize=(10, 6))
    plt.plot(data['DATE_TIME'], data['IRRADIATION'], label='Irradiance - Plant 2')
    plt.title(title)
    plt.xlabel('Date and Time')
    plt.ylabel('Irradiance (W/m^2)')
    plt.legend()
    plt.show()

def plot_module_temperature_data_plant2(data, title="Module Temperature Data - Plant 2"):
    # Plot module temperature data for Plant 2
    plt.figure(figsize=(10, 6))
    plt.plot(data['DATE_TIME'], data['MODULE_TEMPERATURE'], label='Module Temperature - Plant 2')
    plt.title(title)
    plt.xlabel('Date and Time')
    plt.ylabel('Temperature (Celsius)')
    plt.legend()
    plt.show()
