# Esta es la capa de lógica, donde están las FUNCIONES y VALIDACIONES

import os
import archivos as file

class OpcionInvalidaError(Exception): pass
class ValorInvalidoError(Exception): pass
class RodalYaExistenteError(Exception): pass
class EspacioNoValidoError(Exception): pass

global dicc_rodales
dicc_rodales = {}
#dicc_rodales = {
#    'R1'   : {'b_nativo': 40, 'b_exotico': 60, 'propietario': 'F. Henriquez', 'colindancias': {'N': 'R4', 'NW': 'R6', 'NE': 'R3', 'S': '', 'SE': 'R2', 'SW': ''}},
#    'R2'   : {'b_nativo': 12, 'b_exotico': 88, 'propietario': 'F. Henriquez', 'colindancias': {'N': 'R3', 'NW': 'R1', 'NE': '', 'S': '', 'SE': '', 'SW': ''}},
#    'R3'   : {'b_nativo': 98, 'b_exotico': 2, 'propietario': 'R. Maturana', 'colindancias': {'N': 'R5', 'NW': 'R4', 'NE': '', 'S': 'R2', 'SE': '', 'SW': 'R1'}},
#    'R4'   : {'b_nativo': 87, 'b_exotico': 13, 'propietario': 'R. Maturana', 'colindancias': {'N': '', 'NW': 'R7', 'NE': 'R5', 'S': 'R1', 'SE': 'R3', 'SW': 'R6'}},
#    'R5'   : {'b_nativo': 90, 'b_exotico': 10, 'propietario': 'R. Maturana', 'colindancias': {'N': '', 'NW': '', 'NE': '', 'S': 'R3', 'SE': '', 'SW': 'R4'}},
#    'R6'   : {'b_nativo': 40, 'b_exotico': 60, 'propietario': 'Inv. Lazo', 'colindancias': {'N': 'R7', 'NW': '', 'NE': 'R4', 'S': '', 'SE': 'R1', 'SW': ''}},
#    'R7'   : {'b_nativo': 50, 'b_exotico': 50, 'propietario': 'lucas reyes', 'colindancias': {'N': '', 'NW': '', 'NE': '', 'S': 'R6', 'SE': 'R4','SW':''}}
#}
#dicc_rodales = file.construir_diccionario()

def inicializar_diccionario(path: str = 'archivos'):
    global dicc_rodales

    file.generar_archivos(path)
    dicc_rodales = file.construir_diccionario(path)


# Metes una coordenada y te devuelve la opuesta
coordenada_opuesta = {
    "N" : "S",
    "NE" : "SW",
    "NW" : "SE",
    "S" : "N",
    "SE" : "NW",
    "SW" : "NE"
}

# Referencias para validar las colindancias
referencia_validacion = {
    'N':{
        'NE': 'SE',
        'NW': 'SW',
        'S':'S',
        'SE': 'S',
        'SW': 'S',
        'N': 'S'
    },
                     
    'NE':{
        'SE': 'S',
        'N': 'NW',
        'NW': 'SW',
        'SW': 'SW',
        'S': 'SW',
        'NE': 'SW'
    },

    'NW':{
        'N': 'NE',
        'SW': 'S',
        'S': 'SE',
        'SE': 'SE',
        'NE': 'SE',
        'NW': 'SE'
    },

    'S':{
        'SE': 'NE',
        'SW': 'NW',
        'N': 'N',
        'NE': 'N',
        'NW': 'N',
        'S': 'N'
    },

    'SE':{
        'S': 'SW',
        'NE':'SE',
        'NW': 'NW',
        'SW': 'NW',
        'N': 'NW',
        'SE': 'NW'
    },

    'SW':{
        'S': 'SE',
        'NW': 'N',
        'N': 'NE',
        'SE': 'NE',
        'NE': 'NE',
        'SW': 'NE'
    }
}

# Funciones que ojalá se puedan reciclar
def generar_rodal(
        id_rodal: str, 
        propietario: str, 
        nativo: int, 
        exotico: int,
        colin_N = '', colin_NW = '', colin_NE = '', 
        colin_S = '', colin_SW = '', colin_SE = '',
        colindancias_dict = dict()
        ) -> None:
    global dicc_rodales

    if not colindancias_dict:

        colindancias_dict = {
            'N' : colin_N,
            'NW' : colin_NW,
            'NE' : colin_NE,
            'S' : colin_S,
            'SE' : colin_SE,
            'SW' : colin_SW
        }

    datos_rodal = {
        'b_nativo' : nativo,
        'b_exotico' : exotico,
        'propietario' : propietario,
        'colindancias' : colindancias_dict
    }

    dicc_rodales[id_rodal] = datos_rodal


def asignar_colindancias(nuevo_rodal: str, rodal_referencia: str, direccion: str) -> None:
    """Actualiza todas las colindancias de los rodales en base a los rodales 
    que se están agregando"""

    # El value de cada key es para saber la vuelta por la que está pasando
    referencias_subprocesos = { 
        "N" : ["NW","NE"],
        "NE" : ["N","SE"],
        "NW" : ["SW","N"],
        "S" : ["SE","SW"],
        "SE" : ["NE","S"],
        "SW" : ["S","NW"]
    }

    # Referencia para buscar en sentido horario
    vuelta_1_horario = {
        "N": "NE",
        "NE": "SE",
        "NW": "N",
        "S": "SW",
        "SE": "S",
        "SW": "NW"
    }

    # Referencia para buscar en sentido antihorario
    vuelta_2_antihorario = {
        "N": "NW",
        "NE": "N",
        "NW": "SW",
        "S": "SE",
        "SE": "NE",
        "SW": "S"
    }

    vuelta = 1; r_col_v1 = str(); r_col_v2 = str()

    print(f' --- Rodal referencia: {rodal_referencia} ---')

    # En el caso que el rodal que se entregue esté vacío, se detiene la recursividad
    if rodal_referencia == '': 
        print(' -- Rodal_referencia vacío --')
        return

    # Si se llega a un rodal que tiene colindancias, se detiene la recursividad
    if dicc_rodales[rodal_referencia]["colindancias"][coordenada_opuesta[direccion]] != '': 
        print(' -- Vuelta completa --')
        return
    
    # Comenzar el proceso de asignación de colindancias
    if dicc_rodales[rodal_referencia]["colindancias"][coordenada_opuesta[direccion]] == '':

        # Asignar colindancias opuestas
        dicc_rodales[rodal_referencia]["colindancias"][coordenada_opuesta[direccion]] = nuevo_rodal
        dicc_rodales[nuevo_rodal]["colindancias"][direccion] = rodal_referencia
        print(f' A {rodal_referencia} le asigno {nuevo_rodal} en {coordenada_opuesta[direccion]}')
        print(f' A {nuevo_rodal} se le referenció a {rodal_referencia} en {direccion}\n')

        # Inicia proceso de búsqueda
        for coord_a_buscar in referencias_subprocesos[coordenada_opuesta[direccion]]:
            print(f' Busco al {coord_a_buscar} de {rodal_referencia} [vuelta {vuelta}]')

            # Guardar los rodales a buscar en variables
            match vuelta:
                case 1:
                    if dicc_rodales[rodal_referencia]["colindancias"][coord_a_buscar] != '':
                        r_col_v1 = dicc_rodales[rodal_referencia]["colindancias"][coord_a_buscar]
                case 2:
                    if dicc_rodales[rodal_referencia]["colindancias"][coord_a_buscar] != '':
                        r_col_v2 = dicc_rodales[rodal_referencia]["colindancias"][coord_a_buscar]
            
            vuelta += 1
        
        print(f' Rodal al {referencias_subprocesos[coordenada_opuesta[direccion]][0]}: {r_col_v1}')
        print(f' Rodal al {referencias_subprocesos[coordenada_opuesta[direccion]][1]}: {r_col_v2}')

        # Retorna la misma función retornando lo que se encontró en los laterales del rodal referencia
        return (
            asignar_colindancias(nuevo_rodal, r_col_v1, vuelta_1_horario[direccion]),
            asignar_colindancias(nuevo_rodal, r_col_v2, vuelta_2_antihorario[direccion])
        )


def colindancia_valida(rodal_colindante: str, direccion: str) -> bool:
    """Recorrer la lista de rodales, en el caso en que otro rodal tenga al rodal
    colindante de referencia en la misma dirección que el que está siendo creado
    se retorna True para continuar preguntando al usuario que ingrese un rodal válido"""
    for rodal, informacion in dicc_rodales.items():
        if rodal != rodal_colindante:
            if informacion["colindancias"][direccion] == rodal_colindante:
                return True

    return False


def guardar_diccionario() -> None:
    '''Función encargada de invocar al módulo archivos para guardar lo que 
    hay en el diccionario'''
    global dicc_rodales

    file.guardar_en_archivo(dicc_rodales)
    

def validar_ingreso(D:dict) -> None:
    global dicc_rodales

    class IngresoInvalido(Exception):pass
    for rodal in D.keys():
        id_rodal = rodal

    nativo  = D[id_rodal]['b_nativo']
    exotico = D[id_rodal]['b_exotico']
    propietario = D[id_rodal]['propietario']
    colindancias = D[id_rodal]['colindancias']
    validado = False

    try:
        #Validaciones ID
        id_rodal = id_rodal.upper().strip().replace(" ","")
        if id_rodal == "" or id_rodal == "(Ejemplo: R1)":
            raise IngresoInvalido ("Casilla ID Rodal vacia")
        if id_rodal[0] != "R":
            raise IngresoInvalido("La primera letra debe ser una 'R' seguido de números")
        if id_rodal[1:].isdigit() == False:
            raise IngresoInvalido("La primera letra debe ser una 'R' seguido de números")
        if id_rodal in dicc_rodales.keys():
            raise IngresoInvalido("Ese ID ya rodal ya está registrado")
        
        #Validaciones bosque
        if nativo + exotico != 100:
            raise IngresoInvalido ("La suma de los porcentajes de bosques no es 100")

        #Validaciones Propietario
        if propietario == "" or propietario == "(Ejemplo: Inv. Rojas)":
            raise IngresoInvalido ("Casilla Propietario vacia")
        
        # Validaciones Colindancias
        # 1. Se escoge un rodal que tenga una colindancia válida para buscar en torno a ese
        for direct, colin in colindancias.items():
            if not colindancia_valida(colin, direct) and colin != '':
                colindante_valido = [colin, direct]

        # 2. Se itera sobre las colindancias del rodal en creacion y se validan en torno a la válida
        try:
            for direct, colin in colindancias.items():
                if colindante_valido[0] != colin:
                    valido = colindancias_validas(colindante_valido[0], colin, colindante_valido[1], direct) # En linea: 334
                    if not valido:
                        raise IngresoInvalido(f"Colindancias Inválidas")
        except UnboundLocalError: pass
        

    except IngresoInvalido as msj:
            return validado, msj
    
    validado = True

    datos_rodal = {
        'b_nativo' : nativo,
        'b_exotico' : exotico,
        'propietario' : propietario,
        'colindancias' : colindancias
    }

    dicc_rodales[id_rodal] = datos_rodal

    for direct, rod in dicc_rodales[id_rodal]['colindancias'].items():
        if rod != '':
            direccion_referencia = direct
            rodal_referencia = rod
            break
    
    try:
        asignar_colindancias(id_rodal, rodal_referencia, direccion_referencia)
    except UnboundLocalError: pass

    return validado, "Ingreso correcto"
    

def colindancias_validas (rodal_valido: str, rodal_a_validar: str, direccion_valido: str, direccion_a_validar: str):
    if dicc_rodales[rodal_valido]['colindancias'][referencia_validacion[direccion_valido][direccion_a_validar]] != rodal_a_validar:
        # Diccionario "referencia_validacion" en linea: 42
        # La colindancia es invalida
        return False
    # La colindancia es valida
    return True


def retorna_lista_rodales() -> list:
    """Retorna una lista con las IDS de los rodales ya ingresados"""
    global dicc_rodales
    rodales = list(dicc_rodales.keys())
    rodales.append("")
    rodales.sort()
    return rodales


def retorna_lista_propietarios() -> list:
    """Retorna una lista con los propietarios de los rodales ya ingresados"""
    global dicc_rodales
    propietarios = set()
    for rodal in dicc_rodales.keys():
        propietarios.add(dicc_rodales[rodal]["propietario"])
    propietarios = list(propietarios)
    return propietarios

def promedio(arreglo_de_numeros: list) -> float: #funcion de promedio
    return (round((sum(arreglo_de_numeros))/len(arreglo_de_numeros), 2))

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
            exotico_hectareas_total += (exotico/100)*10                 

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

def rodales_colindancias(rodal:str) -> str: #imprimo R1:direccion, R2:direccion, etc para label de colindancias en consultar de obd_firewatch
    #Consigo el string para imprimir en el label de colindancias, desde el dicc_rodales
    global dicc_rodales
    colindancias = dicc_rodales[rodal]['colindancias']
    colindancias_str = ''
    for direccion, rodal_col in colindancias.items():
        if rodal_col != '':
            colindancias_str += f'{rodal_col}:{direccion}, '
    return colindancias_str[:-2]

def simular_afectados(direccion_viento: str, rodal_inicial: str, afectados:set = set()) -> list: 
    #_________________________________INFORMACION_______________________________________
    # Busca recursivamente en el diccionario de rodales según la dirección del viento y añade a 
    #                       un set los rodales afectados encontrados
    # *** RETORNA: una lista de rodales afectados ordenados de menor a mayor ***
    #___________________________________________________________________________________
    vuelta = 1
    direcciones_afectadas = {
        'N': ['N'],
        'NE': ['NE'],
        'SE': ['NE'],
        'S': ['S'],
        'SW': ['SW'],
        'NW': ['NW'],
        'W': ['NW', 'SW'],
        'E': ['NE', 'SE']
    }

    # Caso base: No se encontraron rodales
    if rodal_inicial == '':
        return

    # En el caso de que se hayan encontrado
    if rodal_inicial != '':
        # Añadir al set
        afectados.add(rodal_inicial)
        # Buscar más rodales 
        for direccion in direcciones_afectadas[direccion_viento]:
            match vuelta:
                case 1:
                    siguiente_rodal_1 = dicc_rodales[rodal_inicial]['colindancias'][direccion]
                
                case 2:
                    siguiente_rodal_2 = dicc_rodales[rodal_inicial]['colindancias'][direccion]

            vuelta += 1

    # Devolver lo encontrado (según que dirección se haya entregado)
    if direccion_viento in ['E', 'W']:
        simular_afectados(direccion_viento, siguiente_rodal_1, afectados)
        simular_afectados(direccion_viento, siguiente_rodal_2, afectados)
        afectados = sorted(afectados, key=lambda x: int(x[1:]))
        return afectados
    else:
        simular_afectados(direccion_viento, siguiente_rodal_1, afectados)
        afectados = sorted(afectados, key=lambda x: int(x[1:])) #Ordenar los rodales
        return afectados

def suma_afectados(rodal_inicial: str, list_afectados:list) -> list:
    #_________________________________INFORMACION_______________________________________
    #1. Debe retornar las hectareas totales afectadas por el incendio (cada rodal tiene 10 hectareas)
    #2. Debe retornar las hectareas de bosque nativo afectado con una conversión de (porcentaje*0.1)
    #3. Debe retornar las hectareas de bosque exotico afectado con una conversión de (porcentaje*0.1)
    #4. Debe retornar la set de propietarios afectados
    # *** RETORNA tupla_suma = (hectareas_totales_afectadas, bosque_nativo_afectado, bosque_exotico_afectado) ***
    #___________________________________________________________________________________
    propietarios_afectados = {dicc_rodales[rodal_inicial]['propietario']}
    bosque_nativo_afectado = dicc_rodales[rodal_inicial]['b_nativo'] * 0.1
    bosque_exotico_afectado = dicc_rodales[rodal_inicial]['b_exotico'] * 0.1
 

    for rodal in list_afectados:
        # Excluir el rodal de inicio de la suma (no duplicarlo)
        if rodal != rodal_inicial:
            bosque_nativo_afectado += dicc_rodales[rodal]['b_nativo'] * 0.1
            bosque_exotico_afectado += dicc_rodales[rodal]['b_exotico'] * 0.1
            propietarios_afectados.add(dicc_rodales[rodal]['propietario'])

    hectareas_totales_afectadas = bosque_nativo_afectado + bosque_exotico_afectado
    tupla_suma = (round(hectareas_totales_afectadas, 2), round(bosque_nativo_afectado, 2), round(bosque_exotico_afectado, 2))
    tupla_propietarios = tuple(propietarios_afectados)
    return tupla_suma, tupla_propietarios


#Creo una funcion que me haga una lista de tuplas con los rodales afectados,
# los propietarios afectados y las hectareas afectadas
# lista = [(rodales), (propietarios),(nativo, exotico, total)]

def simular_incendio(direccion_viento: str, rodal_inicial: str) -> list:
    #_________________________________INFORMACION_______________________________________
    #1. Debe desplegar la funcion de "consultar rodal" para el rodal comprometido + direccion
    #2. Debe desplegar la funcion de "consultar rodal" para los rodales afectados
    #3. Debe retornar la lista de incendio
    # *** RETORNA lista_incendio = [(rodales), (propietarios),(nativo, exotico, total)] ***
    #__________________________________________________________________________________
    #
    # consultar_rodal(...) + direccion_viento
    # for a los sets

    rodales_afectados = simular_afectados(direccion_viento, rodal_inicial) #ordeno la lista de afectados
    recursos_comprometidos = suma_afectados(rodal_inicial,rodales_afectados)
    lista_incendio = [rodales_afectados, recursos_comprometidos[1], recursos_comprometidos[0]]
    return lista_incendio

def limpiar_datos_log():
    file.limpiar_datos()

def test():
    global dicc_rodales
    validado, msj = validar_ingreso(D={"R2":{"b_nativo": 20, "b_exotico":80, "propietario": "inv rojas",
                                        "colindancias":{'N' : "",
                                                        'NW' : "",
                                                        'NE' : "",
                                                        'S' : "",
                                                        'SE' : "",
                                                        'SW' : ""}}}
                                                        )
    print (validado, msj)

    validado, msj = validar_ingreso(D={"R1":{"b_nativo": 70, "b_exotico":10, "propietario": "inv rojas",
                                        "colindancias":{'N' : "",
                                                        'NW' : "R2",
                                                        'NE' : "",
                                                        'S' : "",
                                                        'SE' : "",
                                                        'SW' : ""}}}
                                                        )
    
    print (validado, msj)

    validado, msj = validar_ingreso(D={"  r1":{"b_nativo": 70, "b_exotico":30, "propietario": "inv rojas",
                                        "colindancias":{'N' : "",
                                                        'NW' : "R2",
                                                        'NE' : "",
                                                        'S' : "",
                                                        'SE' : "",
                                                        'SW' : ""}}}
                                                        )
    
    print (validado, msj)

    validado, msj = validar_ingreso(D={"r-3":{"b_nativo": 50, "b_exotico":50, "propietario": "inv rojas",
                                        "colindancias":{'N' : "",
                                                        'NW' : "R2",
                                                        'NE' : "",
                                                        'S' : "",
                                                        'SE' : "",
                                                        'SW' : ""}}}
                                                        )
    
    print (validado, msj)

    validado, msj = validar_ingreso(D={"R3":{"b_nativo": 50, "b_exotico":50, "propietario": "inv rojas",
                                        "colindancias":{'N' : "",
                                                        'NW' : "R1",
                                                        'NE' : "",
                                                        'S' : "",
                                                        'SE' : "",
                                                        'SW' : ""}}}
                                                        )
    
    print (validado, msj)

    for key,value in dicc_rodales.items():
        print(f"{key}   : {value}")
        print()

if __name__ == "__main__":
    test()