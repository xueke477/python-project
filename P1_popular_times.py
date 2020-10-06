import pandas as pd

filename = 'chicago.csv'

# load data file into a dataframe
df = pd.read_csv(filename)

# convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract hour from the Start Time column to create an hour column
df['hour'] = [x.hour for x in df['Start Time']]
# test = df.iloc[:][:5]
# print(type(test['hour']))
# print(test['hour'].values)
# print(test['hour'].index)
# print(test['hour'].mode()[0])
# print(test.groupby('hour')['hour'].count().index)

# find the most common hour (from 0 to 23)
popular_hour = df.groupby('hour')['hour'].count().idxmax()

print('Most Frequent Start Hour:', popular_hour)
