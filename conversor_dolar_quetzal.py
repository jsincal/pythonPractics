dolares = input("Cuantos Dolares tienes?: ")
dolares = float(dolares)
valor_quetzal = 0.12852
quetzales = dolares / valor_quetzal
quetzales = round(quetzales, 2)
quetzales = str(quetzales)
print("Tienes Q" +quetzales +" Dolares")