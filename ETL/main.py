from extract import extract_api
from transform import transformation
from load import load_db

print("Starting ETL Pipeline")
print("Initiating extract")
try:
    extract_api()
    print("Extraction completed")
    mydb = transformation()
    print("Transformation completed")
    load_db(mydb)
    print("Loading into database successfully")
except Exception as e:
    print(e)
