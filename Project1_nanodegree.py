import time
import pandas as pd
import numpy as np

CITY_DATA = { 'ch': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'w': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nTo view the available bikeshare data, kindly type:\n (ch) for Chicago\n (ny) for New York City\n (W) for Washington\n ').lower()
    while city not in ('ch','ny','w'):
        print('Invalid input')
        city = input('To view the available bikeshare data, kindly type:\n (ch) for\
                      Chicago\n The letter (ny) for New York City\n The letter (W) for Washington\n ').lower()
      
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january','february','march','april','may','june','all']
    month = input('\n\nTo filter {}\'s data by a particular month, please type the month name or all for not filtering by month:\
                             \n-January\n-February\n-March\n-April\n-May\n-June\n-All\n\n:'.format(city.title())).lower()
    
    while month not in months:
        print('Invalid input')
        month = input('\n\nTo filter {}\'s data by a particular month, please type the month name or all for not filtering by month:\
                             \n-January\n-February\n-March\n-April\n-May\n-June\n-All\n\n:'.format(city.title())).lower()

    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'sunday', 'all']
    day = input('\n\nTo filter {}\'s data by a particular day, please type the day name or all for not filtering by day:\
                             \n-monday\n-tuesday\n-wednesday\n-thursday\n-friday\n-saturday\n-sunday\n-All\n\n:'.format(city.title(),month.title())).lower()
    
    while day not in days:
        print('Invalid input')
        day = input('\n\nTo filter {}\'s data by a particular day, please type the day name or all for not filtering by day:\
                             \n-monday\n-tuesday\n-wednesday\n-thursday\n-friday\n-saturday\n-sunday\n-All\n\n:'.format(city.title(),month.title())).lower()


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
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    # load data file into a dataframe
    #df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]


    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]


    # TO DO: display the most common start hour
    df['hour'] =df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    
    
    print ("most common month is: ", popular_month)
    print ("most common day is: ", popular_day)
    print ("most common hour is: ", popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
   
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]


    # TO DO: display most frequent combination of start station and end station trip
    df['rout'] = df['Start Station'] + ' ' + df['End Station']
    
    popular_rout = df['rout'].mode()[0]
    
    
    print ("most commonly used start station is: ", popular_start_station)
    print ("most commonly used end station is: ", popular_end_station)
    print ("most frequent combination of start station and end station trip is: ", popular_rout)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

  # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    
    #trip duration in minute and second
    minute , second = divmod(total_duration , 60)
    
    # in hour and minutes
    hour, minute = divmod(minute,60)
    
    print(f"total travel time is {hour} hours, {minute} minutes, {second} seconds")

    # TO DO: display mean travel time
    
    average_duration = round(df['Trip Duration'].mean())
    mins , sec = divmod(average_duration , 60)
    
    
    #This filter prints the time in hours, mins, sec format if the mins exceed 60
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe average trip duration is {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nThe average trip duration is {mins} minutes and {sec} seconds.")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_counts = df['User Type'].value_counts()
    print("\ncounts of user types is: ",user_counts)
    
    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print("\ncounts of gender:\n",gender_counts)
    except:
        print("\nThere is no column \"Gender\" in this table")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common_Birth_year = df['Birth Year'].mode()[0]
        
        print(f"\nThe earliest birth year is {earliest}, The recent is {recent}, the common is {common_Birth_year} ")
        
    except:
        print("\nThere is no column \"Birth Year\" in this table")

       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def Display_Data(city):
    print("\nRaw data is available to check... \n")
    display_raw = input('To View the availbale first 5 raw data please type Yes if you want or No if you don\'t want \n').lower()
          
    while display_raw not in ('yes','no'):
          print("\nInvalid input")
          display_raw = input('To View the availbale first 5 raw data please type Yes if you want or No if you don\'t want \n').lower()
          
    while display_raw == 'yes':
        try:
          for chunk in pd.read_csv(CITY_DATA[city], index_col = 0 ,chunksize=5):
                print(chunk)
                display_raw = input('To View the availbale raw in chuncks of 5 rows type Yes if you want or No if you don\'t want \n').lower()
                if display_raw != 'yes':
                    print('Thank You')
                    break
          break

        except KeyboardInterrupt:
            print('Thank you.')
          
    
def main():
      while True:
            
            city, month, day = get_filters()
            df = load_data(city, month, day)
          
            Display_Data(city)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break


if __name__ == "__main__":
	main()
