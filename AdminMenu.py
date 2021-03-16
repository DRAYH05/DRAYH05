import os
import requests
import pymongo
API_URL = 'http://127.0.0.1:5000/'

user = None
def comprobar_admin():
    query = {'user': username, 'password': password}
    projection = {'is_admin': 1}
    result = mydb.Usuarios.find_one(query, projection)
    #if (result == true):
        


def menu():
    os.system('cls')
    print('[1] Login')
    print('[2] Crear cuenta')
    print('[3] Ver hilos')
    print('[4] eliminar hilo')
    print('[0] Salir')



def login():
    user = str(input('usuario: '))
    password = str(input('contraseña: '))
    loginn = {'user':user, 'password': password}
    prueba = requests.get(API_URL + 'login', json = loginn)
    if prueba.status_code == 200:
        print('todo gucci, usuario conectado: ' + user)
        input(' ')
    else:
        print('error amigo T_T, vuelve a intentarlo')
        input(' ')

def creacion_cuenta():
    user = str(input('introduzca un nuevo usuario:' ))
    password = str(input('introduzca una nueva contraseña para el usuario nuevo: ' ))
    password1 = str(input('repita la contraseña: '))
    if password != password1:
        print('error, las contraseñas no coninciden')
        input(' ')
    else:
        creasion = {'user':user, 'password': password}
        prueba = requests.post(API_URL + 'crear_usuario', json = creasion)
        if prueba.status_code == 200:
            print('usuario creado')
            input(' ')

    


def ver_hilos():
    print("[1]- Python")
    print("[2]- AWS")
    print("[3]- Acceso a Datos")
    print("[4]- Borrar comentario")
    print("[5]- Añadir comentario")
    opciones = int(input('elija opcion: '))
    if opciones == 1:
        id_comen = '1'
        requests.get(API_URL + 'visualizar_comentarios/' + id_comen)
        input('')
    elif opciones == 2:
        id_comen = '2'
        requests.get(API_URL + 'visualizar_comentarios/' + id_comen)
        input('')
    elif opciones == 3:
        id_comen = '3'
        requests.get(API_URL + 'visualizar_comentarios/' + id_comen)
        input('')
    elif opciones == 4:
        id_comen = str(input('introduzca el id del comentario a eliminar: '))
        requests.delete(API_URL + 'borrar_comentario/' + id_comen)
    elif opciones == 5:
        id_comen = str(input('introduce el id del hilo que quieres comentar: '))
        comentario = str(input('introduce el comentario en cuestion: '))
        creasion = {'id_hilo':id_comen, 'contenido': comentario}
        prueba = requests.post(API_URL + 'creacion_comentario', json = creasion)
        if prueba.status_code == 200:
            print('comentario creado')
        else:
            print('comentario no creado')

        


def eliminar_hilo():
    id_delete = input('id del hilo a eliminar ')
    delete_hilo = {'id_hilo': id_delete}
    prueba = requests.delete(API_URL + 'eliminar_hilo', json = delete_hilo)
    if prueba.status_code == 200:
        print('hilo eliminado')
        input(' ')
    else :
        print('error')
        input('')

Salir = False

while not Salir:

    # mostrar el menu
    menu()
    OpcionAdmin = int(input('Elija una opcion: '))

    if OpcionAdmin == 1:

        login()

    elif OpcionAdmin == 2:

        creacion_cuenta()

    elif OpcionAdmin == 3:

        ver_hilos()

    elif OpcionAdmin == 4:

        eliminar_hilo()

    elif OpcionAdmin == 0:
        Salir = True
