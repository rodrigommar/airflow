from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.utils.task_group import TaskGroup

with DAG(
    'dag_task_group', 
    description='dag com task group',
    start_date=datetime(2024,1,20),
    schedule_interval=None,
    catchup=False) as dag:
    t1 = BashOperator(task_id='sleep1', bash_command='sleep 3')
    t2 = BashOperator(task_id='sleep2', bash_command='sleep 3')
    t3 = BashOperator(task_id='sleep3', bash_command='sleep 3')
    t4 = BashOperator(task_id='sleep4', bash_command='sleep 3')
    t5 = BashOperator(task_id='sleep5', bash_command='sleep 3')
    t6 = BashOperator(task_id='sleep6', bash_command='sleep 3')
    
    tsk_group = TaskGroup('tsk_group')
    
    t7 = BashOperator(task_id='sleep7', bash_command='sleep 3', task_group=tsk_group)
    t8 = BashOperator(task_id='sleep8', bash_command='sleep 3', task_group=tsk_group)
    t9 = BashOperator(task_id='sleep9', bash_command='sleep 3',
                      trigger_rule='one_failed', task_group=tsk_group)
    
    t1 >> t2 
    t3 >> t4
    [t2, t4] >> t5 >> t6
    t6 >> tsk_group
    