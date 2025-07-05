from transform import transformation
from sqlalchemy import create_engine


def load_db(mydb):
    eng = create_engine("sqlite:///database/newsdatabase.db")
    mydb.to_sql("news", con=eng, if_exists="replace", index=False)
