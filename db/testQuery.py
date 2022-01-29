from mysql.connector import Error
from src.server.server import create_db_connection
from src.db.dbconfig import credentials
from src.db.executeQuery import execute_query
import json

connection = create_db_connection(credentials["host"], credentials["user"], credentials["password"], credentials["db"])
testQuery = """
SELECT roaster.name, coffee.name, price FROM coffee
JOIN roaster ON roaster.roaster_id = coffee.roaster_id
ORDER BY roaster.name DESC;
"""
cursor = connection.cursor()
try:
  cursor.execute(testQuery)
  results = cursor.fetchall()
  connection.commit()
  print("Query successful")
except Error as err:
  print(f"Error: '{err}'")

for r in results:
  print(json.dumps({"roaster": r[0], "coffee_name": r[1]}, sort_keys=True))
