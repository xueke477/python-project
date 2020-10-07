import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply
        no month filter
        (str) day - name of the day of week to filter by, or "all" to apply
        no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs



    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if
    applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply
        no month filter
        (str) day - name of the day of week to filter by, or "all" to apply
        no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel.
    Output depends on month and day.

    Args:
        (str) month - name of the month to filter by, or "all"
        (str) day - name of the day of week to filter by, or "all"
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

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

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start = (df.value_counts('Start Station').idxmax())
    print('The Most Common Start Station: ' + most_common_start)
    # display most commonly used end station
    most_common_end = (df.value_counts('End Station').idxmax())
    print('The Most Common End Station: ' + most_common_end)
    # display most frequent combination of start station and end station trip
    most_common_route_start, most_common_route_end = (
        df.value_counts(['Start Station', 'End Station']).idxmax())
    trip_count = (df.value_counts(['Start Station', 'End Station'])
                  [(most_common_route_start, most_common_route_end)])
    print('The Most Common Route \n' +
          'Starts at: {}\n'.format(most_common_route_start) +
          'Ends at: {}\n'.format(most_common_route_end) +
          'Its total number of trips is {}'.format(trip_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum(skipna=True)
    print('The total travel time is {} seconds.'.format(total_time))

    # display mean travel time
    mean_time = df['Trip Duration'].mean(skipna=True)
    print('The mean travel time is {} seconds.'.format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
