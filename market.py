from kraken.spot import Earn, Funding, Market, Trade, User
from dotenv import load_dotenv
import os

# load_dotenv()

# # Get PUBLIC_KEY and PRIVATE_KEY from .env
# PUBLIC_KEY = os.getenv('PUBLIC_KEY')
# PRIVATE_KEY = os.getenv('PRIVATE_KEY')

# # For Fast API
def get_assets(symbols, public_key, private_key):
    market = Market(key=public_key, secret=private_key)
    return (market.get_assets(assets = symbols))

def get_ticker(symbols, public_key, private_key):
    market = Market(key=public_key, secret=private_key)
    return (market.get_ticker(pair = symbols))

# For Local test
# def get_assets(symbols):
#     market = Market(key=PUBLIC_KEY, secret=PRIVATE_KEY)
#     print(market.get_assets(assets = symbols))

# def get_asset_pairs(symbols):
#     market = Market(key=PUBLIC_KEY, secret=PRIVATE_KEY)
#     print(market.get_ticker(pair = symbols))
    
# if __name__ == "__main__":
#     symbols = ['SOL']
#     get_assets(symbols)
#     symbols = ['SOLUSDT']
#     get_asset_pairs(symbols)