# def imprimir_mensaje():
#     print('Mensaje especial:')
#     print('Estoy aprendiendo a usar funciones')
#
#
# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()


def conversacion(mensaje):
    print('Hola')
    print('Como estas')
    print(mensaje)
    print('Adios')

opcion = input('Elije una ipcion (1,2,3): ')
if opcion =='1':
    conversacion('Elegiste la opcion 1')
elif opcion =='2':
    conversacion('Elegiste la opcion 2')
elif opcion == '3':
    conversacion('Elegiste la opcion 3')
else:
    print('Escribe la opcion correcta')
