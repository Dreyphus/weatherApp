
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('templates/input.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get the data from the form
    user_input = request.form['user_input']
    
    # Process the data (example: convert input to uppercase)
    processed_input = user_input.upper()
    
    # Render a response page showing the processed data
    return render_template('result.html', result=processed_input)

if __name__ == '__main__':
    app.run(debug=True)

