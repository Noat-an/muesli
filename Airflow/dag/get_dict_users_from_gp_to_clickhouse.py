from airflow import DAG
from airflow.decorators import task
from datetime import datetime


with DAG(
    dag_id="get_price_dict_users",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
        ) as dag:

    @task
    def extract(data):
        return data

    @task
    def process(data):
        return data

    @task
    def store(data):
        return data

    store(process(extract(126)))