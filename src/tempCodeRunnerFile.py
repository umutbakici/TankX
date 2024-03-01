import websocket
import json
import pprint
import time
import threading
from datetime import datetime

# Define the callback functions for WebSocket events
def on_open(ws):
    print(f"WebSocket opened for {ws.pair}")

def on_close(ws):
    print(f"WebSocket closed for {ws.pair}")

def on_message(ws, message):
    json_message = json.loads(message)
    
    with open(f"data/{ws.pair}.json", "a") as outfile:
        json.dump(json_message, outfile, indent=4)
        outfile.write('\n')
    pprint.pprint(json_message)
    time.sleep(1)

# Create and run the WebSocket client
def run_websocket_client(pair):
    SOCKET_URL = f"wss://stream.binance.com:9443/ws/{pair.lower()}@bookTicker"

    ws = websocket.WebSocketApp(SOCKET_URL, on_open=on_open, on_close=on_close, on_message=on_message)
    ws.pair = pair
    ws.run_forever()

if __name__ == "__main__":
    with open('data/selected_trading_pairs.json', 'r') as file:
        trading_pairs_list = json.load(file)
    
    threads = []
    for pair in trading_pairs_list:
        thread = threading.Thread(target=run_websocket_client, args=(f"{pair['base_asset']}{pair['quote_asset']}",))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
