from kraken.spot import Earn, Funding, Market, Trade, User
from dotenv import load_dotenv
import os

# load_dotenv()

# # Get PUBLIC_KEY and PRIVATE_KEY from .env
# PUBLIC_KEY = os.getenv('PUBLIC_KEY')
# PRIVATE_KEY = os.getenv('PRIVATE_KEY')

# # # For Fast API
def create_order(ordertype: str='', side: str='', pair: str='', volume: str='', public_key: str='', private_key: str=''):
    trade = Trade(key=public_key, secret=private_key)
    return (trade.create_order(
        pair = pair,
        ordertype = ordertype,
        side = side,
        volume = volume
    ))

# For Local test
# def create_order(ordertype: str='', side: str='', pair: str='', volume: str=''):
#     trade = Trade(key=PUBLIC_KEY, secret=PRIVATE_KEY)
#     print(trade.create_order(
#         pair = pair,
#         ordertype = ordertype,
#         side = side,
#         volume = volume
#     ))

    
# if __name__ == "__main__":
#     ordertype = 'market'
#     side = 'buy'
#     pair = 'SOLUSDT'
#     volume = '0.1'
#     create_order(ordertype, side, pair, volume)
