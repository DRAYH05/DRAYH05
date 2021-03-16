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
    datos = request.get_json()
    username = request.json['user']
    password = request.json['password']
    if username and password:
        myquery = { 'user': username, "password": password}
        x = tabla_users.find_one(myquery)
        if(x == None):
            return jsonify({'ERROR': 'usuario no encontrado'}), 400
        else:
            id = tabla_users.find_one(myquery, {'_id': 1})
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
    creasion = request.get_json()
    username = request.json['user']
    password = request.json['password']
    if username and password:
        if (tabla_users.find_one({'user':username}, {'user': 1}) == None):
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

@app.route('/visualizar_comentarios', methods=['GET'])
def ver_comentarios():
    comentario = tabla_comentarios.find({'id_hilo': ObjectId(id)})
    for x in comentario:
        print(x)
    return jsonify({}), 200

@app.route('/creacion_comentario', methods=['POST'])
def crear_comentario():
    contenido_comentario = request.json['contenido']
    if contenido_comentario:
        x = tabla_comentarios.insert({'id_hilo': id, 'contenido': contenido_comentario})
        return jsonify({'comentario creado'}), 200
    else:
        return jsonify({'ERROR': 'la creacion del comentario no fue posible'}), 400

@app.route('/borrar_comentario/<id>', methods=['DELETE'])
def delete_comentario(id):
    tabla_comentarios.delete_one({'_id': ObjectId(id)})
    return jsonify({'peticion aceptada': 'comentario eliminado'}), 200

@app.route('/eliminar_hilo', methods=['DELETE'])
def delete_hilo():
    datos = request.get_json()
    id_delete = request.json['id_hilo']
    tabla_hilos.delete_one({'id_hilo': id_delete})
    return jsonify({'peticion aceptada': 'hilo eliminado'}), 200



if __name__ == '__main__':
    app.run(debug=True)

