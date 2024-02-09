from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.mongo.hooks.mongo import MongoHook
from datetime import datetime
 
 
def connect_mongodb():
    
    load_dotenv()
    
    username = os.getenv('USER_NAME')
    password = os.getenv('PASSWORD')
    cluster_name = os.getenv('CLUSTER_NAME')
    id_host = os.getenv('ID_HOST')
    schema = os.getenv('SCHEMA')


    escaped_username = quote_plus(username)
    escaped_password = quote_plus(password)

    uri =  f"{schema}://{escaped_username}:{escaped_password}@{cluster_name}.{id_host}"


    try:
        client = MongoClient(uri, server_api=ServerApi('1'), maxPoolSize=10 ,connectTimeoutMS=30000)
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        #print(f"Número de conexões abertas: {client._topology.get_server().pool.connections.count()}")
        #print(f"Tamanho máximo do pool: {client._topology.get_server().pool.max_size}")
        return client
    
    except Exception as e:
        print(e)
