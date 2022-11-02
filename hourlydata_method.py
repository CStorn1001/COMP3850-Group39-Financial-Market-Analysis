#data manipulation libraries
import pandas as pd
import numpy as np 

#data visualisation libraries
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# import matplotlib as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from pandas.plotting import autocorrelation_plot
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from matplotlib import pyplot

#stat models libraries 
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller#for augmented Dickey-Fuller test
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.tsa.api as smt #autocovariance plot

#sklearn predictive modelling
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score

#technical analysis libaries
import talib as ta # Used to perform Technical analysis of financial market data

#others libraries 
import math
import datetime

#libaries to collect path for data extraction
import os
import glob

#This function is created to make it easier to get the hourly intervals for each fx pairings
#0 to 23 for each day
def hourly_intervals(curr_df):
    hr_list = []
    for i in range(0,24):
        hr_list.append(curr_df[(curr_df['Time'].str.contains(f'{i}:00:00'))])
    df = pd.concat(hr_list)
    #sorting by the datetime and dropping all duplicates (if any)
    return df.sort_values(by=['datetime'], ascending=True).drop_duplicates()
#applying the functuon to the remaining dataframes
# dfeuraud_hr = hourly_intervals(dfeuraud)
# dfeurgbp_hr = hourly_intervals(dfeurgbp)
# dfeurusd_hr = hourly_intervals(dfeurusd)
# dfgbpusd_hr = hourly_intervals(dfgbpusd)
# dfaudusd_hr = hourly_intervals(dfaudusd)
directory = os.getcwd()
filepath = f"{directory}\Hourly_data"
dfaudusd_hr = pd.read_csv(f"{filepath}\dfaudusd_hr.csv")
dfeuraud_hr = pd.read_csv(f"{filepath}\dfeuraud_hr.csv")
dfeurgbp_hr = pd.read_csv(f"{filepath}\dfeurgbp_hr.csv")
dfeurusd_hr = pd.read_csv(f"{filepath}\dfeurusd_hr.csv")
dfgbpusd_hr = pd.read_csv(f"{filepath}\dfgbpusd_hr.csv")
dfaudusd_hr.head()

dfaudusd_hr = dfaudusd_hr.drop(dfaudusd_hr.columns[[0]], axis=1)
dfeuraud_hr = dfeuraud_hr.drop(dfeuraud_hr.columns[[0]], axis=1)
dfeurgbp_hr = dfeurgbp_hr.drop(dfeurgbp_hr.columns[[0]], axis=1)
dfeurusd_hr = dfeurusd_hr.drop(dfeurusd_hr.columns[[0]], axis=1)
dfgbpusd_hr = dfgbpusd_hr.drop(dfgbpusd_hr.columns[[0]], axis=1)
dfaudusd_hr.head()

dfs= [dfaudusd_hr, dfeuraud_hr, dfeurgbp_hr, dfeurusd_hr, dfgbpusd_hr]
for i in range(len(dfs)):
    dfs[i][['Date', 'Time']] = dfs[i]['datetime'].str.split(' ', expand=True)
    dfs[i][['Time', 'Useless']]  = dfs[i]['Time'].str.split('+', expand=True)
dfaudusd_hr.head()