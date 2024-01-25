from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG(
    'trigger_rule_all_success', 
    description='Executa se todas as tarefas pai forem bem-sucedidas',
    start_date=datetime(2024,1,20),
    schedule_interval=None,
    catchup=False) as dag:
    t1 = BashOperator(task_id='print_date', bash_command='date')
    t2 = BashOperator(task_id='sleep', bash_command='sleep 5')
    t3 = BashOperator(task_id='templated', bash_command='sleep 5', trigger_rule='all_success')
    
    [t1 , t2] >> t3