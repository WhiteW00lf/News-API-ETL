import pandas as pd
from extract import article_ids, titles, pubdates

def transformation():
    news_dict = {"ids": article_ids, "title": titles, "pubDate": pubdates}

    news_df = pd.DataFrame(news_dict)

    print(news_df.isna().sum())
    return news_df

    

#No null values found!