# Importing required libraries
import yfinance as yf
from flask import request, render_template, jsonify, Flask

# Initializing the Flask app
app = Flask(__name__, template_folder='templates')

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch stock data based on the provided ticker symbol
@app.route('/get_stock_data', methods=['POST'])
def get_stock_data():
    # Get the ticker symbol from the request payload
    ticker = request.get_json()['ticker']
    # Fetch the stock data for the past 1 year using yfinance
    data = yf.Ticker(ticker).history(period='1y')
    # Return the current and opening price of the stock
    return jsonify({'currentPrice': data.iloc[-1].Close,
                    'openPrice': data.iloc[-1].Open})

# Running the Flask app
if __name__ == '__main__':
    app.run(debug=True)