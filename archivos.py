# Esta es la capa de archivos, es la más cercana al csv
# y se dedica a leer y escribir en el archivo
import os

def lee_rodales(archivo_rodales:str) -> dict:
    DICC_RODALES = {}
    if os.path.exists("rodales.csv"): # si existe el archivo, lo abre y lo lee.
        with open("rodales.csv", 'r') as archivo:
            lista = archivo.readlines()
    else:
        with open("rodales.csv", 'w'): # si no existe el archivo, lo crea.
            pass
    return DICC_RODALES

def escribe_rodales(archivo_rodales:str, DICC_RODALES: dict) -> bool:
    """escribe archivo de clientes en formato indicado, retorna 
    True si se hizo exitosamente y False si no"""
    ...

def lee_colindancias(archivo_colindancias:str) -> dict:
    DICC_COLINDANCIAS = {}
    if os.path.exists("colindancias.csv"):
        with open("colindancias.csv", 'r') as archivo:
            lista = archivo.readlines()
    else:
        with open("colindancias.csv", 'w'):
            pass
    return DICC_COLINDANCIAS

def escribe_colindancias(archivo_colindancias:str) -> dict:
    """escribe archivo de clientes en formato indicado, retorna 
    True si se hizo exitosamente y False si no"""
    ...
 


def test():
    # Esta función prueba las funciones de este módulo
    ...

if __name__ == "__main__":
    test()
