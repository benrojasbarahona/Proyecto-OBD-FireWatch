#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Esta es la capa de lógica, donde están las FUNCIONES y VALIDACIONES

import archivos as ar # se importa la capa de datos

<<<<<<< Updated upstream
global D
=======
global A
>>>>>>> Stashed changes
global NOMBRE_BD
NOMBRE_BD = 'clientes.csv'

def lee_archivo_clientes():
    """invoca la lectura de archivo en la capa de datos, deja datos en
    la variable local D"""
    global D
    D = ar.lee_clientes(NOMBRE_BD)

def graba_archivo_clientes():
    """invoca la grabación de archivo en la capa de datos, rercoge
    la información desde la variable local D"""
    global D
    ar.escribe_clientes(NOMBRE_BD, D)