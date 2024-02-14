from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG(
    'my_dag_comlex', 
    description='my dag complex',
    start_date=datetime(2024,1,20),
    schedule_interval=None,
    catchup=False) as dag:
    t1 = BashOperator(task_id='sleep1', bash_command='sleep 3')
    t2 = BashOperator(task_id='sleep2', bash_command='sleep 3')
    t3 = BashOperator(task_id='sleep3', bash_command='sleep 3')
    t4 = BashOperator(task_id='sleep4', bash_command='sleep 3')
    t5 = BashOperator(task_id='sleep5', bash_command='sleep 3')
    t6 = BashOperator(task_id='sleep6', bash_command='sleep 3')
    t7 = BashOperator(task_id='sleep7', bash_command='sleep 3')
    t8 = BashOperator(task_id='sleep8', bash_command='sleep 3')
    t9 = BashOperator(task_id='sleep9', bash_command='sleep 3',
                      trigger_rule='one_failed')
    
    t1 >> t2 
    t3 >> t4
    [t2, t4] >> t5 >> t6
    t6 >> [t7, t8, t9]
    