from flask import Flask, jsonify, request, abort
import json
import requests
import jwt
import time
import pymongo
from datetime import datetime, timedelta
from functools import wraps
application = Flask(__name__)

API_URL = 'http://127.0.0.1:27018/'
API_ENDPOINT = "http://localhost:27018/posts"

respuesta = requests.get(url=API_ENDPOINT) 

posts=[]

option_no_valid = 'Uyy casi pero no. Vuelve a intentarlo'

@application.route('/')
def root():
    return 'La API está Levantada'

#creacion del usuario admin.

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["proyecto"]
tabla = mydb["Usuarios"]

#insertar_fila = { "Usuario": "Jesus", "contrasena": "6666", "Admin": "chi"}
#x = mycol.insert_one(mydict)

#query = {'user': 'Jesus', 'pass': '6666'}
#projection = {'is_admin': 1}
#result = mydb.Usuarios.find_one(query, projection)
#print(result)
#for x in tabla.find({},{ "name": 1, "address": 0 }):
#  print(x)

@application.route('/posts', methods=['GET'])
def get_posts():

    posts = []
    with open('data/posts.json', 'r') as json_file:
        posts = json.load(json_file)
    return jsonify(posts), 200


if __name__ == '__main__':
    application.run(debug=True)