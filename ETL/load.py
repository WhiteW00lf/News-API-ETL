from transform import news_df
from sqlalchemy import create_engine


eng = create_engine("sqlite:///newsdatabase.db")
news_df.to_sql("news", con=eng, if_exists="replace", index=False)
