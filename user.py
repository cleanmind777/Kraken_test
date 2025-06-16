# Get all asset balances.

import http.client
import urllib.request
import urllib.parse
import hashlib
import hmac
import base64
import json
import time

from dotenv import load_dotenv
import os

load_dotenv()

# # Get PUBLIC_KEY and PRIVATE_KEY from .env
PUBLIC_KEY = os.getenv('USER_PUBLIC_KEY')
PRIVATE_KEY = os.getenv('USER_PRIVATE_KEY')

def get_balance():
   response = request(
      method="POST",
      path="/0/private/Balance",
      public_key=PUBLIC_KEY,
      private_key=PRIVATE_KEY,
      environment="https://api.kraken.com",
   )
#    return(response.read().decode())
   response = json.loads(response.read().decode('utf-8'))
   return(response)

def request(method: str = "GET", path: str = "", query: dict | None = None, body: dict | None = None, public_key: str = "", private_key: str = "", environment: str = "") -> http.client.HTTPResponse:
   url = environment + path
   query_str = ""
   if query is not None and len(query) > 0:
      query_str = urllib.parse.urlencode(query)
      url += "?" + query_str
   nonce = ""
   if len(public_key) > 0:
      if body is None:
         body = {}
      nonce = body.get("nonce")
      if nonce is None:
         nonce = get_nonce()
         body["nonce"] = nonce
   headers = {}
   body_str = ""
   if body is not None and len(body) > 0:
      body_str = json.dumps(body)
      headers["Content-Type"] = "application/json"
   if len(public_key) > 0:
      headers["API-Key"] = public_key
      headers["API-Sign"] = get_signature(private_key, query_str+body_str, nonce, path)
   req = urllib.request.Request(
      method=method,
      url=url,
      data=body_str.encode(),
      headers=headers,
   )
   return urllib.request.urlopen(req)

def get_nonce() -> str:
   return str(int(time.time() * 1000))

def get_signature(private_key: str, data: str, nonce: str, path: str) -> str:
   return sign(
      private_key=private_key,
      message=path.encode() + hashlib.sha256(
            (nonce + data)
         .encode()
      ).digest()
   )

def sign(private_key: str, message: bytes) -> str:
   return base64.b64encode(
      hmac.new(
         key=base64.b64decode(private_key),
         msg=message,
         digestmod=hashlib.sha512,
      ).digest()
   ).decode()

