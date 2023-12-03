dicc_rodales = {
        'R1'   : {'b_nativo': 40, 'b_exotico': 60, 'propietario': 'F. Henriquez', 'colindancias': {'N': 'R4', 'NW': 'R6', 'NE': 'R3', 'S': '', 'SE': 'R2', 'SW': ''}},
        'R2'   : {'b_nativo': 12, 'b_exotico': 88, 'propietario': 'F. Henriquez', 'colindancias': {'N': 'R3', 'NW': 'R1', 'NE': '', 'S': '', 'SE': '', 'SW': ''}},
        'R3'   : {'b_nativo': 98, 'b_exotico': 2, 'propietario': 'R. Maturana', 'colindancias': {'N': 'R5', 'NW': 'R4', 'NE': '', 'S': 'R2', 'SE': '', 'SW': 'R1'}},
        'R4'   : {'b_nativo': 87, 'b_exotico': 13, 'propietario': 'R. Maturana', 'colindancias': {'N': '', 'NW': 'R7', 'NE': 'R5', 'S': 'R1', 'SE': 'R3', 'SW': 'R6'}},
        'R5'   : {'b_nativo': 90, 'b_exotico': 10, 'propietario': 'R. Maturana', 'colindancias': {'N': '', 'NW': '', 'NE': '', 'S': 'R3', 'SE': '', 'SW': 'R4'}},
        'R6'   : {'b_nativo': 40, 'b_exotico': 60, 'propietario': 'Inv. Lazo', 'colindancias': {'N': 'R7', 'NW': '', 'NE': 'R4', 'S': '', 'SE': 'R1', 'SW': ''}},
        'R7'   : {'b_nativo': 50, 'b_exotico': 50, 'propietario': 'lucas reyes', 'colindancias': {'N': '', 'NW': '', 'NE': '', 'S': 'R6', 'SE': 'R4', 'SW': ''}}
}

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
    tupla_suma = (hectareas_totales_afectadas, bosque_nativo_afectado, bosque_exotico_afectado)
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

def main():
    rodales_afectados = simular_incendio('E', 'R6')
    print(rodales_afectados)
if __name__ == '__main__':
    main()