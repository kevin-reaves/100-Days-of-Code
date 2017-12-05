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



#Video 4
#Append combines rows of one dataframe into another dataframe

#Concat takes a group of 2+ dataframes and combines the dataframes via
#the rows of the columns. Good for merging multiples with similar data

#Merge allows for SQL style merging of two dataframes, inner, outer, left, right

#Join is similar to merge, join is better when index does matter



#import quandl
#import pandas as pd

#from credentials import *

"""
#df = quandl.get('FMAC/HPI_AL', authtoken=api_key)
#print(df.head())

states = pd.read_html('https://en.wikipedia.org/wiki/List_of'
                      '_states_and_territories_of_the_United_States')

#print(states[0][1])

#prints abbreviations of 50 states
for abbv in states[0][1][2:]:
    print("FMAC/HPI_"+str(abbv))
"""
#video 5

"""
df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

#concat could leave you with NaN, may not mix properly
#concat = pd.concat([df1, df2, df3])
#print(concat)

#appending isn't really what you want to do with data frames
#data frames aren't really meant to be changed
#df4 = df1.append(df2)
#print(df4)

s = pd.Series([80, 2, 50], index = ['HPI','Int_rate','US_GDP_Thousands'])
df4 = df1.append(s, ignore_index = True)

print(df4)
"""

#video 6
"""
df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

#merging is going to give duplicated data
#similar to SQL merging on a given column
#print(pd.merge(df1, df2, on=['HPI' , 'Int_rate']))

df1.set_index("HPI", inplace=True)
df3.set_index("HPI", inplace=True)

joined = df1.join(df3)
print(joined)
"""
#also video 6
"""
df1 = pd.DataFrame({
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                    'Year':[2001, 2002, 2003, 2004]
                    })

df3 = pd.DataFrame({
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53],
                    'Year':[2001, 2003, 2004, 2005]})

merged = pd.merge(df1, df3, on = "Year", how="outer")
merged.set_index("Year", inplace = True)
print(merged)
"""

