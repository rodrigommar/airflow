from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.operators.dagrun_operator import TriggerDagRunOperator

with DAG(
    dag_id='dag_execute_dag1', 
    description='dag que executa outra dag',
    start_date=datetime(2024,1,20),
    schedule_interval=None,
    catchup=False) as dag:
    
    t1 = BashOperator(task_id='sleep1', bash_command='sleep 3')
    t2 = TriggerDagRunOperator(task_id='sleep2', trigger_dag_id='dag_execute_dag2')
    
    t1 >> t2 
