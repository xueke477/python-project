import pandas as pd

test = pd.read_csv('chicago.csv')

df = test.iloc[:][:10]
print(df.columns)
print(df)
# print(type(df.value_counts('User Type')))
# print(df.value_counts('User Type'))
# print(type(df['Trip Duration'][0]))
    # Display counts of user types
print('The counts of user types is the following:')
print(df.value_counts('User Type'))

# Display counts of genders
if 'Gender' in df.columns:
        print('The counts of user genders is the following:')
        print(df.value_counts('Gender'))

# Display earliest, most recent, and most common year of birth
if 'Birth Year' in df.columns:
        min_birth_year = df['Birth Year'].min()
        print('The earliest birth year is {}.'.format(min_birth_year))
        recent_birth_year = df['Birth Year'].max()
        print('The most recent birth year is {}'.format(recent_birth_year))
        common_birth_year = df.value_counts('Birth Year').idxmax()
        print('The most common birth year is {}'.format(common_birth_year))


"""
# display total travel time
total_time = df['Trip Duration'].sum(skipna=True)
print('The total travel time is {} seconds.'.format(total_time))

# display mean travel time
mean_time = df['Trip Duration'].mean(skipna=True)
print('The mean travel time is {} seconds.'.format(mean_time))
"""
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
"""
