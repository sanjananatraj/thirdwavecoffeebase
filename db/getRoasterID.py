import sys
sys.path.append('..\server')
from server import create_db_connection
from readQuery import read_query
from dbconfig import credentials
import pymysql
from decouple import config

def getRoasterID(name):
  db_user = config('CLOUD_SQL_USERNAME')
  db_password = config('CLOUD_SQL_PASSWORD')
  db_name = config('CLOUD_SQL_DATABASE_NAME')
  host = '127.0.0.1'
  cnx = pymysql.connect(user=db_user, password=db_password,
                        host=host, db=db_name, port=3308)
  connection = create_db_connection(credentials["host"], credentials["user"], credentials["password"], credentials["db"])
  roaster_lookup = """
  SELECT roaster_id
  FROM roaster
  WHERE name='%s'
  """ % name

  results = read_query(cnx, roaster_lookup)
  if results:
    for result in results:
      roaster_id = result[0]
  else:
    return 000000

  return roaster_id

  