"""Script to extract daily stock information from Google (GOOG), Microsoft (MSFT) and Amazon (AMZN)."""
import pandas as pd
from models import Rating
from dbManager import dbFactory
import logging

def etl_ratings():    
    df = extract()
    arr = transform(df)
    load(arr)

    
def extract():
    df = pd.read_csv('rating_final.csv',usecols=["userID","placeID","rating"])
    print(df.count())
    return df

def transform(df):
    return [Rating(a.get('userID'),a.get('placeID'),a.get('rating')) for a in df.to_dict(orient='records')]

def load(arr):
    db = dbFactory('postgresql').get_db()
    db.create_database()
    print(len(arr))
    #db.execute(sql="DELETE FROM ratings")
    #db.insert_array_objects(arr_objects=arr)
    db.upsert_objects(objects=arr)

    

if __name__ == "__main__":
    etl_ratings()