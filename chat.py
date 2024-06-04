from tkinter import *
import tkinter as tk

# Crear la ventana
Ventana = tk.Tk()
Ventana.title("UV TEATRO")
Ventana.geometry("300x250+200+100")
Ventana.configure(bg='Light Blue')

# Definir la función para calcular los valores y actualizar las etiquetas
def teatro():
    cantidad = int(cantidad_entr.get())  # Obtener el valor de la entrada de texto

    palco_Pre = 22000
    palco_norm = 29000
    platea_pre = 30000
    platea_norm = 38000

    total = 0
    aporte = 0
    if Ubicacion_opciones.get() == "Palco":
        if Tipo_opciones.get() == "Pre-Venta":
            total = cantidad * palco_Pre
            aporte = total * 0.15
        elif Tipo_opciones.get() == "Normal":
            total = cantidad * palco_norm
            aporte = total * 0.15
    elif Ubicacion_opciones.get() == "Platea":
        if Tipo_opciones.get() == "Pre-Venta":
            total = cantidad * platea_pre
            aporte = total * 0.15
        elif Tipo_opciones.get() == "Normal":
            total = cantidad * platea_norm
            aporte = total * 0.15
    
    # Actualizar las etiquetas con los valores calculados
    venta_lab.config(text=f"Valor venta: {total}")
    aporte_lab.config(text=f"Valor aporte: {aporte}")

# Crear widgets
Ubicacion_lab = tk.Label(Ventana, text="Ubicación:", font=("Ebrima", 10), bg="Light Blue")
Ubicacion_lab.place(x=10, y=20)

Ubicacion_opciones = tk.StringVar(Ventana)
Ubicacion_opciones.set("Palco")  # Opción predeterminada

Ubicacion_Menu = tk.OptionMenu(Ventana, Ubicacion_opciones, "Palco", "Platea")
Ubicacion_Menu.place(x=80, y=20)

tipo_lab = tk.Label(Ventana, text="Tipo:", font=("Ebrima", 10), bg="Light Blue")
tipo_lab.place(x=10, y=50)

Tipo_opciones = tk.StringVar(Ventana)
Tipo_opciones.set("Pre-Venta")  # Opción predeterminada

Tipo_Menu = tk.OptionMenu(Ventana, Tipo_opciones, "Pre-Venta", "Normal")
Tipo_Menu.place(x=80, y=50)

cantidad_lab = tk.Label(Ventana, text="Cantidad:", font=("Ebrima", 10), bg="Light Blue")
cantidad_lab.place(x=10, y=80)

cantidad_entr = tk.Entry(Ventana)
cantidad_entr.place(x=80, y=80)

calcular_bot = tk.Button(Ventana, text="Calcular valores", command=teatro)
calcular_bot.place(x=50, y=110)

venta_lab = tk.Label(Ventana, text="Valor venta:", font=("Ebrima", 10), bg="Light Blue")
venta_lab.place(x=10, y=140)

aporte_lab = tk.Label(Ventana, text="Valor aporte:", font=("Ebrima", 10), bg="Light Blue")
aporte_lab.place(x=10, y=170)

# Ejecutar la aplicación
Ventana.mainloop()
