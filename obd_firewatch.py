# Esta es la capa de , es decir, acá está main() y
# todo lo relacionado a tkinter, es lo que el USUARIO ve.

import logica as log # se imoorta la capa de negocio
import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk

def main():
    root = tk.Tk() # crea ventana principal
    root.columnconfigure([0, 1, 2, 3, 4, 5, 6], minsize = 50, weight = 1)
    root.rowconfigure([0, 1, 2, ], minsize = 100, weight = 1)
    root.title('OBD Firewatch - Consultar') # título de la aplicación
    img_consulta = tk.PhotoImage(file = "assets/iconos/consultare.png").subsample(2,2)
    img_ingresar= tk.PhotoImage(file = "assets/iconos/1.png").subsample(2,2)
    img_incendio= tk.PhotoImage(file = "assets/iconos/2.png").subsample(2,2)
    img_background = tk.PhotoImage(file = "assets/iconos/fondo_verde.png")
    label_bg = tk.Label(root, image=img_background).place(x=-0,y=0)
    img_nube = tk.PhotoImage(file = "assets/iconos/nube.png").subsample(25,25)

    boton_guardar = ttk.Button(root, image=img_nube).grid(row=0,column=0)
    boton_ingreasr = ttk.Button(root, image=img_ingresar, command=lambda:ventana_ingresar()).grid(row=1,column=1)
    boton_incendio = ttk.Button(root, image=img_incendio, command=lambda:ventana_incendio()).grid(row=1,column=3)
    boton_consulta = ttk.Button(root, image=img_consulta, command=lambda:ventana_consulta()).grid(row=1,column=5)

    def ventana_ingresar():
        ventana_ingr = tk.Toplevel(root) # crea ventana ingresar rodales
        #ventana_ingr.columnconfigure([0, 1, 2, 3, 4], minsize = 25, weight = 1)
        #ventana_ingr.rowconfigure([0, 1, 2, 3, 4], minsize = 25, weight = 1) 
        boton_guardar = ttk.Button(ventana_ingr, image=img_nube).grid(row=0,column=0)
        #Entrada Rodal
        tk.Label(ventana_ingr, text = "ID del Rodal").grid(row=1,column=1,sticky="w")
        tk.Label(ventana_ingr, text = "(Ejemplo: R1)",fg="grey").grid(row=1,column=2,sticky="w")
        entrada_rodal = tk.Entry(ventana_ingr, width = 40, borderwidth = 2).grid(row=2,column=1,columnspan=3)
        #Entrada Bosque Nativo
        tk.Label(ventana_ingr, text = "% Bosque Nativo").grid(row=4,column=1,sticky="w")
        tk.Label(ventana_ingr, text = "(Ejemplo: 80)",fg="grey").grid(row=4,column=2,sticky="w")
        entrada_rodal = tk.Entry(ventana_ingr, width = 40, borderwidth = 2).grid(row=5,column=1,columnspan=3)
        #Entrada Bosque Exótico
        tk.Label(ventana_ingr, text = "% Bosque Exótico").grid(row=7,column=1,sticky="w")
        tk.Label(ventana_ingr, text = "(Ejemplo: 20)",fg="grey").grid(row=7,column=2,sticky="w")
        entrada_rodal = tk.Entry(ventana_ingr, width = 40, borderwidth = 2).grid(row=8,column=1,columnspan=3)
        #Entrada Propietario
        tk.Label(ventana_ingr, text = "Nombre del Propietario").grid(row=10,column=1,sticky="w")
        tk.Label(ventana_ingr, text = "(Ejemplo: Inv. Rojas)",fg="grey").grid(row=10,column=2,sticky="w")
        entrada_rodal = tk.Entry(ventana_ingr, width = 40, borderwidth = 2).grid(row=11,column=1,columnspan=3)
        #Boton Añadir Rodal
        boton_rodal = ttk.Button(ventana_ingr, text = "Añadir Rodal").grid(row=12,column=2,sticky="w")
        
        palen_lado=tk.Frame(ventana_ingr,relief="raised",background="#99fb99").grid(row=1,column=5,rowspan=12,columnspan=3)

        r1=tk.Label(palen_lado, text = "ID del Rodal")
        r1.grid(row=1,column=1,sticky="w")
        r2=tk.Label(palen_lado, text = "(Ejemplo: R1)",fg="grey")
        r2.grid(row=1,column=2,sticky="w")
        entrada_rodal = tk.Entry(palen_lado, width = 40, borderwidth = 2).grid(row=2,column=1,columnspan=3)

    def ventana_incendio():
        ventana_inc = tk.Toplevel() # crea ventana simulación incendio

    def ventana_consulta():
        ventana_cons = tk.Toplevel() # crea ventana consulta
        ventana_cons.columnconfigure([0, 1, 2, 3, 4], minsize = 25, weight = 1)
        ventana_cons.rowconfigure([0, 1, 2, 3, 4], minsize = 25, weight = 1)
        ventana_cons.title('OBD Firewatch - Consultar') # título de la ventana
        img_background = tk.PhotoImage(file = "assets/iconos/fondo_verde.png")
        #label_bg = tk.Label(ventana_cons, image=img_background).place(x=-0,y=0)

        boton_guardar = ttk.Button(ventana_cons, image=img_nube).grid(row=0,column=0)

        #Configuro entry con texto temporal
        def temp_text(e):
            entrada_busqueda.delete(0,"end")

        entrada_busqueda = tk.Entry(ventana_cons, width = 30, borderwidth = 2)
        #Considerar mover el .bind a otro lado, actualmente borra texto si cambio el foco a otro lado, quizas otro evento, no focusin
        entrada_busqueda.bind("<FocusIn>", temp_text)
        entrada_busqueda.grid(row=1,column=1,sticky="w")
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
            ventana_cons.focus_set()

        tk.Radiobutton(ventana_cons, text = "Rodal", variable = consulta,
                       value = "Rodal", command=sel).grid(row=2,column=1,sticky="w")
        tk.Radiobutton(ventana_cons, text = "Hectáreas y tipo de bosque", variable = consulta,
                       value = "Bosque", command=sel).grid(row=3,column=1,sticky="w")
        tk.Radiobutton(ventana_cons, text = "Propietario", variable = consulta,
                       value = "Propietario", command=sel).grid(row=4,column=1,sticky="w")

        mensaje = tk.Label(ventana_cons, text = "Ingrese el rodal que desea")
        mensaje.grid(row=0,column=1,sticky="w",columnspan=3)

    root.mainloop()

if __name__ == "__main__":
    main()