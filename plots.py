#!/usr/bin/env python
# coding: utf-8

import numpy as np
import scipy
import pandas as pd
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from matplotlib.pyplot import plot,scatter, show, bar, xlabel, ylabel, title, savefig, figure, tight_layout, xticks,axes

from clean import clean_cols, get_date clean_df grouped_time_cols, hour_year_week

def plot_scatter(groups, _xlabel='time', _ylabel='frequency', _title='frequency of crime over time',_xticks=False):
    scatter(groups.index,groups.values,)
    xlabel(_xlabel)
    ylabel(_ylabel)
    if _xticks:
        xticks(groups.index)
    title(_title)
    filename = _title.lower().replace(' ','_')
    tight_layout()
    savefig(f"charts/{_xlabel}_{filename}.png")
    show()

if __name__ == "__main__":
    df = pd.read_pickle('crimes.pkl')
    df = clean_cols(df)
    df = clean_df(df)
    df = grouped_time_cols(df)

    hour, weekday, week, dayofyear = hour_year_week(df)


    plot_scatter(hour, _xlabel='hour of day')
    plot_scatter(dayofyear, _xlabel='day of year')
    plot_scatter(weekday, _xlabel='day of week',_xticks=True)
    plot_scatter(week, _xlabel='week')

    df.to_pickle('data/clean_df.pkl')

    theft = df[(df.year>=2015) & (df.primary_type=='THEFT')]

    hour, weekday, week, dayofyear = hour_year_week(theft)

    plot_scatter(hour, _xlabel='hour of day')
    plot_scatter(dayofyear, _xlabel='day of year')
    plot_scatter(weekday, _xlabel='day of week',_xticks=True)
    plot_scatter(week, _xlabel='week')

    df['rounded'] = df['date'].dt.round('D')

    grouped = df[(df.year>=2015) & (df.primary_type=='THEFT')].groupby('rounded').count().id

    figure(figsize=(20,10))
    plot(grouped.index, grouped.values)

    new_df = grouped.reset_index()

    new_df = new_df.rename({'rounded':'day','id':'count'}, axis='columns')

    new_df.to_pickle('data/freq_day_theft.pkl')

    test = df[df.year >2017]
    train = df[df.year <=2017]

    testdf = test.groupby('hour').count().id
    traindf = test.groupby('hour').count().id

    traindf

    df[df.primary_type == 'THEFT'].groupby('rounded').count().id



