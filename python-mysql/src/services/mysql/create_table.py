from .connection import run as create_connection
from .execute import run as execute_query
def run():
    query = f"CREATE TABLE person (name VARCHAR(255), address VARCHAR(255))"
    execute_query(query, "persondb")