import json

def select_trading_pairs(trading_pairs_list, asset, count=25):
    selected_pairs = []
    for pair in trading_pairs_list:
        if pair['quote_asset'] == asset:
            selected_pairs.append(pair)
            if len(selected_pairs) >= count:
                break
    return selected_pairs

# Read trading pairs from JSON file
def read_trading_pairs_from_json(file_path):
    with open(file_path, 'r') as file:
        trading_pairs_list = json.load(file)
    return trading_pairs_list

# Read trading pairs from JSON file
trading_pairs_list = read_trading_pairs_from_json('data/binance_trading_pairs.json')

# Select 150 BTC-X pairs
btc_pairs = select_trading_pairs(trading_pairs_list, 'BTC')

# Select 150 ETH-X pairs
eth_pairs = select_trading_pairs(trading_pairs_list, 'ETH')

# Select BTC/ETH pair
btcth_pair = next((pair for pair in trading_pairs_list if pair['base_asset'] == 'BTC' and pair['quote_asset'] == 'ETH'), None)

# Add BTC/ETH pair to the selected pairs if it exists
selected_pairs = btc_pairs + eth_pairs
if btcth_pair:
    selected_pairs.append(btcth_pair)

# Write selected pairs to a new JSON file
def write_selected_pairs_to_json(selected_pairs, file_path):
    file_path=f"data/{file_path}"
    with open(file_path, 'w') as file:
        json.dump(selected_pairs, file, indent=4)

# Specify the file path for the output JSON file
output_file_path = 'selected_trading_pairs.json'

# Write selected pairs to the output JSON file
write_selected_pairs_to_json(selected_pairs, output_file_path)

print("Selected pairs have been saved to:", output_file_path)
