import pandas as pd

# Cargar los datos 
archivo = "D:/PRUEBA TECNICA_ALLIEDGLOBAL.xlsx"
base_datos = pd.read_excel(archivo, sheet_name='BBDD', engine='openpyxl')

# Crear columna TotalMoney si no existe
if 'TotalMoney' not in base_datos:
    base_datos['TotalMoney'] = base_datos['Quantity'] * base_datos['Unit Price']

# PARTE 1 => BASE RELACIONAL
# --------------------------------------
# Tabla de clientes
clients_df = base_datos[['Client']].drop_duplicates().reset_index(drop=True)
clients_df['clientID'] = clients_df.index + 1

# Tabla de productos (corregir "productID")
products_df = base_datos[['Product', 'Category']].drop_duplicates().reset_index(drop=True)
products_df["productID"] = products_df.index + 1  # ¡Corregido el typo!

# Remplazar nombres con IDs
ventas_df = base_datos.merge(clients_df, on='Client')
ventas_df = ventas_df.merge(products_df, on=['Product', 'Category'])

# Crear sales_df (corregir nombres de columnas)
sales_df = ventas_df[['Date', 'clientID', 'productID', 'Quantity', 'Unit Price', 'TotalMoney', 'Region']]
sales_df = sales_df.reset_index(drop=True)
sales_df.index.name = 'SaleID'
sales_df.reset_index(inplace=True)

# Guardar base relacional
with pd.ExcelWriter("base_datos_relacional.xlsx", engine='openpyxl') as writer:
    clients_df.to_excel(writer, sheet_name='Clients', index=False)
    products_df.to_excel(writer, sheet_name='Products', index=False)
    sales_df.to_excel(writer, sheet_name='Sales', index=False)

# PARTE 2 => ANÁLISIS BÁSICO
# --------------------------------------
# 1. Total de ingresos por región
def ingresos_por_region():
    return sales_df.groupby('Region')['TotalMoney'].sum().reset_index()

# 2. Cliente con mayor volumen de compra
def volumen_max_por_cliente():
    volumen_por_cliente = ventas_df.groupby('Client')['Quantity'].sum().reset_index() 
    cliente_top = volumen_por_cliente.sort_values(by='Quantity', ascending=False).head(1)
    return cliente_top

# 3. Ingreso promedio por categoría
def ingreso_por_categoria():
    promedio_categoria = ventas_df.groupby('Category')['TotalMoney'].mean().reset_index()
    return promedio_categoria

# PARTE 3 => CONSULTA ADICIONAL
# --------------------------------------
def producto_mas_vendido():
    # Usar ventas_df o sales_df (no products_df)
    grouped = ventas_df.groupby('Product')['Quantity'].sum().reset_index()  # ¡Corregido el DataFrame!
    producto_top = grouped.sort_values(by='Quantity', ascending=False).head(1)
    return producto_top

# Guardar análisis en Excel (ejecutar funciones con ())
with pd.ExcelWriter("resultados_analisis.xlsx", engine='openpyxl') as writer:
    ingresos_por_region().to_excel(writer, sheet_name="IngresosPorRegion", index=False)
    volumen_max_por_cliente().to_excel(writer, sheet_name="VolumenMaxPorCliente", index=False)
    ingreso_por_categoria().to_excel(writer, sheet_name="IngresoPorCategoria", index=False)
    producto_mas_vendido().to_excel(writer, sheet_name="ProductoMasVendido", index=False)

print("Archivos generados con éxito")
print("- base_datos_relacional.xlsx")
print("- resultados_analisis.xlsx")