import os


def menu():
    os.system('cls')
    print('Usuario: ' + user)
    print('[1] Login')
    print('[2] Crear cuenta')
    print('[3] Ver hilos')
    print('[4] Nuevo hilo')
    print('[0] Salir')


def menu_hilos_Admin():
    # comentario 1
    # comentario 2
    print('[1] Nuevo Comentario')
    print('[0] Volver')


Salir = False

while not Salir:

    # mostrar el menu
    menu()

    OpcionAdmin = int(input('Elija una opcion: '))

    if opcion == 1:
        user = input('Usuario: ')
        password = input('Contraseña: ')


    elif opcion == 2:
        user = input('Usuario: ')
        password = input('Contraseña: ')
        pass1 = input('Repite contraseña: ')

    elif opcion == 3:
        Salir_hilos = False
        os.system('cls')
        while not Salir_hilos:
            menu_hilos_Admin()
            opcion1 = int(input('Elija una opcion: '))
            if opcion1 == 0:
                Salir_hilos = True
            #si estas registrado creas un nuevo comentario

    elif opcion == 0:
        Salir = True
