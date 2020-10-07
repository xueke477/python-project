import pandas as pd

test = pd.read_csv('chicago.csv')

df = test.iloc[:][:15]
# print(df.columns)
# print(df)

"""
# most_common_route =
most_common_route_start, most_common_route_end = (
    df.value_counts(['Start Station', 'End Station']).idxmax())
print(most_common_route_start)
print(most_common_route_end)
trip_count = (df.value_counts(['Start Station', 'End Station'])
              [(most_common_route_start, most_common_route_end)])
print('The Most Common Route: \n' +
      'Starts at: {}\n'.format(most_common_route_start) +
      'Ends at: {}\n'.format(most_common_route_end) +
      'It has a total number of {} trips'.format(trip_count))
"""
df['Start Time'] = pd.to_datetime(df['Start Time'])

df['month'] = df['Start Time'].dt.month_name()
df['day_of_week'] = df['Start Time'].dt.day_name()
df['hour'] = df['Start Time'].dt.hour

month = 'all'
day = 'all'

if month == "all" and day == 'all':
        # display the most common month
        most_common_month = df.value_counts('month').idxmax()
        print('The Most Common Month: ' + most_common_month)
        # display the most common day of week
        most_common_day = (df.value_counts('day_of_week').idxmax())
        print('The Most Common Day: ' + most_common_day)
        # display the most common start hour
        most_common_hour = (df.value_counts('hour').idxmax())
        print('The Most Common Hour: ' + str(most_common_hour))
elif month == 'all' and day != 'all':
        # display the most common month
        most_common_month = df.value_counts('month').idxmax()
        print('The Most Common Month: ' + most_common_month)
        # display the most common start hour
        most_common_hour = (df.value_counts('hour').idxmax())
        print('The Most Common Hour: ' + str(most_common_hour))
elif month != 'all' and day == 'all':
        # display the most common day of week
        most_common_day = (df.value_counts('day_of_week').idxmax())
        print('The Most Common Day: ' + most_common_day)
        # display the most common start hour
        most_common_hour = (df.value_counts('hour').idxmax())
        print('The Most Common Hour: ' + str(most_common_hour))
else:
        # display the most common start hour
        most_common_hour = (df.value_counts('hour').idxmax())
