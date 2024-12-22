from binance.client import Client
import os

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

client = Client(API_KEY, API_SECRET, testnet=True)

def get_balance():
    balance = client.get_asset_balance(asset='USDT')
    return float(balance['free'])

def get_current_price(symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker['price'])

def place_market_order(symbol, quantity):
    order = client.order_market_buy(symbol=symbol, quantity=quantity)
    return order

def place_limit_order(symbol, quantity, price):
    order = client.order_limit_buy(symbol=symbol, quantity=quantity, price=str(price))
    return order

def place_stop_limit_order(symbol, quantity, stop_price, limit_price):
    order = client.order_stop_limit_buy(symbol=symbol, quantity=quantity, price=str(limit_price), stopPrice=str(stop_price))
    return order

def get_trade_history(symbol):
    trades = client.get_my_trades(symbol=symbol)
    return trades
