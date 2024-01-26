from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.email_operator import EmailOperator
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime, timedelta


default_args = {
    'depends_on_past': False,
    'start_date': datetime(2023,3,5),
    'email': ['rodrigommar@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries' : 1,
    'retry_delay' : timedelta(seconds=10)
}

with DAG(
    dag_id='dag_send_email',
    description='dag envia email quadno falha uma task',
    default_args=default_args,
    start_date=datetime(2024,1,20),
    schedule_interval=None,
    catchup=False,
    default_view='graph',
    tags=['sed_email', 'email_failure']
    ) as dag:
    
    
    t1 = BashOperator(task_id='task1', bash_command='sleep 3')
    t2 = BashOperator(task_id='task2', bash_command='sleep 3')
    t3 = BashOperator(task_id='task3', bash_command='sleep 3')
    t4 = BashOperator(task_id='task4', bash_command='exit 1')
    t5 = BashOperator(task_id='task5', bash_command='sleep 3', trigger_rule='none_failed')
    t6 = BashOperator(task_id='task6', bash_command='sleep 3', trigger_rule='none_failed')
    
    send_email = EmailOperator(task_id='send_email',
                               to='rodrigommar@gmail.com',
                               subject='Airflow Error',
                               html_content="""
                                    <h3> Ocorreu um erro inesperado ao executar a DAG. </h3>
                                    <p> DAG: send_email </p>""",                            
                                trigger_rule='one_failed')
    
    [t1,t2] >> t3 >> t4
    t4 >> [t5,t6,send_email]
    
    
