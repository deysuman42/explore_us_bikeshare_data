## TODO: import all necessary packages and functions
from datetime import datetime
import calendar
import time
import pandas as pd
pd.set_option('mode.chained_assignment', None)

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    flag = 1
    filename = None
    
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    
    while flag == 1:
     
      if city.lower() == 'chicago':
        filename = chicago
        flag = 0
      elif city.lower() == 'new york':
        filename = new_york_city
        flag = 0
      elif city.lower() == 'washington':
        filename = washington
        flag = 0
      else:
        city = input('You have selected a wrong City : Choose among: Chicago/New York/Washington\n') 
        flag = 1
        
    return filename
    
def get_time_period():
    
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str) return the filter condition for data i.e month / day / none
    '''
    flag = 1
    
    time_period = input('\nWould you like to filter the data by month, day, or none?'
                        'Type "none" for no time filter.\n')
    while flag == 1:
      if time_period.lower() == 'month':
        flag = 0
        return time_period.lower()
      elif time_period.lower() == 'day':
        flag = 0
        return time_period.lower()
      elif time_period.lower() == 'none':
        flag = 0
        return time_period.lower()
      else:
        flag = 1
        time_period = input('\Invalid response- Please enter either month/day or none\n')
    
        

def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        (str) return the specified month based on the input 
    '''

    flag = 1
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    
    while flag == 1:
      if month.lower() == 'january':
        flag = 0
        return 'january'
      elif month.lower() == 'february':
        flag = 0
        return 'february'
      elif month.lower() == 'march':
        flag = 0
        return 'march'
      elif month.lower() == 'april':
        flag = 0
        return 'april'
      elif month.lower() == 'may':
        flag = 0
        return 'may'
      elif month.lower() == 'june':
        flag = 0
        return 'june'
      else:
        flag = 1
        month = input('\nPlease enter a valid month.\n')
   
def get_day(month):
  
  
    '''Asks the user for a day and returns the specified day.

    Args:
        month.
    Returns:
        (str) return the day of the month based on the date entered by the user and the month passed as argument
    '''

    flag = 1
    day = input('\nWhich day? Please type your response as an integer.\n')
    
    month_value = None

    while flag == 1:
      if month.lower() == 'january':
        if int(day) > 31:
          day = input('\nPlease enter a day between 1 and 31\n')
          flag = 1
        else:
          month_value = '01'
          flag = 0
      elif month.lower() == 'february':
        if int(day) > 28:
          day = input('\nPlease enter a day between 1 and 28\n')
          flag = 1
        else:
          month_value = '02'
          flag = 0
      elif month.lower() == 'march':
        if int(day) > 31:
          day = input('\nPlease enter a day between 1 and 31\n')
          flag = 1
        else:
          month_value = '03'
          flag = 0
      elif month.lower() == 'april':
        if int(day) > 30:
          day = input('\nPlease enter a day between 1 and 30\n')
          flag = 1
        else:
          month_value = '04'
          flag = 0
      elif month.lower() == 'may':
        if int(day) > 31:
          day = input('\nPlease enter a day between 1 and 31\n')
          flag = 1
        else:
          month_value = '05'
          flag = 0
      elif month.lower() == 'june':
        if int(day) > 30:
          day = input('\nPlease enter a day between 1 and 30\n')
          flag = 1
        else:
          month_value = '06'
          flag = 0  
    #Returning the day name of the Week
    return int(day)
   

def get_and_filter_data(city_file, time_period, month, day):

     '''Args:
        city file name , time_period, month and day
     Returns:
       (Dataframe) returns a filtered dataframe based on the filter conditions
     '''
     df_filter = pd.read_csv(city_file)
     df_filter['months'] =  pd.DatetimeIndex(df_filter['Start Time']).month
     df_filter['months'] = df_filter['months'].apply(lambda x: calendar.month_abbr[x])
     df_filter['days'] = pd.DatetimeIndex(df_filter['Start Time']).day
     df_filter['weekdays'] = pd.DatetimeIndex(df_filter['Start Time']).weekday
     df_filter['hours'] = pd.DatetimeIndex(df_filter['Start Time']).hour
      
     if time_period.lower() == 'month':
        month_filter = month[0].upper() + month[1:3]
        df_month = df_filter.loc[df_filter['months'] == month_filter]
        return df_month
     elif time_period.lower() == 'day':
        month_filter = month[0].upper() + month[1:3]
        df_month = df_filter.loc[df_filter['months'] == month_filter]
        df_day = df_month.loc[df_month['days'] == day]
        return df_day
     elif time_period.lower() == 'none':
        return df_filter
        
   
def popular_month(df):
    '''Args:
        dataframe.
    Returns:
      (str)  returns the most popular month for 'Start Time' .
    '''
    
    month_value = df['months'].value_counts().idxmax()
    if month_value == 'Jan':
      most_popular_month = 'January'
    elif month_value == 'Feb':
      most_popular_month = 'February'
    elif month_value == 'Mar':
      most_popular_month = 'March'
    elif month_value == 'Apr':
      most_popular_month = 'April'
    elif month_value == 'May':
      most_popular_month = 'May'
    elif month_value == 'Jun':
      most_popular_month = 'June'
    
    message = "The most popular month for start time is " + most_popular_month
    return message 
 
def popular_day(df):
    '''Args:
        dataframe.
    Returns:
        (str) returns the most popular day for 'Start Time' .
    '''
    day_value = df['weekdays'].value_counts().idxmax()
    
    most_popular_day = "The most popular day of the week for start time is " + calendar.day_name[day_value]
   
    return most_popular_day 
  
  
def popular_hour(df):
       
    '''Args:
        dataframe.
    Returns:
     returns the most popular hour of the day for 'Start Time' of that particular file.
    '''
    
    hour_value = df['hours'].value_counts().idxmax()
    most_popular_hour = "The most popular hour of the day for start time is " + str(hour_value) + '00' + ' hours'
    
    return most_popular_hour
  

def trip_duration(df):
    
    '''Args:
        city file and 'Trip Duration' column.
    Returns:
        (str) returns the total trip duration and average trip duration of that particular file.
    '''
    total_trip_duration = df['Trip Duration'].sum()
    avg_trip_duration = df['Trip Duration'].mean()
    
    trip_duration = "The total trip duraton is " + time.strftime("%H:%M:%S", time.gmtime(total_trip_duration)) + " and average trip duration is " +  time.strftime("%H:%M:%S", time.gmtime(avg_trip_duration))   
    
    return trip_duration
   


def popular_stations(df):
    '''Args:
        city file and 'Trip Duration' column.
    Returns:
      (str)  returns the most popular start station and most popular end station of that particular file.
    '''
    start_station = df['Start Station'].value_counts().idxmax()
    end_station = df['End Station'].value_counts().idxmax()
    
    popular_station = "The most popular start station is " + start_station + " and most popular end station is " + end_station
    
    return popular_station


def popular_trip(df):
    '''Args:
        city file 
    Returns:
       (str) returns the most popular trip of that particular file.
    '''
    df['popular_trip'] = df['Start Station'] + " " + "to" + " " +  df['End Station']
    popular_trip_value = "The most popular trip is " + df['popular_trip'].value_counts().idxmax()
    
    return popular_trip_value
    # TODO: complete function


def users(df):
    '''Args:
        city file , user type
    Returns:
        (int) returns the counts of each user type of that particular file.
    '''
    return df['User Type'].value_counts()


def gender(df):
    '''Args:
        city file , gender count
    Returns:
        (int) returns the gender count  of that particular file.
    '''
    
    return df['Gender'].value_counts()


def birth_years(df):
    '''Args:
        city file , 'Birth Year'
    Returns:
        (str) returns the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years.
    '''
    oldest_user = df['Birth Year'].min()
    youngest_user = df['Birth Year'].max()
    most_popular_user = df['Birth Year'].value_counts().idxmax()
    birth_year = "The oldest user year of birth is " + str(int(oldest_user)) + " , the youngest user year of birth is " +  str(int(youngest_user)) + " and the most popular user year of birth is " + str(int(most_popular_user))
    
    return birth_year
  


def display_data(df):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        city.
    Returns:
        5 rows at a time of the file's data
    '''
    df_day = df[df.columns[:-4]]
    df_day = df_day.reset_index(drop=True)
  
    display = input('\nWould you like to view the individual trip data with firt 5 rows?'
                    'Type \'yes\' or \'no\'.\n')
    if display.lower() == 'yes':
      print(df_day.loc[0:4])
      row_n = 5
      display = 'yes'
      while display.lower() == 'yes':
        display = input('\nWould you like to view the next 5 rows?'
                    'Type \'yes\' or \'no\'.\n')
        if display.lower() == 'yes':
          print(df_day.loc[row_n:row_n + 4])
          row_n += 5 
        else:
          print('Thank You \n')
    else:
      print('Thank You\n')
    
    
def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    if time_period == 'month':
      month = get_month()
      day = 'none'
    elif time_period == 'day':
      month = get_month()
      day = get_day(month)
    elif time_period == 'none':
      month = 'none'
      day = 'none'
      
    df = get_and_filter_data(city, time_period, month, day)
    print('Calculating the first statistic...')

     
    
    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()
        print(popular_month(df))
        #TODO: call popular_month function and print the results
        
        
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        print(popular_day(df))
        # TODO: call popular_day function and print the results
        
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")    

    start_time = time.time()
         
    
    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
    
    print(popular_hour(df))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()
    

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    print(trip_duration(df))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()
    
    print(popular_stations(df))
 
    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()
    
    print(popular_trip(df))

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()
    
    print(users(df))

    # What are the counts of each user type?
    # TODO: call users function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()
    
    if city == washington:
      print('Washington file doesnt have gender data')
    else:
      print(gender(df))

    # What are the counts of gender?
    # TODO: call gender function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()
    if city == washington:
      print('Washington file doesnt have Birth years data')
    else:
      print(birth_years(df))

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results

    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data(df)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()

if __name__ == "__main__":
  statistics()
    
    
    
