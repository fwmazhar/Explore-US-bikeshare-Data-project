
import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

day=""
month=""
df=""
city=''
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    global day
    global month
    global city
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city=input("Please select a city you want to see the data for Chicago, New york city or Washington : ").lower()
        if city == 'chicago' or city == 'new york city'  or city == 'washington':
            break
        else:
            print("Please enter a valid input: ")

    # get user input for month (all, january, february, ... , june)
    while True:
        ask_2=input("Would you like to filer data by month, day or not at all ? Type none for no time filter ").lower()
        if ask_2 == 'month' or ask_2 =='day' or ask_2 =='none':
            break
        else:
            print("Please enter a vaild input ")
            continue

    if ask_2 == 'month':
        day='none'
        while True:

            ask=input("do you want to see the data of a specifc month or do you want all the months : Type any letter to get a specific month  or type all : ").lower()
            if ask == 'all':
                month="all"
                break
            else:
                month=input("which month? January, Februray, March, April, May or june : ").lower()

                if month == 'january' or month == 'februray'  or month == 'march' or month == 'april' or month == 'may' or month == 'june' :
                    break
                else:
                    print("Please enter a valid input: ")
    elif ask_2 =='day':
        month='none'
        while True:
            ask_3=input("do you want to see the data of a specifc day or do you want all the days : Type any letter to get a specific day or type all : ").lower()
            if ask_3 == 'all':
                day="all"
                break
            else:
                day=input("which day? saturday, sunday, monday, tuesday, wednesday, thursday or friday ,saturday will be the start of the week ie. saturday = 0  and so on  : ").lower()
                if day == 'saturday' or day == 'sunday'  or day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' :
                    break
                else:
                    print("Please enter a valid input: ")

    elif ask_2 == "none":
        month='none'
        day='none'

    
    # get user input for day of week (all, monday, tuesday, ... sunday)

    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    global df
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    if month == 'none' and day =='none':
        df = pd.read_csv(CITY_DATA[city])
    elif month != 'none' and day =='none':
        df = pd.read_csv(CITY_DATA[city])
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        if month != 'all':
            # use the index of the months list to get the corresponding int
            months = ['january', 'februray', 'march', 'april', 'may', 'june']
            month = months.index(month)+1
        
            # filter by month to create the new dataframe
            df = df[df['month'] == month]

    elif month == 'none' and day !='none':
        df = pd.read_csv(CITY_DATA[city])
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['day_of_week'] =df['Start Time'].dt.weekday

        if day != 'all':
            # filter by day of week to create the new dataframe
            days=['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday' , 'friday']
            day = days.index(day)
            df = df[df['day_of_week'] == day]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    if month == 'all' or (month =='none' and day == 'none') :
        df['Start Time'] =pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        common_month = df['month'].value_counts().idxmax()
        count_1=df['month'].value_counts()[common_month]
        print('Most common month:', common_month)
        print('count: ' ,count_1)

    
    # display the most common day of week

    if day == 'all' or (month=='none' and day == 'none'):
        df['Start Time'] =pd.to_datetime(df['Start Time'])
        df['day'] = df['Start Time'].dt.day
        common_day = df['day'].value_counts().idxmax()
        count_2=df['day'].value_counts()[common_day]
        print('Most common day of week:', common_day)
        print('count: ' ,count_2)
    


    # display the most common start hour

    df['Start Time'] =pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].value_counts().idxmax()
    count_3=df['hour'].value_counts()[common_hour]
    print('Most Frequent Start Hour:', common_hour)
    print('count: ' ,count_3)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_commonly_start=df['Start Station'].value_counts().idxmax()
    count_4=df['Start Station'].value_counts()[most_commonly_start]
    print('Most commonly used start station :', most_commonly_start)
    print('count: ',count_4)
    # display most commonly used end station
    most_commonly_end=df['End Station'].value_counts().idxmax()
    count_5=df['End Station'].value_counts()[most_commonly_end]
    print('Most commonly used end station :', most_commonly_end)
    print('count: ',count_5)
    # display most frequent combination of start station and end station trip
    #here i have used groupby operation which involves some combination of splitting the object, applying a function, and combining the results.

    most_frequent_comb=df.groupby(['Start Station','End Station']).size().nlargest(1)
    print('Most frequent combination of start and end stations trip \n :', most_frequent_comb)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("Total travel time: ",total_travel_time)

    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print("mean travel time: ",mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if city == 'chicago' or city == 'new york city':
        gender_count=df['Gender'].value_counts()
        print(gender_count)

    # Display earliest, most recent, and most common year of birth
    if city == 'chicago' or city == 'new york city':
        most_earliest=df['Birth Year'].min()
        print("Most earliest birth year: ",most_earliest)
        
        most_recent=df['Birth Year'].max()
        print("Most recent birth year: ",most_recent)
        most_common_year=df['Birth Year'].value_counts().idxmax()
        print("Most common year of birth: ",most_common_year)

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
        counts=0
        inc=5
        while True:
            ans=input('Would you like to see 5 lines of raw data, answer with yes or no : ').lower()
            if ans =='yes':
                df = pd.read_csv(CITY_DATA[city])
                print(df[counts:inc])
                counts+=5
                inc+=5
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
