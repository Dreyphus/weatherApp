import pandas as pd
import weather_check
from flask import Flask, render_template, request, redirect, url_for
import dash
from dash import dcc, html
import plotly.graph_objects as go

long_lat = {'latitude': [53.3498, 51.5072, 48.8575, 35.6764, 40.7128, 28.6139, 25.2048, 39.9042],
            'longitude': [6.2603, 0.1276, 2.3514, 139.6500, 74.0060, 77.2088, 55.2708, 116.4074]}

cities_df = pd.DataFrame(long_lat, index=['dublin', 'london', 'paris', 'tokyo', 'new york', 'new delhi', 'dubai', 'beijing'])

app = Flask(__name__)

dash_app = dash.Dash(__name__, server=app, url_base_pathname='/dash/')

# place-holder array
historical_temp = []

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/submit', methods=['POST'])
def submit():
    # gather input
    year_input = request.form['user_input']
    month_input = request.form['month']
    day_input = request.form['day']
    city_check = request.form['city']
    range_input = request.form['range']

    # retrieve longitute and latitude for city name   
    _lat = cities_df.loc[city_check]['latitude'] 
    _long = cities_df.loc[city_check]['longitude']
    # gets the date
    tar_date = weather_check.make_date(year_input, month_input, day_input)

    today_temp = weather_check.get_today_temperature(_lat, _long, tar_date)
    global historical_temp
    historical_temp = weather_check.get_historical_temperatures(_lat, _long, tar_date, range_input)
    
    return render_template('result.html', result=today_temp, hist_result=historical_temp)

@dash_app.callback(
    dash.dependencies.Output('temp_plot', 'figure'),
    dash.dependencies.Input('dummy-input', 'value')
)

def update_graph(_):
    x_values = [point[0] for point in historical_temp]
    y_values = [point[1] for point in historical_temp]

    _fig = go.Figure(
        data=[go.Scatter(x=x_values, y=y_values, mode='markers+lines', marker=dict(size=8, color='blue'))],
        layout=go.Layout(title="Average temperatures over the selected period", xaxis_title="Year", yaxis_title="Temperatures")
    )
    return _fig

dash_app.layout = html.Div([
    dcc.Graph(id='temp_plot'),
    dcc.Input(id='dummy-input', style={'display': 'none'})
])

if __name__ == '__main__':
    app.run(debug=True)
