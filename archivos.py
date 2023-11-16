# Esta es la capa de archivos, es la más cercana al csv
# y se dedica a leer y escribir en el archivo

def lee_rodales(archivo_rodales:str) -> dict:
    # Lee rodales.csv y retorna un diccionario en donde la 
    # clave es el nombre del cliente y el contenido es una lista con la 
    # dirección, el teléfono y el monto adeudado, si no está, lo crea
    ...
def escribe_rodales(file_clientes:str, DICC_RODALES: dict) -> bool:
    # Lee rodales.csv en el formato indicado y retorna True si salió
    # correctamente, este booleano se usa en la nube
    ...

if __name__ == "__main__":
    test()