import pandas as pd
from datetime import datetime, timedelta
from meteostat import Point, Daily
import statistics

#city = Point(35.6895, 139.6917) # Tokyo

# get today's date
#year = input('What year do you need?')
#year = int(year)
#month = input('What month do you need?')
#month = int(month)
#day = input('What day do you need?')
#day = int(day)
#today = datetime(year, month, day)

# take the input and make it a date


# range for historical data
#years_back = 20
#historical_dates = [today - timedelta(days=365 * i) for i in range(1, years_back + 1)]


def make_date(y, m, d):
    year = int(y)
    month = int(m)
    day = int(d)

    date = datetime(year, month, day)
    return date

def find_city(long, lat):
    city = Point(long, lat)
    return city
    
def get_today_temperature(long, lat, date):
    
    city = Point(long, lat)
    print('PRINTING HERE')
    print(long)
    print(lat)
    data = Daily(city, date, date)
    data = data.fetch()

    # pull today's temp data and print it
    if not data.empty:
        temp_today = data['tavg'].iloc[0]    
        #print(f"Today's Temperature {temp_today}°C")
        return temp_today
    else:
        return None
        #print("No data available for today.")
        #return None

# pull historical data and print it
def get_historical_temperatures():
    historical_data = []
    
    for date in historical_dates:
        data = Daily(city, date, date)
        data = data.fetch()
        
        if not data.empty:
            temp = data['tavg'].iloc[0]
            historical_data.append((date.date(), temp))
        else:
            return None
            #print(f"No data available for {date.date()}")
    
    return historical_data


def get_avg_tmp(temps):
    h_tempsOnly = [index[1] for index in temps]

    return statistics.mean(h_tempsOnly)
    
def get_median_tmp(temps):
    h_tempsOnly = [index[1] for index in temps]

    return statistics.median(h_tempsOnly)
    

#print("Fetching today's and historical temperatures...\n")

#today_temp = get_today_temperature()
#h_temps = get_historical_temperatures()
#average_h_temp = get_avg_tmp(h_temps)
#print(f"Average temp on this date: {average_h_temp}")
#median_h_temp = get_median_tmp(h_temps)
#print(f"Median temp on this date: {median_h_temp}")





