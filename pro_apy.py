from flask import Flask, jsonify, request, abort
import json
import pymongo
from werkzeug.security import generate_password_hash, check_password_hash
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
    print('vuelva a introducir sus credenciales: ')
    username = request.json['user']
    password = request.json['password']
    if username and password:
        myquery = { 'user': username, "password": password}
        x = tabla.find_one(myquery)
        return jsonify({}), 200
        if(x == None):
            return jsonify({'ERROR': 'usuario no encontrado'}), 400
        else:
            id = tabla.find_one(myquery)
            return jsonify({}), 200
    else:   
        return jsonify({'ERROR': 'rellene todos los campos'}), 400
    

#def comprobar_admin():
    #username = request.json['user']
    #password = request.json['password']
    #query = {'user': username, 'password': password}
    #projection = {'is_admin': 1}
    #result = mydb.Usuarios.find_one(query, projection)
    #if (result == true):
        #........
    

@app.route('/crear_usuario', methods=['POST'])
def crear_usuarios():
    username = request.json['user']
    password = request.json['password']
    if username and password:
        if (tabla_users.find({'user':username}, {'user': 1}) == None):
            x = tabla_users.insert({'user':username, 'password':password, 'is_admin': False})
            return jsonify({}), 200
        else:
            return jsonify({'ERROR': 'usuario repetido'}), 400
    else:
        return jsonify({'ERROR': 'la creacion del usuario especificado no fue posible'}), 400

@app.route('/login', methods=['GET'])
def busqueda_usuario():
    login = request.get_json()
    username = request.json['user']
    password = request.json['password']
    if username and password:
        myquery = { 'user': username, "password": password}
        x = tabla_users.find_one(myquery)
        if(x == None):
            return jsonify({'ERROR': 'usuario no encontrado'}), 400
        else:
            return jsonify({}), 200
    else:   
        return jsonify({'ERROR': 'rellene todos los campos'}), 400


@app.route('/ver_hilos', methods=['GET'])
def todos_hilos():
    for x in tabla_hilos.find({}, {'_id': 1, 'user': 1, 'password':1}):
        print(x)
    return jsonify({}), 200

@app.route('/ver_hilos/<id>', methods=['GET'])
def ver_hilo(id):
    hilo = tabla_hilos.find_one({'_id': ObjectId(id)})
    for x in hilo:
        print(x)
    return jsonify({}), 200

@app.route('/borrar_hilos/<id>', methods=['DELETE'])
def delete_hilo(id):
    hilo = tabla_hilos.delete_one({'_id': ObjectId(id)})
    return jsonify({'peticion aceptada': 'usuario eliminado'}), 200

@app.route('/creacion_hilo', methods=['POST'])
def crear_hilo():
    obtener_id()
    nombre_hilo = request.json['nombre']
    contenido = request.json['contenido']
    if nombre_hilo and contenido:
        x = tabla_hilos.insert({'nombre':nombre_hilo, 'id_usuario': id, 'contenido': contenido})
        return jsonify({'hilo creado'}), 200
    else:
        return jsonify({'ERROR': 'la creacion del hilo no fue posible'}), 400

@app.route('/visualizar_comentarios', methods=['GET'])
def ver_comentarios():
    ver_hilo()
    comentario = tabla_comentarios.find({'id_hilo': ObjectId(id)})
    for x in comentario:
        print(x)
    return jsonify({}), 200

@app.route('/creacion_comentario', methods=['POST'])
def crear_comentario():
    ver_hilo()
    contenido_comentario = request.json['contenido']
    if contenido_comentario:
        x = tabla_comentarios.insert({'id_hilo': id, 'Ccontenido': contenido_comentario})
        return jsonify({'comentario creado'}), 200
    else:
        return jsonify({'ERROR': 'la creacion del comentario no fue posible'}), 400

@app.route('/borrar_comentario/<id>', methods=['DELETE'])
def delete_comentario(id):
    comentario = tabla_comentarios.delete_one({'_id': ObjectId(id)})
    return jsonify({'peticion aceptada': 'usuario eliminado'}), 200

if __name__ == '__main__':
    app.run(debug=True)

