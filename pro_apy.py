from flask import Flask, jsonify, request, abort
import json
import time
from datetime import datetime, timedelta
from functools import wraps
import pymongo
from bson import json_util
from bson.objectid import ObjectId
app = Flask(__name__)
app.config['API_MONGO'] = "mongodb://localhost:27017/"


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["proyecto"]
tabla_users = mydb["Usuarios"]
tabla_hilos = mydb['Hilos']
tabla_comentarios = mydb['Comentarios']

@app.route('/')
def root():
    return'API levantada'


def obtener_id():
    

def comprobar_admin():
    query = {'user': username, 'pass': password}
    projection = {'is_admin': 1}
    result = mydb.Usuarios.find_one(query, projection)
    if(result == True):
      print(result)

@app.route('/crear_usuario', methods=['POST'])
def crear_usuarios():
    username = request.json['User']
    password = request.json['pass']
    if username and password:
        x = tabla_users.insert({'User':username, 'pass':password, 'is_admin': False})
        return jsonify({'usuario creado'}), 200
    else:
        return jsonify({'ERROR': 'la creacion del usuario especificado no fue posible'}), 400

@app.route('/login', methods=['GET'])
def busqueda_usuario():
    username = request.json['User']
    password = request.json['pass']
    if username and password:
        myquery = { 'user': username, "pass": password}
        x = tabla.find_one(myquery)
        if(x == None):
            return jsonify({'ERROR': 'usuario no encontrado'}), 400
        else:
            return jsonify({'sesion actual':username}), 200
    else:   
        return jsonify({'ERROR': 'rellene todos los campos'}), 400


@app.route('/ver_hilos', methods=['GET'])
def todos_hilos():
    for x in tabla_hilos.find({}, {'_id': 1, 'User': 1, 'pass':1}):
        print(x)

@app.route('/ver_hilos/<id>', methods=['GET'])
def ver_hilo(id):
    hilo = tabla_hilos.find_one({'_id': ObjectId(id)})
    return jsonify({'peticion aceptada': '\n' + hilo}), 200

@app.route('/ver_hilos/<id>', methods=['DELETE'])
def delete_hilo(id):
    hilo = tabla_hilos.delete_one({'_id': ObjectId(id)})
    return jsonify({'peticion aceptada': 'usuario eliminado'}), 200

@app.route('/creacion_hilo', methods=['POST'])
def crear_hilo():
    






if __name__ == '__main__':
    app.run(debug=True)

