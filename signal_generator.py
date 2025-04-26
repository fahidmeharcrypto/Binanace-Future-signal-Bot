import requests
import random

# Binance Futures public API endpoint
BINANCE_API_URL = 'https://fapi.binance.com/fapi/v1/ticker/price'

# Top trading pairs list
PAIRS = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'XRPUSDT', 'SOLUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT']

def get_live_prices():
    try:
        response = requests.get(BINANCE_API_URL)
        data = response.json()
        prices = {}
        for item in data:
            if item['symbol'] in PAIRS:
                prices[item['symbol']] = float(item['price'])
        return prices
    except Exception as e:
        print(f"Error fetching live prices: {e}")
        return {}

def generate_signals():
    prices = get_live_prices()
    signals = {}
    for pair, price in prices.items():
        signal = random.choice(['LONG', 'SHORT'])
        stop_loss = round(price * (0.98 if signal == 'LONG' else 1.02), 2)
        take_profit = round(price * (1.02 if signal == 'LONG' else 0.98), 2)
        
        signals[pair] = {
            'entry_price': price,
            'signal': signal,
            'stop_loss': stop_loss,
            'take_profit': take_profit
        }
    return signals
