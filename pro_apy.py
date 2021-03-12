from flask import Flask, jsonify, request
import pymongo
import json
import requests
import jwt
import time
from datetime import datetime, timedelta
from functools import wraps
import AdminMenu

#application = Flask(__name__)

#API_URL = 'http://127.0.0.1:5000/'

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["proyecto"]
tabla = mydb["Usuarios"]

#@application.route('/posts', methods=['GET'])
#def get_posts():

query = {'user': User, 'pass': password}
projection = {'is_admin': 1}
result = mydb.Usuarios.find_one(query, projection)
if(result == True):
   AdminMenu.__file__