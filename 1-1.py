import pandas as pd

# call the CSV file and name it as CCTV_Seoul 
# encoding function is for when you are using Korean, if you use English, NVM
CCTV_Seoul = pd.read_csv('G:\\My Drive\\Jongki-study\\05_Manual\\17_Python\\DataScience\\data\\01. CCTV_in_Seoul.csv', encoding='utf-8')

# head shows you the first five rows and if you set a certain number, it shows the amount of data
print(CCTV_Seoul.head())

print(CCTV_Seoul.head(3))

# columns call the index (title of columns)
print(CCTV_Seoul.columns)

# If the below is moved to the above, the output will be changed. 
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : 'Categorize'}, inplace = True)

# [0] after columns shows you the first title in the first column
print(CCTV_Seoul.columns[0])
