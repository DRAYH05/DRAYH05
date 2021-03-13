import os


def menu():
    os.system('cls')
    print('[1] Login')
    print('[2] Crear cuenta')
    print('[3] Ver hilos')
    print('[4] Nuevo hilo')
    print('[0] Salir')


def menu_loged():
    os.system('cls')
    print('Usuario: 'User)
    print('[2] Crear cuenta')
    print('[3] Ver hilos')
    print('[4] Nuevo hilo')
    print('[0] Salir')

def menu_hilos():
    # comentario 1
    # comentario 2
    print('[1] Nuevo Comentario')
    print('[0] Volver')


Salir = False

while not Salir:

    # mostrar el menu
    menu()

    OpcionAdmin = int(input('Elija una opcion: '))

    if OpcionAdmin == 1:
        User = str(input('Usuario: '))
        password = str(input('Contraseña: '))


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