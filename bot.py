import logging
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bot_activity.log"),
        logging.StreamHandler()
    ]
)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        # We initialize without 'testnet=True' inside the constructor 
        # to avoid the automatic Spot Testnet ping.
        self.client = Client(api_key, api_secret)
        
        if testnet:
            # Manually override the URLs to point specifically to Futures Testnet
            self.client.API_URL = 'https://testnet.binancefuture.com/fapi'
            self.client.testnet = True
        
        logging.info("Bot initialized and configured for Futures Testnet.")

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            symbol = symbol.upper().strip() # .strip() removes accidental spaces
            params = {
                'symbol': symbol,
                'side': side.upper().strip(),
                'type': order_type.upper(),
                'quantity': float(quantity), # Ensure quantity is a number
            }

            if order_type.upper() == ORDER_TYPE_LIMIT:
                params['price'] = price
                params['timeInForce'] = TIME_IN_FORCE_GTC
            
            # The corrected condition for Stop-Limit
            elif order_type.upper() == "STOP":
                params['price'] = price
                params['stopPrice'] = stop_price
                params['timeInForce'] = TIME_IN_FORCE_GTC

            logging.info(f"Sending Order: {params}")
            response = self.client.futures_create_order(**params)
            return response

        except Exception as e:
            logging.error(f"Execution Error: {e}")
            return None

def run_cli():
    print("--- Binance Futures Testnet Bot ---")
    api_key = input("Enter API Key: ")
    api_secret = input("Enter API Secret: ")
    
    bot = BasicBot(api_key, api_secret)

    while True:
        print("\n[1] Market Order [2] Limit Order [3] Stop-Limit [4] Exit")
        choice = input("Select Option: ")

        if choice == '4': break

        symbol = input("Symbol (e.g., BTCUSDT): ")
        side = input("Side (BUY/SELL): ")
        qty = input("Quantity: ")

        if choice == '1':
            bot.place_order(symbol, side, ORDER_TYPE_MARKET, qty)
        elif choice == '2':
            price = input("Limit Price: ")
            bot.place_order(symbol, side, ORDER_TYPE_LIMIT, qty, price=price)
        elif choice == '3':
            stop_p = input("Stop Price: ")
            limit_p = input("Limit Price: ")
            bot.place_order(symbol, side, FUTURE_ORDER_TYPE_STOP_LIMIT, qty, price=limit_p, stop_price=stop_p)

if __name__ == "__main__":
    run_cli()