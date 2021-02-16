import os


def menu():
    os.system('cls')
    print('[1] Login')
    print('[2] Crear cuenta')
    print('[3] Ver hilos')
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

    opcion = int(input('Elija una opcion: '))

    if opcion == 1:
        Usuario = input('Usuario: ')
        Contraseña = input('Contraseña: ')
        if Usuario == 1:  # Usuario o contraseña incorrectos
            print('Usuario o contraseña incorrectos')
        else:
            print('Usuario: ')
            print('[1] Login')
            print('[2] Crear cuenta')
            print('[3] Ver hilos')
            print('[4] Nuevo hilo')
            print('[0] Salir')
            print('elija opcion: ')

    elif opcion == 2:
        Usuario = input('Usuario: ')
        Contraseña = input('Contraseña: ')
        Contraseña1 = input('Repite contraseña: ')

    elif opcion == 3:
        Salir_hilos = False
        os.system('cls')
        while not Salir_hilos:
            menu_hilos()
            opcion1 = int(input('Elija una opcion: '))
            if opcion1 == 0:
                Salir_hilos = True
            #if si estas registrado creas un nuevo comentario

    elif opcion == 0:
        Salir = True
