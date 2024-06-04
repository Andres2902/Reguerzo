from tkinter import*
import tkinter as tk

Ventana = tk.Tk() #crear ventana
titulo = Ventana.title("UV TEATRO") #titulo de la ventana
Ventana.geometry("200x200+200+100") #tamaño de la ventana
Ventana.configure(bg='Light Blue') #color de la ventana


def teatro():

    cantidad = int(cantidad_entr.get()) #obtener el valor de la entrada de texto

    palco_Pre = 22000
    palco_norm = 29000
    platea_pre = 30000
    platea_norm = 38000

    
    if Ubicacion_opciones.get() == "Palco": #el .get() para obtener los valores del menú
        if Tipo_opciones.get() == "Pre-Venta": #el .get() para obtener los valores del menú
            total = cantidad * palco_Pre 
            aporte = total * 0.15

        elif Tipo_opciones.get() == "Normal": #el .get() para obtener los valores del menú
            total = cantidad * palco_norm
            aporte = total * 0.15

    elif Ubicacion_opciones.get() == "Platea": #el .get() para obtener los valores del menú
        if Tipo_opciones.get() == "Pre-Venta": #el .get() para obtener los valores del menú
            total = cantidad * platea_pre
            aporte = total * 0.15
 
        elif  Tipo_opciones.get() == "Normal": #el .get() para obtener los valores del menú
            total = cantidad * platea_norm
            aporte = total * 0.15

    # Actualizar las etiquetas con los valores calculados
    venta_lab.config(text=f"Valor venta: {total}") 
    aporte_lab.config(text=f"Valor aporte: {aporte}")
    

Ubicacion_lab = tk.Label(Ventana, text= "Ubicación: " , font=("Ebrima", 10), bg="Light Blue") #label par crear un widget de texto
Ubicacion_lab.place(x= 10 , y= 20) #lugar del widget

Ubicacion_opciones = tk.StringVar(Ventana) #guarda la variable que selecciona en el Menú desplegable
Ubicacion_opciones.set("Palco") #muestra una opcion predeterminada

Ubicacion_Menu = tk.OptionMenu(Ventana, Ubicacion_opciones, "Palco", "Platea" ) #genera un meú despegble, "Ubicacion, donde se guarda, opciones "
Ubicacion_Menu.place(x= 80, y= 20) #Lugar del menú



tipo_lab = tk.Label(Ventana, text= "Tipo: " , font=("Ebrima", 10), bg="Light Blue") #label par crear un widget de texto
tipo_lab.place(x= 10 , y= 50) #lugar del widget

Tipo_opciones = tk.StringVar(Ventana) #guarda la variable que selecciona en el Menú desplegable
Tipo_opciones.set("Pre-Venta") #muestra una opcion predeterminada

Tipo_Menu = tk.OptionMenu(Ventana, Tipo_opciones, "Pre-Venta", "Normal" ) #genera un menú despegble, "Ubicacion, donde se guarda, opciones "
Tipo_Menu.place(x= 80, y= 50) #Lugar del menú



cantidad_lab = tk.Label(Ventana, text= "Cantidad: " , font=("Ebrima", 10), bg="Light Blue") #label par crear un widget de texto
cantidad_lab.place(x= 10 , y= 80) #lugar del widget

cantidad_entr= tk.Entry(Ventana) #crear una entrada de texto
cantidad_entr.place(x=80, y=80) #ubicacion de la entraad de texto




calcular_bot= tk.Button(Ventana, text="Calcular valores", command=teatro) #crear botón 
calcular_bot.place(x= 50 , y= 110 )



venta_lab = tk.Label(Ventana, text= "Valor venta: " , font=("Ebrima", 10), bg="Light Blue") #label par crear un widget de texto
venta_lab.place(x= 10 , y= 140) #lugar del widget

aporte_lab = tk.Label(Ventana, text= "Valor aporte: " , font=("Ebrima", 10), bg="Light Blue") #label par crear un widget de texto
aporte_lab.place(x= 10 , y= 170) #lugar del widget

Ventana.mainloop()
