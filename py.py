import pandas as pd
import json
import os

ARCHIVO_JSON = "json.json"
All_data = "ALLIEN.json"

# Leer los datos existentes del archivo
def cargar_datos():
    if os.path.exists(All_data):
        with open(All_data, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return []

# Guardar datos en el archivo JSON
def guardar_datos(datos):
    with open(All_data, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

# Convertir la lista de diccionarios a DataFrame
datos = cargar_datos()
df = pd.DataFrame(datos)

# Agregar un nuevo usuario
def agregar_usuarios():
    print("\nIngresa los datos del nuevo usuario:")
    Date = (input("Fecha(MM/DD/AAAA): "))
    Client = input("Nombre: ")
    Product = (input("Producto: "))
    Category = input("Categoria (escribe de la A a la D): ")
    Quantity = int(input("Cantidad: "))
    Unit_Price = float(input("Precio Unidad: "))
    Region = input("Region: ")
    TotalMoney = (Quantity * Unit_Price)

    nuevo_usuario = {
        'Date': Date,
        'Client': Client,
        'Product': Product,
        "Category" : Category,
        "Quantity" : Quantity,
        "Unit_Price" : Unit_Price,
        "Region" : Region,
        "TotalMoney" : TotalMoney


    }

    global df
    df = pd.concat([df, pd.DataFrame([nuevo_usuario])], ignore_index=True)
    guardar_datos(df.to_dict(orient='records'))  # Guardar en el archivo JSON
    print('\n¡Usuario Agregado!')


def calcular_ingresos_por_region():
    # Agrupar por región y sumar los TotalMoney
    ingresos_region = df.groupby('Region')['TotalMoney'].sum().reset_index()
    
    # Mostrar los resultados
    print("\nTotal de ingresos por región:")
    print(ingresos_region.to_string(index=False))



def calcular_ingresos_por_region_mayor_a_menor():
    ingresos_region = df.groupby('Region')['TotalMoney'].sum().reset_index()
    ingresos_region = ingresos_region.sort_values('TotalMoney', ascending=False)
    
    print("\nTotal de ingresos por región (ordenado de mayor a menor):")
    print(ingresos_region.to_string(index=False))
# Menú principal
while True:
    print('\n--- Menú ---')
    print("1. Ver DataFrame")
    print("2. Agregar usuario")
    print("3. Salir")
    print("4. Total money por dinero y region...")
    print("5. Menos a mayor totalMoney.")
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
        calcular_ingresos_por_region()
    elif opcion == "5":
        calcular_ingresos_por_region_mayor_a_menor()
    else:
        print("Opción no válida, intenta de nuevo.")
