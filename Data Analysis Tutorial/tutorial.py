#I'm following a tutorial from Youtube for 100DaysOfCode
# https://www.youtube.com/watch?v=Iqjy9UqKKuo


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
print(np.array(df[['Bounce_Rate', 'Visitors']]))

