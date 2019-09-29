import pandas as pd
sales = pd.read_csv('sales.csv', index_col='month')
sales2 = pd.read_csv('sales.csv')
sales3 = pd.read_csv('sales.csv')
sales4 = pd.read_csv('sales.csv')

print(sales.head())
# Create the list of new indexes: new_idx
new_idx = [month.upper() for month in sales.index]

# Assign new_idx to sales.index
sales.index = new_idx

# Print the sales DataFrame
print(sales)

# Assign the string 'MONTHS' to sales.index.name
sales.index.name = 'MONTHS'

# Print the sales DataFrame
print(sales)

# Assign the string 'PRODUCTS' to sales.columns.name
sales.columns.name = 'PRODUCTS'

# Print the sales dataframe again
print(sales)

# Generate the list of months: months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Assign months to sales.index
sales2.index = months

# Print the modified sales DataFrame
print(sales2)


states = ['CA', 'CA', 'NY', 'NY', 'TX', 'TX']

sales3['state'] = states
sales3['month'] = [1, 2, 1, 2, 1, 2]
# Set the index to be the columns ['state', 'month']: sales

sales3  = sales3.set_index(['state', 'month'])
print(sales3)

# Sort the MultiIndex: sales
sales = sales.sort_index()

# Print sales.loc[['CA', 'TX']]
print(sales3.loc[['CA', 'TX']])

# Print sales['CA':'TX']
print(sales3['CA':'TX'])

sales4['state'] = states
sales4['month'] = [1, 2, 1, 2, 1, 2]


# Set the index to the column 'state': sales
sales4 = sales.set_index(sales4['state'])

# Print the sales DataFrame
print(sales4)

# Access the data from 'NY'
print(sales4.loc['NY'])

# Look up data for NY in month 1: NY_month1
NY_month1 = sales3.loc[('NY', 1), :]

# Look up data for CA and TX in month 2: CA_TX_month2
CA_TX_month2 = sales3.loc[(['CA', 'TX'], 2), :]

# Access the inner month index and look up data for all states in month 2: all_month2
all_month2 = sales3.loc[(slice(None), 2), :]

print(NY_month1)
print(CA_TX_month2)
print(all_month2)