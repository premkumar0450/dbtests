import os
import sys
from dotenv import load_dotenv
import pytest
import mysql.connector
from mysql.connector import Error


load_dotenv(".env")

@pytest.fixture(scope="session")
def db_setup():

    Mydb = mysql.connector.connect(host=os.getenv("host"),
                                    database=os.getenv("database"),
                                    user=os.getenv("user"),
                                    password=os.getenv("password"),
                                    port=os.getenv("port"))
    print(Mydb)
    if Mydb.is_connected():
        db_Info = Mydb.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
    return Mydb