from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    
    processed_input = user_input.upper()
    
    return render_template('result.html', result=processed_input)

if __name__ == '__main__':
    app.run(debug=True)

