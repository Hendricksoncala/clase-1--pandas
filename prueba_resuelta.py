import pandas as pd

#Cargar los datos 
archivo = "D:/PRUEBA TECNICA_ALLIEDGLOBAL.xlsx"
base_datos = pd.read_excel(archivo, sheet_name='BBDD', engine='openpyxl')

#Crear una columna de TotalMoney si no existe
if 'TotalMoney' not in base_datos:
    base_datos['TotalMoney'] = base_datos['Quantity'] * base_datos['Unit Price']

#PARTE 1 => BASE RELACIONAL

# Tabla de clientes
clients_df = base_datos[['Client']].drop_duplicates().reset_index(drop=True)
clients_df['clientID'] = clients_df.index + 1

#Tabla de productos 
products_df = base_datos[['Product','Category']].drop_duplicates().reset_index(drop=True)
products_df["prodcutID"] = products_df.index + 1

#Remplazar nombres con IDs
ventas_df = base_datos.merge(clients_df, on='Client')
ventas_df = ventas_df.merge(products_df, on=['Product', 'Category'])

sales_df = ventas_df[['Date', 'ClientID', 'ProductID', 'Quantity', 'Unit Price', 'TotalMoney', 'Region']]
sales_df = sales_df.reset_index(drop=True)
sales_df.index.name = 'SaleID'
sales_df.reset_index(inplace=True)

with pd.ExcelWriter("base_datos_relacional.xlsx", engine='openpyxl') as writer:
    clients_df.to_excel(writer, sheet_name='Clients', index=False)
    products_df.to_excel(writer, sheet_name='Products', index=False)
    sales_df.to_excel(writer, sheet_name='Sales', index=False)


#PARTE 2 => ANALISIS BASICO

# 1. Total de ingresos por region
def ingresos_por_region():
    sales_df.groupby('Region')['TotalMoney'].sum().reset_index()

# 2. Cliente con mayor volumen de compra
def volumen_max_por_cliente(): 
    volumen_por_cliente = ventas_df.groupby('Client')[('Quantity')].sum().reset_index()
    cliente_top = volumen_por_cliente.sort_values(by='Quantity',ascending=False).head(1)
    
# 3. Ingreso promedio por categoria
def ingreso_por_categoria():
    ventas_df[['Category','TotalMoney']]
    promedio_categoria = ventas_df.groupby('Category')['TotalMoney'].mean().reset_index()
