import pandas as pd
import numpy as np

# To generate the column with the pandas' Series function
s = pd.Series([1,3,5,np.nan,6,8])
print(s)

# From '20130101', date_range generates six consecutive days
dates = pd.date_range('20130101', periods=6)
print (dates)

# This work is to create 'DateFrame' with randomly generated 6 rows and 4 columns
# 'index' has 'dates', so that each row has a corresponding date (e.g., 1 = 20130101)
# 'columns' has titles 'a' to 'd' which are corresponding to 4
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['a','b', 'c', 'd'])
print(df)

# 'head' shows you the first three rows and "withour" number in the parentheses brings the first five rows 
print(df.head(3))
# 'index' shows you what title you have in the first column (usually we called it the x-axis)
print(df.index)
# 'columns' calls the data titles (corresponding to the first row)
print(df.columns)
# 'values' shows VALUES without the titles
print(df.values)

# 'sort_values' helps to sort the data
# 'b' is the reference point to re-sort the data set
# 'ascending' or 'descending' is to sort based on user's preference and requires 'True' or 'False'
print(df.sort_values(by='b', ascending=True))
# 'info' calls the outline of the 'df'
print(df.info())
# 'describe' calculates general statistical points such as mean, std, min, 25%, 50%, 75%, max
print(df.describe())

# This shows the data in the column 'a'
print(df['a'])
# This shows the data from the third row to the fifth row
print(df[2:4])
# This shows the data in '20130103' and '20130104'
print(df['20130103':'20130104'])

# '.loc' cuts the data based on the first row and shows it as a column (90 degree flipped)
print(df.loc[dates[0]])
# This calls the columns (a and b) across the data set (the commend of ':')
print(df.loc[:,['a','b']])
# This picks the columns (a and b) and shows the data in '20130103' to '20130104'
print(df.loc['20130103':'20130104',['a','b']])
# This calls data in the specific date in the column 'a'
print(df.loc[dates[0],'a'])

# This calls the data from the third row in all columns
print(df.iloc[3])
# indexes (x-axis), AFTER 3rd row to 5th row, and columns (data), 1st to 2nd
print(df.iloc[3:5,0:2])
# This is to pick a specific data in a specific index (dates)
print(df.iloc[[1,2,4],[0,2,3]])
# This returns all the data in the second row to the third row
print(df.iloc[1:3,:])
# This returns the data in the columns the second and third corresponding all the index
print(df.iloc[:,1:3])

# This returns the data when the data in the column 'a' overs 0
print(df[df.a >0])
# This returns the data when it overs 0 or returns 'NaN'
print(df[df>0])

# This defines 'df2' by copying 'df'
df2 = df.copy()
# 'df2' will have the column 'e' and have the data following the below order
df2['e'] = ['one','two','three', 'four', 'five','six']
print(df2)

# This returns True if there is 'two' or 'four' or returns False
print(df2['e'].isin(['two','four']))
# This returns the data when the column 'e' has 'two' or 'four'
print(df2[df2['e'].isin(['two','four'])])

# This returns the cumulative sum in each column
print(df.apply(np.cumsum))
# This returns the values (max - min) in the data (each column)
print(df.apply(lambda x: x.max() - x.min()))