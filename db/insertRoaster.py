# insertRoaster.py
# given a roaster's name, location, and county, generate UUID and insert it into ROASTER table
from mysql.connector import Error
from src.server.server import create_db_connection
from src.db.dbconfig import credentials
from src.data.roasterlist import makeRoasterTuples
import uuid

#roasters = makeRoasterTuples()

def insertRoasterIntoDB(roasterInfo):
  # method goes here
  # first, establish a connection to the database
  connection = create_db_connection(credentials["host"], credentials["user"], credentials["password"], credentials["db"])
  roaster_query = """
  INSERT INTO roaster (roaster_id, name, location) VALUES (%s,%s,%s)
  """
  execute_list_query(connection, roaster_query, roasterInfo)

def execute_list_query(connection, query, list):
  cursor = connection.cursor()
  try:
    cursor.executemany(query, list)
    connection.commit()
    print("Query successful")
  except Error as err:
    print(f"Error: '{err}'")

def insertSingleRoaster(roasterInfo):
  connection = create_db_connection(credentials["host"], credentials["user"], credentials["password"], credentials["db"])
  roaster_query = """
  INSERT INTO roaster (roaster_id, name, location) VALUES (%s,%s,%s)
  """
  cursor = connection.cursor()
  try:
    cursor.execute(roaster_query, roasterInfo)
    connection.commit()
    print("Query successful")
  except Error as err:
    print(f"Error: '{err}'")

#insertRoasterIntoDB(roasters)
r_id = "r" + str(uuid.uuid4())[:7]
roasterInfo = (r_id, "Taylor Lane Organic Coffee", "Santa Rosa")
# print(roasterInfo)
insertSingleRoaster(roasterInfo)