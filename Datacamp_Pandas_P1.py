import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
url = 'C:/Users/Adrian/Documents/Data\
 _Journalism/DataCamp Lesson Datafiles/worldpop.csv'

list_keys = ['Country', 'Total']
list_values = [(['United States', 'Soviet Union', 'United \
Kingdom']), ([1118, 473, 273])]

zipped = list(zip(list_keys, list_values))
print(zipped)

data = dict(zipped)
df = pd.DataFrame(data)

df.columns = ['Country', 'Total Medals']
print(df)

df1 = pd.read_csv(url)
print(df1)
url1 = 'C:/Users/Adrian/Documents/Data\
 _Journalism/DataCamp Lesson Datafiles/yahoofinancemessy.csv'
df2 = pd.read_csv(url1, delimiter=' ', header=3, comment='#')
print(df2.head())
df2.to_csv('C:/Users/Adrian/Documents/Data\
 _Journalism/DataCamp Lesson Datafiles/file_clean', index=False)

df3 = pd.read_csv('C:/Users/Adrian/Documents/Data\
 _Journalism/DataCamp Lesson Datafiles/austintemp.csv')

df4 = df3['Temperature']
print(df4.head())

df4.plot(color='red')
plt.show()
column_list1 = df3['DewPoint']
column_list1.plot(color='blue')
plt.show()
column_list2 = df3['Temperature', 'DewPoint']
column_list2.plot()
plt.show()
