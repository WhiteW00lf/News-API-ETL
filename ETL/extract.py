from dotenv import load_dotenv
import pandas as pd
import requests
import os

article_ids = []
titles = []
pubdates = []

load_dotenv()
api_key = os.getenv("API_KEY")
url = f"https://newsdata.io/api/1/latest?apikey={api_key}"
resp = requests.get(url)
print(resp.text)
if resp.status_code == 200:
    data = resp.json()

else:
    print(f"Status code - {resp.status_code} -  {resp.text}")

data = resp.json()


for each_entry in data["results"]:
    ids = each_entry["article_id"]
    article_ids.append(ids)
    title = each_entry["title"]
    titles.append(title)
    pubdate = each_entry["pubDate"]
    pubdates.append(pubdate)

print("Finished loading the lists")
