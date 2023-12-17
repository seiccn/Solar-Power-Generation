import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

#import all package needed
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy.stats import normaltest
import holoviews as hv
from holoviews import opts
import cufflinks as cf
hv.extension('bokeh')

# Plant I: Solar Power Generation data
#we take file for plant 1 Generation data
file = '/kaggle/input/solar-power-generation-data/Plant_1_Generation_Data.csv'

plant1_data = pd.read_csv(file) # load data

plant1_data.tail()

print('The number of inverter for data_time {} is {}'.format('15-05-2020 23:00', plant1_data[plant1_data.DATE_TIME == '15-05-2020 23:00']['SOURCE_KEY'].nunique()))

#The number of inverter for data_time 15-05-2020 23:00 is 22

#we compute a sum of 22 inverters
plant1_data = plant1_data.groupby('DATE_TIME')[['DC_POWER','AC_POWER', 'DAILY_YIELD','TOTAL_YIELD']].agg('sum')

#Cleaning data
plant1_data['DATE_TIME'] = pd.to_datetime(plant1_data['DATE_TIME'], errors='coerce')
plant1_data['time'] = plant1_data['DATE_TIME'].dt.time
plant1_data['date'] = pd.to_datetime(plant1_data['DATE_TIME'].dt.date)

plant1_data.shape # (3158, 7)

#we check
plant1_data.head()

#EDA for DC power, AC power and Yield.

# Here, we use

#- Line or scatter plot

#- change rate.

#- Box and Whisker plot

#- calendar plot

#- Bar chart.


#DC Power
#plant1_data.iplot(x= 'time', y='DC_POWER', xTitle='Time',  yTitle= 'DC Power', title='DC POWER plot')
plant1_data.plot(x= 'time', y='DC_POWER', style='.', figsize = (15, 8))
plant1_data.groupby('time')['DC_POWER'].agg('mean').plot(legend=True, colormap='Reds_r')
plt.ylabel('DC Power')
plt.title('DC POWER plot')
plt.show()


#Okay, we are going to see dc power in each day produced by Plant.
#we create calendar_dc data how in each day Plant produce a dc power in each time.

calendar_dc = plant1_data.pivot_table(values='DC_POWER', index='time', columns='date')

# define function to multi plot

def multi_plot(data= None, row = None, col = None, title='DC Power'):
    cols = data.columns # take all column
    gp = plt.figure(figsize=(20,20)) 
    
    gp.subplots_adjust(wspace=0.2, hspace=0.8)
    for i in range(1, len(cols)+1):
        ax = gp.add_subplot(row,col, i)
        data[cols[i-1]].plot(ax=ax, style = 'k.')
        ax.set_title('{} {}'.format(title, cols[i-1]))

multi_plot(data=calendar_dc, row=9, col=4)

#Daily Yield
plant1_data.plot(x='time', y='DAILY_YIELD', style='b.', figsize=(15,5))
plant1_data.groupby('time')['DAILY_YIELD'].agg('mean').plot(legend=True, colormap='Reds_r')
plt.title('DAILY YIELD')
plt.ylabel('Yield')
plt.show()

#data gives us a logistics-like function but after 18:00 the energy decrease slowly; suddenly at 00:00 breakdown.
#pivot table data
daily_yield = plant1_data.pivot_table(values='DAILY_YIELD', index='time', columns='date')


# we plot all daily yield
multi_plot(data=daily_yield.interpolate(), row=9, col=4, title='DAILY YIELD')

#As we can see some daily_yield date (2020-02-06, 2020-05-19,...) have a logistic shape with missing values but others have not.

#plotting a change rate daily yield over time
multi_plot(data=daily_yield.diff()[daily_yield.diff()>0], row=9, col=4, title='new yield')

#Daily Yield each day
daily_yield.boxplot(figsize=(18,5), rot=90, grid=False)
plt.title('DAILY YIELD IN EACH DAY')
plt.show()

#For each day, the daily yield change. some day is high. The observation of all boxes is good, outlier does not exist.

#For further details see Wikipedia's entry for boxplot.

daily_yield.diff()[daily_yield.diff()>0].boxplot(figsize=(18,5), rot=90, grid=False)
plt.title('DAILY YIELD CHANGE RATE EACH 15 MIN EACH DAY')
plt.show()

#Only two days have an outlier 2020-03-06 and 2020-05-21.
#we compute a daily yield for each date.
dyield = plant1_data.groupby('date')['DAILY_YIELD'].agg('sum')


dyield.plot.bar(figsize=(15,5), legend=True)
plt.title('Daily YIELD')
plt.show()
