""" 
    mi idea a partir del archivo 'rodales.csv' extraer la información de dos maneras, una para cada
    diccionario, uno que tenga un diccionario en la cual sus llaves sean los propietarios, y en sus argumentos
    para cada respectivo propietario, agregar el rodal el cual es dueño, sus porcentajes de exotico y nativo.
    
    luego en la otra manera de guardar la información, quiero hacer otro diccionario, el cual tenga como claves
    los rodales, y en sus argumentos, sus porcentajes de nativo, exotico y propietario de ser necesario.
    
    estas dos formas de almacenar la información a partir de un solo archivo me va a permitir trabajar mucho mas
    libremente con los datos y poder extraer informacion mas rapidamente de manera mas fluida, para que de esta
    manera, poder mostrar la informacion en menos lineas y menos analizis de datos.

"""

#    @shyupss_    #
def promedio(arreglo_de_numeros: list) -> float: #funcion de promedio
    return (round((sum(arreglo_de_numeros))/len(arreglo_de_numeros), 2))

def consultar_() -> dict:

    #lectura del archivo csv...
    with open('rodales.csv', 'r') as info:
        lineas_rodales_info = info.readlines()

    propietario_key = {}; rodal_key = {} # <--- "data_pack"
    
    #filtro las lineas y las almaceno para ambos tipos de "data_pack"
    for linea in lineas_rodales_info:
        rodal, nativo, exotico, propieario = linea.strip('\n').split(', ')
        #  guardo los datos en los distintos "data_pack"

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
       
        # <--------------------------------------------------------------------------------------->
    for prop in propietario_key:                            #limpio datos innecesarios
        propietario_key[prop].pop('array_nativo'), propietario_key[prop].pop('array_exotico')

    return(propietario_key, rodal_key)

def por_propietario(propietario:str) -> str: # consulta por propietario
    dict_propietario, _ = consultar_()
    rodales_prop, natividad, exotico = dict_propietario[propietario].values()
    return (rodales_prop, natividad, exotico)

def por_rodal(rodal:str): #consulta por rodales
    _, dict_rodal = consultar_()
    propietario, natividad, exotico = dict_rodal[rodal].values()
    return (propietario, natividad, exotico)

def por_lista_hectarea(str_rodales: str) -> dict: # string del tipo: R1, R3-R9, R10
    #   Defino variables a utilizar.
    split_str_rodales = str_rodales.split(', '); rodales_total = []; _, dict_rodal = consultar_()
    nativo_hectareas_total = 0; exotico_hectareas_total = 0;
    # <===========================================================================================================>
    for paso_rodal in split_str_rodales:
        if '-' in paso_rodal:
            temp = paso_rodal.replace('R', '').split('-')
            for agregando in range(int(temp[0]), int(temp[-1])+1, 1):   # ingreso todos los radales que se estan
                rodales_total.append(f'R{agregando}')                   # consultando a la lista rodales_total.
        else:
            rodales_total.append(paso_rodal)

    for rodal in rodales_total:

        try:
            _, natividad, exotico = dict_rodal[rodal].values()          # cálculo de los porcentajes de hectareas
            nativo_hectareas_total += (natividad/100)*10                # respecto a la natividad y lo exótico.
            exotico_hectareas_total += (exotico/100)*10                 # uwu

        except KeyError:
            ...

    return round(nativo_hectareas_total, 2), round(exotico_hectareas_total, 2)

def cant_rodales() -> tuple: # tupla de los rodales disponibles a consultar...
    _, b = consultar_()
    return tuple(b.keys())

def cant_propietarios() -> tuple: # tupla de los porpietarios disponibles a consultar
    a, _ = consultar_()
    return tuple(a.keys())

a, _ = por_lista_hectarea('R1, R3-R9, R10')
print(a)