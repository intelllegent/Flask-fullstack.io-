from flask import Flask, render_template
import requests


app = Flask(__name__)

API_URL = 'https://financialmodelingprep.com//api/v3/stock/real-time-price/{ticker}'


def fetch_price(ticker):
    data = requests.get(API_URL.format(ticker=ticker.upper()),
                        params={'apikey': 'demo'}).json()
    return data["price"]


@app.route('/stock/<ticker>')
def stock(ticker):
    price = fetch_price(ticker)
    return render_template('stock_quote.html', ticker=ticker.upper(), stock_price=price)


@app.route('/')
def home_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
