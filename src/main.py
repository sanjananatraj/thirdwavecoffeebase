# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_cloudsql_mysql]
import os

from flask import Flask, jsonify, render_template, make_response, url_for, redirect
from flaskext.mysql import MySQL
from flask_restful import Resource, Api
from flask_cors import CORS
from waitress import serve
import pymysql

from decouple import config

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

app = Flask(__name__)
mysql = MySQL()
api = Api(app)
CORS(app)

app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False # to allow ascii characters
# serve all static files using Flask for now
@app.route("/README.md")
def readme():
  return redirect(url_for('static', filename='README.md'))

@app.route("/_coverpage.md")
def coverpage():
  return redirect(url_for('static', filename='_coverpage.md'))

@app.route("/favicon.ico")
def favicon():
  return redirect(url_for('static', filename='favicon.ico'))

@app.route('/')
def main():
    return render_template('index.html')
# [END gae_python37_cloudsql_mysql]

def convert_mysql_decimal_to_float(decimal_object):
  if (decimal_object == None):
    return None
  else:
    return float(decimal_object)

# get all coffees by roaster name. no arg returns a list of roasters in database
class Roasters(Resource):
  def get(self, name=None):
    """
    Roasters GET method. Retrieves all roaster names found in the third wave coffee base database, unless the name of the roaster is provided. If provided, then information about the roaster is returned instead.
    :param name: Name of the roster to retrieve, parameter is optional
    :return: Roaster, 200 HTTP status code
    """
    if os.environ.get('GAE_ENV') == 'standard':
    # If deployed, use the local socket interface for accessing Cloud SQL
      unix_socket = '/cloudsql/{}'.format(db_connection_name)
      cnx = pymysql.connect(user=db_user, password=db_password,
                            unix_socket=unix_socket, db=db_name)
    else:
      print("running locally")
      db_user = config('CLOUD_SQL_USERNAME')
      db_password = config('CLOUD_SQL_PASSWORD')
      db_name = config('CLOUD_SQL_DATABASE_NAME')
      host = '127.0.0.1'
      cnx = pymysql.connect(user=db_user, password=db_password,
                            host=host, db=db_name, port=3308)

    if not name:
      try:
        with cnx.cursor() as cursor:
          cursor.execute(""" 
          select distinct roaster.name from roaster
          inner join coffee on roaster.roaster_id = coffee.roaster_id
          order by roaster.name asc 
          """)
          results = cursor.fetchall()
          flat_list = [roaster for sublist in results for roaster in sublist]
          content = {'roasters': flat_list}
          
        cursor.close()
        cnx.close()
        return make_response(jsonify(content), 200)
      except Exception as e:
        print("Error: ", e)
        return make_response({'error': str(e)})

    if name:
      try:
        with cnx.cursor() as cursor:
          cursor.execute(""" 
          select roaster.roaster_id, roaster.name, roaster.location, coffee.coffee_id, coffee.name, price, description, coffee.origin, coffee.type, coffee.process, coffee.roast_level, coffee.tasting_notes from coffee
          join roaster on roaster.roaster_id = coffee.roaster_id
          where roaster.name=%s
          order by coffee.name asc   
          """, name)
          results = cursor.fetchall()
          coffee_list = []
          content = {}

          if results:
            first = results[0]
            for result in results:
              if result[11]:
                tasting_notes = result[11].split(",")
              coffee = {'id': result[3], 'name': result[4], 'price': convert_mysql_decimal_to_float(result[5]), 'description': result[6], 'origin': result[7], 'type': result[8], 'process': result[9], 'roastLevel': result[10], 'tastingNotes': [s.strip() for s in tasting_notes] if result[11] else []}
              coffee_list.append(coffee)
              coffee = {}
            content = {'id': first[0], 'name': first[1], 'location': first[2], 'coffees': coffee_list}
          else:
            cursor.close()
            cnx.close()
            return make_response({
                'error': 'roaster not found',
                'code': 404
            }, 404)

          cursor.close()
          cnx.close()
          return make_response(jsonify(content), 200)
      except Exception as e:
        print("Error: ", e)
        return make_response({'error': str(e)})
        

class RoastersByID(Resource):
  def get(self, id):
    if os.environ.get('GAE_ENV') == 'standard':
    # If deployed, use the local socket interface for accessing Cloud SQL
      unix_socket = '/cloudsql/{}'.format(db_connection_name)
      cnx = pymysql.connect(user=db_user, password=db_password,
                            unix_socket=unix_socket, db=db_name)
    else:
      print("running locally")
      db_user = config('CLOUD_SQL_USERNAME')
      db_password = config('CLOUD_SQL_PASSWORD')
      db_name = config('CLOUD_SQL_DATABASE_NAME')
      host = '127.0.0.1'
      cnx = pymysql.connect(user=db_user, password=db_password,
                            host=host, db=db_name, port=3308)
    
    if id:
      try:
        with cnx.cursor() as cursor:
          cursor.execute(""" 
            select roaster.roaster_id, roaster.name, roaster.location, coffee.coffee_id, coffee.name, price, description, coffee.origin, coffee.type, coffee.process, coffee.roast_level, coffee.tasting_notes from coffee
            join roaster on roaster.roaster_id = coffee.roaster_id
            where roaster.roaster_id=%s
            order by coffee.name asc   
            """, id)
          results = cursor.fetchall()
          coffee_list = []
          content = {}

          if results:
            first = results[0]
            for result in results:
              if result[11]:
                tasting_notes = result[11].split(",")
              coffee = {'id': result[3], 'name': result[4], 'price': convert_mysql_decimal_to_float(result[5]), 'description': result[6], 'origin': result[7], 'type': result[8], 'process': result[9], 'roastLevel': result[10], 'tastingNotes': [s.strip() for s in tasting_notes] if result[11] else []}
              coffee_list.append(coffee)
              coffee = {}
            content = {'id': first[0], 'name': first[1], 'location': first[2], 'coffees': coffee_list}
          else:
            cursor.close()
            cnx.close()
            return make_response({
                'error': 'roaster id not found',
                'code': 404
            }, 404)

          cursor.close()
          cnx.close()
          return make_response(jsonify(content), 200)
      
      except Exception as e:
        print("Error: ", e)
        return make_response({'error': str(e)})
                        
class Location(Resource):
  """
  Location GET method. If no location parameter, return a list of locations that roasters are based in. If parameter includes a city name, return a list of roasters that are based in that location.
  :param location: Location name (city only), optional
  :return: A list of roasters that operate in said location. If no parameter, a list of all locations
  """
  def get(self, location=None):

    if os.environ.get('GAE_ENV') == 'standard':
    # If deployed, use the local socket interface for accessing Cloud SQL
      unix_socket = '/cloudsql/{}'.format(db_connection_name)
      cnx = pymysql.connect(user=db_user, password=db_password,
                            unix_socket=unix_socket, db=db_name)
    else:
      print("running locally")
      db_user = config('CLOUD_SQL_USERNAME')
      db_password = config('CLOUD_SQL_PASSWORD')
      db_name = config('CLOUD_SQL_DATABASE_NAME')
      host = '127.0.0.1'
      cnx = pymysql.connect(user=db_user, password=db_password,
                            host=host, db=db_name, port=3308)

    if not location:
      try:
        with cnx.cursor() as cursor:
          cursor.execute("""
          select distinct location from roaster
          inner join coffee on roaster.roaster_id = coffee.roaster_id
          order by location asc
          """)
          results = cursor.fetchall()
          flat_list = [location for sublist in results for location in sublist]
          content = {'locations': flat_list}

          cursor.close()
          cnx.close()
          return make_response(jsonify(content), 200)

      except Exception as e:
        return make_response({'error': str(e)})

    if location:
      try:
        with cnx.cursor() as cursor:
          cursor.execute("""
            select distinct roaster.name from roaster
            inner join coffee on roaster.roaster_id = coffee.roaster_id
            where location=%s
            order by name asc
            """, location)
          results = cursor.fetchall()
          flat_list = []
          
          if results:
            flat_list = [roaster for sublist in results for roaster in sublist]
        
          content = {
              'location': location, 
              'roasters': flat_list
          }

          cursor.close()
          cnx.close()
          return make_response(jsonify(content), 200)
      
      except Exception as e:
        return make_response({'error': str(e)})

class Coffee(Resource):
  """
  Coffee Resource class GET method. Returns information about a coffee. Must have a param, name, to get detail listings about coffee.
  :param name: Name of a coffee product listing
  :return: Details about said coffee
  """
  def get(self, name):
    if os.environ.get('GAE_ENV') == 'standard':
    # If deployed, use the local socket interface for accessing Cloud SQL
      unix_socket = '/cloudsql/{}'.format(db_connection_name)
      cnx = pymysql.connect(user=db_user, password=db_password,
                            unix_socket=unix_socket, db=db_name)
    else:
      print("running locally")
      db_user = config('CLOUD_SQL_USERNAME')
      db_password = config('CLOUD_SQL_PASSWORD')
      db_name = config('CLOUD_SQL_DATABASE_NAME')
      host = '127.0.0.1'
      cnx = pymysql.connect(user=db_user, password=db_password,
                            host=host, db=db_name, port=3308)

    try:
      with cnx.cursor() as cursor:
        cursor.execute("""
          select coffee.coffee_id, coffee.name, price, description, coffee.origin, coffee.type, coffee.process, coffee.roast_level, coffee.tasting_notes, roaster.name from coffee
          join roaster on roaster.roaster_id = coffee.roaster_id
          where coffee.name=%s
          """, name)
        result = cursor.fetchone()
        content = {}

        if result:
          if result[8]: # if coffee listing has info about tasting notes that are in string form, split into array
            tasting_notes = result[8].split(",")
          content = {
              'id': result[0],
              'name': result[1], 
              'price': result[2], 
              'description': result[3],
              'origin': result[4],
              'type': result[5],
              'process': result[6],
              'roastLevel': result[7],
              'tastingNotes': [s.strip() for s in tasting_notes] if result[8] else [], 
              'roaster': result[9]
          }
        else:
          cursor.close()
          cnx.close()
          return make_response({
              'error': 'coffee listing not found',
              'code': 404
          }, 404)

        cursor.close()
        cnx.close()
        return make_response(jsonify(content), 200)
    
    except Exception as e:
      return make_response({'error': str(e)})

class CoffeeByID(Resource):
  """
  Same as Coffee Resource, just by getting coffee by ID instead of its name.
  :param id: unique coffee listing str id
  :return: info about Coffee
  """
  def get(self, id):
    if os.environ.get('GAE_ENV') == 'standard':
    # If deployed, use the local socket interface for accessing Cloud SQL
      unix_socket = '/cloudsql/{}'.format(db_connection_name)
      cnx = pymysql.connect(user=db_user, password=db_password,
                            unix_socket=unix_socket, db=db_name)
    else:
      print("running locally")
      db_user = config('CLOUD_SQL_USERNAME')
      db_password = config('CLOUD_SQL_PASSWORD')
      db_name = config('CLOUD_SQL_DATABASE_NAME')
      host = '127.0.0.1'
      cnx = pymysql.connect(user=db_user, password=db_password,
                            host=host, db=db_name, port=3308)

    try:
      with cnx.cursor() as cursor:
        cursor.execute("""
          select coffee.coffee_id, coffee.name, price, description, coffee.origin, coffee.type, coffee.process, coffee.roast_level, coffee.tasting_notes, roaster.name from coffee
          join roaster on roaster.roaster_id = coffee.roaster_id
          where coffee.coffee_id=%s
          """, id)
        result = cursor.fetchone()
        content = {}

        if result:
          if result[8]:
            tasting_notes = result[8].split(",")
          content = {
              'id': result[0],
              'name': result[1], 
              'price': result[2], 
              'description': result[3],
              'origin': result[4],
              'type': result[5],
              'process': result[6],
              'roastLevel': result[7],
              'tastingNotes': [s.strip() for s in tasting_notes] if result[8] else [], 
              'roaster': result[9]
          }
        else:
          cursor.close()
          cnx.close()
          return make_response({
            'error': 'coffee id not found',
            'code': 404
          }, 404)
        
        cursor.close()
        cnx.close()

        return make_response(jsonify(content), 200)
    
    except Exception as e:
      return make_response({'error': str(e)})

class Origin(Resource):
  """
  Origin class GET method. Based on an origin (city/region/country/continent), return a list of coffees that originate from said origin. Only works for single origin coffees. If no parameter, return a list of origins where coffees in the database are from.
  :param origin: Origin of coffee
  :return: Coffees from that origin
  """
  def get(self, origin=None):
    if os.environ.get('GAE_ENV') == 'standard':
    # If deployed, use the local socket interface for accessing Cloud SQL
      unix_socket = '/cloudsql/{}'.format(db_connection_name)
      cnx = pymysql.connect(user=db_user, password=db_password,
                            unix_socket=unix_socket, db=db_name)
    else:
      print("running locally")
      db_user = config('CLOUD_SQL_USERNAME')
      db_password = config('CLOUD_SQL_PASSWORD')
      db_name = config('CLOUD_SQL_DATABASE_NAME')
      host = '127.0.0.1'
      cnx = pymysql.connect(user=db_user, password=db_password,
                            host=host, db=db_name, port=3308)
    
    if not origin:
      try:
        with cnx.cursor() as cursor:
          cursor.execute("""
            select distinct origin from coffee
            where origin NOT LIKE '%,%'
            order by origin asc;
            """)
          results = cursor.fetchall()
          flat_list = []
          content = {}
          
          if results:
            flat_list = [origin for sublist in results for origin in sublist]
            content = {'origins': flat_list}

          cursor.close()
          cnx.close()

          return make_response(jsonify(content), 200)
      
      except Exception as e:
        return make_response({'error': str(e)})

    if origin:
      try:
        with cnx.cursor() as cursor:
          cursor.execute("""
            select coffee_id, coffee.name, price, description, process, roast_level, tasting_notes, roaster.name from coffee
            join roaster on roaster.roaster_id = coffee.roaster_id
            where coffee.origin=%s
            order by coffee.name asc;
            """, origin)
          results = cursor.fetchall()
          coffee_list = []
          content = {}
          
          if results:
            for result in results:
              if result[6]:
                tasting_notes = result[6].split(",")
          
              coffee = {'id': result[0], 'name': result[1], 'price': convert_mysql_decimal_to_float(result[2]), 'description': result[3], 'process': result[4], 'roastLevel': result[5], 'tastingNotes': [s.strip() for s in tasting_notes] if result[6] else [], 'roaster': result[7]}

              coffee_list.append(coffee)
              coffee = {}
            
            content = {'coffees': coffee_list}
          else:
            cursor.close()
            cnx.close()
            return make_response({
              'error': 'origin not found in database',
              'code': 404
            }, 404)

          cursor.close()
          cnx.close()
          
          return make_response(jsonify(content), 200)

      except Exception as e:
        print("Error: ", e)
        return make_response({'error': str(e)})

api.add_resource(Roasters, '/roasters/', '/roasters/<name>', endpoint='roasters')
api.add_resource(RoastersByID, '/roasters/id/<id>', endpoint='roasterid')
api.add_resource(Location, '/locations/', '/locations/<location>', endpoint='locations')
api.add_resource(Coffee, '/coffees/<name>', endpoint='coffees')
api.add_resource(CoffeeByID, '/coffees/id/<id>', endpoint='coffeeid')
api.add_resource(Origin, '/origins/', '/origins/<origin>', endpoint='origins')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
