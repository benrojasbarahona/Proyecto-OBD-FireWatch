import tkinter as tk

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.title("Redimensionar Pantalla")
        self.geometry("400x300")

        # Configuración de los pesos de las filas y columnas
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Crear rectángulos
        rectangulo1 = tk.Frame(self, bg="red")
        rectangulo2 = tk.Frame(self, bg="green")
        rectangulo3 = tk.Frame(self, bg="blue")

        # Ubicar rectángulos en la ventana
        rectangulo1.grid(row=0, column=0, sticky="nsew")
        rectangulo2.grid(row=0, column=1, sticky="nsew")
        rectangulo3.grid(row=0, column=2, sticky="nsew")

        # Configurar el peso de las columnas para que se redimensionen
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Configurar el peso de las filas para que se redimensionen
        self.rowconfigure(0, weight=1)

if __name__ == "__main__":
    app = Ventana()
    app.mainloop()
