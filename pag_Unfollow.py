print('[1] Login')
print('[2] Crear cuenta')
print('[3] Ver hilos')
print('[0] Salir')
opcion = int(input('Elija una opcion: '))

if opcion == 1:
    Usuario = input('Usuario: ')
    Contraseña = input('Contraseña: ')
    if  Usuario == 1: #Usuario o contraseña incorrectos
        print('Usuario o contraseña incorrectos')
    else:
        print('Usuario: ')
        print('[1] Login')
        print('[2] Crear cuenta')
        print('[3] Ver hilos')
        print('[4] Nuevo hilo')
        print('[0] Salir')
        print('elija opcion: ')


if opcion == 2:
    Usuario = input('Usuario: ')
    Contraseña = input('Contraseña: ')
    Contraseña1 = input('Repite contraseña: ')


if opcion == 3:
    #comentario 1
    #comentario 2
    print('[1] Nuevo Comentario')
    print('[0] Volver')


if opcion == 4:
    exit