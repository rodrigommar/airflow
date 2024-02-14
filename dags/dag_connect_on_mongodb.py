
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

def create_uri_mongodb():
    
    load_dotenv()
    
    schema = os.getenv('SCHEMA')
    username = os.getenv('USER_NAME')
    password = os.getenv('PASSWORD')
    cluster_name = os.getenv('CLUSTER_NAME')
    id_host = os.getenv('ID_HOST')
    

    escaped_username = quote_plus(username)
    escaped_password = quote_plus(password)

    uri = f"{schema}://{escaped_username}:{escaped_password}@{cluster_name}.{id_host}"

    return uri


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
    def try_connect_on_mongodb(**kwargs):
        ti = kwargs['ti']
        mongodb_uri = ti.xcom_pull(task_ids='test_connection_with_mongodb')

        try:
            client = MongoClient(mongodb_uri, server_api=ServerApi('1'), maxPoolSize=10, connectTimeoutMS=30000)
            client.admin.command('ping')
            print("Conexão MongoDB bem-sucedida!")
        except Exception as e:
            print(f"Falha ao conectar ao MongoDB: {e}")


    # task
    task_connect_on_mongodb = PythonOperator(
    task_id='test_connection_with_mongodb',
    python_callable=create_uri_mongodb,
    provide_context=True,
    )

    # task
    task_to_verify_connection = PythonOperator(
        task_id='verifica_conexao',
        python_callable=try_connect_on_mongodb,
        provide_context=True,
    )

    # Definindo a precedência das tasks
    task_connect_on_mongodb >> task_to_verify_connection 
