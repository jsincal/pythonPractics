menu = """"
Bienvenido al conversor de monedas 💰🪙💲🤑

1 - Pesos colombianos
2 - Pesos colombianos
3 - Pesos argentinos

Elige una opcion: """

opcion = input(menu)

if opcion == '1':
    pesos = input("Cuantos pesos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 7.78
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" +dolares +" Dolares")
elif opcion == '2':
    pesos = input("Cuantos pesos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" +dolares +" Dolares")
elif opcion == '3':
    pesos = input("Cuantos pesos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" +dolares +" Dolares")
else:
    print("Elija una opcion correcta.")
