from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime


with DAG(
    'my_fourth_dag', 
    description='my fourth dag',
    schedule_interval=None,
    start_date=datetime(2024,1,20)) as dag:
        
    t1 = BashOperator(task_id='task1', bash_command='sleep 3')
    t2 = BashOperator(task_id='task2', bash_command='sleep 3')
    t3 = BashOperator(task_id='task3', bash_command='sleep 3')
    
    t1.set_upstream(t2)
    t2.set_upstream(t3)