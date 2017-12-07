import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style

style.use("fivethirtyeight")

from credentials import *


def mortgage_30y():
    df = quandl.get("FMAC/MORTG", trim_start="1975-01-01", authtoken = api_key)
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0

    # correction from video game from youtube comment
    df = df.resample('1D').mean()
    df = df.resample('M').mean()
    df.columns = ['M30']

    return df

def state_list():
    states = pd.read_html('https://en.wikipedia.org/wiki/List_of'
                          '_states_and_territories_of_the_United_States')
    return states[0][1][2:]

def grab_initial_state_data():
    states = state_list()
    main_df = pd.DataFrame()

    # prints abbreviations of 50 states
    for abbv in states:
        query = "FMAC/HPI_" + str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df.rename(columns={'Value': str(abbv)}, inplace=True)
        df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100.0

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    # csv is an option
    # main_df.to_csv('housingPrices.csv')
    # main_df = pd.read_csv('housingPrices.csv')

    # default version, pandas version looks better
    # pickle_out = open("states.pickle", "wb")
    # $pickle.dump(main_df, pickle_out)
    # pickle_out.close()

    main_df.to_pickle("states.pickle")

def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0

    return df

    # default version, pandas version looks better
    # grab_initial_state_data()
    # pickle_in = open("states.pickle", "rb")
    # HPI_data = pickle.load(pickle_in)


    # grab_initial_state_data()

    #HPI_data = pd.read_pickle("states.pickle")

    # Graphs HPI data against national average
    # benchmark = HPI_Benchmark()

    # fig = plt.figure()
    # ax1 = plt.subplot2grid((1,1),(0,0))
    #
    # HPI_data.plot(ax = ax1)
    # benchmark.plot(ax = ax1, color="k", linewidth=10)
    # plt.legend().remove()
    # plt.show()

    # Correlation, shows min/max/mean/std
    # HPI_State_Correlation = HPI_data.corr()
    # print(HPI_State_Correlation.describe())

    # fig = plt.figure()
    # ax1 = plt.subplot2grid((2, 1), (0, 0))
    # ax2 = plt.subplot2grid((2, 1), (1, 0), sharex=ax1)

    # moving average for a year
    # HPI_data['AL12MA'] = pd.rolling_mean(HPI_data['AL'], 12)
    # HPI_data['AL12STD'] = pd.rolling_std(HPI_data['AL'], 12)

    # HPI_data.dropna(inplace=True)


    # HPI_data[['AL', 'AL12MA']].plot(ax=ax1)
    # HPI_data[['AL12STD']].plot(ax=ax2)

    # AL_AK_12corr = pd.rolling_corr(HPI_data['AL'], HPI_data['AK'], 12)
    #
    # HPI_data['AL'].plot(ax=ax1, label='AL HPI')
    # HPI_data['AK'].plot(ax=ax1, label='AK HPI')
    #
    # AL_AK_12corr.plot(ax=ax2, label="AL_AK_12corr")
    #
    # plt.legend(loc=4)
    # plt.show()

HPI_data = pd.read_pickle('states.pickle')
m30 = mortgage_30y()
HPI_Bench = HPI_Benchmark()
HPI = HPI_Bench.join(m30)

state_HPI_M30 = HPI_data.join(m30)

print(state_HPI_M30.corr()['M30'].describe())