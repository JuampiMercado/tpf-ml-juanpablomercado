"""Script to extract daily stock information from Google (GOOG), Microsoft (MSFT) and Amazon (AMZN)."""
import pandas as pd
from models import Place
from dbManager import dbFactory
import boto3
import io
import logging
logging.basicConfig(level=logging.INFO)

s3 = boto3.client('s3')


def etl_places():
    logging.info('Starting ETL places...')
    logging.info('Reading from csv...')
    df = extract()
    logging.info('Working with places dataset...')
    arr = transform(df)
    logging.info('Saving into database ' + str(len(arr)) + ' records' )
    load(arr)
    logging.info('Operation finished.')

    
def extract():
    #places = pd.read_csv('places.csv',usecols=["placeID","name","city","state","country"])
    #s3 = boto3.resource('s3')
    #ap = s3.Bucket('arn:aws:s3:::cdetpml:tpfaccesspoint-5yk47jsamg8xnz91qf6b4p57cwx3cuse1a-s3alias/[S3 Access Point name]')
    #for obj in ap.objects.all():  
    #    print(obj.key)  
    #    print(obj.get()['Body'].read())
    response = s3.get_object(Bucket='arn:aws:s3:us-east-1:296921149145:accesspoint/tpfaccesspoint', Key='places.csv')
    places = pd.read_csv(io.BytesIO(response['Body'].read()))
    return places

def transform(df):
    df['city'] = df['city'].replace('?','')
    df['state'] = df['state'].replace('?','')
    df['country'] = 'Mexico'
    return [Place(a.get('placeID'),a.get('name'),a.get('city'),a.get('state'),a.get('country')) for a in df.to_dict(orient='records')]

def load(arr):
    db = dbFactory('postgresql').get_db()
    db.create_database()
    db.upsert_objects(objects=arr)

    

if __name__ == "__main__":
    etl_places()

#sudo docker-compose exec airflow-webserver psql -h postgres -U airflow -d ETL