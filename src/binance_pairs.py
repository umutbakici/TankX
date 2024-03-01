import requests
import json

def get_all_trading_pairs():
    url = "https://api.binance.com/api/v3/exchangeInfo"
    response = requests.get(url)
    data = response.json()
    
    trading_pairs = []

    if 'symbols' in data:
        for symbol in data['symbols']:
            trading_pairs.append((symbol['baseAsset'], symbol['quoteAsset']))
    
    return trading_pairs

def append_trading_pairs_to_json(trading_pairs, file_path):
    pairs_list = [{"base_asset": pair[0], "quote_asset": pair[1]} for pair in trading_pairs]
    file_path=f"data/{file_path}"
    with open(file_path, 'w') as file:
        json.dump(pairs_list, file, indent=4)

# Get all trading pairs from Binance
all_pairs = get_all_trading_pairs()

# Append the pairs to a JSON file
append_trading_pairs_to_json(all_pairs, 'binance_trading_pairs.json')
