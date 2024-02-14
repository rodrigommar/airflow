from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args= {
    'depends_on_past': False,
    'start_date': datetime(2024,1,19),
    'email' : ['sidiamar6@gmail.com'],
    'email_on_failure': ['sidiamar6@gmail.com'],
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10)
}


with DAG(
    dag_id='dag_default_args',
    default_args=default_args,
    description='Uma dag que usar default_args()',
    schedule_interval=None,
    start_date=datetime(2024,1,20),
    catchup=False,
    tags=['default_args']) as dag:
    
    
    t1 = BashOperator(task_id='task1', bash_command='sleep 3')
    t2 = BashOperator(task_id='task2', bash_command='sleep 3')
    t3 = BashOperator(task_id='task3', bash_command='sleep 3')
    
    
    t1 >> t2 >> t3