# Esta es la capa de lógica, donde están las FUNCIONES y VALIDACIONES

import os

class OpcionInvalidaError(Exception): pass
class ValorInvalidoError(Exception): pass
class RodalYaExistenteError(Exception): pass
class EspacioNoValidoError(Exception): pass

dicc_rodales = {}

# Metes una coordenada y te devuelve la opuesta
coordenada_opuesta = {
    "N" : "S",
    "NE" : "SW",
    "NW" : "SE",
    "S" : "N",
    "SE" : "NW",
    "SW" : "NE"
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
        ):
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


def asignar_colindancias(nuevo_rodal: str, rodal_referencia: str, direccion: str, origen: str):
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
        print(' -- Rodal_referencia vacío --')
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
            asignar_colindancias(nuevo_rodal, r_col_v1, vuelta_1_horario[direccion], origen),
            asignar_colindancias(nuevo_rodal, r_col_v2, vuelta_2_antihorario[direccion], origen)
        )

def colindancia_valida(rodal_colindante: str, direccion: str) -> bool:
    """Recorrer la lista de rodales, en el caso en que otro rodal tenga al rodal
    colindante de referencia en la misma dirección que el que está siendo creado
    se retorna True para continuar preguntando al usuario que ingrese un rodal válido"""
    global dicc_rodales
    if rodal_colindante != "":
        for rodal, informacion in dicc_rodales.items():
            if rodal != rodal_colindante:
                if informacion["colindancias"][direccion] == rodal_colindante:
                    return True
    return False


def validar_ingreso(D:dict):
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
        
        #Validaciones Colindancias
        for direccion, rodal_col in colindancias.items():
            if colindancia_valida(rodal_col, direccion):
                raise IngresoInvalido ("Colindancias no validas")

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
    
    return validado, "Ingreso correcto"
    


def retorna_lista_rodales() -> list:
    """retorna auna lista con las IDS de los rodales ya ingresados"""
    global dicc_rodales
    rodales = list(dicc_rodales.keys())
    rodales.append("")
    rodales.sort()
    return rodales

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