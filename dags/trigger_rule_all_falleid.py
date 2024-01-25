from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG(
    'trigger_rule_all_failed', 
    description=' Executa se todas as tarefas pai falharem.',
    start_date=datetime(2024,1,20),
    schedule_interval=None,
    catchup=False) as dag:
    t1 = BashOperator(task_id='print_date', bash_command='exit 1')
    t2 = BashOperator(task_id='sleep', bash_command='exit 1')
    t3 = BashOperator(task_id='templated', bash_command='sleep 5',
                      trigger_rule='all_failed')
    
    [t1 , t2] >> t3