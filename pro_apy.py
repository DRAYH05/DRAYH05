from flask import Flask, jsonify, request, abort
import json
import jwt
import time
import pymongo
from datetime import datetime, timedelta
from functools import wraps
application = Flask(__name__)

@application.route('/')
def root():
    return 'La API está Levantada'

#creacion del usuario admin.

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["proyecto"]
tabla = mydb["Usuarios"]

#insertar_fila = { "Usuario": "Jesus", "contrasena": "6666", "Admin": "chi"}
#x = mycol.insert_one(mydict)

query = {'user': 'Jesus', 'pass': '6666'}
projection = {'is_admin': 1}
result = mydb.Usuarios.find_one(query, projection)
print(result)
#for x in tabla.find({},{ "name": 1, "address": 0 }):
#  print(x)

