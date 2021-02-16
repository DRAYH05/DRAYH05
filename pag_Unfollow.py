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
    Usuario = int(input('Usuario: '))
    Contraseña = int(input('Contraseña: '))
    Contraseña1 = int(input('Repite contraseña: '))
