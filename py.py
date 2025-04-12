import pandas as pd
import json
import os

ARCHIVO_JSON = "json.json"

# Leer los datos existentes del archivo
def cargar_datos():
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return []

# Guardar datos en el archivo JSON
def guardar_datos(datos):
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

# Convertir la lista de diccionarios a DataFrame
datos = cargar_datos()
df = pd.DataFrame(datos)

# Agregar un nuevo usuario
def agregar_usuarios():
    print("\nIngresa los datos del nuevo usuario:")
    Nombre = input("Nombre: ")
    Edad = int(input("Edad: "))
    Compras = input("Compras (escribe una sola por ahora): ")

    nuevo_usuario = {
        'Nombre': Nombre,
        'Edad': Edad,
        'Compras': Compras
    }

    global df
    df = pd.concat([df, pd.DataFrame([nuevo_usuario])], ignore_index=True)
    guardar_datos(df.to_dict(orient='records'))  # Guardar en el archivo JSON
    print('\n¡Usuario Agregado!')


def filtrar_usuarios():
    print("que lo que")

# Menú principal
while True:
    print('\n--- Menú ---')
    print("1. Ver DataFrame")
    print("2. Agregar usuario")
    print("3. Salir")
    print("4. Filtrar usuarios por...")
    opcion = input('Selecciona una opción: ')

    if opcion == "1":
        print('\nDataFrame actual:')
        print(df)
    elif opcion == "2":
        agregar_usuarios()
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    elif opcion == "4":
        filtrar_usuarios()
    else:
        print("Opción no válida, intenta de nuevo.")
