import os
import pymssql

def get_db_connection() -> pymssql.Connection:
    server = os.getenv('MSSQL_SERVER')
    database = os.getenv('MSSQL_DB')
    username = os.getenv('MSSQL_LOGIN')
    password = os.getenv('MSSQL_PASSWORD')
    
    conn = pymssql.connect(
        server=server,  # Use the service name defined in your docker-compose.yml
        user=username,               # This should match MSSQL_USER from your environment file
        password=password,  # This should match MSSQL_SA_PASSWORD from your environment file
        database=database       # This should match MSSQL_DB from your environment file
    )
    return conn