import GetWebSocketToken
from dotenv import load_dotenv
import os

load_dotenv()

# Get PUBLIC_KEY and PRIVATE_KEY from .env
PUBLIC_KEY = os.getenv('PUBLIC_KEY')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')

WEBSOCKETTOKEN = GetWebSocketToken.get_token(PUBLIC_KEY, PRIVATE_KEY)
print(WEBSOCKETTOKEN)