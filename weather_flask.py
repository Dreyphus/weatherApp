import pandas as pd
import weather_check
from flask import Flask, render_template, request

long_lat = {'longitute': [35.6895],
            'latitude': [139.6917]}

cities_df = pd.DataFrame(long_lat, index=['tokyo'])

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/submit', methods=['POST'])
def submit():
    year_input = request.form['user_input']
    month_input = request.form['month']
    day_input = request.form['day']

    city_check = request.form['city']

    #checks the data fram of cities for the city name provided   
    long = cities_df.loc[city_check]['longitute'] 
    lat = cities_df.loc[city_check]['latitude']
    #gets the date
    date = weather_check.make_date(year_input, month_input, day_input)

    today_temp = weather_check.get_today_temperature(long, lat, date)
    
    return render_template('result.html', result=today_temp)

if __name__ == '__main__':
    app.run(debug=True)
