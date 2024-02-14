from airflow.hooks.base import BaseHook
from pymongo import MongoClient

class MongoAtlasHook(BaseHook):
    def __init__(self, mongo_conn_id='MongoDB_atlas', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mongo_conn_id = mongo_conn_id
        self.connection = None

    def get_conn(self):
        """
        Obtém a conexão com o MongoDB Atlas.
        """
        if self.connection is None:
            conn_info = self.get_connection(self.mongo_conn_id)
            mongo_uri = conn_info.get_uri()

            if not mongo_uri:
                raise ValueError("MongoDB URI is empty. Please check your connection settings.")

            if not mongo_uri.startswith('mongodb://') and not mongo_uri.startswith('mongodb+srv://'):
                raise ValueError("Invalid URI scheme. URI must begin with 'mongodb://' or 'mongodb+srv://'")

            self.connection = MongoClient(mongo_uri)
        return self.connection
