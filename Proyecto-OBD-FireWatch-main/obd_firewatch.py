# Esta es la capa de , es decir, acá está main() y
# todo lo relacionado a tkinter, es lo que el USUARIO ve.

import logica as log # se imoorta la capa de negocio
import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk

def main():
    root = tk.Tk()
    root.columnconfigure([0, 1, 2, 3, 4, 5, 6], minsize=50, weight=1)
    root.rowconfigure([0, 1, 2, 3], minsize=100, weight=1)
    root.title('OBD Firewatch - Consultar')
    root.configure(bg="#675F2A")

    # Configurar la imagen de fondo
    img_background = tk.PhotoImage(file="assets/iconos/background.png")
    label_bg = tk.Label(root, image=img_background)
    label_bg.place(x=0, y=0, relwidth=1, relheight=1)  # Configurar para que llene toda la ventana

    img_logo = tk.PhotoImage(file="assets/iconos/logo.png")
    img_consulta = tk.PhotoImage(file="assets/iconos/consultare.png").subsample(2, 2)
    img_ingresar = tk.PhotoImage(file="assets/iconos/1.png").subsample(2, 2)
    img_incendio = tk.PhotoImage(file="assets/iconos/2.png").subsample(2, 2)

    # Agregar una fila para el logo centrado
    label_logo = tk.Label(root, image=img_logo, bg="#675F2A")
    label_logo.grid(row=0, column=1, columnspan=5)

    #boton_guardar = ttk.Button(root, image=img_nube).grid(row=0,column=0)
    
    boton_ingreasr = ttk.Button(root, image=img_ingresar, command=lambda:ventana_ingresar()).grid(row=1,column=1)
    boton_incendio = ttk.Button(root, image=img_incendio, command=lambda:ventana_incendio()).grid(row=1,column=3)
    boton_consulta = ttk.Button(root, image=img_consulta, command=lambda:ventana_consulta()).grid(row=1,column=5)

    def ventana_ingresar():
        ventana_ingr = tk.Toplevel() # crea ventana ingresar rodales

    def ventana_incendio():
        ventana_inc = tk.Toplevel() # crea ventana simulación incendio

    def ventana_consulta():
        # DIMENSIONES DE LA VENTANA
        ventana_cons = tk.Toplevel()
        ventana_cons.geometry("650x250")
        ventana_cons.minsize(650, 250)
        ventana_cons.configure(bg="#675F2A")  # Cambia el color de fondo de la ventana
        ventana_cons.title('OBD Firewatch - Consultar')

        # Crear un Frame dentro de la ventana_cons
        frame_consulta = tk.Frame(ventana_cons, bg="#675F2A")
        frame_consulta.pack(expand=True, fill="both")

        # Configuro entry con texto temporal
        def temp_text(e):
            entrada_busqueda.delete(0, "end")

        entrada_busqueda = tk.Entry(frame_consulta, width=30, borderwidth=2, bg="white", fg="black")
        entrada_busqueda.bind("<FocusIn>", temp_text)
        entrada_busqueda.grid(row=1, column=1, sticky="w")
        entrada_busqueda.insert(0, "Ejemplo: R1")

        # Configuro Radiobuttons de consulta
        consulta = tk.StringVar()
        consulta.set("Rodal")

        def sel():
            entrada_busqueda.delete(0, "end")
            if consulta.get() == "Propietario":
                texto_temporal = "Seleccione el Propietario"
            elif consulta.get() == "Bosque":
                texto_temporal = "Ejemplo: R1, R9-R14, R4"
            else:
                texto_temporal = "Ejemplo: R1"
            entrada_busqueda.insert(0, texto_temporal)
            ventana_cons.focus_set()

        tk.Radiobutton(frame_consulta, text="Rodal", variable=consulta,
                value="Rodal", command=sel, bg="#675F2A", fg="white").grid(row=2, column=1, sticky="w")

        tk.Radiobutton(frame_consulta, text="Hectáreas y tipo de bosque", variable=consulta,
                        value="Bosque", command=sel, bg="#675F2A", fg="white").grid(row=3, column=1, sticky="w")

        tk.Radiobutton(frame_consulta, text="Propietario", variable=consulta,
                        value="Propietario", command=sel, bg="#675F2A", fg="white").grid(row=4, column=1, sticky="w")

        mensaje = tk.Label(frame_consulta, text="Consultar por", bg="#675F2A", fg="white")
        mensaje.grid(row=0, column=1, sticky="w", padx=(10, 0))

        # Columna al lado de consultar, con texto que explique cómo consultar
        info_frame = tk.Frame(frame_consulta, borderwidth=2, relief="groove", bg="#675F2A")
        info_frame.grid(row=0, column=2, rowspan=5, sticky="nsew", padx=(10, 10), pady=(10, 10))

        info_explicativo = tk.Label(info_frame, text="¿Cómo consultar?", bg="#675F2A", fg="white")
        info_explicativo.grid(row=0, column=0, sticky="w", padx=(10, 10), pady=(10, 10))

        # Nuevo texto explicativo
        texto_explicativo = ("Rodal: Para consultar las características o estado de un rodal, debe escribir una R y "
                            "posterior a la letra, el número respectivo del rodal. Por ejemplo, si usted escribe "
                            "\"R14\", le saldrá en pantalla toda la información sobre el Rodal 14. Hectáreas: Para "
                            "consultar sobre una cantidad determinada de hectáreas, debe usar una coma entre cada rodal "
                            "y un guion, si es que desea además, preguntar sobre un determinado rango de rodales. Por ejemplo, "
                            "si usted escribe \"R1, R3-R6, R9\" en pantalla obtendrá la información de los rodales R1, R3, R4, R5, R6 y R9.")

        info_explicativo = tk.Label(info_frame, text=texto_explicativo, wraplength=300, justify="left", bg="#675F2A", fg="white")
        info_explicativo.grid(row=1, column=0, sticky="w", padx=(10, 10), pady=(10, 10))


        # Loop principal de la ventana
        ventana_cons.mainloop()

    if __name__ == "__main__":
        root.mainloop()

if __name__ == "__main__":
    main()