import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

monthlist=['all','january','february','march','april','may','june','july','august','september','october','november','december']

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
    city_list = ['chicago', 'new york city', 'washington']
    city = input("\nSelect a city: Chicago, New York City, or Washington \n")
    city = city.lower()
       
    while city not in city_list:
        city = input("\nSorry, that is invalid. Please select a valid city or type 'quit' to stop"+'\n' )
        city = city.lower()
        if city == 'quit':
            break    
                     
    
    # get user input for month (all, january, february, ... , june)
    month=input("\nWhich month would you like to filter on? All, January, February, March,...")
    month= month.lower()
    
    while month not in monthlist:
        month=input("\nSorry I didn't catch that. Enter All or a month like: Jan, Feb, Mar,...\n")
        month= month.lower()
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    daylist=['all','m','tu','w','th','f','sa','su']
    day=input("\nWhich day would you like to filter on? M, Tu, W,...")
    day= day.lower()
    
    while day not in daylist:
        day=input("\nSorry I didn't catch that. Enter a month like: Jan, Feb, Mar,...\n")
        day= day.lower()

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
    df['End Time'] = pd.to_datetime(df['End Time']) 
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name
    df['Start Hour'] = df['Start Time'].dt.hour
    df['Trip'] = df['Start Station']+" to "+ df['End Station']
    
    if month != 'all':
        df = df[df['Month']== monthlist.index(month)]
        
        
    if day != 'all':
        if day == 'm':
            day = 'Monday'
        elif day == 'tu':
            day = 'Tuesday'
        elif day == 'w':
            day = 'Wednesday'
        elif day == 'th':
            day = 'Thursday'
        elif day == 'f':
            day = 'Friday'
        elif day == 'sa':
            day = 'Saturday'
        elif day == 'su':
            day = 'Sunday'
        df = df[df['Day of Week']== day]
                
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("\nThe most common month is: "+monthlist[df['Month'].mode()[0]].capitalize())

    # display the most common day of week
    print("\nThe most common day of the week is: " + df['Day of Week'].mode()[0])    
    
    # display the most common start hour
    print("\nThe most common start hour is: " + str(df['Start Hour'].mode()[0]) + ":00")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("\nThe most common start station is: " + df['Start Station'].mode()[0])   

    # display most commonly used end station
    print("\nThe most common End station is: " + df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print("\nThe most common trip is: " + df['Trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("\nThe total travel time is: " + str(sum(df['Trip Duration']))+" minutes")

    # display mean travel time
    print("\nThe mean travel time is: " + str(sum(df['Trip Duration'])/len(df['Trip Duration']))+" minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("\n Count of User Groups: \n")
    print(df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' in df.columns:
        print("\n Count of User Groups: \n")
        print(df['Gender'].value_counts())
    
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("Most recent birth year: " + str(df['Birth Year'].max()))
        print("Earliest birth year: " + str(df['Birth Year'].min()))
        print("Most common birth year: " + str(df['Birth Year'].mode()[0]))

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
        
        raw_data = input("Would you like to see the raw data? Yes or No")
        raw_data = raw_data.lower()
        counter = 0
        while raw_data != 'no':
            print(df[counter:counter+5])
            counter += 5
            raw_data = input("Would you like to see more? Yes or No \n")
            raw_data = raw_data.lower()
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()