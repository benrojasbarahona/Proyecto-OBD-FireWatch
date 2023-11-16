#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Esta es la capa de archivos, es la más cercana al csv
# y se dedica a leer y escribir en el archivo

def lee_clientes(file_clientes:str) -> dict:
    # Lee rodales.csv y retorna un diccionario en donde la 
    # clave es el nombre del cliente y el contenido es una lista con la 
    # dirección, el teléfono y el monto adeudado"""
    D = {}
    with open(file_clientes,'r') as file_in:
        L = file_in.readlines()
        for cliente in L:
            detalle = cliente.split(',')
            D[detalle[0].strip("'")] = [detalle[1].strip("'"),
                                        detalle[2].strip("'"),
                                        int(detalle[3].strip())]
    return D

def escribe_clientes(file_clientes:str, D: dict) -> bool:
    """escribe archivo de clientes en formato indicado, retorna 
    True si se hizo exitosamente y False si no"""
    try:
        with open(file_clientes,'w') as file_out:
            for cliente, info in D.items():
                file_out.write(f"'{cliente}','{info[0]}','{info[1]}',{info[2]}\n")
        return True
    except Exception:
        return False

# test de las funciones implementadas en este archivo
def test():
    
    D = lee_clientes('bla.test')
    print(D,'\n-----------')
    # agrega registro a mano:
    D['Marta Brunet'] = ['Pasaje Mistral 3244','+56 9 7385 1230',15280]
    print(D,'\n-----------')
    print(escribe_clientes('bla2.test', D))

if __name__ == "__main__":
    test()