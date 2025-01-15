from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# API Route: Fetch stock price
@app.route('/get_stock_price', methods=['GET'])
def get_stock_price():
    ticker = request.args.get('ticker', 'INFY')  # Default ticker: INFY
    exchange = request.args.get('exchange', 'NSE')  # Default exchange: NSE
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        price = float(soup.find(class_="rPF6Lc").text.strip()[1:].replace(",", ""))
        return jsonify({'ticker': ticker, 'exchange': exchange, 'price': price})
    except Exception as e:
        return jsonify({'error': 'Failed to fetch stock price', 'details': str(e)})

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)
