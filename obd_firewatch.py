# Esta es la capa de , es decir, acá está main() y
# todo lo relacionado a tkinter, es lo que el USUARIO ve.

import logica as log # se imoorta la capa de negocio
import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import añadir_rodal_bingus as bingus

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

def validar_porcentajes(porcentaje_bosque_nativo, porcentaje_bosque_exotico):
    if porcentaje_bosque_nativo + porcentaje_bosque_exotico == 100:
        return True
    else:
        return False


def main():
    root = tk.Tk() # crea ventana principal
    root.columnconfigure([0, 1, 2, 3, 4, 5, 6], minsize = 50, weight = 1)
    root.rowconfigure([0, 1, 2, ], minsize = 100, weight = 1)
    root.title('OBD Firewatch - Consultar') # título de la aplicación
    img_consulta = tk.PhotoImage(file = "assets/iconos/consultare.png").subsample(2,2)
    img_ingresar= tk.PhotoImage(file = "assets/iconos/1.png").subsample(2,2)
    img_incendio= tk.PhotoImage(file = "assets/iconos/2.png").subsample(2,2)
    img_background = tk.PhotoImage(file = "assets/iconos/fondo_ventana1.png")
    label_bg = tk.Label(root, image=img_background).place(x=-0,y=0)
    img_nube = tk.PhotoImage(file = "assets/iconos/nube.png").subsample(25,25)

    def guardar_archivo():
            """Handler boton guardar archivo"""
            print("estoy guardando wiiiiiiiiiii")

    boton_guardar = ttk.Button(root, image=img_nube, command=guardar_archivo).grid(row=0,column=0)
    boton_ingreasr = ttk.Button(root, image=img_ingresar, command=lambda:ventana_ingresar()).grid(row=1,column=1)
    boton_incendio = ttk.Button(root, image=img_incendio, command=lambda:ventana_incendio()).grid(row=1,column=3)
    boton_consulta = ttk.Button(root, image=img_consulta, command=lambda:ventana_consulta()).grid(row=1,column=5)

    def ventana_error_ingreso(msg:str):
        ventana_erorr_ing = tk.Toplevel()
        ventana_erorr_ing.columnconfigure([0, 1, 2, 3, 4], minsize = 25, weight = 1)
        ventana_erorr_ing.rowconfigure([0, 1, 2, 3, 4], minsize = 25, weight = 1)
        tk.Label(ventana_erorr_ing, text = msg).grid(row=1,column=2,sticky="w")
        boton_cerrar= ttk.Button(ventana_erorr_ing, text = "OK", command = ventana_erorr_ing.destroy)
        boton_cerrar.grid(row=3,column=2)

    def ventana_ingreso_correcto():
        ventana_ing_correcto = tk.Toplevel()
        ventana_ing_correcto.columnconfigure([0, 1, 2], minsize = 250, weight = 1)
        ventana_ing_correcto.rowconfigure([0, 1, 2], minsize = 250, weight = 1)
        tk.Label(ventana_ingreso_correcto, text = "Su rodal ha sido ingresado correctamente !").grid(row=1,column=2,sticky="w")
        boton_cerrar= ttk.Button(ventana_ingreso_correcto, text = "OK", command = ventana_ingreso_correcto.destroy)
        boton_cerrar.grid(row=3,column=2)



    def ventana_ingresar():
        ventana_ingr = tk.Toplevel(root) # crea ventana ingresar rodales
        ventana_ingr.columnconfigure([0, 1, 2, 3, 4], minsize = 25, weight = 1)
        ventana_ingr.rowconfigure([0, 1, 2, 3, 4], minsize = 25, weight = 1)
        ventana_ingr.wm_attributes('-transparentcolor', '#ab23ff')
        label_bg = tk.Label(ventana_ingr, image=img_background)
        label_bg.place(x=-0,y=0)

        panel_izquierdo=tk.Frame(ventana_ingr, bg = "#675F2A",)
        panel_izquierdo.grid(row=1,column=1)
        panel_derecho=tk.Frame(ventana_ingr, bd=7, bg = "#675F2A", relief=tk.RAISED)
        #,highlightbackground="black", highlightthickness=1
        panel_derecho.columnconfigure([1, 2], minsize = 25, weight = 1)
        panel_derecho.grid(row=1,column=3)
        panel_abajo=tk.Frame(ventana_ingr,relief="raised")
        panel_abajo.grid(row=2,column=1,rowspan=2)
        
        boton_guardar = ttk.Button(ventana_ingr, image=img_nube, command=guardar_archivo).grid(row=0,column=0,sticky="N")
        
        def boton_entrada_rodal():
            """Handler validaciones archivo"""
            datos_rodal = {}
            print("primero valido, despues retorno o tiro error")
            try:
                datos_rodal[str(entrada_rodal.get())] = {"propietario":str(entrada_propietario.get()), 
                                                        "b_nativo":int(entrada_nativo.get()),
                                                        "b_exotico": int(entrada_exotico.get()),
                                                        "colindancias" : {'N' : entrada_norte.get(),
                                                        'NW' : entrada_noroeste.get(),
                                                        'NE' : entrada_noreste.get(),
                                                        'S' : entrada_sur.get(),
                                                        'SE' : entrada_sureste.get(),
                                                        'SW' : entrada_suroeste.get()}}
                
                #Aqui se lo doy a logica para validar lo mas probable

                msgbox.showinfo("Rodal","Rodal añadido correctamente")
                
            except ValueError:
                ventana_error_ingreso("Error alguno de los valores esta vacio o es incorrecto")

            #ventana_ingreso_correcto()                

        #Entrada Rodal
        tk.Label(panel_izquierdo, text = "ID del Rodal", fg ="#EFD1D1", bg = "#675F2A").grid(row=1,column=1,sticky="w")
        tk.Label(panel_izquierdo, text = "(Ejemplo: R1)",fg="#EFD1D1", bg = "#675F2A").grid(row=1,column=2,sticky="w")
        entrada_rodal = tk.Entry(panel_izquierdo, width = 40, borderwidth = 2, bg = "#FFEA9E")
        entrada_rodal.grid(row=2,column=1,columnspan=3)

        #Entrada Bosque Nativo
        tk.Label(panel_izquierdo, text = "% Bosque Nativo",fg = "#EFD1D1", bg = "#675F2A").grid(row=4,column=1,sticky="w", pady = 10)
        tk.Label(panel_izquierdo, text = "(Ejemplo: 80)",fg="#EFD1D1").grid(row=4,column=2,sticky="w")
        entrada_nativo = tk.Entry(panel_izquierdo, width = 40, borderwidth = 2, bg = "#FFEA9E")
        entrada_nativo.grid(row=5,column=1,columnspan=3)

        #Entrada Bosque Exótico
        tk.Label(panel_izquierdo, text = "% Bosque Exótico", fg ="#EFD1D1", bg = "#675F2A").grid(row=7,column=1,sticky="w", pady = 10)
        tk.Label(panel_izquierdo, text = "(Ejemplo: 20)",fg="#EFD1D1").grid(row=7,column=2,sticky="w")
        entrada_exotico = tk.Entry(panel_izquierdo, width = 40, borderwidth = 2, bg = "#FFEA9E")
        entrada_exotico.grid(row=8,column=1,columnspan=3)

        #Entrada Propietario
        tk.Label(panel_izquierdo, text = "Nombre del Propietario", fg = "#EFD1D1", bg = "#675F2A").grid(row=10,column=1,sticky="w", pady = 10)
        tk.Label(panel_izquierdo, text = "(Ejemplo: Inv. Rojas)",fg="#EFD1D1").grid(row=10,column=2,sticky="w")
        entrada_propietario = tk.Entry(panel_izquierdo, width = 40, borderwidth = 2, bg = "#FFEA9E")
        entrada_propietario.grid(row=11,column=1,columnspan=3)

        #Setuo Colindancias Combobox
        tk.Label(panel_derecho, text = "Colindancias").grid(row=0,column=1,sticky="e")

        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground= "#FFEA9E", background= "#EBD792")

        tk.Label(panel_derecho, text = "Norte").grid(row=1,column=1,sticky="w",padx=10)
        entrada_norte = ttk.Combobox(panel_derecho, state = "readonly", values = ["","R1"])
        entrada_norte.grid(row=2,column=1,columnspan=3,padx=10)

        tk.Label(panel_derecho, text = "Noreste").grid(row=3,column=1,sticky="w",padx=10, pady = 10)
        entrada_noreste = ttk.Combobox(panel_derecho, state = "readonly",values = ["","R3"])
        entrada_noreste.grid(row=4,column=1,columnspan=3)

        tk.Label(panel_derecho, text = "Noroeste").grid(row=5,column=1,sticky="w",padx=10, pady = 10)
        entrada_noroeste = ttk.Combobox(panel_derecho,state = "readonly", values = ["","R1","R2","R3"])
        entrada_noroeste.grid(row=6,column=1,columnspan=3)

        tk.Label(panel_derecho, text = "Sur").grid(row=7,column=1,sticky="w",padx=10, pady = 10)
        entrada_sur = ttk.Combobox(panel_derecho,state = "readonly", values = ["","R1","R2","R3"])
        entrada_sur.grid(row=8,column=1,columnspan=3)

        tk.Label(panel_derecho, text = "Sureste").grid(row=9,column=1,sticky="w",padx=10, pady = 10)
        entrada_sureste = ttk.Combobox(panel_derecho,state = "readonly", values = ["","R1","R2","R3"])
        entrada_sureste.grid(row=10,column=1,columnspan=3)

        tk.Label(panel_derecho, text = "Suroeste").grid(row=11,column=1,sticky="w",padx=10, pady = 10)
        entrada_suroeste = ttk.Combobox(panel_derecho,state = "readonly", values = ["","R1","R2","R3"])
        entrada_suroeste.grid(row=12,column=1,columnspan=3)

        #Boton Añadir Rodal
        boton_rodal = ttk.Button(panel_abajo, text = "Añadir Rodal", command=boton_entrada_rodal).grid(row=1,column=1)

    def ventana_incendio():
        ventana_inc = tk.Toplevel() # crea ventana simulación incendio

    def ventana_consulta():
        ventana_cons = tk.Toplevel() # crea ventana consulta
        ventana_cons.columnconfigure([0, 1, 2, 3, 4], minsize = 25, weight = 1)
        ventana_cons.rowconfigure([0, 1, 2, 3, 4], minsize = 25, weight = 1)
        ventana_cons.title('OBD Firewatch - Consultar') # título de la ventana
        img_background = tk.PhotoImage(file = "assets/iconos/fondo_ventana1.png")
        label_bg = tk.Label(ventana_cons, image=img_background).place(x=-0,y=0)

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