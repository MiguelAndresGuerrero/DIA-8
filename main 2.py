#saludar al usuario y darle la bienvenida
name = input("Ingresa tu nombre: ")
print("Bienvenido", name)

# Definir un diccionario con información de frutas (nombre, precio, cantidad)
frutas = {
    'manzana': (0.75, 50),
    'banana': (0.35, 100),
    'pera': (0.60, 30),
    'naranja': (0.40, 70),
    'kiwi': (0.90, 80)
}

# Convertir todos los nombres de frutas a mayúsculas
Fru_Mayus = {fruta.upper(): info for fruta, info in frutas.items()}

# Imprimir el nombre de las frutas con precio inferior a 0.50
print("Frutas con precio inferior a 0.50:")
for fruta, (precio, cantidad) in frutas.items():
    if precio < 0.50:
        print(fruta)

# buscamos la fruta con mayor cantidad en stock
fruta_max_stock = max(frutas, key=lambda x: frutas[x][1])
print("Fruta con la máxima cantidad en stock:", fruta_max_stock)

# Ordenar las frutas de manera decreciente por el valor en stock
frutas_ordenadas = sorted(frutas.items(), key=lambda x: x[1][0] * x[1][1], reverse=True)

# creado por Miguel Guerrero C.C 1090381839