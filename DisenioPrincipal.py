import tkinter as tk
from tkinter import ttk

# Varibles globales
i = 0
Fun1 = []
Fun2 = []

def abrir_ventana_secundaria():
    # Crear una ventana secundaria.
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana secundaria")
    ventana_secundaria.config(width=300, height=200)

    # Crear un botón dentro de la ventana secundaria para cerrarla.
    boton_cerrar = ttk.Button(ventana_secundaria, text="Cerrar ventana", command=ventana_secundaria.destroy)
    boton_cerrar.place(x=75, y=75)

def click_boton(valor, e_texto, texto_var):
    global i
    # Insertar el valor en el Entry
    e_texto.insert(i, str(valor))
    i += len(valor)
    # Actualizar la variable de seguimiento
    texto_var.set(e_texto.get())
    punto = True

def click_borrar(e_texto, texto_var):
    global i
    # Borrar los valores
    e_texto.delete(0, i)
    i = 0
    # Actualizar la varible de seguimiento
    texto_var.set(e_texto.get())

def click_funcion1(e_texto, texto_var, label1_var):
    global i, Fun1
    # Sacar los valores de la función
    Aux1 = e_texto.get()
    Aux2 = [int(x) for x in Aux1.split(" ")]
    Fun1 = Aux2
    # Actualizar valores
    label1_var.set("Cargado...")
    texto_var.set("")
    i = 0
    print(Fun1)

def click_funcion2(e_texto, texto_var, label2_var):
    global i, Fun2
    # Sacar los valores de la función
    Aux1 = e_texto.get()
    Aux2 = [int(x) for x in Aux1.split(" ")]
    Fun2 = Aux2
    # Actualizar valores
    label2_var.set("Cargado...")
    texto_var.set("")
    i = 0
    print(Fun2)

def main():
    # Crear la ventana principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Ventana principal")
    ventana_principal.config(width=400, height=450)

    # Variables auxiliares
    texto_var = tk.StringVar()  # Variable de seguimiento entrada texto
    label1_var = tk.StringVar()  # Variable de seguimiento para cargar funcion1
    label2_var = tk.StringVar()  # Variable de seguimiento para cargar funcion2

    # Texto que se muestra en pantalla
    lblFuncion = ttk.Label(ventana_principal, text="Ingrese la función: ", font=("Calibri 12"))
    lblFuncion.place(x=20, y=0)
    txtFuncion = tk.Entry(ventana_principal, font=("Calibri 14"), width= 35, textvariable=texto_var)
    txtFuncion.place(x=20, y=30)

    # Botones Númericos
    boton1 = tk.Button(ventana_principal, text="1", width=5, height= 2, command=lambda: click_boton("1", txtFuncion, texto_var))
    boton1.place(x=10, y=70)
    boton2 = tk.Button(ventana_principal, text="2", width=5, height= 2, command=lambda: click_boton("2", txtFuncion, texto_var))
    boton2.place(x=60, y=70)
    boton3 = tk.Button(ventana_principal, text="3", width=5, height= 2, command=lambda: click_boton("3", txtFuncion, texto_var))
    boton3.place(x=110, y=70)
    boton4 = tk.Button(ventana_principal, text="4", width=5, height= 2, command=lambda: click_boton("4", txtFuncion, texto_var))
    boton4.place(x=10, y=120)
    boton5 = tk.Button(ventana_principal, text="5", width=5, height= 2, command=lambda: click_boton("5", txtFuncion, texto_var))
    boton5.place(x=60, y=120)
    boton6 = tk.Button(ventana_principal, text="6", width=5, height= 2, command=lambda: click_boton("6", txtFuncion, texto_var))
    boton6.place(x=110, y=120)
    boton7 = tk.Button(ventana_principal, text="7", width=5, height= 2, command=lambda: click_boton("7", txtFuncion, texto_var))
    boton7.place(x=10, y=170)
    boton8 = tk.Button(ventana_principal, text="8", width=5, height= 2, command=lambda: click_boton("8", txtFuncion, texto_var))
    boton8.place(x=60, y=170)
    boton9 = tk.Button(ventana_principal, text="9", width=5, height= 2, command=lambda: click_boton("9", txtFuncion, texto_var))
    boton9.place(x=110, y=170)
    boton0 = tk.Button(ventana_principal, text="0", width=5, height= 2, command=lambda: click_boton("0", txtFuncion, texto_var))
    boton0.place(x=60, y=220)

    # Botones de escritura auxiliares
    boton_borrar = tk.Button(ventana_principal, text= "AC", width= 5, height= 2, command= lambda: click_borrar(txtFuncion, texto_var))
    boton_borrar.place(x = 110, y = 220)
    boton_punto = tk.Button(ventana_principal, text=".", width= 5, height= 2, command= lambda: click_boton(".", txtFuncion, texto_var))
    boton_punto.place(x= 10, y=220)
    boton_suma = tk.Button(ventana_principal, text= "+", width= 5, height= 2, command= lambda: click_boton(" +", txtFuncion, texto_var))
    boton_suma.place(x= 170, y=70)
    boton_resta = tk.Button(ventana_principal, text= "-", width= 5, height= 2, command= lambda: click_boton(" -", txtFuncion, texto_var))
    boton_resta.place(x= 170, y=120)

    # label para mostrar cargado de 1ra y 2da función
    label_funcion1 = tk.Label(ventana_principal, text="...", textvariable= label1_var)
    label_funcion1.place(x=325, y=70)
    label_funcion2 = tk.Label(ventana_principal, text="...", textvariable= label2_var)
    label_funcion2.place(x=325, y=100)
    # botones para cargar las funciones
    boton_funcion1 = tk.Button(ventana_principal, text= "Funcion1", width= 9, height= 1, command= lambda: click_funcion1(txtFuncion, texto_var, label1_var))
    boton_funcion1.place(x= 250, y = 70)
    boton_funcion2 = tk.Button(ventana_principal, text= "Funcion2", width= 9, height= 1, command= lambda: click_funcion2(txtFuncion, texto_var, label2_var))
    boton_funcion2.place(x= 250, y = 100)

    # Mostrar el ingreso de opciones
    label_Opciones = tk.Label(ventana_principal, text="Ingrese las opciones:", font=("Calibri 12"))
    label_Opciones.place(x=10, y=300)
    # Crear variables para almacenar los estados de los chekbox (bool)
    chkLagrange_value = tk.BooleanVar()
    chkVandermondeReales_value = tk.BooleanVar()
    chkVandermondeImaginarios_value = tk.BooleanVar()
    chkIterativoBitReverso_value = tk.BooleanVar()
    # Crear los chekbox con texto
    chkLagrange = ttk.Checkbutton(ventana_principal, text="Multiplicadores de Lagrange", variable=chkLagrange_value)
    chkLagrange.place(x= 10, y= 330)
    chkVandermondeR = ttk.Checkbutton(ventana_principal, text="MFFT, usando Matriz de Vandermonde en Reales", variable=chkVandermondeReales_value)
    chkVandermondeR.place(x= 10, y= 350)
    chkVandermondeI = ttk.Checkbutton(ventana_principal, text="FFT, usando matriz de Vandermonde en Imaginarios", variable=chkVandermondeImaginarios_value)
    chkVandermondeI.place(x= 10, y= 370)
    chkIterativo = ttk.Checkbutton(ventana_principal, text="Método iterativo con bit reverso", variable=chkIterativoBitReverso_value)
    chkIterativo.place(x= 10, y= 390)

    # Crear un botón dentro de la ventana principal que abre la ventana secundaria.
    boton_abrir = ttk.Button(ventana_principal, text="Calcular", command=abrir_ventana_secundaria)
    boton_abrir.place(x=200, y=200)

    ventana_principal.mainloop()

if __name__ == "__main__":
    main()
