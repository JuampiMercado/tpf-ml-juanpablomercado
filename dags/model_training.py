from dbManager import dbFactory
import logging
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from models import Recommendation
#from fuzzywuzzy import process

logging.basicConfig(level=logging.INFO)


def model_training():
    logging.info('Start model training...')
    
    ratings = extract_from_db()
    ratings['rating'] = ratings['rating'].astype('int')
    logging.info('Extracting ratings from database...')
    places_ratings = ratings.pivot(index="placeid",columns="userid",values="rating").fillna(0)
    
    
    #return
    logging.info('Splitting data into train and test datasets...')
    x = places_ratings.iloc[:, :-1].values
    y = places_ratings.iloc[:, -1].values
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)
    
    logging.info('Model-fitting...')
    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)
    n_neighbors = 5
    classifier = KNeighborsClassifier(n_neighbors = n_neighbors, metric = 'minkowski', p = 2)
    classifier.fit(x_train, y_train)

    logging.info('Predict...')
    y_pred = classifier.predict(x_test)
    cm = confusion_matrix(y_test, y_pred)
    logging.info('Confusion matriz:')
    logging.info(cm)
    logging.info('Accuracy: ' + str(accuracy_score(y_test, y_pred)))
    distance,indices = classifier.kneighbors(n_neighbors=n_neighbors)

    logging.info('Deleting old predictions...')
    deletePredictions()
    logging.info('Creating array...')
    i = 0
    arr = []
    for idx in indices:
        for id in idx:
            arr.append(Recommendation(places_ratings.iloc[i].name,places_ratings.iloc[id].name))
        i=i+1
    logging.info('Saving into database ' + str(len(arr)) + ' records' )
    load(arr)
    logging.info('Operation finished.')
    

def extract_from_db():
    db = dbFactory('postgresql').get_db()
    df = db.to_frame('select userid, placeid, rating from ratings')
    return df

def load(arr):
    db = dbFactory('postgresql').get_db()
    db.create_database()
    db.upsert_objects(objects=arr)

def deletePredictions():
    db = dbFactory('postgresql').get_db()
    db.execute('delete from recommendations')

if __name__ == '__main__':
    model_training()