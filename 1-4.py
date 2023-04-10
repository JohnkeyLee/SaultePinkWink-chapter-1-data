import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#### this process is to use Korean in 'matplotlib'
import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')
#### The above code is to set up the font and validate the KOREAN

# call the CSV file and name it as CCTV_Seoul 
# encoding function is for when you are using Korean, if you use English, NVM
CCTV_Seoul = pd.read_csv('G:\\My Drive\\Jongki-study\\05_Manual\\17_Python\\DataScience\\data\\01. CCTV_in_Seoul.csv', encoding='utf-8')
print(CCTV_Seoul.head())
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : 'District', CCTV_Seoul.columns[1] : 'Total', CCTV_Seoul.columns[2] : 'Before 2013', CCTV_Seoul.columns[3] : '2014', CCTV_Seoul.columns[4] : '2015', CCTV_Seoul.columns[5] : '2016'}, inplace=True)
print(CCTV_Seoul.head())

# This is to sort by '소계' in ascending order
print(CCTV_Seoul.sort_values(by='Total', ascending=True).head())
# This is to sort by '소계' in descending order
print(CCTV_Seoul.sort_values(by='Total', ascending=False).head())

# This process is to check the increased rate of number of CCTV
CCTV_Seoul['Recent increased rates'] = (CCTV_Seoul['2016'] + CCTV_Seoul['2015'] + CCTV_Seoul['2014']) / CCTV_Seoul['Before 2013'] * 100
print(CCTV_Seoul.sort_values(by='Recent increased rates', ascending=False).head())

# Check the population data 
pop_Seoul = pd.read_csv('G:\\My Drive\\Jongki-study\\05_Manual\\17_Python\\DataScience\\data\\01. population_in_Seoul.csv', encoding='utf-8', header=2, usecols=[1, 3, 6, 9, 13])
pop_Seoul.rename(columns={pop_Seoul.columns[0] : 'District', pop_Seoul.columns[1] : 'Population', pop_Seoul.columns[2] : 'Korean', pop_Seoul.columns[3] : 'Forigner', pop_Seoul.columns[4] : 'Eldery'}, inplace=True)
print(pop_Seoul.head())
# However, we don't need '합계', 'sum', so this is to delete the first row
pop_Seoul.drop([0], inplace=True)
print(pop_Seoul.head())

# 'unique' function summarizes data appeared at least once in the data set, 'District'
print(pop_Seoul['District'].unique)
# However, somewhere in this data set, they have 'NaN', so this code is to find the Null value
# The meaning is that among the data set, if there is 'NaN', it returns 'True'. 
# BUT, instead of returning this, by using the double bracket, it will return what and where in the whole data set
# print(pop_Seoul['District'].isnull())
print(pop_Seoul[pop_Seoul['District'].isnull()])
# This is to delete the Null data point
# IF THERE IS NaN, please use "pop_Seoul.drop([nn], inplace=True)""

# This is to generate two columns for 'Forigner percentage' and 'Eldery percentage' 
pop_Seoul['Forigner percentage'] = pop_Seoul['Forigner'] / pop_Seoul['Population'] * 100
pop_Seoul['Eldery percentage'] = pop_Seoul['Eldery'] / pop_Seoul['Population'] * 100
print(pop_Seoul.head())
print(pop_Seoul.sort_values(by='Population', ascending=False).head())
print(pop_Seoul.sort_values(by='Forigner', ascending=False).head())
print(pop_Seoul.sort_values(by='Forigner percentage', ascending=False).head())
print(pop_Seoul.sort_values(by='Eldery', ascending=False).head())
print(pop_Seoul.sort_values(by='Eldery percentage', ascending=False).head())

# This is to merge two data sets based on 'District'
data_result = pd.merge(CCTV_Seoul, pop_Seoul, on = 'District')
print(data_result.head())

# This is to delete unnecessary columns (data)
del data_result['Before 2013']
del data_result['2014']
del data_result['2015']
del data_result['2016']
print(data_result.head())

# This is to set an index to organize data set
data_result.set_index('District', inplace=True)
print(data_result.head())

# This is to calculate the correlation coefficient (r^2), and it shows you a result as a matirix type 
# [[ 1.         -0.13607433]
# [-0.13607433  1.        ]] You can read the diagonal numbers, not '1'
print(np.corrcoef(data_result['Forigner percentage'], data_result['Total']))
print(np.corrcoef(data_result['Eldery percentage'], data_result['Total']))
print(np.corrcoef(data_result['Population'], data_result['Total']))

# This is to re-organize data set based on 'Total' and 'Population'
print(data_result.sort_values(by='Total', ascending=False).head())
print(data_result.sort_values(by='Population', ascending=False).head())

# This is to plot for 'Total' and the graph will be drawn as a horizontal bar ('barh')s
data_result['Total'].plot(kind='barh', grid=True, figsize=(10,10))
plt.show()
# This is a different to the above because it is sorting value (descending)
data_result['Total'].sort_values().plot(kind='barh', grid=True, figsize=(10,10))
plt.show()
# 
data_result['CCTV ratio'] = data_result['Total'] / data_result['Population'] * 100
data_result['CCTV ratio'].sort_values().plot(kind='barh', grid=True, figsize=(10,10))
plt.show()
plt.figure(figsize=(10,6))
# 's=50' is the size of marker
plt.scatter(data_result['Population'], data_result['Total'], s=50)
plt.xlabel('Population')
plt.ylabel('CCTV')
plt.grid()
plt.show()

# The below work is to generate the representative line on the graph using 'polyfit' and 'poly1d'
fp1 = np.polyfit(data_result['Population'], data_result['Total'], 1)
print(fp1)
# This is to generate x-axis
f1 = np.poly1d(fp1)
# This is to generate y-axis
fx = np.linspace(100000, 700000, 100)
plt.figure(figsize=(10,10))
plt.scatter(data_result['Population'], data_result['Total'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')
plt.xlabel('Population')
plt.ylabel('CCTV')
plt.grid()
plt.show()

# This paragraph is to create colored error bar and name the data far from the line
fp1 = np.polyfit(data_result['Population'], data_result['Total'], 1)
f1 = np.poly1d(fp1)
fx = np.linspace(100000, 700000, 100)
data_result['Error'] = np.abs(data_result['Total'] - f1(data_result['Population']))
df_sort = data_result.sort_values(by='Error', ascending=False)
print(df_sort.head())
plt.figure(figsize=(14,10))
plt.scatter(data_result['Population'], data_result['Total'], c=data_result['Error'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')

# This is to write the names the farest to the 10th from the line
# '1.02' and '0.98' are to locate the name for each like how far from the scatter
for n in range (10):
    plt.text(df_sort['Population'][n]*1.02, df_sort['Total'][n]*0.98, df_sort.index[n], fontsize=15)

plt.xlabel('Population')
plt.ylabel('Per capita')
plt.colorbar()
plt.grid()
plt.show()