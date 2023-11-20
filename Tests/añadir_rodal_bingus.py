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
2. Implementar función recursiva (Guía en onenote) <-- PROGRESO
3. Todo el tema de archivos <-- PENDIENTE
"""

class OpcionInvalidaError(Exception): pass
class ValorInvalidoError(Exception): pass
class RodalYaExistenteError(Exception): pass
class EspacioNoValidoError(Exception): pass

# Funciones que ojalá se puedan reciclar
def generar_rodal(
        id_rodal: str, 
        propietario: str, 
        nativo: int, 
        exotico: int,
        colin_N = "none", colin_NW = "none", colin_NE = "none", 
        colin_S = "none", colin_SW = "none", colin_SE = "none"
        ):
    global dicc_rodales

    colindancias = {
        'N' : colin_N,
        'NW' : colin_NW,
        'NE' : colin_NE,
        'S' : colin_S,
        'SE' : colin_SE,
        'SW' : colin_SW
    }

    datos_rodal = {
        'propietario' : propietario,
        'b_nativo' : nativo,
        'b_exotico' : exotico,
        'colindancias' : colindancias
    }

    dicc_rodales[id_rodal] = datos_rodal


def asignar_colindancias(rodal_entregado: str, rodal_colindante: str, direccion: str):

    referencia_coordenadas = {
        "N" : "S",
        "NE" : "SW",
        "NW" : "SE",
        "S" : "N",
        "SE" : "NW",
        "SW" : "NE"
    }
    referencias_subprocesos = {
        "N" : ["NE", "NW"],
        "NE" : ["N", "SE"],
        "NW" : ["N", "SW"],
        "S" : ["SE", "SW"],
        "SE" : ["S", "NE"],
        "SW" : ["S", "NW"]
    }
    if not rodal_colindante == "none":
        # Asignar colindancia opuesta
        dicc_rodales[rodal_colindante]["colindancias"][referencia_coordenadas[direccion]] = rodal_entregado


def validar_rodal(rodal_colindante: str, direccion: str) -> bool:
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

    # Inicializar archivos, en caso que no existan agregar headers
    try:
        with open('Tests/info_rodales.csv', 'r'): existe_rodales = True
    except FileNotFoundError: existe_rodales = False

    try:
        with open('Tests/info_colindancias.csv', 'r'): existe_colindancias = True
    except FileNotFoundError: existe_colindancias = False

    if not existe_rodales:
        with open('Tests/info_rodales.csv', 'w') as headers:
            headers.write("ID, Nombre_Propietario, %_Bosque_nativo, %_Bosque_exotico")
    
    if not existe_colindancias:
        with open('Tests/info_colindancias.csv', 'w') as headers:
            headers.write("ID, rodal colindante, direccion colindancia")

    # Rearmar dicc_rodales desde lo almacenado en el archivo


def guardar_en_archivo():
    """Esta funcion debe guardar los datos en dicc_rodales para que se puedan utilizar
    en una siguiente ejecución del programa"""
    ...

# Programa
def main():
    # Guardar todos los datos en variables
    leer_en_archivo()

    mensaje = """<<< OBD Firewatch >>>\n
 Opciones:
 1. Añadir rodal
 2. Salir y guardar
 3. Salir sin guardar
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
    
    # Variables colindancias
    colin_norte,colin_noroeste,colin_noreste,colin_sur,colin_sureste,colin_suroeste = [0, 0, 0, 0, 0, 0]
    rodal_colindante = "none"

    # Main loop
    loop = True
    while loop:

        while True:
            try:
                opcion = int(input(mensaje))
                if opcion not in [1, 2, 3]:
                    raise OpcionInvalidaError
                break
            except ValueError: print("< Ingrese un caracter válido >\n")
            except OpcionInvalidaError: print("< Opción inválida, ingrese nuevamente >\n")

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
                                        if validar_rodal(rodal_colindante, info_colin):
                                            colin_norte = 0 # Si no se resetea el valor, hace conflicto al ingresar el rodal
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
                                        if validar_rodal(rodal_colindante, info_colin):
                                            colin_noreste = 0   # Si no se resetea el valor, hace conflicto al ingresar el rodal
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
                                        if validar_rodal(rodal_colindante, info_colin):
                                            colin_noroeste = 0  # Si no se resetea el valor, hace conflicto al ingresar el rodal
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
                                        if validar_rodal(rodal_colindante, info_colin):
                                            colin_suroeste = 0  # Si no se resetea el valor, hace conflicto al ingresar el rodal
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
                                        if validar_rodal(rodal_colindante, info_colin):
                                            colin_sureste = 0   # Si no se resetea el valor, hace conflicto al ingresar el rodal
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
                                        if validar_rodal(rodal_colindante, info_colin):
                                            colin_sur = 0   # Si no se resetea el valor, hace conflicto al ingresar el rodal
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
                try: 
                    print(f"Se encuentra al {referencia_coordenadas[info_colin]} de {rodal_colindante}\n")
                    asignar_colindancias(id_rodal, rodal_colindante, info_colin)
                except UnboundLocalError: pass
                #print(f"N : {colin_norte}, NE : {colin_noreste}, NW : {colin_noroeste}, S : {colin_sur}, SE : {colin_sureste}, SW : {colin_suroeste}, Col : {rodal_colindante}")

                generar_rodal(
                    id_rodal, propietario, pb_nativo, pb_exotico,
                    colin_N = colin_norte, colin_NE = colin_noreste, colin_NW = colin_noroeste,
                    colin_S = colin_sur, colin_SE = colin_sureste, colin_SW = colin_suroeste
                )

                for key,value in dicc_rodales.items():
                    print(f"{key}   :   {value}")

            # 2. SALIR Y GUARDAR
            case 2:
                ...
            # 3. SALIR SIN GUARDAR
            case 3:
                while True:
                    try:
                        seguro = input("\n¿Estás seguro que quieres salir sin guardar?(S/N)\n> ").lower()
                        if seguro not in ["s", "n", "si", "no"]:
                            raise OpcionInvalidaError
                        break
                    except OpcionInvalidaError: print("< Opción inválida, ingrese nuevamente >\n")

                if seguro in ["s", "si"]:
                    print("\nGracias por ver suscribanse a shyupss en youtube")
                    loop = False
                if seguro in ["n", "no"]:
                    print()
                


if __name__ == '__main__':
    main()