from fastapi import FastAPI
import GetWebSocketToken
from dotenv import load_dotenv
import os

load_dotenv()

# Get PUBLIC_KEY and PRIVATE_KEY from .env
PUBLIC_KEY = os.getenv('PUBLIC_KEY')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')

#Get WebSocketToken
WEBSOCKETTOKEN = GetWebSocketToken.get_token(PUBLIC_KEY, PRIVATE_KEY)

