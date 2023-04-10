import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])

print(df1)
print(df2)
print(df3)

# This is to generate one data set with three different data sets 
# 'concat' fuction is order-sensitive
result = pd.concat([df1,df2,df3])
print(result)
result2 = pd.concat([df1,df3,df2])
print(result2)

# This is to generate the multi-indexes
result = pd.concat([df1,df2,df3], keys=['x','y','z'])
print(result)
print(result.index)
print(result.index.get_level_values(0))
print(result.index.get_level_values(1))

df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'], 
                    'D': ['D2', 'D3', 'D6', 'D7'],
                    'F': ['F2', 'F3', 'F6', 'F7']},
                   index=[2, 3, 6, 7])

# In terms of 'axis' in 'concat', it has a default 0 
result3 = pd.concat([df1, df4])
print(result3)
# 'axis=1' merges the data based on the index (x-axis, time-series, etc.)
result4 = pd.concat([df1, df4], axis=1)
print(result4)
# 'join='inner'' cuts other parts having NaN
result5 = pd.concat([df1, df4], axis=1, join='inner')
print(result5)
# This is to re-match the df4's index to df1's index
result6 = pd.concat([df1, df4.reindex(df1.index)], axis = 1)
print(result6)
# This is merge the data regardless of the idex, but it is the order sensitive
result7 = pd.concat([df1, df4], ignore_index=True)
print(result7)
result8 = pd.concat([df4, df1], ignore_index=True)
print(result8)

left = pd.DataFrame({'key': ['K0', 'K4', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)

# This is to re-order the data set based on common 'key' index
print(pd.merge(left, right, on='key'))
# This is to merge two data set based on 'key' index on 'left' data set
print(pd.merge(left, right, how='left', on='key'))
# "'outher'" merges every data 
print(pd.merge(left, right, how='outer', on='key'))
# "'inner'" merges within a common parameter (here is 'key')
print(pd.merge(left, right, how='inner', on='key'))