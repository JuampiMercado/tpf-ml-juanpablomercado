from sqlalchemy import create_engine, tuple_
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import insert
from models import Base
import pandas as pd
from configuration import get_config
import sqlite3
import logging

db_params = get_config("db_params")

class dbManager():

    def __init__(self, dialect, db):
        self.dialect = dialect
        self.db = db
        self._engine = None
        

    def _get_engine(self,db_uri):
        if not self._engine:
            self._engine = create_engine(db_uri)
        return self._engine

    def _connect(self):
        return self._get_engine().connect()

    @staticmethod
    def _cursor_columns(cursor):
        if hasattr(cursor, 'keys'):
            return cursor.keys()
        else:
            return [c[0] for c in cursor.description]

    def execute(self, sql, connection=None):
        if connection is None:
            connection = self._connect()
        return connection.execute(sql)

    def insert_from_frame(self, df, table, if_exists='append', index=False, **kwargs):
        connection = self._connect()
        with connection:
            df.to_sql(table, connection, if_exists=if_exists, index=index, **kwargs)

    def to_frame(self, *args, **kwargs):
        cursor = self.execute(*args, **kwargs)
        if not cursor:
            return
        data = cursor.fetchall()
        if data:
            df = pd.DataFrame(data, columns=self._cursor_columns(cursor))
        else:
            df = pd.DataFrame()
        return df
    
    def create_database(self):
        pass
    
    def create_model(self):
        engine = self._get_engine()
        Base.metadata.create_all(engine)

    def insert_array_objects(self,arr_objects):
        engine = self._get_engine()
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        with Session() as session:    
            session.bulk_save_objects(objects=arr_objects)
            session.commit()

    def upsert_objects(self,objects):
        engine = self._get_engine()
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        
        with Session() as session:   
            print('Objetos: ' + str(len(objects))) 
            i = 0
            for e in objects:
                i = i+1
                try:
                    session.merge(e)
                except Exception as ex:
                    print(ex)
            session.commit()
            print('Ciclos: ' + str(i)) 
        

    
    

class PostgresClient(dbManager):
    def __init__(self):
        dbManager.__init__(self,dialect='postgresql',db=db_params["postgresql"])
        

    def _get_engine(self):
        db_uri = f"postgresql://{self.db['user']}:{self.db['password']}@{self.db['host']}:{self.db['port']}/{self.db['database']}"
        return dbManager._get_engine(self,db_uri=db_uri)

    def create_database(self):
        engine = self._get_engine()
        if not database_exists(engine.url):
            create_database(engine.url)

class SqLiteClient(dbManager):
    def __init__(self):
        dbManager.__init__(self,dialect='sqlite',db=db_params["sqlite"])
        

    def _get_engine(self):
        db_uri = f"sqlite:///{self.db['database']}"
        return dbManager._get_engine(self,db_uri=db_uri)

    def create_database(self):
        try:
            conn = sqlite3.connect(self.db['database'])
            conn.close()
        except:
            logging.error('Error creating sqlite database')



class dbFactory():
    def __init__(self,db_type,env='prod'):
        self.db_type = db_type
        if(env =='dev'):
            db_params["postgresql"]["host"] = "localhost"
    
    def get_db(self):
        if self.db_type == 'postgresql':
            return PostgresClient()
        if self.db_type == 'sqlite':
            return SqLiteClient()



if __name__ == '__main__':
    dbFactory = dbFactory('postgresql')
    db = dbFactory.get_db()
    print(db.to_frame('SELECT * FROM stock_value'))