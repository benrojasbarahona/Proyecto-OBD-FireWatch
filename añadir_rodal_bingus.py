"""
Código hecho para testeo por Bingus pingus

IMPORTANTES:
# Forma de dicc_rodales
    {"id_rodal_1" : {
            'propietario': 'Lucas Reyes', 
            'b_nativo': 50, 
            'b_exotico': 50, 
            'colindancias': {'N': R3, 'NW': R5, 'NE': R2, 'S': 0, 'SE': 0, 'SW': 0}
        },
        "id_rodal_2": ...}

PENDIENTE:
1. Validar que el rodal referencia no tenga un rodal existente en la misma posición <-- RESUELTO
2. Implementar función recursiva (Guía en onenote) <-- RESUELTO
3. Todo el tema de archivos <-- PENDIENTE
"""
import os

class OpcionInvalidaError(Exception): pass
class ValorInvalidoError(Exception): pass
class RodalYaExistenteError(Exception): pass
class EspacioNoValidoError(Exception): pass

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

    for rodal, informacion in dicc_rodales.items():
        if rodal != rodal_colindante:
            if informacion["colindancias"][direccion] == rodal_colindante:
                return True

    return False


def leer_en_archivo():
    """El trabajo de esta función es crear archivos en el caso de que no existan antes y
    para cada ejecución del programa, al principio armar el diccionario "dicc_rodales" para que
    se guarde el progreso del usuario"""

    # Inicializar archivos
    try:
        with open('Tests/rodales.csv', 'x'): existe_rodales = False
    except FileExistsError: existe_rodales = True

    try:
        with open('Tests/colindancias.csv', 'x'): existe_colindancias = False
    except FileExistsError: existe_colindancias = True

    # Rearmar dicc_rodales desde lo almacenado en el archivo
    temp_colindancias = dict()

    # Armar el diccionario temporal de colindancias
    if existe_colindancias:
        with open('Tests/colindancias.csv', 'r', encoding = 'utf-8') as archivo:
            datos = archivo.read().splitlines()
        
        for colindancia in datos:
            id_rodal, colindante, direccion = colindancia.split(",")
            id_rodal.strip(); colindante.strip(); direccion.strip()

            if id_rodal not in temp_colindancias:
                temp_colindancias[id_rodal] = {'N':'','NW':'','NE':'','S':'','SE':'','SW':''}

            temp_colindancias[id_rodal][direccion] = colindante.strip('"').strip('"')

    # Extraer los datos de los rodales
    if existe_rodales:
        with open('Tests/rodales.csv', 'r', encoding = 'utf-8') as archivo:
            datos = archivo.read().splitlines()

        for rodal in datos:
            id_rodal, b_nativo, b_exotico, propietario = rodal.split(",")
            id_rodal.strip(); b_nativo.strip(); b_exotico.strip(); propietario.strip()

            # Generar todo utilizando la función generar_rodal
            generar_rodal(id_rodal, propietario, int(b_nativo), int(b_exotico), colindancias_dict = temp_colindancias[id_rodal])


def guardar_en_archivo(modo_escritura = 'a'):
    """Esta funcion debe guardar los datos en dicc_rodales para que se puedan utilizar
    en una siguiente ejecución del programa"""

    # Escribir en el archivo de rodales
    with open('Tests/rodales.csv', modo_escritura, encoding = "utf-8") as archivo:

        for id_rodal, datos in dicc_rodales.items():
            archivo.write(f'{id_rodal}, ')

            for tipo, dato in datos.items():

                if tipo != "colindancias" and tipo != "propietario":
                    archivo.write(f'{dato}, ')
                elif tipo == "propietario":
                    archivo.write(f'{dato}\n')

    # Escribir las colindancias en el archivo
    with open('Tests/colindancias.csv', modo_escritura, encoding = 'utf-8') as archivo:

        for id_rodal, datos in dicc_rodales.items():
            for direccion, colindante in dicc_rodales[id_rodal]['colindancias'].items():

                if colindante != '':
                    archivo.write(f'{id_rodal}, {colindante}, {direccion}\n')

def limpiar_datos():

    with open('Tests/colindancias.csv', 'w', encoding = 'utf-8'):
        pass

    with open('Tests/rodales.csv', 'w', encoding = 'utf-8'):
        pass


# Programa
def main():

    mensaje = """<<< OBD Firewatch >>>\n
 Opciones:
 1. Añadir rodal
 2. Guardar datos
 3. Eliminar datos
 4. Salir
 > """
    referencia_coordenadas = {
        "N" : "Sur",
        "NE" : "Suroeste",
        "NW" : "Sureste",
        "S" : "Norte",
        "SE" : "Noroeste",
        "SW" : "Noreste"
    }
    
    global dicc_rodales
    dicc_rodales = dict()

    # Reconstruir dicc_rodales
    leer_en_archivo()

    # # ----- debug :3 -----
    # for key,value in dicc_rodales.items():
    #     print(f"{key}   : {value}")
    # print()

    # Main loop
    loop = True
    while loop:

        # Preguntar por la opción del menú
        while True:
            try:
                opcion = int(input(mensaje))
                if opcion not in [1, 2, 3, 4]:
                    raise OpcionInvalidaError
                break
            except ValueError: print("< Ingrese un caracter válido >\n")
            except OpcionInvalidaError: print("< Opción inválida, ingrese nuevamente >\n")

        # Según lo que haya escogido el usuario
        match opcion:
            # 1. AÑADIR RODAL
            case 1:
                # Preguntar por el ID
                while True:
                    try:
                        id_rodal = int(input("\n> Ingrese el ID del rodal:\nEjemplo: R1, R2...\n> R"))
                        id_rodal = "R" + str(id_rodal)
                        if id_rodal in dicc_rodales:
                            raise RodalYaExistenteError
                        break
                    except ValueError: print("< Ingrese un caracter válido >")
                    except RodalYaExistenteError: print("< El rodal ya existe >")

                # Preguntar por el propietario
                propietario = input("\n> Ingrese el nombre del propietario:\n> ")

                # Preguntar por el porcentaje de bosque (Quedará mejor en interfaz gráfica)
                while True:
                    try:
                        tipo = int(input("\n> Porcentaje de bosque:\nSeleccione una opción, se completará automáticamente la otra\n1. Bosque Nativo\n2. Bosque Exótico\n> "))
                        if tipo not in [1, 2]:
                            raise OpcionInvalidaError
                        break

                    except ValueError: print("< Ingrese un caracter válido >")
                    except OpcionInvalidaError: print("< Opción inválida, ingrese nuevamente >")
                
                match tipo:
                    # Bosque nativo
                    case 1:
                        while True:
                            try:
                                pb_nativo = int(input("\n> Ingrese el porcentaje de bosque nativo:\n> % "))
                                if pb_nativo > 100 or pb_nativo < 0:
                                    raise ValorInvalidoError
                                pb_exotico = 100 - pb_nativo
                                break
                            except ValueError: print("< Ingrese un caracter válido >")
                            except ValorInvalidoError: print("< Ingrese un valor válido >")
                    # Bosque exótico
                    case 2:
                        while True:
                            try:
                                pb_exotico = int(input("\n> Ingrese el porcentaje de bosque nativo:\n> % "))
                                if pb_exotico > 100 or pb_exotico < 0:
                                    raise ValorInvalidoError
                                pb_nativo = 100 - pb_exotico
                                break
                            except ValueError: print("< Ingrese un caracter válido >")
                            except ValorInvalidoError: print("< Ingrese un valor válido >")

                print(f'Bosque Nativo: %{pb_nativo}\nBosque Exótico: %{pb_exotico}\n')

                # IMPORTANTE RESETEAR LAS VARIABLES CADA VEZ QUE SE VAYA A AGREGAR UN NUEVO RODAL
                colin_norte,colin_noroeste,colin_noreste,colin_sur,colin_sureste,colin_suroeste = ['', '', '', '', '', '']
                rodal_colindante = "none"

                # Colindancias
                if not dicc_rodales: invalido = False
                else: invalido = True
                while invalido:
                    while True:
                        try:
                            opcion = int(input(f"\n> Asigne las colindancias del rodal:\n1. Norte\n2. Noreste\n3. Noroeste\n4. Suroeste\n5. Sureste\n6. Sur\n> "))
                            if opcion not in [1, 2, 3, 4, 5, 6]:
                                raise ValorInvalidoError
                            break
                        except ValueError: print("< Ingrese un caracter válido >")
                        except ValorInvalidoError: print("< Ingrese un valor válido >")
                        
                    # Asignar colindancias
                    if invalido:
                        match opcion:
                            # Norte
                            case 1:
                                while True:
                                    try: 
                                        rodal_colindante = int(input("\n> Rodal al norte:\n> R"))
                                        rodal_colindante = "R" + str(rodal_colindante)
                                        if rodal_colindante not in dicc_rodales:
                                            raise OpcionInvalidaError
                                        info_colin = "N"
                                        if colindancia_valida(rodal_colindante, info_colin):
                                            colin_norte = '' # Si no se resetea el valor, hace conflicto al ingresar el rodal
                                            raise EspacioNoValidoError
                                        invalido = False
                                        colin_norte = rodal_colindante
                                        break
                                    except ValueError: print("< Ingrese un caracter válido >")
                                    except OpcionInvalidaError: print("< El rodal no existe >")
                                    except EspacioNoValidoError:
                                        print("\n< El espacio ya está siendo ocupado por otro rodal >") 
                                        invalido = True; break
                            # Noreste
                            case 2:
                                while True:
                                    try: 
                                        rodal_colindante = int(input("\n> Rodal al noreste:\n> R"))
                                        rodal_colindante = "R" + str(rodal_colindante)
                                        if rodal_colindante not in dicc_rodales:
                                            raise OpcionInvalidaError
                                        info_colin = "NE"
                                        if colindancia_valida(rodal_colindante, info_colin):
                                            colin_noreste = ''   # Si no se resetea el valor, hace conflicto al ingresar el rodal
                                            raise EspacioNoValidoError
                                        invalido = False
                                        colin_noreste = rodal_colindante
                                        break
                                    except ValueError: print("< Ingrese un caracter válido >")
                                    except OpcionInvalidaError: print("< El rodal no existe >")
                                    except EspacioNoValidoError:
                                        print("\n< El espacio ya está siendo ocupado por otro rodal >") 
                                        invalido = True; break
                            # Noroeste
                            case 3:
                                while True:
                                    try: 
                                        rodal_colindante = int(input("\n> Rodal al noroeste:\n> R"))
                                        rodal_colindante = "R" + str(rodal_colindante)
                                        if rodal_colindante not in dicc_rodales:
                                            raise OpcionInvalidaError
                                        info_colin = "NW"
                                        if colindancia_valida(rodal_colindante, info_colin):
                                            colin_noroeste = ''  # Si no se resetea el valor, hace conflicto al ingresar el rodal
                                            raise EspacioNoValidoError
                                        invalido = False
                                        colin_noroeste = rodal_colindante
                                        break
                                    except ValueError: print("< Ingrese un caracter válido >")
                                    except OpcionInvalidaError: print("< El rodal no existe >")
                                    except EspacioNoValidoError:
                                        print("\n< El espacio ya está siendo ocupado por otro rodal >") 
                                        invalido = True; break
                            # Suroeste
                            case 4:
                                while True:
                                    try: 
                                        rodal_colindante = int(input("\n> Rodal al suroeste:\n> R"))
                                        rodal_colindante = "R" + str(rodal_colindante)
                                        if rodal_colindante not in dicc_rodales:
                                            raise OpcionInvalidaError
                                        info_colin = "SW"
                                        if colindancia_valida(rodal_colindante, info_colin):
                                            colin_suroeste = ''  # Si no se resetea el valor, hace conflicto al ingresar el rodal
                                            raise EspacioNoValidoError
                                        invalido = False
                                        colin_suroeste = rodal_colindante
                                        break
                                    except ValueError: print("< Ingrese un caracter válido >")
                                    except OpcionInvalidaError: print("< El rodal no existe >")
                                    except EspacioNoValidoError:
                                        print("\n< El espacio ya está siendo ocupado por otro rodal >") 
                                        invalido = True; break
                            # Sureste
                            case 5:
                                while True:
                                    try: 
                                        rodal_colindante = int(input("\n> Rodal al sureste:\n> R"))
                                        rodal_colindante = "R" + str(rodal_colindante)
                                        if rodal_colindante not in dicc_rodales:
                                            raise OpcionInvalidaError
                                        info_colin = "SE"
                                        if colindancia_valida(rodal_colindante, info_colin):
                                            colin_sureste = ''   # Si no se resetea el valor, hace conflicto al ingresar el rodal
                                            raise EspacioNoValidoError
                                        invalido = False
                                        colin_sureste = rodal_colindante
                                        break
                                    except ValueError: print("< Ingrese un caracter válido >")
                                    except OpcionInvalidaError: print("< El rodal no existe >")
                                    except EspacioNoValidoError:
                                        print("\n< El espacio ya está siendo ocupado por otro rodal >") 
                                        invalido = True; break
                            # Sur
                            case 6:
                                while True:
                                    try: 
                                        rodal_colindante = int(input("\n> Rodal al sur:\n> R"))
                                        rodal_colindante = "R" + str(rodal_colindante)
                                        if rodal_colindante not in dicc_rodales:
                                            raise OpcionInvalidaError
                                        info_colin = "S"
                                        if colindancia_valida(rodal_colindante, info_colin):
                                            colin_sur = ''   # Si no se resetea el valor, hace conflicto al ingresar el rodal
                                            raise EspacioNoValidoError
                                        invalido = False
                                        colin_sur = rodal_colindante
                                        break
                                    except ValueError: print("< Ingrese un caracter válido >")
                                    except OpcionInvalidaError: print("< El rodal no existe >")
                                    except EspacioNoValidoError:
                                        print("\n< El espacio ya está siendo ocupado por otro rodal >") 
                                        invalido = True; break
                        #print(f"{id_rodal} : {rodal_colindante} : {info_colin}")
                    
                print(f"\nResumen del rodal ingresado:\nID: {id_rodal}\nPropietario: {propietario}\n% Bosque nativo: {pb_nativo}\n% Bosque exótico: {pb_exotico}")
                # Primero se debe generar el rodal para que exista en el diccionario, luego se pueden actualizar las colindancias
                generar_rodal(
                    id_rodal, propietario, pb_nativo, pb_exotico,
                    colin_N = colin_norte, colin_NE = colin_noreste, colin_NW = colin_noroeste,
                    colin_S = colin_sur, colin_SE = colin_sureste, colin_SW = colin_suroeste
                )
                # Luego se imprime la colindancia y se actualiza gracias a la funcion recursiva
                try: 
                    # Dentro de una excepcion en caso de que info_colin no exista
                    print(f"Se encuentra al {referencia_coordenadas[info_colin]} de {rodal_colindante}\n")
                    asignar_colindancias(id_rodal, rodal_colindante, info_colin, rodal_colindante)
                except UnboundLocalError: pass

                # -------------- debug --------------
                for key,value in dicc_rodales.items():
                    print(f"{key}   : {value}")
                print()

            # 2. GUARDAR DATOS
            case 2:
                guardar_en_archivo()
                print('\n< Datos guardados exitosamente >\n')

            # 3. LIMPIAR ARCHIVO
            case 3:
                while True:
                    try:
                        seguro = input("\n¿Estás seguro que quieres eliminar los datos?(S/N)\n> ").lower()
                        if seguro not in ["s", "n", "si", "no"]:
                            raise OpcionInvalidaError
                        break
                    except OpcionInvalidaError: print("< Opción inválida, ingrese nuevamente >\n")

                if seguro in ["s", "si"]:
                    limpiar_datos()
                    print()
                if seguro in ["n", "no"]:
                    print()

            # 4. SALIR
            case 4:
                while True:
                    try:
                        seguro = input("\n¿Estás seguro que quieres salir?(S/N)\n> ").lower()
                        if seguro not in ["s", "n", "si", "no"]:
                            raise OpcionInvalidaError
                        break
                    except OpcionInvalidaError: print("< Opción inválida, ingrese nuevamente >\n")

                if seguro in ["s", "si"]:
                    print("\no/")
                    loop = False
                if seguro in ["n", "no"]:
                    print()
                
if __name__ == '__main__':
    main()