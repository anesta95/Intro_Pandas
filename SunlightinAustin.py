import pandas as pd
import matplotlib.pyplot as plt
import os
import csv
os.chdir('C:/Users/Adrian/Documents/Data_Journalism/DataCamp \
         Lesson Datafiles/')

df_headers = pd.read_csv('NOAAaustinclimate.csv', header=None)
df_climate = pd.read_csv('austintemp.csv', index_col='Date', parse_dates=True)
column_labels = open('NOAAaustincolumns.txt', mode='r')
column_labels_list = column_labels.read().split(',')
list_to_drop = open('NOAAaustindrop.csv', mode='r')
reader1 = csv.reader(list_to_drop, delimiter=',')
list_to_drop_list = list(list_to_drop)
print(column_labels_list)

# Assign the new column labels to the DataFrame: df.columns
df_headers.columns = column_labels_list

# Remove the appropriate columns: df_dropped
df_dropped = df_headers.drop(list_to_drop, axis='columns')

# Print the output of df_dropped.head()
print(df_dropped.head())

# Convert the date column to string: df_dropped['date']
df_dropped['date'] = df_dropped['date'].astype(str)

# Pad leading zeros to the Time column: df_dropped['Time']
df_dropped['Time'] = df_dropped['Time'].apply(lambda x: '{:0>4}'.format(x))

# Concatenate the new date and Time columns: date_string
date_string = df_dropped['date'] + df_dropped['Time']

# Convert the date_string Series to datetime: date_times
date_times = pd.to_datetime(date_string, format='%Y%m%d%H%M')

# Set the index to be the new date_times container: df_clean
df_clean = df_dropped.set_index(date_times)

df_clean['dry_bulb_faren'] = pd.to_numeric(df_clean['dry_bulb_faren'],
                                           errors='coerce')

print(df_clean.loc['2011-06-20 8:00:00': '2011-06-20 9:00:00',
      'dry_bulb_faren'])

# Convert the wind_speed and dew_point_faren columns to numeric values
df_clean['wind_speed'] = pd.to_numeric(df_clean['wind_speed'], errors='coerce')
df_clean['dew_point_faren'] = pd.to_numeric(df_clean['dew_point_faren'],
                                            errors='coerce')

# Print the median of the dry_bulb_faren column
print(df_clean['dry_bulb_faren'].median())

print(df_clean.loc['2011-04':'2011-06', 'dry_bulb_faren'].median())

# Print the median of the dry_bulb_faren column for the month of January
print(df_clean.loc['2011-01', 'dry_bulb_faren'].median())

# Downsample df_clean by day and aggregate by mean: daily_mean_2011
daily_mean_2011 = df_clean.resample('D').mean()

daily_temp_2011 = daily_mean_2011['dry_bulb_faren'].values

# Downsample df_climate by day and aggregate by mean: daily_climate
daily_climate = df_climate.resample('D').mean()

daily_temp_climate = daily_climate.reset_index()['Temperature']

# Compute the difference between the two arrays and print the mean difference
difference = daily_temp_2011 - daily_temp_climate
print(difference.mean())

# Using df_clean, when is sky_condition 'CLR'?
is_sky_clear = df_clean['sky_condition'] == 'CLR'

# Filter df_clean using is_sky_clear
sunny = df_clean[is_sky_clear]

# Resample sunny by day then calculate the max
sunny_daily_max = sunny.resample('D').max()

# See the result
print(sunny_daily_max.head())

# Using df_clean, when does sky_condition contain 'OVC'?
is_sky_overcast = df_clean['sky_condition'].str.contains('OVC')

# Filter df_clean using is_sky_overcast
overcast = df_clean.loc[is_sky_overcast]

# Resample overcast by day then calculate the max
overcast_daily_max = overcast.resample('D').max()

# See the result
print(overcast_daily_max.head())

# Calculate the mean of sunny_daily_max
sunny_daily_max_mean = sunny_daily_max.mean()

# Calculate the mean of overcast_daily_max
overcast_daily_max_mean = overcast_daily_max.mean()

# Print the difference (sunny minus overcast)
print(sunny_daily_max_mean - overcast_daily_max_mean)

weekly_mean = df_clean[['visibility', 'dry_bulb_faren']].resample('W').mean()

# Print the output of weekly_mean.corr()
print(weekly_mean.corr())

# Plot weekly_mean with subplots=True
weekly_mean.plot(subplots=True)
plt.show()

resampled = is_sky_clear.resample('D')

# Calculate the number of sunny hours per day
sunny_hours = resampled.sum()

# Calculate the number of measured hours per day
total_hours = resampled.count()

# Calculate the fraction of hours per day that were sunny
sunny_fraction = sunny_hours / total_hours
print(sunny_fraction)
sunny_fraction.plot(kind='box')
plt.show()


monthly_max = df_clean[['dew_point_faren',
                        'dry_bulb_faren']].resample('M').max()

# Generate a histogram with bins=8, alpha=0.5, subplots=True
# monthly_max.plot(kind='hist', bins=8, alpha=0.5, subplots=True)

# Show the plot
plt.show()

# Extract the maximum temperature in August 2010 from df_climate: august_max
august_max = df_climate.loc['2010-08', 'Temperature'].max()
print(august_max)

august_2011 = df_clean.loc['2011-Aug', 'dry_bulb_faren'].resample('D').max()

august_2011_high = august_2011.loc[august_2011 > august_max]

# Construct a CDF of august_2011_high
august_2011_high.plot(kind='hist', density=True, cumulative=True, bins=10)

# Display the plot
plt.show()
