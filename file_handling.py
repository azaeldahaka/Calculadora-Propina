import os

def guardar_facturas(facturas):
    # Ruta de la carpeta para almacenar el archivo txt
    ruta_carpeta = "C:/Users/Usuario/git/RepoCalcuPropina/Calculadora-Propina/facturas"

    # Crear la carpeta si no existe
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

    # Ruta del archivo txt
    ruta_archivo = os.path.join(ruta_carpeta, "facturas.txt")

    # Escribir las facturas en el archivo
    with open(ruta_archivo, "w") as archivo:
        for factura in facturas:
            factura_formateada = ",".join([f"{valor:.2f}" for valor in factura])
            archivo.write(f"{factura_formateada}\n")

def cargar_facturas():
    # Ruta de la carpeta para almacenar el archivo txt
    ruta_carpeta = "C:/Users/Usuario/git/RepoCalcuPropina/Calculadora-Propina/facturas"

    # Ruta del archivo txt
    ruta_archivo = os.path.join(ruta_carpeta, "facturas.txt")

    # Verificar si el archivo existe
    if os.path.exists(ruta_archivo):
        # Leer las facturas desde el archivo
        with open(ruta_archivo, "r") as archivo:
            facturas = [linea.strip().split(",") for linea in archivo.readlines()]
            facturas_formateadas = [[float(valor) for valor in factura] for factura in facturas]
            return facturas_formateadas
    else:
        return []
