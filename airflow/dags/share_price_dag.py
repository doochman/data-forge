import yaml
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def load_config(**kwargs):
    with open('/opt/airflow/pipelines/share_price_pipeline/config.yml') as f:
        config = yaml.safe_load(f)
    kwargs['ti'].xcom_push(key='config', value=config)

def start_producer(**kwargs):
    config = kwargs['ti'].xcom_pull(task_ids='load_config', key='config')
    print("Starting producer with config:", config)
    
    # Run producer.py script (this would ideally be inside a Docker container)
    subprocess.run(['python', '/opt/airflow/pipelines/share_price_pipeline/producer.py'])

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    'share_price_pipeline',
    default_args=default_args,
    schedule_interval=None,  # Manually triggered for now
    catchup=False
) as dag:
    task1 = PythonOperator(
        task_id='load_config',
        python_callable=load_config,
        provide_context=True
    )

    task2 = PythonOperator(
        task_id='start_producer',
        python_callable=start_producer,
        provide_context=True
    )

    task1 >> task2
