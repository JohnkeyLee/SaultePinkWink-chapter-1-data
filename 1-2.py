import pandas as pd

# Read CSV file and recognize Korean 
# Cut off the first two rows uisng header function
# Bring columns 1, 3, 6, 9, 13 with usecols function
pop_Seoul = pd.read_csv('G:\\My Drive\\Jongki-study\\05_Manual\\17_Python\\DataScience\\data\\01. population_in_Seoul.csv', encoding='utf-8', header=2, usecols=[1, 3, 6, 9, 13])

#rename function is to change the column's title
pop_Seoul.rename(columns={pop_Seoul.columns[0] : 'District', pop_Seoul.columns[1] : 'Population', pop_Seoul.columns[2] : 'Korean', pop_Seoul.columns[3] : 'Forigner', pop_Seoul.columns[4] : 'Eldery'}, inplace=True)
print(pop_Seoul.head())