# Esta es la capa de , es decir, acá está main() y
# todo lo relacionado a tkinter, es lo que el USUARIO ve.

import logica as log # se imoorta la capa de negocio
import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import filedialog
import tkinter.ttk as ttk
import añadir_rodal_bingus as bingus


def main():
    root = tk.Tk() # crea ventana principal
    root.title('OBD Firewatch') # título de la aplicación
    root.columnconfigure([0, 1, 2, 3, 4, 5, 6], minsize = 50, weight = 1)
    root.rowconfigure([0, 1, 2, ], minsize = 100, weight = 1)

    #logo = tk.PhotoImage(file = "assets/iconos/logo.png")
    #root.iconphoto(True, logo)

    img_consulta = tk.PhotoImage(file = "assets/iconos/consultare.png").subsample(2,2)
    img_ingresar= tk.PhotoImage(file = "assets/iconos/1.png").subsample(2,2)
    img_incendio= tk.PhotoImage(file = "assets/iconos/2.png").subsample(2,2)
    img_background = tk.PhotoImage(file = "assets/iconos/fondo_ventana1.png")
    label_bg = tk.Label(root, image=img_background).place(x=-0,y=0)
    img_nube = tk.PhotoImage(file = "assets/iconos/nube.png").subsample(25,25)

    ventana_abierta = False

    def cerrando_ventana():
        nonlocal ventana_abierta
        if msgbox.askokcancel("Quit", "¿Desea salir y guardar ?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", cerrando_ventana)
    
    def abrir_ingreso():
        nonlocal ventana_abierta
        if ventana_abierta == False:
            ventana_ingresar()
            ventana_abierta = True
        else:
            msgbox.showinfo("Error","Ya posee una ventana abierta")

    def abrir_incendio():
        nonlocal ventana_abierta
        if ventana_abierta == False:
            ventana_incendio()
            ventana_abierta = True
        else:
            msgbox.showinfo("Error","Ya posee una ventana abierta")

    def abrir_consulta():
        nonlocal ventana_abierta
        if ventana_abierta == False:
            ventana_consulta()
            ventana_abierta = True
        else:
            msgbox.showinfo("Error","Ya posee una ventana abierta")

    def dialogo_abrir_archivo():
        direccion_archivo = filedialog.askopenfilename(title="Abrir Archivo", 
                                                       filetypes=[("Archivos CSV", "*.csv")])
        if direccion_archivo:
            archivo_seleccionado.config(text=f"Archivo Seleccionado: {direccion_archivo}")
            #process_file(file_path)

    boton_abrir = tk.Button(root, text = "Abrir Archivo", fg = "#343434", bg = "#C4A11E",font = ("Clear Sans", 10, "bold"),
                             command=dialogo_abrir_archivo).grid(row=0,column=0,columnspan=2,padx = 10,sticky = "w")
    archivo_seleccionado = tk.Label(root, text = "Archivo seleccionado: ",fg ="#EFD1D1", 
                                    bg = "#675F2A", font=("Clear Sans", 10, "bold"))
    archivo_seleccionado.grid(row=0, column= 2, columnspan=6,sticky="w")

    boton_ingreasr = ttk.Button(root, image=img_ingresar, command=lambda:abrir_ingreso()).grid(row=1,column=1)

    boton_incendio = ttk.Button(root, image=img_incendio, command=lambda:abrir_incendio()).grid(row=1,column=3)

    boton_consulta = ttk.Button(root, image=img_consulta, command=lambda:abrir_consulta()).grid(row=1,column=5)


    def ventana_error_ingreso(msg:str):
        ventana_erorr_ing = tk.Toplevel()
        ventana_erorr_ing.columnconfigure([0, 1, 2, 3, 4], minsize = 25, weight = 1)
        ventana_erorr_ing.rowconfigure([0, 1, 2, 3, 4], minsize = 25, weight = 1)
        tk.Label(ventana_erorr_ing, text = msg).grid(row=1,column=2,sticky="w")
        boton_cerrar= ttk.Button(ventana_erorr_ing, text = "OK", command = ventana_erorr_ing.destroy)
        boton_cerrar.grid(row=3,column=2)

    def ventana_ingresar():
        ventana_ingr = tk.Toplevel(root) # crea ventana ingresar rodales
        ventana_ingr.title('OBD Firewatch - Ingresar') # título de la aplicación
        ventana_ingr.columnconfigure([0, 4, 5, 6, 7], minsize = 25, weight = 1)
        ventana_ingr.rowconfigure([0, 15], minsize = 25, weight = 1)
        label_bg = tk.Label(ventana_ingr, image=img_background)
        label_bg.place(x=-0,y=0)

        F_entrada = ("Clear Sans", 14, "bold") #tuplas de fuente para usar mas abajo
        F_entry = ("Clear Sans", 12, "bold")
        F_ejemplo = ("Clear Sans", 9, "bold")
        F_col = ("Clear Sans", 10, "bold")

        panel_derecho=tk.Frame(ventana_ingr, bd=7, bg = "#675F2A", relief=tk.RAISED) #panel derecho para colindancias
        panel_derecho.columnconfigure([1, 2], minsize = 25, weight = 1)
        panel_derecho.rowconfigure([3,6,9,12,15,18], minsize = 10, weight = 1)
        panel_derecho.grid(row=1,column=6,rowspan=14)
        
        def cerrando_ventana():
            nonlocal ventana_abierta
            if msgbox.askokcancel("Quit", "¿Desea cerrar esta ventana?"):
                ventana_abierta = False
                ventana_ingr.destroy()

        ventana_ingr.protocol("WM_DELETE_WINDOW", cerrando_ventana)

        contador_id = 0
        contador_nat = 0
        contador_exo = 0
        contador_prop = 0

        def temp_rodal(e):
            """Handler que borra texto en la entrada al primer focusin"""
            nonlocal contador_id
            if contador_id == 0:
                entrada_rodal.delete(0,"end")
                contador_id +=1
            else:
                pass

        def temp_exotico(e):
            """Handler que borra texto en la entrada al primer focusin"""
            nonlocal contador_exo
            if contador_exo == 0:
                entrada_exotico.delete(0,"end")
                contador_exo +=1
            else:
                pass

        def temp_nativo(e):
            """Handler que borra texto en la entrada al primer focusin"""
            nonlocal contador_nat
            if contador_nat == 0:
                entrada_nativo.delete(0,"end")
                contador_nat +=1
            else:
                pass

        def temp_propietario(e):
            """Handler que borra texto en la entrada al primer focusin"""
            nonlocal contador_prop
            if contador_prop == 0:
                entrada_propietario.delete(0,"end")
                contador_prop +=1
            else:
                pass

        def boton_entrada_rodal():
            """Handler validaciones archivo"""
            class IngresoNoValido (Exception):
                pass

            nonlocal contador_id
            nonlocal contador_nat
            nonlocal contador_exo
            nonlocal contador_prop

            datos_rodal = {}

            print("primero valido, despues retorno o tiro error")
            try: #Si casillas bosques nativo o exotico no tiene solo numeros, levanta excepción ValueError
                datos_rodal[str(entrada_rodal.get())] = {"b_nativo":int(entrada_nativo.get()),
                                                        "b_exotico": int(entrada_exotico.get()),
                                                        "propietario":str(entrada_propietario.get()), 
                                                        "colindancias" : {'N' : entrada_norte.get(),
                                                        'NW' : entrada_noroeste.get(),
                                                        'NE' : entrada_noreste.get(),
                                                        'S' : entrada_sur.get(),
                                                        'SE' : entrada_sureste.get(),
                                                        'SW' : entrada_suroeste.get()}}
                
                #bool, msj = log.validar_rodal(datos_rodal)
                #INGRESE AQUI PASE DICC A LOG PARA VALIDAR

                #AQUI IRIA PASE A LEVANTAR OTRA EXCEPCION SI NO VALIDADO
                if (bool == False):
                    raise IngresoNoValido (msj)

                contador_id = 0 #Vuelta contadores texto temporal a 0
                contador_nat = 0
                contador_exo = 0
                contador_prop = 0

                entrada_rodal.delete(0,"end") #Borro lo que habia en las entradas
                entrada_nativo.delete(0,"end")
                entrada_exotico.delete(0,"end")
                entrada_propietario.delete(0,"end")

                ventana_ingr.focus_force() #cambio devuelta a la ventana de ingreso (para los widget)

                entrada_rodal.insert(0,"Ejemplo: R1") #Vuelvo a ingresar los textos temporales a las casillas
                entrada_nativo.insert(0,"Ejemplo: 80")
                entrada_exotico.insert(0, "Ejemplo: 20")
                entrada_propietario.insert(0, "Ejemplo: Inv. Rojas")

                #ventana_ingreso_correcto()
                msgbox.showinfo("Ingreso","Ingreso Correcto") #Aviso que todo se ingreso correctamente
            
            except IngresoNoValido as msj:
                ventana_error_ingreso(msj)

            except ValueError:
                ventana_error_ingreso("ERROR, Ingrese solo números en casillas bosque nativo y exótico")

            #ventana_ingreso_correcto()                

        #Entrada Rodal
        tk.Label(ventana_ingr, text = "ID del Rodal", fg ="#EFD1D1", 
                 bg = "#675F2A",font = F_entrada).grid(row=1,column=1,sticky="w")
        tk.Label(ventana_ingr, text = "(Ejemplo: R1)",fg="#EFD1D1", 
                 bg = "#675F2A", font = F_ejemplo).grid(row=1,column=2,sticky="w")
        entrada_rodal = tk.Entry(ventana_ingr, width = 40, borderwidth = 2, 
                                 bg = "#FFEA9E", font = F_entry)
        entrada_rodal.grid(row=2,column=1,columnspan=3, sticky = "nw")
        entrada_rodal.bind("<FocusIn>", temp_rodal)
        entrada_rodal.insert(0,"Ejemplo: R1")

        #Entrada Bosque Nativo
        tk.Label(ventana_ingr, text = "% Bosque Nativo",fg = "#EFD1D1", 
                 bg = "#675F2A", font = F_entrada).grid(row=4,column=1,sticky="w")
        tk.Label(ventana_ingr, text = "(Ejemplo: 80)",fg="#EFD1D1",
                 bg = "#675F2A", font = F_ejemplo).grid(row=4,column=2,sticky="w")
        entrada_nativo = tk.Entry(ventana_ingr, width = 40, borderwidth = 2, 
                                  bg = "#FFEA9E", font = F_entry)
        entrada_nativo.grid(row=5,column=1,columnspan=3, sticky = "nw")
        entrada_nativo.bind("<FocusIn>", temp_nativo)
        entrada_nativo.insert(0,"Ejemplo: 80")

        #Entrada Bosque Exótico
        tk.Label(ventana_ingr, text = "% Bosque Exótico", fg ="#EFD1D1", 
                 bg = "#675F2A", font = F_entrada).grid(row=7,column=1,sticky="w")
        tk.Label(ventana_ingr, text = "(Ejemplo: 20)",fg="#EFD1D1",
                 bg = "#675F2A", font = F_ejemplo).grid(row=7,column=2,sticky="w")
        entrada_exotico = tk.Entry(ventana_ingr, width = 40, borderwidth = 2, 
                                   bg = "#FFEA9E", font = F_entry)
        entrada_exotico.grid(row=8,column=1,columnspan=3, sticky = "nw")
        entrada_exotico.bind("<FocusIn>", temp_exotico)
        entrada_exotico.insert(0, "Ejemplo: 20")

        #Entrada Propietario
        tk.Label(ventana_ingr, text = "Nombre del Propietario", fg = "#EFD1D1", 
                 bg = "#675F2A", font = F_entrada).grid(row=10,column=1,sticky="w")
        tk.Label(ventana_ingr, text = "(Ejemplo: Inv. Rojas)", fg = "#EFD1D1", 
                 bg = "#675F2A", font = F_ejemplo).grid(row=10,column=2,sticky="w")
        entrada_propietario = tk.Entry(ventana_ingr, width = 40, borderwidth = 2, 
                                       bg = "#FFEA9E", font = F_entry)
        entrada_propietario.grid(row=11, column=1, columnspan=3, sticky = "nw")
        entrada_propietario.bind("<FocusIn>", temp_propietario)
        entrada_propietario.insert(0, "Ejemplo: Inv. Rojas")

        #Setup Colindancias Combobox
        tk.Label(panel_derecho, text = "Colindancias", fg = "#EFD1D1", 
                 bg = "#675F2A", font = F_entry).grid(row=0,column=1,sticky="e")
        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground= "#FFEA9E", background= "#EBD792")

        #Colindancia al norte
        tk.Label(panel_derecho, text = "Norte", fg = "#EFD1D1", 
                 bg = "#675F2A", font = F_col).grid(row=1,column=1,sticky="w",padx=10)
        entrada_norte = ttk.Combobox(panel_derecho, state = "readonly",
                                      values = log.retorna_lista_rodales())
        entrada_norte.grid(row=2,column=1,columnspan=3,padx=10)

        #Colindancia al NE
        tk.Label(panel_derecho, text = "Noreste", fg = "#EFD1D1", 
                 bg = "#675F2A", font = F_col).grid(row=4,column=1,sticky="w",padx=10)
        entrada_noreste = ttk.Combobox(panel_derecho, state = "readonly",
                                       values = log.retorna_lista_rodales())
        entrada_noreste.grid(row=5,column=1,columnspan=3)

        #Colindancia al NW
        tk.Label(panel_derecho, text = "Noroeste", fg = "#EFD1D1",
                  bg = "#675F2A", font = F_col).grid(row=7,column=1,sticky="w",padx=10)
        entrada_noroeste = ttk.Combobox(panel_derecho,state = "readonly", 
                                        values = log.retorna_lista_rodales())
        entrada_noroeste.grid(row=8,column=1,columnspan=3)

        #Colindancia al S
        tk.Label(panel_derecho, text = "Sur",  fg = "#EFD1D1", 
                 bg = "#675F2A", font = F_col).grid(row=10,column=1,sticky="w",padx=10)
        entrada_sur = ttk.Combobox(panel_derecho,state = "readonly", 
                                   values = log.retorna_lista_rodales())
        entrada_sur.grid(row=11,column=1,columnspan=3)

        #Colindancia al SE
        tk.Label(panel_derecho, text = "Sureste", fg = "#EFD1D1", 
                 bg = "#675F2A", font = F_col).grid(row=13,column=1,sticky="w",padx=10)
        entrada_sureste = ttk.Combobox(panel_derecho,state = "readonly",
                                        values = log.retorna_lista_rodales())
        entrada_sureste.grid(row=14,column=1,columnspan=3)

        #Colindancia al SW
        tk.Label(panel_derecho, text = "Suroeste", fg = "#EFD1D1", 
                 bg = "#675F2A", font = F_col).grid(row=16,column=1,sticky="w",padx=10)
        entrada_suroeste = ttk.Combobox(panel_derecho,state = "readonly",
                                        values = log.retorna_lista_rodales())
        entrada_suroeste.grid(row=17,column=1,columnspan=3)

        #Boton Añadir Rodal
        boton_rodal = tk.Button(ventana_ingr, text = "Añadir Rodal", fg = "#343434", 
                                bg = "#C4A11E", font = F_entrada, command=boton_entrada_rodal)
        boton_rodal.grid(row=12,column=2,pady=20)

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