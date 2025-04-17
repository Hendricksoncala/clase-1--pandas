import pandas as pd

# Cargar los datos (versión actualizada)
base_datos = pd.read_excel(
    r"D:\PRUEBA TECNICA_ALLIEDGLOBAL.xlsx",
    sheet_name='BBDD',
    engine='openpyxl'
)

# 🧹 Eliminar columnas completamente vacías
base_datos = base_datos.dropna(axis=1, how='all')

# 🧽 Limpiar nombres de columnas (quitar espacios, puntos, etc.)
base_datos.columns = base_datos.columns.str.strip().str.replace(".", "", regex=False)

# Crear columna totalmoney
if "TotalMoney" not in base_datos:
    base_datos["TotalMoney"] = base_datos['Quantity'] * base_datos['Unit Price']

# Función para mostrar el DataFrame
def ver_dataframe():
    print("\nDataFrame completo:")
    print(base_datos)

# Función para filtrar por región
def datos_por_region():
    print("\nRegiones disponibles:", base_datos['Region'].unique())
    region = input("Ingresa la región a filtrar (North/South/East/West): ").capitalize()
    filtro = base_datos[base_datos['Region'] == region]
    print(f"\nDatos para la región {region}:")
    print(filtro)

# Función para totales por categoría
def datos_por_categoria():
    print("\nTotal de ventas por categoría:")
    print(base_datos.groupby('Category')['TotalMoney'].sum())

# Menú interactivo mejorado
def menu_principal():
    while True:
        print('\n--- Menú de Análisis ---')
        print("1. Ver datos completos")
        print("2. Filtrar por región")
        print("3. Ver totales por categoría")
        print("4. Salir")
        
        opcion = input('Selecciona una opción (1-4): ').strip()
        
        if opcion == "1":
            ver_dataframe()
        elif opcion == "2":
            datos_por_region()
        elif opcion == "3":
            datos_por_categoria()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor ingresa un número del 1 al 4.")

# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()