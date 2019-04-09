import pandas as pd

def clean_cols(df):
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

def get_date(df,col):
    return pd.to_datetime(df[col],format='%m/%d/%Y %I:%M:%S %p')

def clean_df(df):
    df = df.copy()
    df.date = get_date(df,'date')
    df.updated_on = get_date(df,'updated_on')
    df.district = df.district.fillna(-1).astype(int)
    df.ward = df.ward.fillna(-1).astype(int)
    return df

def grouped_time_cols(dd):
    dd['weekday'] = dd.date.dt.weekday
    dd['dayofyear'] = dd.date.dt.dayofyear
    dd['week'] = dd.date.dt.week
    dd['hour'] = dd.date.dt.hour
    return dd

def hour_year_week(t):
    hour = t.groupby('hour').count().id
    weekday = t.groupby('weekday').count().id
    week = t.groupby('week').count().id
    dayofyear = t.groupby('dayofyear').count().ids
    return (hour, weekday, week, dayofyear)