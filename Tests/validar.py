from main import *
#valida los porcentajes de bosque nativo y bosque plantado
def validar_id_rodal(id_rodal, ids_rodales):
    #Verifica que no se haya ingresado un id_rodal vacío, que el primer caracter sea una R o r y que el resto sean números
    while True:
        while id_rodal == "" or id_rodal == " ":
            id_rodal = input("¡Error! La primera letra debe ser una 'R' seguido de números: ")
        while id_rodal[0] != "R" and id_rodal[0] != "r":
            id_rodal = input("¡Error! La primera letra debe ser una 'R' seguido de números: ")
        while not id_rodal[1:].isdigit():
            id_rodal = input("¡Error! La primera letra debe ser una 'R' seguido de números: ")
        id_rodal = id_rodal.upper()
        while id_rodal in ids_rodales:
            id_rodal = input("¡Error! Ese ID ya rodal ya está registrado. Ingrese otro: ")
            id_rodal = validar_id_rodal(id_rodal)
        return id_rodal

def cadena_no_vacia(cadena):
    #Verifica que la cadena no esté vacía o sean solamente espacios
    while cadena == "" or cadena.isspace():
        cadena = input("¡Error! No puede estar vacío: ")
    return cadena



def validar_porcentajes(porcentaje_bosque_nativo, porcentaje_bosque_exotico):
    if porcentaje_bosque_nativo + porcentaje_bosque_exotico == 100:
        return True
    else:
        return False

def validar_colindancias():
    print("""
A continuación, tiene que ingresar las colindancias del rodal. Las opciones son:
1.- N
2.- NE
3.- NW
4.- S
5.- SE
6.- SW
9.- 0 (ninguna colindancia)""")
    lista_de_colindancias = ["N", "NE", "NW", "S", "SE", "SW", "0"]
    colindancias = input("Ingrese las colindacias (por ejemplo: NE, S, SW): ")
    colindancias = colindancias.upper()
    if colindancias in lista_de_colindancias:
        return True
    else:
        return False

def validar_sentido_viento():
    lista_de_sentidos = ["N", "NE", "NW", "S", "SE", "SW"]
    sentido_viento = sentido_viento.upper()
    if sentido_viento in lista_de_sentidos:
        return True
    else:
        return False

#def validar_si_esta_ingresado(ids_rodales):
#    id_rodal = input("ID del rodal: ")
#    while id_rodal not in ids_rodales:
#        id_rodal = input("¡Error! El rodal no está registrado. Ingrese un rodal válido: ")
#    return id_rodal