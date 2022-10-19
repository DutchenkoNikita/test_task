"""
Created on Mon Feb  7 14:10:42 2022

@author: Okhrimchuk Roman
for Sierentz Global Merchants

Test task
"""

# TODO Import the necessary libraries
import pandas as pd
import numpy as np

# TODO Import the dataset
import seaborn as sns

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
path = r'./data/weather_dataset.data'
data = pd.read_csv(path, sep="\s+", decimal=",")
print(data.head())

# TODO  Assign it to a variable called data and replace the first 3 columns by a proper datetime index
data["Yr"] = "19" + data["Yr"].astype(str)
data["Date"] = pd.to_datetime((data["Dy"].astype(str) + " " + data["Mo"].astype(str) + " " + data["Yr"].astype(str)))
data = data.drop(['Yr', 'Mo', 'Dy'], axis=1)
print(data.head())
# TODO Check if everything is okay with the data. Create functions to delete/fix rows with strange cases and apply them
data['loc4'] = np.where((data['loc4'] == "None"), 0, data['loc4'])
data['loc5'] = np.where((data['loc5'] == "nodata"), 0, data['loc5'])
data['loc9'] = np.where((data['loc9'] == "1.0k"), 0, data['loc9'])
data['loc10'] = np.where((data['loc10'] == "NONE"), 0, data['loc10'])
data['loc12'] = np.where((data['loc12'] == "-123*None"), 0, data['loc12'])
for col in data.columns[:(len(data.columns) - 1)]:
    data[col] = [str(x).replace(',', '.') for x in data[col]]
    data[col] = data[col].astype(float)


# TODO Write a function in order to fix date (this relate only to the year info) and apply it

# TODO Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns]
data.set_index(data.Date, inplace=True)
data.drop(['Date'], axis=1, inplace=True)

# TODO Compute how many values are missing for each location over the entire record
print(f'Values are missing for each location - \n{data.isna().sum()}')
# TODO Compute how many non-missing values there are in total

print(f'Non-missing values there are in total - {sum(data.notnull().sum().to_list())}')

# TODO Calculate the mean windspeeds of the windspeeds over all the locations and all the times

print(f'The mean windspeeds of the windspeeds over all the locations: \n{data.mean()}')

print(f'Average value for each date: \n{data.mean(axis=1)}')

# TODO Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days

print(data.describe())
loc_stats = pd.DataFrame({'min': data.min(), 'max': data.max(), 'mean': data.mean(), 'std': data.std()})
print(loc_stats)
# TODO Find the average windspeed in January for each location

print(f'The average windspeed in January for each location: \n{data.loc[data.index.month == 1].mean()}')

# TODO Downsample the record to a yearly frequency for each location
print(data.resample('A').mean().dropna().head())
# TODO Downsample the record to a monthly frequency for each location
print(data.resample('M').mean().dropna().head())

# TODO Downsample the record to a weekly frequency for each location
print(data.resample('W').mean().dropna().head())

# TODO Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 21 weeks


res = data.loc[(data.index.date > pd.to_datetime("1961-01-01")) & (data.index.date < pd.to_datetime("1961-05-29"))].resample('W').mean().dropna()
result_data = pd.DataFrame({'min': res.min(), 'max': res.max(), 'mean': res.mean(), 'std': res.std()})
print(result_data)