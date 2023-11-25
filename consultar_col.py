""" 
    mi idea a partir del archivo 'rodales.csv' extraer la información de dos maneras, una para cada
    diccionario, uno que tenga un diccionario en la cual sus llaves sean los propietarios, y en sus argumentos
    para cada respectivo propietario, agregar el rodal el cual es dueño, sus porcentajes de exotico y nativo.
    
    luego en la otra manera de guardar la información, quiero hacer otro diccionario, el cual tenga como claves
    los rodales, y en sus argumentos, sus porcentajes de nativo, exotico y propietario de ser necesario.
    
    estas dos formas de almacenar la información a partir de un solo archivo me va a permitir trabajar mucho mas
    libremente con los datos y poder extraer informacion mas rapidamente de manera mas fluida, para que de esta
    manera, poder mostrar la informacion en menos lineas y menos analizis de datos.

"""#    @shyupss_    #

def consultar_(archivo__: str) -> dict:

    def promedio(arreglo_de_numeros: list) -> float: #funcion de promedio
        return (round((sum(arreglo_de_numeros))/len(arreglo_de_numeros), 2))
    
    #lectura del archivo csv...
    with open(archivo__, 'r') as info:
        lineas_rodales_info = info.readlines()

    propietario_key = {}; rodal_key = {} # <--- "data_pack"
    
    #filtro las lineas y las almaceno para ambos tipos de "data_pack"
    for linea in lineas_rodales_info:
        rodal, propieario, nativo, exotico = linea.strip('\n').split(', ')
        #  guardo los datos en los distintos "data_pack"
        propieario = propieario.lower().replace(' ', '_')
        #filtrar el str de propietario

        #  <--------------------------------------------------------------------------------------->
        if propieario not in propietario_key:
            propietario_key[propieario] = {'rodales': rodal, 'nativo': float(nativo), 'exotico': float(exotico),
                                           'array_nativo': [float(nativo)], 'array_exotico': [float(exotico)]}
        else:
            propietario_key[propieario]['array_nativo'].append(float(nativo))
            propietario_key[propieario]['array_exotico'].append(float(exotico))
            propietario_key[propieario]['rodales'] += f', {rodal}'
            propietario_key[propieario]['nativo'] = promedio(propietario_key[propieario]['array_nativo'])
            propietario_key[propieario]['exotico'] = promedio(propietario_key[propieario]['array_exotico'])
        # <--------------------------------------------------------------------------------------->
        if rodal not in rodal_key:
            rodal_key[rodal] = {'propietario': propieario, 'nativo': float(nativo), 'exotico': float(exotico)}
        else:
            ... #el pepe
        # <--------------------------------------------------------------------------------------->
    for prop in propietario_key:                            #limpio datos innecesarios
        propietario_key[prop].pop('array_nativo'), propietario_key[prop].pop('array_exotico')

    return(propietario_key, rodal_key)

def por_propietario(propietario:str) -> str:

    propietario_ = propietario.lower().replace(' ', '_')    # se filtra el str del input del usuario
    dict_propietario, _ = consultar_('rodales.csv')         # llamo el dato necesario

    if propietario_ not in dict_propietario:                # si no esta el propietario..., de lo contrario...

        print('no esta po wons, coloca otro') # ALSDKJALÑSDJKLÑASKDLÑASKLÑDKALÑSD POR DEFINIRR XDDDDD

    else:                                                   # de lo contrario...
        rodales_prop, natividad, exotico = dict_propietario[propietario_].values()
        return (rodales_prop, natividad, exotico)           # devuelvo los datos en forma de tupla

def por_rodal(rodal:str):
    _, dict_rodal = consultar_('rodales.csv')
    ...

print(por_propietario('simu lacro'))