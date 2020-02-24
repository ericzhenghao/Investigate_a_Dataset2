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
    def input_mod(input_print,error_print,enterable_list):
        ret = input(input_print).lower()
        while ret not in enterable_list:
            ret = input(error_print).lower()
        return ret
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input_mod('Please input the city name:',
              'Error!Please input the correct city name.',
              ['chicago','new york city','washington'])
   


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input_mod('Please input the month:',
              'Error!Please try other monthes.',
              ['all','january','february','march','april','may','june'])
    
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input_mod('Please input the day of week:',
              'Error!Please input the right day of week.',
              ['all', 'monday', 'tuesday','wednesday','thurday ','saturday','sunday'])
    def input_mod(input_print,error_print,enterable_list):
        ret = input(input_print).lower()
        while ret not in enterable_list:
            ret = input(error_print).lower()
        return ret
    

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    if month != 'all':
        month_option = ['january', 'february', 'march', 'april', 'may', 'june']
        month_int = month_option.index(month) + 1
        df = df[df['month'] == month_int]

    df['day'] = df['Start Time'].dt.weekday
    if day != 'all':
        day_option = [ 'monday', 'tuesday','wednesday','thurday ','friday','saturday','sunday']
        day_int = day_option.index(day)
        df = df[df['day'] == day_int]    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print(df.head())
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is:', common_month)

    # TO DO: display the most common day of week
    common_day_week = df['day'].mode()[0]
    print('The most common month is:', common_day_week)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour 
    common_start = df['hour'].value_counts().index[0]
    print('Most commonly used start station: ',common_start)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].value_counts().index[0]
    print('\nMost commonly used start station: \n',common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].value_counts().index[0]
    print('\nMost commonly used end station:\n',common_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station']+'/ '+df['End Station']
    common_combine = df['combination'].value_counts().index[0]
    print('\nMost frequent combination of start and end station trip: \n',common_combine)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('\nTotal travel time:\n ',total_time)


    # TO DO: display mean travel time
    mean_time=df['Trip Duration'].mean()
    print('\nMean travel time:\n ',mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nThe results of counts of user types is:\n",user_types)

    # TO DO: Display counts of gender
    cities_columns = df.columns
    if 'Gender' in cities_columns:
        user_gender = df['Gender'].value_counts()
        print('Male:\n',user_gender.loc['Male'],'\nFemale:\n',user_gender.loc['Female'])
    else:
        print("Sorry, this city don't have gender data." )


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in cities_columns:
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common =  df['Birth Year'].mode()[0]
        print("\nearliest of birth is:\n", earliest)
        print("\nmost recent of birth is:\n", recent)
        print("\nmost common year of birth is:\n", common)
    else:
        print("Sorry, this city don't have birth year data." )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
