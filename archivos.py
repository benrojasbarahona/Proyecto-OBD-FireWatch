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

def generar_archivos(directorio_archivos: str = 'archivos'):
    '''Esta función crea los archivos en caso de que no existan'''

    # Crea (en caso de que no exista) el archivo rodales.csv
    try:
        with open(f'{directorio_archivos}/rodales.csv', 'x', encoding = 'utf-8'):
            print('< El archivo rodales.csv ha sido generado >')
            rodales_generado = True
    except FileExistsError: rodales_generado = False

    # Crea (en caso de que no exista) el archivo colindancias.csv
    try:
        with open(f'{directorio_archivos}/colindancias.csv', 'x', encoding = 'utf-8'):
            colindancias_generado = True
            print('< El archivo colindancias.csv ha sido generado >\n')
    except FileExistsError: colindancias_generado = False
    
    # Si el archivo rodales.csv fue recien generado, escribir headers
    if rodales_generado:
        with open(f'{directorio_archivos}/rodales.csv', 'w', encoding = 'utf-8') as archivo:
            archivo.write("# rodal %nativo %exotico propietario\n")

    # Si el archivo colindancias.csv fue recien generado, escribir headers
    if colindancias_generado:
        with open(f'{directorio_archivos}/colindancias.csv', 'w', encoding = 'utf-8') as archivo:
            archivo.write("# rodal_nuevo rodal_existente orientacion\n")


def construir_diccionario(directorio_archivos: str = 'archivos') -> dict:
    """El trabajo de esta función es para cada inicio del programa, leer el archivo para
    reconstruir el diccionario que contiene la información de todos los rodales registrados
    por el usuario"""

    temp_colindancias = dict()
    dicc_rodales = dict()

    # Armar el diccionario temporal de colindancias
    with open(f'{directorio_archivos}/colindancias.csv', 'r', encoding = 'utf-8') as archivo:
        linea = archivo.readlines()
    
    for colindancia in linea[1:]:
        datos = colindancia.split(",")

        if datos[0].strip("'") not in temp_colindancias:
            temp_colindancias[datos[0].strip("'")] = {'N': '', 'NW': '', 'NE': '', 'S': '', 'SW': '', 'SE': ''}

        temp_colindancias[datos[0].strip("'")][datos[2].strip().strip("'")] = datos[1].strip("'")

    # Extraer los datos de los rodales
    with open(f'{directorio_archivos}/rodales.csv', 'r', encoding = 'utf-8') as archivo:
        linea = archivo.read().splitlines()

    # Reconstruir dicc_rodales manualmente
    for rodal in linea[1:]:
        datos = rodal.split(",")

        if datos[0].strip("'") not in dicc_rodales:
            dicc_rodales[datos[0].strip("'")] = {
                'b_nativo' : int(),
                'b_exotico' : int(),
                'propietario' : str(),
                'colindancias' : dict()
            }
        
        dicc_rodales[datos[0].strip("'")]['b_nativo'] = datos[1].strip()
        dicc_rodales[datos[0].strip("'")]['b_exotico'] = datos[2].strip()
        dicc_rodales[datos[0].strip("'")]['propietario'] = datos[3].strip("'").strip()
        dicc_rodales[datos[0].strip("'")]['colindancias'] = temp_colindancias[datos[0].strip("'")]

    return dicc_rodales


def guardar_en_archivo(dicc_rodales: dict, modo_escritura: str = 'a', directorio_archivos: str = 'archivos'):
    """Esta funcion debe guardar los datos en dicc_rodales para que se puedan utilizar
    en una siguiente ejecución del programa"""
    rodales_existentes = set()
    generar_archivos()

    # Primero leer el archivo para comprobar qué id de rodal ya está guardada (para evitar copias)
    with open(f'{directorio_archivos}/rodales.csv', 'r', encoding = 'utf-8') as archivo:
        linea = archivo.readlines()

    for rodal in linea[1:]:
        datos = rodal.split(",")
        rodales_existentes.add(datos[0].strip("'"))

    # Escribir en el archivo de rodales
    with open(f'{directorio_archivos}/rodales.csv', modo_escritura, encoding = "utf-8") as archivo:

        for id_rodal, datos in dicc_rodales.items():
            if id_rodal not in rodales_existentes:
                
                archivo.write(f"'{id_rodal}',")
                for tipo, dato in datos.items():

                    if tipo != "colindancias" and tipo != "propietario":
                        archivo.write(f"{dato},")
                    elif tipo == "propietario":
                        archivo.write(f"'{dato}'\n")

    # Escribir las colindancias en el archivo
    with open(f'{directorio_archivos}/colindancias.csv', modo_escritura, encoding = 'utf-8') as archivo:

        for id_rodal, datos in dicc_rodales.items():
            if id_rodal not in rodales_existentes:
                for direccion, colindante in dicc_rodales[id_rodal]['colindancias'].items():

                    if colindante != '':
                        archivo.write(f"'{id_rodal}','{colindante}','{direccion}'\n")

    print(dicc_rodales)


def limpiar_datos():
    '''Esta función está encargada de limpiar los datos de los rodales en
    los archivos'''

    with open('Tests/colindancias.csv', 'w', encoding = 'utf-8') as archivo:
        archivo.write("# rodal_nuevo rodal_existente orientacion\n")

    with open('Tests/rodales.csv', 'w', encoding = 'utf-8') as archivo:
        archivo.write("# rodal %nativo %exotico propietario\n")

    
def test():
    # Esta función prueba las funciones de este módulo
    ...

if __name__ == "__main__":
    test()