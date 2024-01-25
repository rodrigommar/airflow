from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG(
    'my_first_dag', 
    description='my first dag',
    start_date=datetime(2024,1,20),
    schedule_interval=None,
    catchup=False) as dag:
    t1 = BashOperator(task_id='print_date', bash_command='date')
    t2 = BashOperator(task_id='sleep', bash_command='sleep 5')
    t3 = BashOperator(task_id='templated', bash_command='sleep 5')
    
    t1 >> t2 >> t3