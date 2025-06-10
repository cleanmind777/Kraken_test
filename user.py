from kraken.spot import Earn, Funding, Market, Trade, User
from dotenv import load_dotenv
import os

load_dotenv()

# Get PUBLIC_KEY and PRIVATE_KEY from .env
PUBLIC_KEY = os.getenv('PUBLIC_KEY')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')

# def get_balance(public_key: str = "", private_key: str = "") -> str:
#     user = User(key=public_key, secret=private_key)
#     print(user.get_account_balance())

def get_balance():
    user = User(key=PUBLIC_KEY, secret=PRIVATE_KEY)
    print(user.get_account_balance())

if __name__ == "__main__":
    get_balance()