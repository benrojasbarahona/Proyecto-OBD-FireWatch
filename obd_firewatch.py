# Esta es la capa de , es decir, acá está main() y
# todo lo relacionado a tkinter, es lo que el USUARIO ve.

import logica as log # se importa la capa de negocio
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import filedialog
import re

consulta_abierta = False
#limpiar_datos boton limpiar en main
def main():
    root = tk.Tk() # crea ventana principal
    root.title('OBD Firewatch') # título de la aplicación
    root.columnconfigure([0, 1, 2, 3, 4, 5, 6], minsize = 50, weight = 1)
    root.rowconfigure([0, 1, 2, ], minsize = 100, weight = 1)
    root.resizable(False, False)

   # log.inicializar_diccionario()

    #logo = tk.PhotoImage(file = "assets/iconos/logo.png")
    #root.iconphoto(True, logo)

    img_consulta = tk.PhotoImage(file = "assets/iconos/consultare.png").subsample(2,2)
    img_ingresar= tk.PhotoImage(file = "assets/iconos/1.png").subsample(2,2)
    img_incendio= tk.PhotoImage(file = "assets/iconos/2.png").subsample(2,2)
    img_background = tk.PhotoImage(file = "assets/iconos/fondo_ventana1.png")
    label_bg = tk.Label(root, image=img_background).place(x=-0,y=0)
    img_nube = tk.PhotoImage(file = "assets/iconos/nube.png").subsample(25,25)

    ventana_abierta = False

    def cerrando_ventana(): #---------------------------------------------------------------------------------------------------
        nonlocal ventana_abierta
        if msgbox.askokcancel("Quit", "¿Desea guardar y salir?"):
            #log.guardar_diccionario()
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", cerrando_ventana)
    
    def handler_limpiar_datos():
        if msgbox.askyesno("Limpiar datos", "¿Desea limpiar los datos de prueba?"):
            log.limpiar_datos_log()
            msgbox.showinfo('Datos limpiados','Los datos de prueba fueron limpiados')

    boton_limpiar = tk.Button(root, text = "Limpiar Datos", fg = "#343434", bg = "#C4A11E",font = ("Clear Sans", 10, "bold"),
                              command=handler_limpiar_datos).grid(row=0,column=5,columnspan=2,padx = 10,sticky = "e")
    
    def abrir_ingreso():
        nonlocal ventana_abierta
        if ventana_abierta == False:
            #arr.generar_archivos()
            ventana_ingresar()
            ventana_abierta = True
        else:
            msgbox.showerror("Error","Ya posee una ventana abierta")

    def abrir_incendio():
        nonlocal ventana_abierta
        if ventana_abierta == False:
            ventana_incendio()
            
            ventana_abierta = True
        else:
            msgbox.showerror("Error","Ya posee una ventana abierta")

    def abrir_consulta():
        nonlocal ventana_abierta
        if ventana_abierta == False:
            ventana_consulta()
            ventana_abierta = True
        else:
            msgbox.showerror("Error","Ya posee una ventana abierta")

    def dialogo_abrir_archivo():
        direccion_archivo = filedialog.askdirectory(title="Abrir Carpeta")
        if direccion_archivo:
            carpeta_seleccionada.config(text=f"Carpeta Seleccionada: {direccion_archivo}")
            #arr.generar_archivos(direccion_archivo)

    boton_abrir = tk.Button(root, text = "Abrir Carpeta", fg = "#343434", bg = "#C4A11E",font = ("Clear Sans", 10, "bold"),
                             command=dialogo_abrir_archivo).grid(row=0,column=0,columnspan=2,padx = 10,sticky = "w")
    
    carpeta_seleccionada = tk.Label(root, text = "Carpeta Seleccionada: ",fg ="#EFD1D1", 
                                    bg = "#675F2A", font=("Clear Sans", 10, "bold"))
    
    carpeta_seleccionada.grid(row=0, column= 2, columnspan=6,sticky="w")

    boton_ingreasr = ttk.Button(root, image=img_ingresar, command=lambda:abrir_ingreso()).grid(row=1,column=1)

    boton_incendio = ttk.Button(root, image=img_incendio, command=lambda:abrir_incendio()).grid(row=1,column=3)

    boton_consulta = ttk.Button(root, image=img_consulta, command=lambda:abrir_consulta()).grid(row=1,column=5)

    def ventana_ingresar(): #-------------------------------- Ventana Ingresar --------------------------------------------------
        ventana_ingr = tk.Toplevel(root) # crea ventana ingresar rodales
        ventana_ingr.title('OBD Firewatch - Ingresar') # título de la aplicación
        ventana_ingr.columnconfigure([0, 4, 5, 6, 7], minsize = 25, weight = 1)
        ventana_ingr.rowconfigure([0, 15], minsize = 25, weight = 1)
        ventana_ingr.resizable(False, False)
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
            ventana_abierta = False
            log.guardar_diccionario() # TENTATIVO A CAMBIO --------------------------------------------------------
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
                #INGRESE AQUI PASE DICC A LOG PARA VALIDAR
                valido, msj = log.validar_ingreso(datos_rodal)
                #AQUI IRIA PASE A LEVANTAR OTRA EXCEPCION SI NO VALIDADO
                if (valido == False):
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

                entrada_norte.config(values = log.retorna_lista_rodales())
                entrada_noreste.config(values = log.retorna_lista_rodales())
                entrada_noroeste.config(values = log.retorna_lista_rodales())
                entrada_sur.config(values = log.retorna_lista_rodales())
                entrada_sureste.config(values = log.retorna_lista_rodales())
                entrada_suroeste.config(values = log.retorna_lista_rodales())

                msgbox.showinfo("CORRECTO","Rodal ingresado correctamente", parent = ventana_ingr) #Aviso que todo se ingreso correctamente
            
            except IngresoNoValido as msj:
                msgbox.showerror("ERROR", msj, parent = ventana_ingr)

            except ValueError:
                msgbox.showerror("ERROR","Ingrese solo números en casillas bosque nativo y exótico", parent = ventana_ingr)

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

    def reporte_incendio(rodal_inicial: str, viento: str):
        ventana_reporte = tk.Toplevel()
        ventana_reporte.title('Proyección de incendio')
        ventana_reporte.columnconfigure([0,2,4], minsize=15, weight=1)
        ventana_reporte.rowconfigure([0,2,4], minsize=15, weight=1)
        ventana_reporte.resizable(False, False)

        img_fondo = tk.PhotoImage(file="assets\iconos\simular_incendio.png")

        background_label = tk.Label(ventana_reporte, image=img_fondo)
        background_label.image = img_fondo  # Establece la imagen
        background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Coloca la imagen en toda la ventana

        def cerrando_ventana():
            """Handler cerrar ventana"""
            global reporte_abierto
            reporte_abierto = False
            ventana_reporte.destroy()
        
        ventana_reporte.protocol("WM_DELETE_WINDOW", cerrando_ventana)

        #Setup frames para ventana reporte incendio
        frame_rodal = tk.Frame(ventana_reporte, bd=7, bg = "#AB431D", relief=tk.RAISED)
        frame_rodal.rowconfigure([0,7], minsize=5, weight=1)
        frame_rodal.columnconfigure([0,2,4], minsize=5, weight=1)
        frame_rodal.grid(row=1, column=1)

        frame_riesgo_incendio = tk.Frame(ventana_reporte, bd=7, bg = "#AB431D", relief=tk.RAISED)
        frame_riesgo_incendio.rowconfigure([0,7], minsize=5, weight=1) #hasta largo lista propietarios
        frame_riesgo_incendio.columnconfigure([0,5], minsize=5, weight=1)
        frame_riesgo_incendio.grid(row=2, column=1)

        frame_comprometidos = tk.Frame(ventana_reporte, bd=7, bg = "#AB431D", relief=tk.RAISED)
        frame_comprometidos.rowconfigure([0,7], minsize=5, weight=1)
        frame_comprometidos.columnconfigure([0,2], minsize=5, weight=1)
        frame_comprometidos.grid(row=1, column=3, rowspan=2)

        #Relleno frame_rodal con informacion
        
        datos_rodal_inicial = log.por_rodal(rodal_inicial)
        #[propietario, natividad, exotico]
        tk.Label(frame_rodal, text = "RODAL INICIO INCENDIO", bg="#AB431D", 
                 font=("Clear Sans", 14, "bold")).grid(row=1, column=1, columnspan=2, sticky="nw")
        
        textos_frame_rodal = ["ID:","% Nativo:", "% Exótico:", "Propietario:", "Dirección Viento:"]

        for i in range(len(textos_frame_rodal)):
            tk.Label(frame_rodal, text = textos_frame_rodal[i], bg="#AB431D", 
                     font=("Clear Sans", 12)).grid(row=2+i, column=1, sticky="nw")
        
        tk.Label(frame_rodal, text=rodal_inicial, bg="#AB431D",
                    font=("Clear Sans", 12)).grid(row=2, column=1, sticky="nw", padx= (140,0))
        
        tk.Label(frame_rodal, text=datos_rodal_inicial[1], bg="#AB431D",
                    font=("Clear Sans", 12)).grid(row=3, column=1, sticky="nw", padx= (140,0))
        
        tk.Label(frame_rodal, text=datos_rodal_inicial[2], bg="#AB431D",
                    font=("Clear Sans", 12)).grid(row=4, column=1, sticky="nw", padx= (140,0))
        
        tk.Label(frame_rodal, text=datos_rodal_inicial[0], bg="#AB431D",
                    font=("Clear Sans", 12)).grid(row=5, column=1, sticky="nw", padx= (140,0))
        
        tk.Label(frame_rodal, text=viento, bg="#AB431D",
                    font=("Clear Sans", 12)).grid(row=6, column=1, sticky="nw", padx= (140,0))
        
        #Relleno frame_riesgo_incendio con información
        rodales_afectados,_,_ = log.simular_incendio(viento, rodal_inicial)
        #[rodales_afectados, recursos_comprometidos[1], recursos_comprometidos[0]]

        tk.Label(frame_riesgo_incendio, text = "RODALES EN RIESGO DE INCENDIO", bg="#AB431D",
                 font=("Clear Sans", 14, "bold")).grid(row=1, column=1, columnspan=4, sticky="nw")

        textos_frame_riesgo = ["Rodal","% Nativo", "% Exótico", "Propietario"]

        for i in range(len(textos_frame_riesgo)):
            tk.Label(frame_riesgo_incendio, text = textos_frame_riesgo[i], bg="#AB431D", 
                     font=("Clear Sans", 12, "bold")).grid(row=2, column=1+i, sticky="nw")

        for i in range(len(rodales_afectados)):
            if rodales_afectados[i] != rodal_inicial:
                datos_rodal = log.por_rodal(rodales_afectados[i])
                #[propietario, natividad, exotico]
                tk.Label(frame_riesgo_incendio, text = rodales_afectados[i], bg="#AB431D", 
                         font=("Clear Sans", 12)).grid(row=3+i, column=1, sticky="nw")

                tk.Label(frame_riesgo_incendio, text = datos_rodal[1], bg="#AB431D", 
                         font=("Clear Sans", 12)).grid(row=3+i, column=2, sticky="nw")

                tk.Label(frame_riesgo_incendio, text = datos_rodal[2], bg="#AB431D", 
                         font=("Clear Sans", 12)).grid(row=3+i, column=3, sticky="nw")

                tk.Label(frame_riesgo_incendio, text = datos_rodal[0], bg="#AB431D", 
                         font=("Clear Sans", 12)).grid(row=3+i, column=4, sticky="nw")
        
        #Relleno frame_comprometidos

        tupla_suma, tupla_propietarios = log.suma_afectados(rodal_inicial, list(rodales_afectados))
        #(hectareas_totales_afectadas, bosque_nativo_afectado, bosque_exotico_afectado)

        tk.Label(frame_comprometidos, text = "ROCURSOS COMPROMETIDOS", bg="#AB431D",
                 font=("Clear Sans", 14, "bold")).grid(row=1, column=1, sticky="nw")
        
        textos_recursos = ["Superficie Total:","Superficie Nativos:", "Superficie exótico:"]
        
        for i in range(len(textos_recursos)):
            tk.Label(frame_comprometidos, text = textos_recursos[i], bg="#AB431D",
                     font=("Clear Sans", 12)).grid(row=2+i, column=1, sticky="nw")
            tk.Label(frame_comprometidos, text = tupla_suma[i], bg="#AB431D",
                     font=("Clear Sans", 12)).grid(row=2+i, column=1, sticky="nw", padx = (140,0))
        

        tk.Label(frame_comprometidos, text="PROPIETARIOS COMPROMETIDOS", bg="#AB431D",
                 font=("Clear Sans", 14, "bold")).grid(row=5, column=1, sticky="nw")
        
        for i in range(len(tupla_propietarios)):
            tk.Label(frame_comprometidos, text = tupla_propietarios[i], bg="#AB431D",
                     font=("Clear Sans", 12)).grid(row=6+i, column=1, sticky="nw")
        
    def ventana_incendio():
        ventana_inc = tk.Toplevel() # crea ventana simulación incendio
        ventana_inc.geometry("500x400")
        ventana_inc.title('OBD Firewatch - Incendio')  # título de la ventana
        ventana_inc.resizable(False, False)  # no se puede cambiar el tamaño de la ventana

        def cerrando_ventana():
            """Handler cerrar ventana"""
            nonlocal ventana_abierta
            ventana_abierta = False
            ventana_inc.destroy()
        
        ventana_inc.protocol("WM_DELETE_WINDOW", cerrando_ventana)

        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground= "#FFEA9E", background= "#EBD792")

        img_fondo = tk.PhotoImage(file="assets\iconos\simular_incendio.png")

        background_label = tk.Label(ventana_inc, image=img_fondo)
        background_label.image = img_fondo  # Establece la imagen
        background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Coloca la imagen en toda la ventana

        F_entrada = ("Clear Sans", 14, "bold")

        label_id_rodal = tk.Label(ventana_inc, text="ID del rodal", fg="white", bg= "#820400", font=F_entrada)
        label_id_rodal.place(x=20, y=20)

        rodal_options = log.retorna_lista_rodales()
        rodal_combobox = ttk.Combobox(ventana_inc, values=rodal_options, state="readonly", width=51, style="clam.TCombobox")
        rodal_combobox.place(x=22, y=50)  # Establece la posición del combobox

        label_dir_viento = tk.Label(ventana_inc, text="Dir. del viento (N, NE, NO, S, SE, SO)", fg="white", bg="#820400", font=F_entrada)
        label_dir_viento.place(x=20, y=100)

        opciones_viento = ["N", "NE", "E", "SE", "S", "SW", "W" ,"NW"]
        direccion_combobox = ttk.Combobox(ventana_inc, values=opciones_viento, state="readonly", width=51, style="clam.TCombobox")
        direccion_combobox.place(x=22, y=130)

        def simular_incendio():
            rodal_seleccionado = rodal_combobox.get()
            direccion_viento = direccion_combobox.get()
            if rodal_seleccionado and direccion_viento:  # Verifica que ambos combobox no estén en su estado predeterminado ("")
                consulta_abierta = True
                reporte_incendio(rodal_seleccionado, direccion_viento)

            else:
                msgbox.showerror("Error", "Por favor selecciona valores  válidos para ID del rodal y dirección del viento")

        boton_simular = tk.Button(ventana_inc, text="Simular Incendio", command=simular_incendio, bg='#820400', fg='white')
        boton_simular.place(x=190, y=350)

        img_sobre_boton = tk.PhotoImage(file="assets\iconos\direcciones_viento.png")  # Cambia "ruta_de_la_imagen.png" por la ruta de tu imagen
        label_imagen = tk.Label(ventana_inc, image=img_sobre_boton)
        label_imagen.image = img_sobre_boton  # Establece la imagen
        label_imagen.place(x=160, y=165)


    def ventana_resultados_rodal(datos_rodal: list, rodal: str):
                                #[propietario, natividad, exotico]
        
        ventana_res = tk.Toplevel()
        ventana_res.columnconfigure([0, 1, 2], minsize=15, weight=1)
        ventana_res.rowconfigure([0, 10], minsize=10, weight=1)
        ventana_res.resizable(False, False)

        label_bg = tk.Label(ventana_res, image=img_background)
        label_bg.place(x=0,y=0)

        def cerrando_consulta():
            """Handler cerrar consulta"""
            global consulta_abierta
            consulta_abierta = False
            ventana_res.destroy()
        
        colindancias = ["muchas","pocas"]

        ventana_res.protocol("WM_DELETE_WINDOW", cerrando_consulta)
        
        tk.Label (ventana_res, text = "Rodal Consultado:", fg = "#EFD1D1", bg = "#675F2A", 
                    font = ("Clear Sans", 13, "bold")).grid(row=1, column=1, sticky="w")
        tk.Label (ventana_res, text = rodal, fg = "#EFD1D1", bg = "#675F2A", 
                    font = ("Clear Sans", 13)).grid(row=1, column=1, sticky="w", padx= (150,0))
        
        tk.Label (ventana_res, text = "Propietario: ", fg = "#EFD1D1", bg = "#675F2A", 
                    font = ("Clear Sans", 13, "bold")).grid(row=2, column=1, sticky="w")
        tk.Label (ventana_res, text = datos_rodal[0], fg = "#EFD1D1", bg = "#675F2A", 
                    font = ("Clear Sans", 13)).grid(row=2, column=1, sticky="w", padx = (95,0))
        
        tk.Label (ventana_res, text = "Porcentaje Bosque Nativo: ", fg = "#EFD1D1", bg = "#675F2A", 
                    font = ("Clear Sans", 13, "bold")).grid(row=3, column=1, sticky="w")
        tk.Label (ventana_res, text = f"{datos_rodal[1]} %", fg = "#EFD1D1", bg = "#675F2A", 
                    font = ("Clear Sans", 13)).grid(row=3, column=1, sticky="w", padx=(215,0))
        
        tk.Label (ventana_res, text = "Porcentaje Bosque Exótico: ", fg = "#EFD1D1", bg = "#675F2A", 
                    font = ("Clear Sans", 13, "bold")).grid(row=4, column=1, sticky="w")
        tk.Label (ventana_res, text = f"{datos_rodal[2]} %", fg = "#EFD1D1", bg = "#675F2A", 
                    font = ("Clear Sans", 13)).grid(row=4, column=1, sticky="w", padx=(227,0))
        
        tk.Label (ventana_res, text = "Rodales colindantes: ", fg = "#EFD1D1", bg = "#675F2A", 
                    font = ("Clear Sans", 13, "bold")).grid(row=5, column=1, sticky="w")
        tk.Label (ventana_res, text = colindancias, fg = "#EFD1D1", bg = "#675F2A", 
                    font = ("Clear Sans", 13)).grid(row=6, column=1, sticky="w", pady=(0,10))
        

        canvas = tk.Canvas(ventana_res, width=270, height=270, bg = "#675F2A")
        canvas.grid(row=7, column=1, sticky="nw")
        st = 0
        coord = 15, 15, 250, 250
        pieValor = [datos_rodal[1], datos_rodal[2]]
        pieColor = ["Green", "#0B320E"]

        #Genera grafico de torta en base a porcentajes bosque nativo y exotico
        for val,col in zip(pieValor, pieColor):    
            canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
            st = st + val*3.6 

        tk.Label (ventana_res, text = "Bosque Nativo", fg = "#EFD1D1", bg = "#675F2A", 
                    font = ("Clear Sans", 13)).grid(row=8, column=1, sticky="nw",padx=(25,0))
        tk.Label (ventana_res,bg = "Green", width=2, height=1).grid(row=8, column=1, sticky="w")
        
        tk.Label (ventana_res, text = "Bosque Exotico", fg = "#EFD1D1", bg = "#675F2A", 
                    font = ("Clear Sans", 13)).grid(row=9, column=1, sticky="nw",padx=(25,0))
        tk.Label (ventana_res,bg = "#0B320E", width=2, height=1).grid(row=9, column=1, sticky="w")
        
    def ventana_resultados_propietario(datos_rodales_prop: list, prop_a_consultar: str):
                                      #[rodales_prop, natividad, exotico]
        ventana_res = tk.Toplevel()
        ventana_res.columnconfigure([0, 1, 2], minsize=15, weight=1)
        ventana_res.rowconfigure([0, 8], minsize=10, weight=1)
        ventana_res.resizable(False, False)

        label_bg = tk.Label(ventana_res, image=img_background)
        label_bg.place(x=0,y=0)

        def cerrando_consulta():
            """Handler cerrar consulta"""
            global consulta_abierta
            consulta_abierta = False
            ventana_res.destroy()
        
        F_bold = ("Clear Sans", 12, "bold")
        F_min = ("Clear Sans", 12)

        ventana_res.protocol("WM_DELETE_WINDOW", cerrando_consulta)

        tk.Label (ventana_res, text = prop_a_consultar, fg = "#EFD1D1", bg = "#675F2A", 
                      font = ("Clear Sans", 15, "bold underline")).grid(row=1, column=1, sticky="w", pady=15)
        
        tk.Label (ventana_res, text = "Cantidad de rodales:", fg = "#EFD1D1", bg = "#675F2A", 
                      font = F_bold).grid(row=2, column=1, sticky="nw")
        tk.Label (ventana_res, text = len(datos_rodales_prop[0]), fg = "#EFD1D1", bg = "#675F2A", 
                      font = F_min).grid(row=2, column=1, sticky="w",padx= (165,0))
        
        tk.Label (ventana_res, text = datos_rodales_prop[0], fg = "#EFD1D1", bg = "#675F2A", 
                      font = F_min).grid(row=3, column=1, sticky="w")
        
        tk.Label (ventana_res, text = "Hectareas bosque nativo:", fg = "#EFD1D1", bg = "#675F2A", 
                      font = F_bold).grid(row=4, column=1, sticky="nw")
        tk.Label (ventana_res, text = f"{datos_rodales_prop[1]} ha", fg = "#EFD1D1", bg = "#675F2A", 
                      font = F_min).grid(row=4, column=1, sticky="sw",padx= (210,0))
        
        tk.Label (ventana_res, text = "Hectareas bosque exótico:", fg = "#EFD1D1", bg = "#675F2A", 
                      font = F_bold).grid(row=5, column=1, sticky="nw")
        tk.Label (ventana_res, text = f"{datos_rodales_prop[2]} ha", fg = "#EFD1D1", bg = "#675F2A", 
                      font = F_min).grid(row=5, column=1, sticky="sw",padx= (220,0), pady=(0,15))

        #Setup Canvas para gráfico de torta
        canvas = tk.Canvas(ventana_res, width=270, height=270, bg = "#675F2A")
        canvas.grid(row=6, column=1, sticky="nw")
        st = 0
        coord = 15, 15, 250, 250
        porcentaje_hect_nat = datos_rodales_prop[1]/(datos_rodales_prop[1] + datos_rodales_prop[2])*100
        porcentaje_hect_exo = datos_rodales_prop[2]/(datos_rodales_prop[1] + datos_rodales_prop[2])*100
        pieValor = [porcentaje_hect_nat, porcentaje_hect_exo]
        pieColor = ["Green", "#0B320E"]

        #Genera grafico de torta en base a porcentajes bosque nativo y exotico
        for val,col in zip(pieValor, pieColor):    
            canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
            st = st + val*3.6 

        #Leyenda gráfico de torta
        tk.Label (ventana_res, text = "Bosque Nativo", fg = "#EFD1D1", bg = "#675F2A", 
                    font = ("Clear Sans", 13)).grid(row=8, column=1, sticky="nw",padx=(25,0))
        tk.Label (ventana_res,bg = "Green", width=2, height=1).grid(row=8, column=1, sticky="w")
        
        tk.Label (ventana_res, text = "Bosque Exotico", fg = "#EFD1D1", bg = "#675F2A", 
                    font = ("Clear Sans", 13)).grid(row=9, column=1, sticky="nw",padx=(25,0))
        tk.Label (ventana_res,bg = "#0B320E", width=2, height=1).grid(row=9, column=1, sticky="w")


    def ventana_resultado_rango(hectareas_totales: list, rango_a_consultar: str):
        #list(round(nativo_hectareas_total, 2), round(exotico_hectareas_total, 2)
        
        ventana_res = tk.Toplevel()
        ventana_res.columnconfigure([0, 1, 2], minsize=25, weight=1)
        ventana_res.rowconfigure([0, 6, 7, 8, 9], minsize=25, weight=1)
        ventana_res.resizable(False, False)
        label_bg = tk.Label(ventana_res, image=img_background)
        label_bg.place(x=0,y=0)

        def cerrando_consulta():
            """Handler cerrar consulta"""
            global consulta_abierta
            consulta_abierta = False
            ventana_res.destroy()
        
        ventana_res.protocol("WM_DELETE_WINDOW", cerrando_consulta)

        tk.Label (ventana_res, text = "Rodales consultados:", fg = "#EFD1D1", bg = "#675F2A", 
                      font = ("Clear Sans", 13, "bold")).grid(row=1, column=1, sticky="nw")
        tk.Label (ventana_res, text = rango_a_consultar, fg = "#EFD1D1", bg = "#675F2A", 
                      font = ("Clear Sans", 12)).grid(row=2, column=1, sticky="w")
        
        tk.Label (ventana_res, text = "Hectareas bosque nativo:", fg = "#EFD1D1", bg = "#675F2A", 
                      font = ("Clear Sans", 13, "bold")).grid(row=3, column=1, sticky="nw")
        tk.Label (ventana_res, text = f"{hectareas_totales[0]} ha", fg = "#EFD1D1", bg = "#675F2A", 
                      font = ("Clear Sans", 12)).grid(row=3, column=1, sticky="w", padx=(210,0))
        
        tk.Label (ventana_res, text = "Hectareas bosque exotico:", fg = "#EFD1D1", bg = "#675F2A", 
                      font = ("Clear Sans", 13, "bold")).grid(row=4, column=1, sticky="nw")
        tk.Label (ventana_res, text = f"{hectareas_totales[1]} ha", fg = "#EFD1D1", bg = "#675F2A", 
                      font = ("Clear Sans", 12)).grid(row=4, column=1, sticky="w", padx=(220,0),pady=(0,15))
        
        #Setup Canvas para gráfico de torta
        canvas = tk.Canvas(ventana_res, width=270, height=270, bg = "#675F2A")
        canvas.grid(row=5, column=1, sticky="nw")
        st = 0
        coord = 15, 15, 250, 250
        porcentaje_hect_nat = hectareas_totales[0]/(hectareas_totales[0] + hectareas_totales[1])*100
        porcentaje_hect_exo = hectareas_totales[1]/(hectareas_totales[0] + hectareas_totales[1])*100
        pieValor = [porcentaje_hect_nat, porcentaje_hect_exo]
        pieColor = ["Green", "#0B320E"]

        #Genera grafico de torta en base a porcentajes bosque nativo y exotico
        for val,col in zip(pieValor, pieColor):    
            canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
            st = st + val*3.6 

        #Leyenda gráfico de torta
        tk.Label (ventana_res, text = "Bosque Nativo", fg = "#EFD1D1", bg = "#675F2A", 
                    font = ("Clear Sans", 13)).grid(row=6, column=1, sticky="nw",padx=(25,0))
        tk.Label (ventana_res,bg = "Green", width=2, height=1).grid(row=6, column=1, sticky="w")
        
        tk.Label (ventana_res, text = "Bosque Exotico", fg = "#EFD1D1", bg = "#675F2A", 
                    font = ("Clear Sans", 13)).grid(row=7, column=1, sticky="nw",padx=(25,0))
        tk.Label (ventana_res,bg = "#0B320E", width=2, height=1).grid(row=7, column=1, sticky="w")
        

    def ventana_consulta(): # ----------------------- Ventana Consulta -------------------------------------------------
        ventana_cons = tk.Toplevel()
        ventana_cons.title('OBD Firewatch - Consultar')
        ventana_cons.resizable(False, False)
        ventana_cons.columnconfigure([0, 1, 2, 3], minsize = 25, weight = 1)
        ventana_cons.rowconfigure([0, 1, 5,6,7,8], minsize = 25, weight = 1)

        label_bg = tk.Label(ventana_cons, image=img_background)
        label_bg.place(x=-0,y=0)

        F_radiob = ("Clear Sans", 13, "bold") #tuplas de fuente para usar mas abajo
        F_rango = ("Clear Sans", 12, "bold")
        F_texto = ("Clear Sans", 9, "bold")
        F_col = ("Clear Sans", 13, "bold")

        def cerrando_ventana():
            """Handler cerrar ventana"""
            nonlocal ventana_abierta
            ventana_abierta = False
            ventana_cons.destroy()
        
        ventana_cons.protocol("WM_DELETE_WINDOW", cerrando_ventana)

        # Configuro Radiobuttons de consulta
        mensaje = tk.Label(ventana_cons, text="Consultar por:", bg="#675F2A", fg="#EFD1D1", font= F_radiob)
        mensaje.grid(row=0, column=1, sticky="sw")

        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground= "#FFEA9E", background= "#EBD792")

        consulta_temp= ttk.Combobox(ventana_cons,state = "readonly",width = 29, font= F_rango,
                                        values = log.retorna_lista_rodales())
        consulta_temp.grid(row=1, column = 1, columnspan = 2)
        consulta = tk.StringVar()
        consulta.set("Rodal")
        
        def sel():
            nonlocal consulta_temp
            if consulta.get() == "Rodal":
                consulta_temp.destroy()
                consulta_temp = ttk.Combobox(ventana_cons,state = "readonly",width = 29, font= F_rango,
                                        values = log.retorna_lista_rodales())
                consulta_temp.grid(row=1, column = 1, columnspan = 2, sticky="w")

            elif consulta.get() == "Propietario":
                consulta_temp.destroy()
                consulta_temp = ttk.Combobox(ventana_cons,state = "readonly",width = 29, font= F_rango,
                                        values = log.retorna_lista_propietarios())
                consulta_temp.grid(row=1, column = 1, columnspan = 2, sticky="w")

            elif consulta.get() == "Bosque":

                consulta_temp.destroy()

                def temp_text(e):
                    nonlocal consulta_temp
                    consulta_temp.delete(0, "end")

                texto_temporal = "Ejemplo: R1, R9-R14, R4"
                consulta_temp = tk.Entry(ventana_cons, width=30, borderwidth=2, bg="white", 
                                            fg="black", font= F_rango)
                consulta_temp.bind("<FocusIn>", temp_text)
                consulta_temp.grid(row=1, column=1, columnspan= 2, sticky="w")
                consulta_temp.insert(0, texto_temporal)

            ventana_cons.focus_set()

        def consultar():
            """Handler boton consulta"""
            global consulta_abierta

            if consulta_abierta == False:
                if consulta.get() == "Rodal":
                    rodal_a_consultar = consulta_temp.get()
                    datos_rodal = log.por_rodal(rodal_a_consultar)
                    #[propietario, natividad, exotico]
                    ventana_resultados_rodal(datos_rodal , rodal_a_consultar)
                    consulta_abierta = True

                elif consulta.get() == "Propietario":
                    prop_a_consultar = consulta_temp.get()
                    datos_rodales_propietario = log.por_propietario(prop_a_consultar)
                    #[rodales_prop, natividad, exotico]
                    ventana_resultados_propietario(datos_rodales_propietario, prop_a_consultar)
                    consulta_abierta = True

                elif consulta.get() == "Bosque":
                    rango_a_consultar = consulta_temp.get()
                    validar_entrada = re.match(r'^R\d+(-R\d+)?(, R\d+(-R\d+)?)*$', rango_a_consultar) #Si se escribe un string inválido, sale un error
                    if validar_entrada:
                        lista_hect = log.por_hectarea(rango_a_consultar)
                        ventana_resultado_rango(lista_hect, rango_a_consultar)
                        consulta_abierta = True

                    else:
                        msgbox.showerror("ERROR", "Ingreso inválido. Siga las instrucciones, por favor.", parent=ventana_cons)
            else:
                msgbox.showerror("ERROR", "Ya posee una ventana de consulta abierta", parent = ventana_cons)

        
        #Radiobotones para especificar consulta
        tk.Radiobutton(ventana_cons, text="Rodal", variable=consulta, value="Rodal", font=F_radiob, 
                       command=sel, bg="#675F2A", fg="#EFD1D1", selectcolor='Black').grid(row=2, column=1, sticky="w")

        tk.Radiobutton(ventana_cons, text="Hectáreas y tipo de bosque", variable=consulta, value="Bosque", font=F_radiob,
                       command=sel, bg="#675F2A", fg="#EFD1D1", selectcolor='Black').grid(row=3, column=1, sticky="w")

        tk.Radiobutton(ventana_cons, text="Propietario", variable=consulta,value="Propietario", font=F_radiob,
                       command=sel, bg="#675F2A", fg="#EFD1D1", selectcolor='Black').grid(row=4, column=1, sticky="w")
        
        boton_consulta = tk.Button(ventana_cons, text = "Consultar", fg = "#343434", 
                                bg = "#C4A11E", font = F_col, command=consultar) #Boton consulta
        boton_consulta.grid(row=6,column=1,pady=20)

        # Columna al lado de consultar, con texto que explique cómo consultar
        info_frame = tk.Frame(ventana_cons, borderwidth=2, relief="groove", bg="#675F2A")
        info_frame.grid(row=1, column=3, rowspan=7, sticky="nsew")

        info_explicativo = tk.Label(info_frame, text="¿Cómo consultar?", bg="#675F2A", fg="white", font=F_texto)
        info_explicativo.grid(row=0, column=0, sticky="w", padx=(10, 10), pady=(10, 10))

        # Nuevo texto explicativo
        texto_explicativo = ("Rodal: Para consultar las características o estado de un rodal, debe escribir una R y "
                            "posterior a la letra, el número respectivo del rodal. Por ejemplo, si usted escribe "
                            "\"R14\", le saldrá en pantalla toda la información sobre el Rodal 14. Hectáreas: Para "
                            "consultar sobre una cantidad determinada de hectáreas, debe usar una coma entre cada rodal "
                            "y un guion, si es que desea además, preguntar sobre un determinado rango de rodales. Por ejemplo, "
                            "si usted escribe \"R1, R3-R6, R9\" en pantalla obtendrá la información de los rodales R1, R3, R4, R5, R6 y R9.")

        info_explicativo = tk.Label(info_frame, text=texto_explicativo, wraplength=300, justify="left", 
                                    bg="#675F2A", fg="white", font=F_texto)
        info_explicativo.grid(row=1, column=0, sticky="w", padx=(10, 10), pady=(10, 10))



    root.mainloop()

if __name__ == "__main__":
    main()
