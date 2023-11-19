# Esta es la capa de lógica, donde están las FUNCIONES y VALIDACIONES

import archivos as ar # se importa la capa de datos

global DICC_RODALES
global DICC_COLINDANCIAS

ARCHIVO_R = 'rodales.csv'
ARCHIVO_C = 'colindancias.csv'

def lee_archivo_rodales():
    global DICC_RODALES
    """invoca la lectura de archivo en la capa de datos, deja datos 
    la variable local DICC_RODALES"""
    DICC_RODALES = ar.lee_rodales(ARCHIVO_R)

def lee_archivo_colindancias():
    global DICC_COLINDANCIAS
    """invoca la lectura de archivo en la capa de datos, deja datos 
    la variable local DICC_COLINDANCIAS"""
    DICC_COLINDANCIAS = ar.lee_colindancias(ARCHIVO_C)

def validar_rodal():
    ...
def validar_porcentaje():
    ...
def consulta_un_rodal():
    ...
def consulta_rango_rodales():
    ...
def consultar_colindantes():
    ...
def obtener_bosque():
    ...
def obtener_propietario():
    ...
def obtener_colindantes():
    ...
def traducir_rango():
    ...
def colindantes_en_riesgo():
    ...
def calcular_hectarea():
    ...
def filtrar_por_propietario():
    ...
def agregar_rodal():
    ...
def simular_incendio():
    ...
def consultar_rodal():
    ...
def consultar_hectarea():
    ...
def consultar_hect_propietario():
    ...
def consulta_rango_rodales():
    ...

def test():
    lee_archivo_rodales()
    lee_archivo_colindancias()

if __name__ == "__main__":
    test()