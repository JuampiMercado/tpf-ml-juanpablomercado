"""Script to extract daily stock information from Google (GOOG), Microsoft (MSFT) and Amazon (AMZN)."""
import pandas as pd
from models import Place
from dbManager import dbFactory

def etl_places():    
    df = extract()
    arr = transform(df)
    load(arr)

    
def extract():
    places = pd.read_csv('geoplaces2.csv',usecols=["placeID","name","city","state","country"])
    return places

def transform(df):
    return [Place(a.get('placeID'),a.get('name'),a.get('city'),a.get('state'),a.get('country')) for a in df.to_dict(orient='records')]

def load(arr):
    db = dbFactory('postgresql').get_db()
    db.create_database()
    db.upsert_objects(objects=arr)

    

if __name__ == "__main__":
    etl_places()

#sudo docker-compose exec airflow-webserver psql -h postgres -U airflow