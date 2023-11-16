#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Esta es la capa del main, es decir, acá está main() y
# todo lo relacionado a tkinter, es lo que el USUARIO ve.

import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import logica as log # se imoorta la capa de negocio

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.title("Redimensionar Pantalla")
        self.geometry("600x400")

        # Configuración de los pesos de las filas y columnas
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Crear botones con colores
        boton1 = tk.Button(self, text="Botón 1", bg="red", padx=10, pady=10)
        boton2 = tk.Button(self, text="Botón 2", bg="green", padx=10, pady=10)
        boton3 = tk.Button(self, text="Botón 3", bg="blue", padx=10, pady=10)

        # Ubicar botones en la ventana con espaciado
        boton1.grid(row=0, column=0, padx=(20, 10), pady=(40, 0), sticky="nsew")
        boton2.grid(row=0, column=1, padx=10, pady=(40, 0), sticky="nsew")
        boton3.grid(row=0, column=2, padx=(10, 20), pady=(40, 0), sticky="nsew")

        # Configurar el peso de las columnas para que se redimensionen
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Configurar el peso de las filas para que se redimensionen
        self.rowconfigure(0, weight=1)

if __name__ == "__main__":
    app = Ventana()
    app.mainloop()
