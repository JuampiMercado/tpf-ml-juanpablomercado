"""ETL DAG."""
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

from create_tables import main as model_creation
from etl_places import etl_places 
from etl_ratings import etl_ratings
from model_training import model_training

with DAG(
    "etl_dag",
    schedule_interval=timedelta(minutes=1),
    start_date=datetime(2022, 11, 29),
    catchup=False,
) as dag:
    dummy_start_task = DummyOperator(task_id="init")
    model_creation = PythonOperator(
        task_id = "modelCreation",
        python_callable = model_creation
    )
    etl_places = PythonOperator(
        task_id="etlPlaces",
        python_callable = etl_places
    )
    etl_ratings = PythonOperator(
        task_id="etlRatings",
        python_callable = etl_ratings
    )
    model_training = PythonOperator(
        task_id="analytics",
        python_callable = model_training
    )
    dummy_start_task >> model_creation >> etl_places >> etl_ratings >> model_training