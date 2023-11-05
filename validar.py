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

def validar_colindancias(colindancias):
    lista_de_colindancias = ["N", "S", "E", "O", "NE", "NO", "SE", "SO"]
    colindancias = colindancias.upper()
    if colindancias == "N" or colindancias == "S" or colindancias == "E" or colindancias == "O" or colindancias == "NE" or colindancias == "NO" or colindancias == "SE" or colindancias == "SO":
        return True
    else:
        return False
