from dotenv import load_dotenv
load_dotenv()

import os

CLIENT_ID = os.getenv('client_id') 
CLIENT_SECRET = os.getenv('client_secret') 


HOST = os.getenv("host")
USER = os.getenv("user")
PASSWORD = os.getenv("password")
DB = os.getenv("db")
CONTRACT_ID = os.getenv("contract_id")


