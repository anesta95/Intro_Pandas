import pandas as pd

df = pd.DataFrame([
    [1, '3 inch screw', 0.5, 0.75],
    [2, '2 inch nail', 0.10, 0.25],
    [3, 'hammer', 3.00, 5.50],
    [4, 'screwdriver', 2.50, 3.00]
],
    columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']
df['Is taxed?'] = 'Yes'
df['Revenue'] = df.Price - df['Cost to Manufacture']

df1 = pd.DataFrame([
    ['JOHN SMITH', 'john.smith@gmail.com'],
    ['Jane Doe', 'jdoe@yahoo.com'],
    ['joe schmo', 'joeschmo@hotmail.com']
],
    columns=['Name', 'Email'])

df1['Lowercase Name'] = df.Name.apply(lower)

print(df)
print(df1)
file = 'C:/Users/Adrian/Documents/Data Journalism/Datacamp Lesson \
        Datafiles/titanic.csv'
titanic = pd.read_csv(file)
print(titanic.head())
