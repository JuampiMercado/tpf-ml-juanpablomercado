"""Script to extract daily stock information from Google (GOOG), Microsoft (MSFT) and Amazon (AMZN)."""
import pandas as pd
from models import Rating
from dbManager import dbFactory
import logging
logging.basicConfig(level=logging.INFO)


def etl_ratings():    
    logging.info('Starting ETL ratings...')
    logging.info('Reading from csv...')
    df = extract()
    logging.info('Working with rating dataset...')
    arr = transform(df)
    logging.info('Saving into database ' + str(len(arr)) + ' records' )
    load(arr)
    logging.info('Operation finished.')

    
def extract():
    df = pd.read_csv('ratings.csv',usecols=["userID","placeID","rating"])
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