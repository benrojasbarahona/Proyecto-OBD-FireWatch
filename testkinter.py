#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk

def main():
    root = tk.Tk() # crea ventana principal
    root.config(width=300, height=200)
    root.title('OBD Firewatch - Consultar') # título de la aplicación
    img_background = tk.PhotoImage(file = "assets/iconos/fondo_verde.png")
    #label_bg = tk.Label(root, image=img_background).place(x=-0,y=0)

    img_nube = tk.PhotoImage(file = "assets/iconos/nube.png").subsample(25,25)
    boton_guardar = ttk.Button(root, image=img_nube).place(x=10,y=10)

    #Configuro entry con texto temporal
    def temp_text(e):
        entrada_busqueda.delete(0,"end")

    entrada_busqueda = tk.Entry(root, width = 30, borderwidth = 2)
    #Considerar mover el .bind a otro lado, actualmente borra texto si cambio el foco a otro lado, quizas otro evento, no focusin
    entrada_busqueda.bind("<FocusIn>", temp_text)
    entrada_busqueda.place(x = 40, y = 80)
    entrada_busqueda.insert(0,"Ejemplo: R1")

    #Configuro Radiobuttons de consulta
    consulta = tk.StringVar()
    consulta.set("Rodal")

    def sel(): #Handler, cambia el texto temporal, fuerza foco a la ventana para que vuelva a funcionar el texto temporal
        entrada_busqueda.delete(0,"end")
        if consulta.get() == "Propietario":
            texto2 = "Seleccione el Propietario"
            texto_temporal = "Seleccione el Propietario"
        if consulta.get() == "Bosque":
            texto2 = "Ingrese el rango de rodales"
            texto_temporal = "Ejemplo: R1, R9-R14, R4"
        if consulta.get() == "Rodal":
            texto2= "Ingrese el rodal"
            texto_temporal = "Ejemplo: R1"
        texto = texto2 + " que desea consultar"
        mensaje.config(text = texto)
        entrada_busqueda.insert(0,texto_temporal)
        root.focus_set()
    
    tk.Radiobutton(root, text = "Rodal", variable = consulta,
                   value = "Rodal", command=sel).place(x=40,y=105)
    tk.Radiobutton(root, text = "Hectáreas y tipo de bosque", variable = consulta,
                   value = "Bosque", command=sel).place(x=40,y=125)
    tk.Radiobutton(root, text = "Propietario", variable = consulta,
                   value = "Propietario", command=sel).place(x=40,y=145)
    
    mensaje = tk.Label(root, text = "Ingrese el rodal que desea")
    mensaje.place(x=40,y=60)

    root.mainloop()

if __name__ == "__main__":
    main()