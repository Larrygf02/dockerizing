from .connection import run as create_connection
from .execute import run as execute_query
def run():
    query = f"CREATE DATABASE persondb"
    execute_query(query)
    