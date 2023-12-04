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
#   <================================================================================================================================================================>
dicc_rodales = {
       'R1'   : {'b_nativo': 40, 'b_exotico': 60, 'propietario': 'F. Henriquez', 'colindancias': {'N': 'R4', 'NW': 'R6', 'NE': 'R3', 'S': '', 'SE': 'R2', 'SW': ''}},
       'R2'   : {'b_nativo': 12, 'b_exotico': 88, 'propietario': 'F. Henriquez', 'colindancias': {'N': 'R3', 'NW': 'R1', 'NE': '', 'S': '', 'SE': '', 'SW': ''}},
       'R3'   : {'b_nativo': 98, 'b_exotico': 2, 'propietario': 'R. Maturana', 'colindancias': {'N': 'R5', 'NW': 'R4', 'NE': '', 'S': 'R2', 'SE': '', 'SW': 'R1'}},
       'R4'   : {'b_nativo': 87, 'b_exotico': 13, 'propietario': 'R. Maturana', 'colindancias': {'N': '', 'NW': 'R7', 'NE': 'R5', 'S': 'R1', 'SE': 'R3', 'SW': 'R6'}},
       'R5'   : {'b_nativo': 90, 'b_exotico': 10, 'propietario': 'R. Maturana', 'colindancias': {'N': '', 'NW': '', 'NE': '', 'S': 'R3', 'SE': '', 'SW': 'R4'}},
       'R6'   : {'b_nativo': 40, 'b_exotico': 60, 'propietario': 'Inv. Lazo', 'colindancias': {'N': 'R7', 'NW': '', 'NE': 'R4', 'S': '', 'SE': 'R1', 'SW': ''}},
       'R7'   : {'b_nativo': 50, 'b_exotico': 50, 'propietario': 'lucas reyes', 'colindancias': {'N': '', 'NW': '', 'NE': '', 'S': 'R6', 'SE': 'R4', 'SW': ''}}
   }
#   <================================================================================================================================================================>
def consultar_() -> dict:

    #lectura del archivo diccionario global...

    propietario_key = {}; rodal_key = {} # <--- "data_pack"

    global dicc_rodales
    
    #filtro las lineas y las almaceno para ambos tipos de "data_pack"
    for rodal_lectura in dicc_rodales:
        nativo, exotico, propieario, _ = dicc_rodales[rodal_lectura].values()

        #  guardo los datos en los distintos "data_pack"
        #  <=====================================================================================================>
        if propieario not in propietario_key:
            propietario_key[propieario] = {'rodales': rodal_lectura, 'nativo': float(nativo), 'exotico': float(exotico),
                                           'array_nativo': [float(nativo)], 'array_exotico': [float(exotico)]}
        else:
            propietario_key[propieario]['array_nativo'].append(float(nativo))
            propietario_key[propieario]['array_exotico'].append(float(exotico))
            propietario_key[propieario]['rodales'] += f', {rodal_lectura}'
            propietario_key[propieario]['nativo'] = promedio(propietario_key[propieario]['array_nativo'])
            propietario_key[propieario]['exotico'] = promedio(propietario_key[propieario]['array_exotico'])

        # <=====================================================================================================>
        if rodal_lectura not in rodal_key:
            rodal_key[rodal_lectura] = {'propietario': propieario, 'nativo': float(nativo), 'exotico': float(exotico)}
       
        # <=====================================================================================================>
    for prop in propietario_key:                            #limpio datos innecesarios
        propietario_key[prop].pop('array_nativo'), propietario_key[prop].pop('array_exotico')

    return(propietario_key, rodal_key)

#HACE FALTA LEER EL DICCIONARIO GLOBAL.
def por_rodal(rodal:str): #consulta por rodales
    _, dict_rodal = consultar_()
    propietario, natividad, exotico = dict_rodal[rodal].values()
    return [propietario, natividad, exotico]
    #   Retorno de propietario, natividad, exotico al preguntar por algún rodal en particular
    #   ejemplo de salida ... -> ['Rodales Pepe', '87', '13']
    #   tipo: lista de strings

def por_propietario(propietario:str) -> str: # consulta por propietario
    # colocar validacion (función a parte)
    dict_propietario, _ = consultar_()
    rodales_prop, natividad, exotico = dict_propietario[propietario].values()
    return [rodales_prop, natividad, exotico]
    #   Retorno de la cantidad de los rodales los cuales es propietario,
    #   natividad, exotico al preguntar por algún rodal en particular.
    #   ejemplo de salida ... -> ['Rodales Pepe', '87', '13']
    #   tipo: tupla de strings

def por_hectarea(str_rodales: str) -> dict: # string del tipo: R1, R3-R9, R10
    #   Defino variables a utilizar.
    split_str_rodales = str_rodales.split(', '); rodales_total = []; _, dict_rodal = consultar_()
    nativo_hectareas_total = 0; exotico_hectareas_total = 0;
    # <===========================================================================================================>
    for paso_rodal in split_str_rodales:
        if '-' in paso_rodal:
            temp = paso_rodal.replace('R', '').split('-')
            if int(temp[0]) > int(temp[-1]):
                for agregando in range(int(temp[0]), int(temp[-1])-1, -1):  
                    rodales_total.append(f'R{agregando}')
            else:
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

    return [round(nativo_hectareas_total, 2), round(exotico_hectareas_total, 2)]
    #   Retorno de las hectarias totales de nativos y exoticos
    #   ejemplo de salida...-> esto retorna dos valores, por ende... -> (24, 27.5)
    #   tipo: lista de dos valores flotantes (se puede conciderar una tupla de flotantes)

def cant_rodales() -> tuple: # tupla de los rodales disponibles a consultar... (ayuda al combobox)
    _, b = consultar_()
    lista_ = list(b.keys())
    return sorted(lista_, key=lambda x: int(x[1:]))
                            # ejemplo de salida ... -> ['R1', 'R3', 'R6', 'R7', 'R8', 'R9', 'R10']
                            # tipo: lista de string's

def cant_propietarios() -> tuple: # tupla de los porpietarios disponibles a consultar ... (ayuda al combobox)
    a, _ = consultar_()
    return list(a.keys())   # ejemplo de salida ... -> ['Rodales Csazsar', 'Bingus Radianes',
                            #                               'Simu Asociados', 'Toledo.s Rodales']
                            # tipo: lista de string's

print(por_hectarea('R1, R9-R3, R10'))