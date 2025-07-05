# News-API-ETL
# 📰 News ETL Pipeline

This project extracts the latest news data from the [NewsData.io API](https://newsdata.io/), transforms and cleans it, and loads it into a local database for analysis.

---

## 📊 **Project Overview**

- **Extract**: Fetches live news data using NewsData.io API.
- **Transform**: Cleans and structures the data into a pandas DataFrame.
- **Load**: Stores the cleaned data into a SQLite database.

---

## 🛠 **Tech Stack**
- Python 3.x
- pandas
- requests
- python-dotenv
- SQLite (via `sqlite3` or `SQLAlchemy`)

---

## ⚙️ **Setup Instructions**

1. **Clone the repository**
```bash
git clone https://github.com/WhiteW00lf/News-API-ETL-.git
cd news-etl-pipeline
pip install -r requirements.txt
python3 main.py
```

2. To automate the entire ETL process, you can schedule a job with cron or windows scheduler to run ``` main.py ``` once at your prefered time of the day.


