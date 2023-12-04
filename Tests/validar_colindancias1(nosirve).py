dicc_rodales = {
'R1': {'b_nativo': '32', 'b_exotico': '68', 'propietario': 'NDSJKNDKAS', 'colindancias': {'N': 'R4', 'NW': 'R6', 'NE': 'R3', 'S': '', 'SW': '', 'SE': 'R2'}},
'R2': {'b_nativo': '23', 'b_exotico': '77', 'propietario': 'NSDJKNDFJSA', 'colindancias': {'N': 'R3', 'NW': 'R1', 'NE': '', 'S': '', 'SW': '', 'SE': ''}},      
'R3': {'b_nativo': '32', 'b_exotico': '68', 'propietario': 'ADBHJKSABNJDK', 'colindancias': {'N': 'R5', 'NW': 'R4', 'NE': '', 'S': 'R2', 'SW': 'R1', 'SE': ''}},
'R4': {'b_nativo': '43', 'b_exotico': '57', 'propietario': 'NDAJKASND', 'colindancias': {'N': '', 'NW': 'R7', 'NE': 'R5', 'S': 'R1', 'SW': 'R6', 'SE': 'R3'}},  
'R5': {'b_nativo': '43', 'b_exotico': '57', 'propietario': 'NDJKSANJDKAS', 'colindancias': {'N': '', 'NW': '', 'NE': '', 'S': 'R3', 'SW': 'R4', 'SE': ''}},     
'R6': {'b_nativo': '43', 'b_exotico': '57', 'propietario': 'JKDASNLKD', 'colindancias': {'N': 'R7', 'NW': '', 'NE': 'R4', 'S': '', 'SW': '', 'SE': 'R1'}},      
'R7': {'b_nativo': '43', 'b_exotico': '57', 'propietario': 'BNDJKSABNDJKSA', 'colindancias': {'N': '', 'NW': '', 'NE': '', 'S': 'R6', 'SW': '', 'SE': 'R4'}}
}

coordenada_opuesta = {
    "N" : "S",
    "NE" : "SW",
    "NW" : "SE",
    "S" : "N",
    "SE" : "NW",
    "SW" : "NE"
}


def asignar_colindancias(nuevo_rodal: str, rodal_referencia: str, direccion: str, origen: str, diccionario: dict()):
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
    if diccionario[rodal_referencia]["colindancias"][coordenada_opuesta[direccion]] != '': 
        print(' -- Vuelta completa --')
        return
    
    # Comenzar el proceso de asignación de colindancias
    if diccionario[rodal_referencia]["colindancias"][coordenada_opuesta[direccion]] == '':

        # Asignar colindancias opuestas
        diccionario[rodal_referencia]["colindancias"][coordenada_opuesta[direccion]] = nuevo_rodal
        diccionario[nuevo_rodal]["colindancias"][direccion] = rodal_referencia
        print(f' A {rodal_referencia} le asigno {nuevo_rodal} en {coordenada_opuesta[direccion]}')
        print(f' A {nuevo_rodal} se le referenció a {rodal_referencia} en {direccion}\n')

        # Inicia proceso de búsqueda
        for coord_a_buscar in referencias_subprocesos[coordenada_opuesta[direccion]]:
            print(f' Busco al {coord_a_buscar} de {rodal_referencia} [vuelta {vuelta}]')

            # Guardar los rodales a buscar en variables
            match vuelta:
                case 1:
                    if diccionario[rodal_referencia]["colindancias"][coord_a_buscar] != '':
                        r_col_v1 = diccionario[rodal_referencia]["colindancias"][coord_a_buscar]
                case 2:
                    if diccionario[rodal_referencia]["colindancias"][coord_a_buscar] != '':
                        r_col_v2 = diccionario[rodal_referencia]["colindancias"][coord_a_buscar]
            
            vuelta += 1
        
        print(f' Rodal al {referencias_subprocesos[coordenada_opuesta[direccion]][0]}: {r_col_v1}')
        print(f' Rodal al {referencias_subprocesos[coordenada_opuesta[direccion]][1]}: {r_col_v2}')

        # Retorna la misma función retornando lo que se encontró en los laterales del rodal referencia
        asignar_colindancias(nuevo_rodal, r_col_v1, vuelta_1_horario[direccion], origen),
        asignar_colindancias(nuevo_rodal, r_col_v2, vuelta_2_antihorario[direccion], origen)
        return (diccionario)
    

def validar_colindancias(datos_rodal: dict, primer_rodal: str, direccion_1er_rodal: str) -> bool:
    '''Comprueba colindancias'''
    global dicc_rodales
    auxiliar = dicc_rodales.copy()
    rodal, datos = datos_rodal.items()
    auxiliar[rodal] = datos

    auxiliar = asignar_colindancias(rodal, primer_rodal, direccion_1er_rodal, auxiliar)
    
    for direct, rod in dicc_rodales[rodal]['colindancias'].items():
        if rod != '':
            if auxiliar[rodal]['colindancias'][direct] != rod:
                return False
    
    #dicc_rodales = asignar_colindancias(rodal, primer_rodal, direccion_1er_rodal, dicc_rodales)
    return True


if __name__ == '__main__':
    validar_colindancias()