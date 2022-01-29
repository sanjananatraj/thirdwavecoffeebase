# server.py
# file that creates the roasters and coffees databases
import sys
sys.path.append('..\db')
import mysql.connector
from mysql.connector import Error
from dbconfig import credentials
from executeQuery import execute_query

def create_server_connection(host_name, user_name, user_password):
  connection = None
  try:
    connection = mysql.connector.connect(
      host=host_name,
      user=user_name,
      passwd=user_password,
    )
    print("MySQL Database server connection successful")
  except Error as err:
    print(f"Error: '{err}'")

  return connection

# serverConnection = create_server_connection(credentials["host"], credentials["user"], credentials["password"])

def create_database(connection, query):
  cursor = connection.cursor()
  try:
    cursor.execute(query)
    print("Database created succesfully")
  except Error as err:
    print(f"Error: '{err}'")

create_database_query = "CREATE DATABASE %s" % (credentials["db"])
# create_database(serverConnection, create_database_query)

def create_db_connection(host_name, user_name, user_password, db_name):
  connection = None
  try:
      connection = mysql.connector.connect(
          host=host_name,
          user=user_name,
          passwd=user_password,
          database=db_name
      )
      print("MySQL Database connection successful")
  except Error as err:
      print(f"Error: '{err}'")

  return connection

connection = create_db_connection(credentials["host"], credentials["user"], credentials["password"], credentials["db"])

create_roaster_table = """CREATE TABLE IF NOT EXISTS roaster ( 
  roaster_id VARCHAR(8) PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  location VARCHAR(50) NOT NULL
) """
# execute_query(connection, create_roaster_table)

# create table for coffee roaster
create_coffee_table = """CREATE TABLE IF NOT EXISTS coffee ( 
  coffee_id VARCHAR(8) NOT NULL,
  roaster_id VARCHAR(8) NOT NULL,
  name VARCHAR(500) NOT NULL,
  price DECIMAL,
  description VARCHAR(1000),
  PRIMARY KEY(coffee_id),
  FOREIGN KEY(roaster_id) REFERENCES roaster(roaster_id) ON DELETE CASCADE
);"""
# execute_query(connection, create_coffee_table)

