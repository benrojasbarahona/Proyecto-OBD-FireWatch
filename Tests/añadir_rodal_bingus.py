"""
Código hecho para testeo por Bingus pingus

IMPORTANTE: Respecto con la clase rodal, se puede hacer perfectamente sin el uso de clases, es simplemente usar un diccionario.
usé clases porque con ellas es mucho más natural definir un objeto que tenga atributos y metodos propios, piensenla como un
diccionario con otra sintaxis, escribí como inicializar un objeto rodal más abajo, disculpen si es mucho texto JSAKJDSK

Para inicializar (crear) un rodal: 
       Rodal(Id, propietario, bosque_nativo, bosque_exotico, colindancias...)
       Por defecto las colindancias serán 0, es decir, el rodal no es colindante a nada por ese lado
       Inicializar en una variable, esa variable se puede utilizar en otras estructuras de datos
       Si se quiere saber un dato específico, se consulta de la siguiente manera:

            rodal = Rodal(R1, "Lucas reyes", 50, 50)  // se inicializa el rodal
            print(rodal.id) // printea R1
            print(rodal.propietario) // printea Lucas reyes

       Se pueden tambien modificar los datos en cualquier momento de la misma manera:

            rodal.propietario = "Simultaneo Manzanita"
            print(rodal.propietario) // printea Simultaneo Manzanita


"""
class Rodal:
    """ Para crear un rodal:\n 
        Rodal(Id, propietario, bosque_nativo, bosque_exotico, colindancias...)"""
    
    def __init__(self,
            id_rodal: str, propietario: str, nativo: int, exotico: int,
            col_N = 0, col_NW = 0, col_NE = 0, 
            col_S = 0, col_SW = 0, col_SE = 0): # Por defecto es colindante a 0, osea a nada
        # Datos
        self.id = id_rodal
        self.propietario = propietario
        self.bosque_nativo = nativo
        self.bosque_exotico = exotico

        # Colindancias
        self.colin_norte = col_N
        self.colin_noreste = col_NE
        self.colin_noroeste = col_NW
        self.colin_sur = col_S
        self.colin_sureste = col_SE
        self.colin_suroeste = col_SW

class OpcionInvalidaError(Exception): pass
class ValorInvalidoError(Exception): pass

# Funciones que ojalá se puedan reciclar
def generar_rodal(
        id_rodal: str, 
        propietario: str, 
        nativo: int, 
        exotico: int,
        colin_N = 0, colin_NW = 0, colin_NE = 0, 
        colin_S = 0, colin_SW = 0, colin_SE = 0
        ):
    ...

def guardar_en_archivo(rodales: list):
    ...

# Programa
def main():
    # Inicializar archivos, en caso que no existan agregar headers
    try:
        with open('Tests/rodales.csv', 'r'): existe_rodales = True
    except FileNotFoundError: existe_rodales = False

    try:
        with open('Tests/colindancias.csv', 'r'): existe_colindancias = True
    except FileNotFoundError: existe_colindancias = False

    if not existe_rodales:
        with open('Tests/rodales.csv', 'w') as headers:
            headers.write("ID, Nombre_Propietario, %_Bosque_nativo, %_Bosque_exotico")
    
    if not existe_colindancias:
        with open('Tests/colindancias.csv', 'w') as headers:
            headers.write("ID, norte, noreste, noroeste, sur, sureste, suroeste")

    mensaje = """<<< OBD Firewatch >>>\n
 Opciones:
 1. Añadir rodal
 2. Salir y guardar
 3. Salir sin guardar
 > """
    
    # Variables colindancias
    norte, noreste, noroeste, sur, sureste, suroeste = ["none", "none", "none", "none", "none", "none"]
    referencia_coordenadas = {
        "N" : "S",
        "NE" : "SW",
        "NW" : "SE",
        "S" : "N",
        "SE" : "NW",
        "SW" : "NE"
    }

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
                        break
                    except ValueError: print("< Ingrese un caracter válido >")

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

                # Colindancias (ohno)
                colin_loop = True
                while colin_loop:
                    while True:
                        try:
                            opcion = int(input(f"\n> Asigne las colindancias del rodal:\n1. Norte -> {norte}\n2. Noreste -> {noreste}\n3. Noroeste -> {noroeste}\n4. Suroeste -> {suroeste}\n5. Sureste -> {sureste}\n6. Sur -> {sur}\n7. Listo\n> "))
                            if opcion not in [1, 2, 3, 4, 5, 6, 7]:
                                raise ValorInvalidoError
                            break
                        except ValueError: print("< Ingrese un caracter válido >")
                        except ValorInvalidoError: print("< Ingrese un valor válido >")
                    
                    # Asignar colindancias
                    match opcion:
                        # Norte
                        case 1:
                            ...
                        # Noreste
                        case 2:
                            ...
                        # Noroeste
                        case 3:
                            ...
                        # Suroeste
                        case 4:
                            ...
                        # Sureste
                        case 5:
                            ...
                        # Sur
                        case 6:
                            ...
                        # Salir
                        case 7:
                            colin_loop = False
                            print(f"\nResumen del rodal ingresado:\nID: {id_rodal}\nPropietario: {propietario}\n% Bosque nativo: {pb_nativo}\n% Bosque exótico: {pb_exotico}\n")

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