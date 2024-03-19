import tkinter as tk

def calcular_polinomio():
    # Aquí puedes agregar la lógica para calcular el polinomio
    pass

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz de Polinomio")

# Crear los elementos de la interfaz
etiqueta = tk.Label(ventana, text="Ingrese los coeficientes del polinomio:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Calcular", command=calcular_polinomio)
boton.pack()

# Iniciar el bucle de eventos
ventana.mainloop()
