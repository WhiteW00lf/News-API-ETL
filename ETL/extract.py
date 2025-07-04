from dotenv import load_dotenv
import pandas as pd 
import requests
import os

load_dotenv()
api_key = os.getenv('API_KEY')
url=f"https://newsdata.io/api/1/latest?apikey={api_key}&q=India"
resp = requests.get(url)
if(resp.status_code == 200):
    data = resp.json()
    print(data)
else:
    print(f"Status code - {resp.status_code} -  {resp.text}")