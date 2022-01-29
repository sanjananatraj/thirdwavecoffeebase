from mysql.connector import Error

def read_query(connection, query):
  cursor = connection.cursor()
  result = None
  try:
    cursor.execute(query)
    result = cursor.fetchall()
    return result
  except Error as err:
    print(f"Error: '{err}'")
