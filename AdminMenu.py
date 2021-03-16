import os
import requests
import pymongo
API_URL = 'http://127.0.0.1:5000/'


def comprobar_admin():
    query = {'user': username, 'password': password}
    projection = {'is_admin': 1}
    result = mydb.Usuarios.find_one(query, projection)
    #if (result == true):
        #........


def menu():
    os.system('cls')
    print('[1] Login')
    print('[2] Crear cuenta')
    print('[3] Ver hilos')
    print('[4] Nuevo hilo')
    print('[0] Salir')


def menu_loged():
    admin_option = int(input('\nopcion: '))
    os.system('cls')
    print('Usuario: ' + user)
    print('[1] Login')
    print('[2] Crear cuenta')
    print('[3] Ver hilos')
    print('[4] Nuevo hilo')
    print('[0] Salir')

def login():
    user = str(input('usuario: '))
    password = str(input('contraseña: '))
    loginn = {'user':user, 'password': password}
    prueba = requests.get(API_URL + 'login', json = loginn)
    if prueba.status_code == 200:
        print('todo gucci')
        input(' ')
    else:
        print('error amigo T_T')
        input(' ')


Salir = False

while not Salir:

    # mostrar el menu
    menu()

    OpcionAdmin = int(input('Elija una opcion: '))

    if OpcionAdmin == 1:
        login()


    elif OpcionAdmin == 2:
        User = str(input('Usuario: '))
        password = str(input('Contraseña: '))
        password1 = str(input('Repite contraseña: '))

    elif OpcionAdmin == 3:
        Salir_hilos = False
        os.system('cls')
        while not Salir_hilos:
            menu_hilos()
            opcion1 = int(input('Elija una opcion: '))
            if opcion1 == 0:
                Salir_hilos = True
            #si estas registrado creas un nuevo comentario

    elif OpcionAdmin == 0:
        Salir = True
