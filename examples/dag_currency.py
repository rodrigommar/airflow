from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from pymongo import MongoClient
from urllib.parse import quote_plus

def test_mongo_connection():
    # Configurar as informações de conexão MongoDB
    
    # Configurar as informações de conexão MongoDB
    username = "rodrigommar"
    password = "noah@2525"
    cluster_url = "data-climate.iujaf2q.mongodb.net"
    database_name = "db-climate"

    escaped_username = quote_plus(username)
    escaped_password = quote_plus(password)
    
    # Construir o URI de conexão escapando nome de usuário e senha
    mongo_uri = f"mongodb+srv://{escaped_username}:{escaped_password}@{cluster_url}/?retryWrites=true&w=majority"
    
    #mongo_uri = "mongodb+srv://rodrigommar:noah@2525@data-climate.iujaf2q.mongodb.net/?retryWrites=true&w=majority"
    #database_name = "db-climate"

    # Testar a conexão MongoDB
    try:
        client = MongoClient(mongo_uri)
        db = client[database_name]
        collections = db.list_collection_names()
        print(f"Collections in {database_name}: {collections}")
        return True
    except Exception as e:
        print(f"Error connecting to MongoDB: {str(e)}")
        return False

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'test_mongo_connection',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    catchup=False
)

test_task = PythonOperator(
    task_id='test_mongo_connection',
    python_callable=test_mongo_connection,
    dag=dag,
)

if __name__ == "__main__":
    dag.cli()
