import pandas as pd

test = pd.read_csv('chicago.csv')

df = test.iloc[:10, :]
# [:][:10]
print(df.columns)
print(df)
# print(type(df.value_counts('User Type')))

"""
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
