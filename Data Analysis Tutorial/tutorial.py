#I'm following a tutorial from Youtube for 100DaysOfCode
# https://www.youtube.com/watch?v=Iqjy9UqKKuo

"""
#Video 2
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

web_stats = {'Day': [1, 2, 3, 4, 5, 6],
             'Visitors': [43, 53, 34, 45, 64, 34],
             'Bounce_Rate': [65, 72, 62, 64, 54, 66]
             }

df = pd.DataFrame(web_stats)

#df.head() df.tail() -- first/last 5 rows, df.head(2) changes to 2

#df.set_index returns a new data frame
#df = df.set_index('Day')
df.set_index('Day', inplace=True)

#df['Visitors'], df.Visitors, need Bounce_Rate for dot version

#print(df[['Bounce_Rate', 'Visitors']])
#print(df.Visitors.tolist())

#Arrays not supported natively, numpy array
#print(np.array(df[['Bounce_Rate', 'Visitors']]))
"""


"""
#Video 3
#https://www.quandl.com/data/ZILLOW/C3159_TURNAH-Zillow-Home-Value-Index-City-Turnover-All-Homes-Greenville-AL
#ZILLOW-C3159_TURNAH.csv

import pandas as pd

df = pd.read_csv('ZILLOW-C3159_TURNAH.csv')

df.set_index('Date', inplace=True)

#outputs with new index to csv
df.to_csv('newcsv2.csv')

#df = pd.read_csv('newcsv2.csv')
#here we're back to date not being an index, csv doesn't have an index
#print(df.head())

#sets date as index when pulled in
df = pd.read_csv('newcsv2.csv', index_col=0)
#print(df.head())

#remember, index is not a column
df.columns = ['Greenville_HPI']

#print(df.head())

#df.to_csv('newcsv3.csv')

#only want data in csv, no headers
#df.to_csv('newcsv4.csv', header=False)

df = pd.read_csv('newcsv4.csv', names=['Date', 'Greenville_HPI'], index_col=0)
print(df.head())

#saves to html
df.to_html('example.html')


df = pd.read_csv('newcsv4.csv', names=['Date', 'Greenville_HPI'])
#print(df.head())

#rename a single column
df.rename(columns={'Greenville_HPI':'36037_HPI'}, inplace=True)
print(df.head())
"""
