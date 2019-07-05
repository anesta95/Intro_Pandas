import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir('C:/Users/Adrian/Documents/Data\
 _Journalism/DataCamp Lesson Datafiles')
df = pd.read_csv('womendegrees.csv')
# Print the minimum value of the Engineering column
print(df['Engineering'].min())

# Print the maximum value of the Engineering column
print(df['Engineering'].max())

# Construct the mean percentage per year: mean
mean = df.mean(axis='columns')

# Plot the average percentage per year
mean.plot()

# Display the plot
plt.show()

df1 = pd.read_csv('titanic2.csv')
# Print summary statistics of the fare column with .describe()
print(df1['fare'].describe())

# Generate a box plot of the fare column
df1['fare'].plot(kind='box')

# Show the plot
plt.show()
df2 = pd.read_csv('automobiles.csv')

global_mean = df2['mpg'].mean()
global_std = df2['mpg'].std()
print(global_mean)
print(global_std)
us = df2[df2['origin'] == 'US']
us_mean = us.mean()
us_std = us.std()

# Print the differences
print(us_mean)
print(us_std)
# Display the box plots on 3 separate rows and 1 column
fig, axes = plt.subplots(nrows=3, ncols=1)

# Generate a box plot of the fare prices for the First passenger class
df1.loc[df1['pclass'] == 1].plot(ax=axes[0], y='fare', kind='box')

# Generate a box plot of the fare prices for the Second passenger class
df1.loc[df1['pclass'] == 2].plot(ax=axes[1], y='fare', kind='box')

# Generate a box plot of the fare prices for the Third passenger class
df1.loc[df1['pclass'] == 3].plot(ax=axes[2], y='fare', kind='box')

# Display the plot
plt.show()
