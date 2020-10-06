import pandas as pd

df = pd.read_csv('chicago.csv')

test = df.iloc[:][:10]

test['Start Time'] = pd.to_datetime(test['Start Time'])

test['month'] = [x.month for x in test['Start Time']]
test['day_of_week'] = [x.weekday() for x in test['Start Time']]

print(test.loc[test['month'] == 4, ['Start Time', 'month', 'day_of_week']])

"""
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
print(CITY_DATA['Chicago'.lower()])

month = "march"
print(type(month))
print(month)

month = 3
print(type(month))
print(month)

month = month == 4
print(type(month))
print(month)

"""
