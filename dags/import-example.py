import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from haversine import haversine


with DAG(dag_id='import-example', schedule_interval=None, start_date=days_ago(1)) as dag:

    def some_code():        
        lyon = (45.7597, 4.8422) # (lat, lon)
        paris = (48.8567, 2.3508)
        print(haversine(lyon, paris))

    run = PythonOperator(
        task_id='run',
        python_callable=some_code
    )

