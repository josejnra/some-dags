import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


with DAG(dag_id='basic-dag', schedule_interval=None, start_date=days_ago(1)) as dag:

    def some_code():
        time.sleep(10 * 60)

    run = PythonOperator(
        task_id='run',
        python_callable=some_code
    )

