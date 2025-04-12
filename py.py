import pandas as pd
import json

# data = {
#     'Nombre': ['Juan', 'Ana', 'Luis', 'Laura'],
#     'Edad': [25, 33, 30, 28],
#     'Ciudad': ['Barcelona', 'Madrid', 'New York', 'Valencia']
# }

# df = pd.DataFrame(data)

#Leer los datos existentes del archivo
def cargar_datos():
    with open("json.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)

#Guardar datos del archivo
def guardar_datos(datos):
    with open("json.json", "w", encoding="utf-8") as archivo:
        return json.load(archivo)
    
#Agregar un nuevo cliente
def agregar_usuarios():
    print("\nIngresa los datos del nuevo usuario:")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    ciudad = input("Ciudad: ")

    nuevo_usuario = {
        'Nombre': nombre,
        'Edad': edad,
        'Ciudad': ciudad
    }

    global df
    df = pd.concat([df, pd.DataFrame([nuevo_usuario])], ignore_index=True)  # Coma eliminada
    print('\n¡Usuario Agregado!')

while True:
    print('\n--- Menú ---')
    print("1. Ver DataFrame")
    print("2. Agregar usuario")
    print("3. Salir")
    opcion = input('Selecciona una opción: ')

    if opcion == "1":
        print('\nDataFrame actual:')
        print(df)
    elif opcion == "2":
        agregar_usuarios()
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")