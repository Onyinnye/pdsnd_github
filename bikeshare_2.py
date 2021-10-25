import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
             
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities = ['chicago', 'new york city', 'washington']
        city = input("What city would you want to explore? (chicago, new york city or washington?)\n").lower()
        if city in cities:
            break
        else:
            print("Sorry we don't have that data!")
   
    # get user input for month (all, january, february, ... , june)
    while True:
        months = ('all','january','february','march','april','may','june')
        month = input("what month would you like to explore? (january, february, march, april, may, june or all?):\n").lower()
        if month in months:
            break
        else:
            print("This is not a month!")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday')
        day = input("What day would you like to explore? (monday, tuesday, wednesday, thursday, friday, saturday,sunday or all?):\n").lower()
        if day in days:
            break
        else:
            print("oh dear!, this is not a day")



    print('-'*40)
    return city, month, day



def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time']) ##converts start time to datetime
    df['month'] = df['Start Time'].dt.month ##creates a month column
    df['day_of_week'] = df['Start Time'].dt.day_name() ##creates a day of week column
    df['start_hour'] = df['Start Time'].dt.hour #creates the start hour

    if month != 'all':## individual month selection
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
        df = df[df['month']==month]
    if day != 'all':## selecting day of week
        df = df[df['day_of_week']==day.title()]








    return df

def display_data(df):
    ''' This displays 5 lines of the dataset as the users chooses'''
    input_data=input("\nWould you like to view the first five lines of this dataset?yes/no\n").lower()
    start_loc = 0
    while input_data == 'yes':
        start_loc += 5 
        print(df.iloc[start_loc-5:start_loc, : ])
        
        input_data = input("Do you wish to see the next five?\n").lower()
 

def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == 'all':
        print("The most common month is:\n{}".format(df['month'].value_counts().idxmax()))

    # display the most common day of week
    if day == 'all':
        print("The most common day of the week is:\n{}".format(df['day_of_week'].value_counts().idxmax()))

    # display the most common start hour
    print("The most common start hour is:\n{}".format(df['start_hour'].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station is:\n{}".format(df['Start Station'].value_counts().idxmax()))

    # display most commonly used end station
    print("The most commonly used end station is:\n{}".format(df['End Station'].value_counts().idxmax()))

    # display most frequent combination of start station and end station trip
    most_frequent_combo = df.groupby(["Start Station", "End Station"]).size().sort_values(ascending= False)
    print("The most frequent combination is:\n{}".format(most_frequent_combo.head(1)))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time is:\n{}".format(df['Trip Duration'].sum()))


    # display mean travel time
    print("Average travel time is:\n{}".format(df['Trip Duration'].mean()))

    # display min travel time
    print("Minimum travel time is:\n{}".format(df['Trip Duration'].max()))

    # display max travel time
    print("Maximum travel time is:\n{}".format(df['Trip Duration'].max()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("The user types are \n{}".format(df['User Type'].value_counts()))

    # Display counts of gender
    if 'Gender' in df.columns:
        print("There are \n{}".format(df['Gender'].value_counts()))

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("The earliest birth year is:\n{}".format(int(df['Birth Year'].min())))
        print("The most recent birth year is:\n{}".format(int(df['Birth Year'].max())))
        print("The most common birth year is:\n{}".format(int(df['Birth Year'].value_counts().idxmax())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city,month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
