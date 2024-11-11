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
    _year = int(y)
    _month = int(m)
    _day = int(d)

    tar_date = datetime(_year, _month, _day)
    return tar_date

def find_city(long, lat):
    city = Point(long, lat)
    return city
    
def get_today_temperature(long, lat, tar_date):

    _city = Point(long, lat)
    _data = Daily(_city, tar_date, tar_date)
    _data = _data.fetch()

    # pull today's temp data and print it
    if not _data.empty:
        temp_today = _data['tavg'].iloc[0]    
        #print(f"Today's Temperature {temp_today}C")
        return temp_today
    else:
        return None
        #print("No data available for today.")
        #return None

# pull historical data and print it
def get_historical_temperatures(lat, long, in_date, tar_range):
    #generate dates for the range in years
    _city = Point(lat, long)
    years_back = int(tar_range)
    years_back+=1
    historical_dates = [in_date - timedelta(days=365 * i) for i in range(0, years_back)]
    
    historical_data = []
    
    for _date in historical_dates:
        _data = Daily(_city, _date, _date)
        _data = _data.fetch()
        
        if not _data.empty:
            _temp = _data['tavg'].iloc[0]
            historical_data.append((_date.date(), _temp))
        else:
            historical_data.append((_date.date(), 'No data'))
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





