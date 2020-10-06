import pandas as pd

filename = 'chicago.csv'

# load data file into a dataframe
df = pd.read_csv(filename)

# convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])
print(type(df['Start Time'][:2]))
print(df['Start Time'][:2])
print([x.hour for x in df['Start Time'][:2]])
# print(df['Start Time'][:2].hour)
# print(type(df['Start Time'][:2].hour))

# extract hour from the Start Time column to create an hour column
# df['hour'] =

# find the most common hour (from 0 to 23)
# popular_hour =

# print('Most Frequent Start Hour:', popular_hour)
