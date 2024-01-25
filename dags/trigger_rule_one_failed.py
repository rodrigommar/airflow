from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime


with DAG(
    'trigger_rule_one_failled', 
    description='my fiveth dag - trigger-rule 1',
    schedule_interval=None,
    start_date=datetime(2024,1,20)) as dag:
        
    t1 = BashOperator(task_id='task1', bash_command='exit 1')
    t2 = BashOperator(task_id='task2', bash_command='sleep 3')
    t3 = BashOperator(task_id='task3', bash_command='sleep 3', trigger_rule='one_failed')
    
    [t1 , t2] >> t3