import pandas as pd

test = pd.read_csv('chicago.csv')

df = test.iloc[:][:10]

df['Start Time'] = pd.to_datetime(df['Start Time'])

df['month'] = df['Start Time'].dt.month_name()
df['day_of_week'] = df['Start Time'].dt.day_name()
df['hour'] = df['Start Time'].dt.hour

month = 'all'
day = 'all'

if month == "all" and day == 'all':
        # display the most common month
        most_common_month = df.groupby('month')['month'].count().idxmax()
        print('The Most Common Month: ' + most_common_month)
        # display the most common day of week
        most_common_day = (df.groupby('day_of_week')['day_of_week']
                           .count().idxmax())
        print('The Most Common Day: ' + most_common_day)
        # display the most common start hour
        most_common_hour = (df.groupby('hour')['hour']
                           .count().idxmax())
        print('The Most Common Hour: ' + str(most_common_hour))
elif month == 'all' and day != 'all':
        # display the most common month
        most_common_month = df.groupby('month')['month'].count().idxmax()
        print('The Most Common Month: ' + most_common_month)
        # display the most common start hour
        most_common_hour = (df.groupby('hour')['hour']
                           .count().idxmax())
        print('The Most Common Hour: ' + str(most_common_hour))
elif month != 'all' and day == 'all':
        # display the most common day of week
        most_common_day = (df.groupby('day_of_week')['day_of_week']
                           .count().idxmax())
        print('The Most Common Day: ' + most_common_day)
        # display the most common start hour
        most_common_hour = (df.groupby('hour')['hour']
                           .count().idxmax())
        print('The Most Common Hour: ' + str(most_common_hour))
else:
        # display the most common start hour
        most_common_hour = (df.groupby('hour')['hour']
                           .count().idxmax())

