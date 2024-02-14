from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG(
    'dag_execute_dag2', 
    description='dag que executa outra dag',
    start_date=datetime(2024,1,20),
    schedule_interval=None,
    catchup=False) as dag:
    
    t1 = BashOperator(task_id='sleep1', bash_command='sleep 3')
    t2 = BashOperator(task_id='sleep2', bash_command='sleep 3')
    
    t1 >> t2 
