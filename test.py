print('JAnuary'.title())

"""
import pandas as pd

test = pd.read_csv('washington.csv')

df = test[:][:10]
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['month'] = df['Start Time'].dt.month_name()
df['day_of_week'] = df['Start Time'].dt.day_name()
df['hour'] = df['Start Time'].dt.hour

print(df.columns)
print(type(df.iloc[0, :-3]))
print(df.iloc[0, :-3])
# print(df)
# print(type(df.value_counts('User Type')))
"""
"""
print('The counts of user types is the following:')
print(df.value_counts('User Type'))
def prompt_interaction():
    print('Would you like to see the next set of statistics? Enter y or n.')
    command = input()
    while command not in ['y', 'n']:
        print('Please enter y or n.')
    if command == 'n':
        break


while True:
    prompt_interaction()
    print('Next.')

    restart = input('\nWould you like to restart? Enter y or n.\n')
    if restart.lower() != 'y':
        break

print('End')
"""
