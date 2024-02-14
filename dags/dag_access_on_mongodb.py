
#import referente a funções
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from  dotenv import load_dotenv
from urllib.parse import quote_plus
import os

# import de bibliotecas referente a DAG
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta



# ===========area destinada a funções ========================================

def select_db():
    ...



def select_collection():
    ...


# ===========area destinada a DAG ========================================

default_args = {
    'depends_on_past': False,
    'start_date': datetime(2024,2,1),
    'email': ['rodrigommar@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10)
}


with DAG(
    'dag_connect_on_mongodb',
    description='Acessa o banco mongodb',
    default_args=default_args,
    schedule_interval='@daily',
    catchup= False,
    default_view='graph',
    tags=['mongodb, connect_mongodb']
) as dag:

    # task
    task_select_database = PythonOperator(
    task_id='test_connection_with_mongodb',
    python_callable=select_db,
    provide_context=True,
    )

    # task
    task_select_collection = PythonOperator(
        task_id='verifica_conexao',
        python_callable=select_collection,
        provide_context=True,
    )

    # Definindo a precedência das tasks
    task_select_database >> task_select_collection 
