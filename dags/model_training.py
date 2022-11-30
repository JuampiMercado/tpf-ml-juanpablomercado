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

logging.basicConfig(level=logging.DEBUG)


def model_training():
    logging.info('Start model training...')
    
    ratings = extract_from_db()
    ratings['rating'] = ratings['rating'].astype('int')
    places_ratings = ratings.pivot(index="placeid",columns="userid",values="rating").fillna(0)
    
    #logging.info(places_ratings)
    #return
    x = places_ratings.iloc[:, :-1].values
    y = places_ratings.iloc[:, -1].values
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)
    
    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)
    n_neighbors = 5
    classifier = KNeighborsClassifier(n_neighbors = n_neighbors, metric = 'minkowski', p = 2)
    #logging.info('x train')
    #logging.info(x_train)
    #logging.info('y train')
    #logging.info(y_train)
    classifier.fit(x_train, y_train)

    
    y_pred = classifier.predict(x_test)
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    accuracy_score(y_test, y_pred)
    distance,indices = classifier.kneighbors(n_neighbors=n_neighbors)
    
    i = 0
    arr = []
    for idx in indices:
        #logging.debug(','.join(str(x) for x in idx))
        arr.append(Recommendation(places_ratings.iloc[i].name,','.join(str(x) for x in idx)))
        i=i+1
    load(arr)
    logging.debug(arr)
    

def extract_from_db():
    db = dbFactory('postgresql').get_db()
    df = db.to_frame('select userid, placeid, rating from ratings')
    return df

def load(arr):
    db = dbFactory('postgresql').get_db()
    db.create_database()
    db.upsert_objects(objects=arr)

if __name__ == '__main__':
    model_training()