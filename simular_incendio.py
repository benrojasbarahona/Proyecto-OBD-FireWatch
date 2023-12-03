#Cada rodal es una figura hexagonal con las direcciones de los lados como se muestra en la figura.
#sus lados tienen colindancias hacia el norte (N), noreste (NE), sureste (SE), sur (S), suroeste (SW) y noroeste (NW).

def main(): 

    # Diccionario de colindancias desde el archivo
    # RN : {propietario: 'nombre', b_nativo: 0, b_exotico: 0, colindancias: {N: 'R1', NW: 'R2', NE: 0, S: 0, SE: 0, SW: 0}
    diccionario_rodales = {
        'R1'   : {'propietario': 'Ben', 'b_nativo': 40, 'b_exotico': 60, 'colindancias': {'N': 'R4', 'NW': 'R6', 'NE': 'R3', 'S': 0, 'SE': 'R2', 'SW': 0}},
        'R2'   : {'propietario': 'Joe', 'b_nativo': 12, 'b_exotico': 88, 'colindancias': {'N': 'R3', 'NW': 'R1', 'NE': 0, 'S': 0, 'SE': 0, 'SW': 0}},
        'R3'   : {'propietario': 'Karl', 'b_nativo': 98, 'b_exotico': 2, 'colindancias': {'N': 'R5', 'NW': 'R4', 'NE': 0, 'S': 'R2', 'SE': 0, 'SW': 'R1'}},
        'R4'   : {'propietario': 'JH', 'b_nativo': 87, 'b_exotico': 13, 'colindancias': {'N': 0, 'NW': 'R7', 'NE': 'R5', 'S': 'R1', 'SE': 'R3', 'SW': 'R6'}},
        'R5'   : {'propietario': 'Trump', 'b_nativo': 90, 'b_exotico': 10, 'colindancias': {'N': 0, 'NW': 0, 'NE': 0, 'S': 'R3', 'SE': 0, 'SW': '0'}} , 
        'R6'   : {'propietario': 'Van', 'b_nativo': 40, 'b_exotico': 60, 'colindancias': {'N': 'R7', 'NW': 0, 'NE': 'R4', 'S': 0, 'SE': 'R1', 'SW': 0}},
        'R7'  : {'propietario': 'Leo', 'b_nativo': 50, 'b_exotico': 50, 'colindancias': {'N': 0, 'NW': 0, 'NE': 0, 'S': 'R6', 'SE': 'R4', 'SW': 0}}} 

    # Simular incendio en un rodal y mostrar los rodales afectados
    rodal_comprometido = input('Ingrese rodal comprometido inicial, para simular incendio: ')
    direccion = input('Ingrese dirección del viento (dirección del incendio): ')
    rodales_afectados = simular_incendio(rodal_comprometido, direccion, diccionario_rodales)

    print('Los rodales afectados son: ', rodales_afectados)
#  Creo una funcion la cual recibe como parametro el diccionario de colindancias,
#  el rodal comprometido y la direccion del viento, para simular el incendio y hacia donde se propaga.
#  Las direcciones del viento pueden ser: N, NE, SE, S, SW, NW, E, W. 
#  Cabe señalar que E afecta a NE y SE, y W afecta a NW y SW, debido a la forma hexagonal de los rodales.
#  1. La funcion retorna una lista con los rodales afectados y flotantes de las hectareas afectadas.
#  2. La funcion debe ser recursiva.

def simular_incendio(rodal_comprometido, direccion, dicc_rodales):

    #_________________________________INFORMACION_______________________________________
    #1. Debe desplegar la funcion de "consultar rodal" para el rodal comprometido + direccion
    #2. Debe desplegar la funcion de "consultar rodal" para los rodales afectados
    #3. Debe retornar la set de rodales afectados
    #4. Debe retornar la set de propietarios afectados
    #5. Debe retornar las hectareas totales afectadas por el incendio (cada rodal tiene 10 hectareas)
    #6. Debe retornar las hectareas de bosque nativo afectado con una conversión de (porcentaje*0.1)
    #7. Debe retornar las hectareas de bosque exotico afectado con una conversión de (porcentaje*0.1)
    #___________________________________________________________________________________

    # Listas
    rodales_riesgo_incendio = set()
    propietarios_afectados = set()

    # Contadores
    bosque_nativo_afectado = dicc_rodales[rodal_comprometido]['b_nativo'] * 0.1
    bosque_exotico_afectado = dicc_rodales[rodal_comprometido]['b_exotico'] * 0.1
    hectareas_totales_afectadas = 0.

    # Agregar el rodal comprometido a las lista de propietarios
    propietarios_afectados.add(dicc_rodales[rodal_comprometido]['propietario'])

    # Definir las direcciones afectadas según la dirección del viento
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

    # Iterar sobre las direcciones afectadas y agregar los rodales afectados
    for dir_afectada in direcciones_afectadas[direccion]:
        rodal_afectado = dicc_rodales[rodal_comprometido]['colindancias'][dir_afectada]
        if rodal_afectado != 0:
            rodales_riesgo_incendio.add(rodal_afectado)
            propietarios_afectados.add(dicc_rodales[rodal_afectado]['propietario'])
            
            
    bosque_nativo_afectado += dicc_rodales[rodal_afectado]['b_nativo'] * 0.1
    bosque_exotico_afectado += dicc_rodales[rodal_afectado]['b_exotico'] * 0.1
    hectareas_totales_afectadas = bosque_nativo_afectado + bosque_exotico_afectado
    
    return rodales_riesgo_incendio, propietarios_afectados, bosque_nativo_afectado, bosque_exotico_afectado, hectareas_totales_afectadas

    #Realizo recursividad para los rodales afectados, recorro el set de rodales afectados y llamo a la funcion,
    #solo si el rodal afectado no ha sido afectado anteriormente.
    #Hago un break si no existen colindancias en la direccion del viento.
    #Retorno finalmente

if __name__ == '__main__':
    main()

