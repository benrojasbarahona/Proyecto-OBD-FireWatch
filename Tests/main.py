import os
import validar as val

"""
La organización de defensa del bosque (en adelante simplemente la “ODB”) se preocupa de proteger los
recursos forestales, en particular los bosques nativos. Para esto, mantienen un registro de las especies que
se encuentran en cada sector del bosque (denominado rodal, con una superficie de 10 ha cada uno.

Los bosques deben protegerse, pero primero debemos conocerlos. Para saber qué hay en ellos, debemos poder
ubicarnos. Nosotros reconocemos un área geográfica hexagonal que denominamos rodal. Cada rodal tiene un
identificador y contiene información sobre las especies que habitan en él. Para facilitar el manejo,
todos los rodales son del mismo tamaño.

Al momento de registrarlos, a continuación del primero se agrega un segundo, y asociado a él se anota la
dirección en donde se encuentra el rodal que ya se había registrado anteriormente.

Cada vez que se agrega un rodal, se anota la dirección en donde se encuentran los rodales colindantes
anteriormente registrados.

Nota que si un rodal A está al sur de otro B, entonces el B está al norte de A, aunque no se anote
explícitamente. Esto será IMPORTANTE más adelante. Así se van agregando todos los rodales uno a uno, en cualquier 
dirección, pero siempre es el nuevo rdal el que apunta a los que estaban registrados antes hasta completar la superficie
total, con todos los rodales conectados con sus vecinos.

Se puede declarar un incendio en uno de los rodales. Aparte de la ubicación, se conoce la dirección del viento.
Siguiendo las relaciones de colindancia, se puede prever hacia qué áreas vecinas se propagará el fuego. Interesa
saber, DE MANERA RECURSIVA, hasta dónde podría extenderse el fuego, para estimar los daños potenciales a la flora y
la fauna del bosque.

El sentido de propagación puede ser en 8 direccones distintas: N, S, E, W, NE, SE, SW y NW. Como en nuestro
ejemplo, el sentido de propagación no siempre coincide con el sentido en que se ha anotado la relación de
colindancia, por lo que hay que considerar las relaciones implícitas: Si el viento sopla hacia el Este, un rodal
que está al NW o SW de otro, le propagará el fuego.

Se requiere crear un programa en Python que almacene la información de los rodales y las relaciones de
colindancia entre ellos, y que sea capaz de informar los rodales que están en riesgo de incendio una vez
que se declare un incendio en uno de los rodales. Los datos de los rodales y sus colindancias deben
almacenarse en archivos. El programa debe ofrecer estas funcionalidades a través de una interfaz gráfica.


Formalmente, se han establecido una serie de requisitos a cumplir por el programa, los que son listados en
la tabla siguiente:

El sistema debe permitir al usuario ingresar rodales de manera persistente a archivos
en formato CSV, recogiendo los siguientes datos:
1.- Identificador del rodal, ID (string)
2.- Porcentaje de bosque nativo (int)
3.- Porcentaje de bosque exótico (int)
4.- Nombre del propietario (string)
5.- Colindancias en los 6 sentidos (N, NE, SE, S, SW, NW)

Se debe validar que el ID del rodal esté compuesto por la letra “R” seguida con un
número entero correlativo de (R1, R2, etc.), el cual debe ser único.

Se debe validar que la suma de los porcentajes de bosque nativo y exótico totalice 100.

Las colindancias deben indicar, para cada sentido, el ID de los rodales que se encuentran
alrededor del rodal que se esté ingresando. La cantidad de colindancias informadas puede
ir desde cero (rodal sin vecinos) a seis (rodal completamente rodeado)

"""

def ingresar_rodal(ids_rodales):
    id_rodal = input("Ingrese el ID del rodal: ")
    while id_rodal in ids_rodales:
        id_rodal = input("Ingrese el ID del rodal: ")
    #usa la función validar_id_rodal de validar.py
    id_rodal = val.validar_id_rodal(id_rodal, ids_rodales)
    ids_rodales.append(id_rodal)
    return id_rodal

def ingresar_colindancias():
    # lista_de_colindancias = ["N", "NE", "NW", "S", "SE", "SW", "0"], validar que lo que ingrese el usuario esté aquí
    print("""
A continuación, tiene que ingresar las colindancias del rodal. Las opciones son:
1.- N
2.- NE
3.- NW
4.- S
5.- SE
6.- SW
9.- 0 (ninguna colindancia)""")
    colindancias = input("Ingrese las colidancias: ")
    colindancias = colindancias.split(",")
    return colindancias
    
def simular_incendios():
    global ids_rodales
    #Implementa una función recursiva que reciba como parámetro el id del rodal que se está quemando y el sentido del viento, 
    # y que retorne una lista con los ids de los rodales que se quemarán.
    while True:
        print("---------- OBD ----------")
        id_rodal = input("Ingrese el ID del rodal que desea quemar: ")
        while id_rodal not in ids_rodales:
            id_rodal = input("¡Error! Ingrese un rodal registrado: ")
        print("---------- OBD ----------")
        print("""
A continuación, tiene que ingresar el sentido del viento del rodal. Las opciones son:
1.- N
2.- NE
3.- NW
4.- S
5.- SE
6.- SW""")
        sentido_viento = input("Sentido del viento: ")
        while val.validar_sentido_viento(sentido_viento) == False:
            sentido_viento = input("Sentido del viento: ")
        print("Okay! vamos a simular el incendio")
        

def main():
    global ids_rodales
    print(
    '''---------- OBD ----------
    ¿Qué desea hacer?
    N°1: Ingresar un nuevo rodal
    N°2: Ver los datos de algún rodal
    N°3: Editar información de un rodal
    N°4: Eliminar un rodal
    N°5: Desplegar informe completo
    N°6: Simular Incendio
     ''')
    listas_dicts_rodales = [] # Lista de diccionarios de rodales. Cada diccionario es un rodal y sus datos asociados son sus valores, tales como id, nombre, etc.
    ids_rodales = [] # Lista de ids de rodales. Los ids son los nombres de los rodales
    
    if os.path.exists("rodales.csv"): # si existe el archivo, lo abre y lo lee.
        with open("rodales.csv", 'r') as archivo:
            lista = archivo.readlines()
    else:
        with open("rodales.csv", 'w'): # error, se borra el rodal anterior o no se agregan nuevos rodales
            pass
    if os.path.exists("colindancias.csv"):
        with open("colindancias.csv", 'r') as archivo:
            lista = archivo.readlines()
    else:
        with open("colindancias.csv", 'w'):
            pass
    
    while True:
        try:
            while True:
                opcion = int(input("Ingrese el número de la opción que desea realizar: "))
                if opcion < 1 or opcion > 6:
                    print("¡Error! Ingrese una opción válida")
                else: 
                    break
            if opcion == 1:
                print("---------- OBD ----------")
                print("Ingrese los datos del rodal")
                print("-------------------------")
                while True:
                    id_rodal = ingresar_rodal(ids_rodales)
                    porcentaje_bosque_nativo = int(input("Porcentaje de bosque nativo: "))
                    porcentaje_bosque_exotico = int(input("Porcentaje de bosque exótico: "))
                    while val.validar_porcentajes(porcentaje_bosque_nativo, porcentaje_bosque_exotico) == False:
                        print("¡Error! El porcentaje tiene que sumar 100")
                        porcentaje_bosque_nativo = int(input("Porcentaje de bosque nativo: "))
                        porcentaje_bosque_exotico = int(input("Porcentaje de bosque exótico: "))
                    nombre_propietario = input("Nombre del propietario: ")
                    nombre_propietario = val.cadena_no_vacia(nombre_propietario)
                    colindancias = ingresar_colindancias()
                    diccionario_rodal = {"ID": id_rodal, "Porcentaje de bosque nativo": porcentaje_bosque_nativo, "Porcentaje de bosque exótico": porcentaje_bosque_exotico, "Nombre del propietario": nombre_propietario, "Colindancias": colindancias}
                    listas_dicts_rodales.append(diccionario_rodal)
                    with open("rodales.csv", 'a') as archivo:
                        archivo.write(id_rodal + "," + str(porcentaje_bosque_nativo) + "," + str(porcentaje_bosque_exotico) + "," + nombre_propietario + "\n")
                    with open("colindancias.csv", 'a') as archivo:
                       for colindancia in colindancias:
                            archivo.write(id_rodal + "," + colindancia + "\n")
                    print("---------- OBD ----------")
                    print("Rodal ingresado con éxito")
                    print("---------- OBD ----------")
                    ids_rodales.append(id_rodal)
                    continuar = input("¿Desea ingresar otro rodal? (S/N): ")
                    if continuar == "N" or continuar == "n":
                        break
                break


            if opcion == 2:
                print(ids_rodales)
                print("---------- OBD ----------")
                print("Ingrese el ID del rodal que desea ver: ")
                id_rodal = input("ID del rodal: ")
                while id_rodal not in ids_rodales:
                    id_rodal = input("ID del rodal: ")
                for diccionario_rodal in listas_dicts_rodales:
                    if diccionario_rodal["ID"] == id_rodal:
                        print("---------- OBD ----------")
                        print("ID: " + diccionario_rodal["ID"])
                        print("Porcentaje de bosque nativo: " + diccionario_rodal["Porcentaje de bosque nativo"])
                        print("Porcentaje de bosque exótico: " + diccionario_rodal["Porcentaje de bosque exótico"])
                        print("Nombre del propietario: " + diccionario_rodal["Nombre del propietario"])
                        print("Colindancias: " + str(diccionario_rodal["Colindancias"]))
                        print("---------- OBD ----------")
                        
            if opcion == 3:
                print("---------- OBD ----------")
                print("Ingrese el ID del rodal que desea editar: ")
                id_rodal = input("ID del rodal: ")
                while id_rodal not in ids_rodales:
                    id_rodal = input("ID del rodal: ")
                for diccionario_rodal in listas_dicts_rodales:
                    if diccionario_rodal["ID"] == id_rodal:
                        print("---------- OBD ----------")
                        print("ID: " + diccionario_rodal["ID"])
                        print("Porcentaje de bosque nativo: " + diccionario_rodal["Porcentaje de bosque nativo"])
                        print("Porcentaje de bosque exótico: " + diccionario_rodal["Porcentaje de bosque exótico"])
                        print("Nombre del propietario: " + diccionario_rodal["Nombre del propietario"])
                        print("Colindancias: " + str(diccionario_rodal["Colindancias"]))
                        print("---------- OBD ----------")
                        print("Ingrese los nuevos datos del rodal: ")
                        id_rodal = input("ID del rodal: ")
                        while id_rodal in ids_rodales:
                            id_rodal = input("ID del rodal: ")
                        ids_rodales.append(id_rodal)
                        porcentaje_bosque_nativo = input("Porcentaje de bosque nativo: ")
                        porcentaje_bosque_exotico = input("Porcentaje de bosque exótico: ")
                        while val.validar_porcentajes(porcentaje_bosque_nativo, porcentaje_bosque_exotico) == False:
                            porcentaje_bosque_nativo = input("Porcentaje de bosque nativo: ")
                            porcentaje_bosque_exotico = input("Porcentaje de bosque exótico: ")
                        nombre_propietario = input("Nombre del propietario: ")
                        colindancias = input("Colindancias: ")
                        while val.validar_colindancias(colindancias) == False:
                            colindancias = input("Colindancias: ")
                        colindancias = colindancias.split(",")
                        diccionario_rodal = {"ID": id_rodal, "Porcentaje de bosque nativo": porcentaje_bosque_nativo, "Porcentaje de bosque exótico": porcentaje_bosque_exotico, "Nombre del propietario": nombre_propietario, "Colindancias": colindancias}
                        listas_dicts_rodales.append(diccionario_rodal)
                        with open("rodales.csv", 'a') as archivo:
                            archivo.write(id_rodal + "," + porcentaje_bosque_nativo + "," + porcentaje_bosque_exotico + "," + nombre_propietario + "\n")
                        with open("colindancias.csv", 'a') as archivo:
                            for colindancia in colindancias:
                                archivo.write(id_rodal + "," + colindancia + "\n")
                        print("---------- OBD ----------")
                        print("Rodal editado con éxito")
                        print("---------- OBD ----------")

            if opcion == 4:
                while True:
                    print("---------- OBD ----------")
                    print("Ingrese el ID del rodal que desea eliminar: ")
                    id_rodal = input("ID del rodal: ")
                    while id_rodal not in ids_rodales:
                        id_rodal = input("¡Error! Ese rodal no está registrado. Ingrese otro:")
                    for diccionario_rodal in listas_dicts_rodales:
                        if diccionario_rodal["ID"] == id_rodal:
                            listas_dicts_rodales.remove(diccionario_rodal)
                            print("---------- OBD ----------")
                            print("Rodal eliminado con éxito")
                            print("---------- OBD ----------")
                    continuar = input("¿Desea ingresar otro rodal? (S/N): ")
                    if continuar == "N" or continuar == "n":
                        break
                print("---------- OBD ----------")
                print("Rodales: ")
                for diccionario_rodal in listas_dicts_rodales:
                    print(diccionario_rodal["ID"] + ": " + diccionario_rodal["Nombre del propietario"])
                print("---------- OBD ----------")
                print("Colindancias: ")
                with open("colindancias.csv", 'r') as archivo:
                    lista = archivo.readlines()
                    for linea in lista:
                        print(linea)

            if opcion == 6:
                #Implementa una función recursiva que reciba como parámetro el id del rodal que se está quemando y el sentido del viento, 
                # y que retorne una lista con los ids de los rodales que se quemarán.
                while True:
                    simular_incendios()
                    

        except ValueError:
            print("¡Error! Ingrese una opción válida: ")
    
if __name__ == "__main__":
    main()
