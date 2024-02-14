from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta


def task_write(**kwargs):
    kwargs['ti'].xcom_push(key='valorcom1', value=10200)
    
def task_read(**kwargs):
    valor = kwargs['ti'].xcom_pull(key='valorcom1')
    print(f'valor recuperado: {valor}')
    

with DAG(
    dag_id='dag_xcon',
    description='my dag with xcon working',
    start_date=datetime(2024,1,20),
    schedule_interval=None,
    catchup=False) as dag:
    
    
    t1 = PythonOperator(task_id='task1', python_callable=task_write)
    t2 = PythonOperator(task_id='task2', python_callable=task_read)
    
    t1 >> t2