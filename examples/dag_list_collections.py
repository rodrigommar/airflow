from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from hooks_mongodb import MongoAtlasHook

def list_collections():
    mongo_hook = MongoAtlasHook(mongo_conn_id='MongoDB_atlas')    
    connection = mongo_hook.get_conn()
    database_name = 'db-climate'  # substitua pelo nome real do seu banco de dados
    collections = connection[database_name].list_collection_names()
    print(f"Collections in {database_name}: {collections}")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 2),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'mongo_atlas_example',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    catchup=False
)

list_collections_task = PythonOperator(
    task_id='list_collections',
    python_callable=list_collections,
    dag=dag,
)
