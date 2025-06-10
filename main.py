from fastapi import FastAPI
# import GetWebSocketToken, user, market, order
import user, market, order
from dotenv import load_dotenv
import os

load_dotenv()

# Get PUBLIC_KEY and PRIVATE_KEY from .env
PUBLIC_KEY = os.getenv('PUBLIC_KEY')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')

#Get WebSocketToken
# WEBSOCKETTOKEN = GetWebSocketToken.get_token(PUBLIC_KEY, PRIVATE_KEY)

app = FastAPI()

# Get User Balance
@app.get("/user/balance")
async def get_balance():
    print(user.get_balance(PUBLIC_KEY, PRIVATE_KEY))
    
# Create Order
@app.get("/order/create/")
async def create_order(pair: str='', type: str='', volume: str = ''):
    # print(order.create_order(pair, type, volume))
    response = order.create_order(pair, type, volume)
    # print(response)
    return response
