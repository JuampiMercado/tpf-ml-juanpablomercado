import logging
from datetime import date
import pandas as pd
from sqlalchemy import create_engine
from utils import Utils


class DBManager:
    @staticmethod
    def __connect():
        """
        Crea una nueva conexión en la base de datos
        
        Parámetros
        ----------
        -

        Retorna
        -------
        sqlalchemy.engine connection
        """
        try:
            params = Utils.config()
            s = f"postgresql://{params['user']}:{params['password']}@{params['host']}:{params['port']}/{params['database']}"
            engine = create_engine(s)
            return engine.connect()
        except Exception as e:
            logging.error("Error estableciendo la configuración de la conexión con la base de datos.")
            logging.error(e)
        
        
    @staticmethod
    def query(query):
        """
        Ejecuta una consulta en la base de datos

        Parámetros
        ----------
        query:string

        Retorna
        -------
        Pandas data frame
        """
        try:
            df = []
            with DBManager.__connect() as conn:
                #logging.info('Conexión establecida')
                df= pd.read_sql(query, conn)
                #logging.info('[READ] ' + query)
            return df
        except:
            logging.error('Error al ejecutar la consulta: ' + query)
            return pd.DataFrame([])
    @staticmethod
    def execute(sql):
        """
        Ejecuta una instrucción SQL

        Parámetros
        ----------
        sql:string

        Retorna
        ------
        -
        """
        try:
            with DBManager.__connect() as conn:
                #print('Conexión establecida')
                conn.execute(sql)
                #print('Ejecución de consulta: ' + sql )
        except:
            logging.error('Error al ejecutar la instrucción: ' + sql)

    @staticmethod
    def to_sql(df,table):
        """
        Save a data frame into table
        Parameters
        ----------
        df:data frame
        table: string

        Returns
        -------
        None
        """
        try:
            with DBManager.__connect() as conn:
                df.to_sql(name=table,con=conn,if_exists='append',index=False)
                #print('[WRITE] ' + table)
        except:
            logging.error('Error al insertar el data set en la tabla: ' + table)