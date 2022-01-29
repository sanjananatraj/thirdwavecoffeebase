import sys
sys.path.append('..\server')
from server import create_db_connection
from readQuery import read_query
from dbconfig import credentials

def getRoasterID(name):
  connection = create_db_connection(credentials["host"], credentials["user"], credentials["password"], credentials["db"])
  roaster_lookup = """
  SELECT roaster_id
  FROM roaster
  WHERE name='%s'
  """ % name

  results = read_query(connection, roaster_lookup)
  if results:
    for result in results:
      roaster_id = result[0]
  else:
    return 000000

  return roaster_id

  