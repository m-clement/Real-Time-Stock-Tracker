## Real Time Stock Tracker

### Overview
Real Time Stock Tracker is a web application that allows users to track stock prices in real-time. By entering a stock's ticker symbol, users can see the current price and the percentage change for the day. The app uses the `yfinance` library to fetch stock data and `Flask` to serve the application. This project was created by following the YouTube tutorial ["Real-Time Stock Price Tracker in Python"](https://www.youtube.com/watch?v=GSHFzqqPq5U) by NeuralNine.

### Installation and Setup
1. Ensure you have Python installed on your machine.
2. Install the required Python packages:
   - For Linux/macOS: 
     ```
     pip3 install Flask pandas yfinance
     ```
   - For Windows:
     ```
     pip install Flask pandas yfinance
     ```
3. Navigate to the `RealTimeStockTracker` directory.
4. Run the Flask application:
```
python app.py
```

### Usage
- On the main page, enter the ticker symbol of a stock you want to track.
- The application will display the current stock price and the percentage change for the day.
- You can add multiple stocks to track and remove any stocks from the display, or change the refresh timer.

### Contributing
If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.


