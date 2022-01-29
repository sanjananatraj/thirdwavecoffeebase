# insertCoffee.py
# function that inserts coffees info into COFFEE table in database
import sys
sys.path.append('../server')
from mysql.connector import Error
from server import create_db_connection
from dbconfig import credentials

def insertCoffeeIntoDB(coffeeList):
  # first, establish a connection to the database
  connection = create_db_connection(credentials["host"], credentials["user"], credentials["password"], credentials["db"])
  coffee_data_query = """
  INSERT INTO coffee (coffee_id, roaster_id, name, price, description)
  VALUES (%s, %s, %s, %s, %s)
  """
  execute_list_query(connection, coffee_data_query, coffeeList)

def execute_list_query(connection, query, list):
  cursor = connection.cursor()
  try:
    cursor.executemany(query, list)
    connection.commit()
    print("Query OK. Successfully added coffees into database.")
  except Error as err:
    print(f"Error: '{err}'")


