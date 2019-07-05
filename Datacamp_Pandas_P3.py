import pandas as pd
import matplotlib.pyplot as plt
import os
os.chdir('C:/Users/Adrian/Documents/Data\
 _Journalism/DataCamp Lesson Datafiles/')

df = pd.read_csv('austintemp.csv', index_col='Date', parse_dates=True)

# Extract the hour from 9pm to 10pm on '2010-10-11': ts1
ts1 = df.loc['2010-10-11 21:00:00':'2010-10-11 22:00:00']

# Extract '2010-07-04' from ts0: ts2
ts2 = df.loc['2010-07-04']

# Extract data from '2010-12-15' to '2010-12-31': ts3
ts3 = df.loc['2010-12-15':'2010-12-31']

print(ts1)
print(ts2)
print(ts3)

df1 = df.loc[:, 'Temperature'].resample('6h').mean()
df2 = df.loc[:, 'Temperature'].resample('D').count()
print(df1)
print(df2)

august = df['Temperature']['2010-August']

august_highs = august.resample('D').max()

february = df['Temperature']['2010-February']

february_lows = february.resample('D').min()

print(august_highs)
print(february_lows)

unsmoothed = df['Temperature']['2010-08-01': '2010-08-15']

smoothed = unsmoothed.rolling(window=24).mean()

august = pd.DataFrame({'smoothed': smoothed, 'unsmoothed': unsmoothed})

august.plot()
plt.show()


daily_highs_smoothed = august_highs.rolling(window=7).mean()

sw = pd.read_csv('austinswflightdata.csv', index_col='Date (MM/DD/YYYY)',
                 parse_dates=True)

sw.columns = sw.columns.str.strip()

dallas = sw['Destination Airport'].str.contains('DAL')

daily_departures = dallas.resample('D').sum()

stats = daily_departures.describe()
print(daily_departures)
print(stats)

df.Temperature['2010-06':'2010-08'].plot()
plt.show()
plt.clf()

df.Temperature['2010-06-10': '2010-06-17'].plot()
plt.show()
plt.clf()
