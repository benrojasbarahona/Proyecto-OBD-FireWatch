# Esta es la capa de archivos, es la más cercana al csv
# y se dedica a leer y escribir en el archivo

def generar_archivos(directorio_archivos: str = 'archivos'):
    '''Esta función crea los archivos en caso de que no existan
    (se ejecuta en construir diccionario)'''

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


def buscar_directorio() -> str:
    # Generar el archivo config.csv en el caso de que no exista
    try:
        with open(f'archivos/config.csv', 'x', encoding = 'utf-8'):
            print('< El archivo config.csv ha sido generado >')
            config_generado = True
    except FileExistsError: config_generado = False

    # Si el archivo config.csv fue recien generado, escribir headers
    if config_generado:
        with open(f'archivos/config.csv', 'w', encoding = 'utf-8') as archivo:
            archivo.write("# Direccion_archivos\n")

    with open(f'archivos/config.csv', 'r', encoding = 'utf-8') as archivo:
        directorio = archivo.read().splitlines()
    
    try: return directorio[1]
    except IndexError: return 'archivos'


def guardar_directorio(directorio: str):
    with open(f'archivos/config.csv', 'r', encoding = 'utf-8') as archivo:
        datos = archivo.read().splitlines()

    try:
        if datos[1] == directorio:
            return
    
    except IndexError:
        with open(f'archivos/config.csv', 'a', encoding = 'utf-8') as archivo:
            archivo.write(f'{directorio}\n')


def construir_diccionario(directorio_archivos: str = 'archivos') -> dict:
    """El trabajo de esta función es para cada inicio del programa, leer el archivo para
    reconstruir el diccionario que contiene la información de todos los rodales registrados
    por el usuario
    (SE DEBE EJECUTAR AL INICIO DEL PROGRAMA)"""

    temp_colindancias = dict()
    dicc_rodales = dict()

    generar_archivos()

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
        try:
            dicc_rodales[datos[0].strip("'")]['colindancias'] = temp_colindancias[datos[0].strip("'")]
        except KeyError: 
            dicc_rodales[datos[0].strip("'")]['colindancias'] = {'N': '', 'NW': '', 'NE': '', 'S': '', 'SW': '', 'SE': ''}

    return dicc_rodales


def guardar_en_archivo(dicc_rodales: dict, modo_escritura: str = 'a', directorio_archivos: str = 'archivos'):
    """Esta funcion debe guardar los datos en dicc_rodales para que se puedan utilizar
    en una siguiente ejecución del programa
    (SE EJECUTA CADA VEZ QUE SE GUARDE UN RODAL)"""
    
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


def limpiar_datos(directorio: str = 'archivos'):
    '''Esta función está encargada de limpiar los datos de los rodales en
    los archivos
    (AÑADIR UN BOTON PARA ESTO)'''

    with open(f'{directorio}/colindancias.csv', 'w', encoding = 'utf-8') as archivo:
        archivo.write("# rodal_nuevo rodal_existente orientacion\n")

    with open(f'{directorio}/rodales.csv', 'w', encoding = 'utf-8') as archivo:
        archivo.write("# rodal %nativo %exotico propietario\n")

    
def test():
    # Esta función prueba las funciones de este módulo
    print('bingus')

if __name__ == "__main__":
    test()