import tkinter as tk
from tkinter import ttk
from fft_imaginario import *
from fft_iterativo import *
from fft_lagrange import *
from fft_reales import *

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

def Calcular(Lagrange_v, Iterativo_v, VandermondeI_v, VandermondeR_v):
    global Fun1, Fun2
    Resp = ""
    Tiempos = []
    Respuestas = []
    if (Lagrange_v):
        TiempoMS, RespuestaL = appFFT_Lagrange(Fun1, Fun2)
        Tiempos.append(TiempoMS)
        Respuestas.append(RespuestaL)
    if (Iterativo_v):
        TiempoMS, RespuestaI = appFFT_Iterativo(Fun1, Fun2)
        Tiempos.append(TiempoMS)
        Respuestas.append(RespuestaI)
    if (VandermondeI_v):
        TiempoMS, RespuestaVI = appFFT_Imaginario(Fun1, Fun2)
        Tiempos.append(TiempoMS)
        Respuestas.append(RespuestaVI)
    if (VandermondeR_v):
        TiempoMS, RespuestaVR = appFFT_Reales(Fun1, Fun2)
        Tiempos.append(TiempoMS)
        Respuestas.append(RespuestaVR)
    Aux = Respuestas[0]
    Respuesta = [str(k) if (k < 0) else "+"+str(k) for k in Aux]
    for k in range(0, len(Respuesta)):
        Resp += " "*len(Respuesta[k])*2
        if (k <= 1):
            if (k == 0):
                Resp += " "
            else:
                Resp += "  "
        else:
            Resp += " " + str(k)
    Resp += "\n"
    for k in range(0, len(Respuesta)):
        Resp += Respuesta[k]
        if (k == 0):
            Resp += " "
        else:
            Resp += "X "
    texto_respuesta.delete("1.0", "end")
    texto_respuesta.insert("1.0", Resp)

def click_borrarTodo():
    label1_var.set("")
    label2_var.set("")
    texto_respuesta.delete("1.0", "end")
    Lagrange_v.set(False)
    VandermondeR_v.set(False)
    VandermondeI_v.set(False)
    Iterativo_v.set(False)

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Ventana principal")
ventana_principal.config(width=570, height=400)

# Variables auxiliares
texto_var = tk.StringVar()  # Variable de seguimiento entrada texto
label1_var = tk.StringVar()  # Variable de seguimiento para cargar funcion1
label2_var = tk.StringVar()  # Variable de seguimiento para cargar funcion2

# Texto que se muestra en pantalla
lblFuncion = ttk.Label(ventana_principal, text="Ingrese los coeficientes del polinomio: ", font=("Calibri 14"))
lblFuncion.place(x=20, y=5)
txtFuncion = tk.Entry(ventana_principal, font=("Calibri 12"), width= 68, textvariable=texto_var)
txtFuncion.place(x=10, y=38)

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
label_Opciones.place(x=345, y=140)
# Crear variables para almacenar los estados de los chekbox (bool)
Lagrange_v = tk.BooleanVar()
VandermondeR_v = tk.BooleanVar()
VandermondeI_v = tk.BooleanVar()
Iterativo_v = tk.BooleanVar()
# Crear los chekbox con texto
chkLagrange = ttk.Checkbutton(ventana_principal, text="FFT: Multiplicadores de Lagrange", variable=Lagrange_v)
chkLagrange.place(x= 350, y= 170)
chkVandermondeR = ttk.Checkbutton(ventana_principal, text="FFT: Vandermonde en Reales", variable=VandermondeR_v)
chkVandermondeR.place(x= 350, y= 190)
chkVandermondeI = ttk.Checkbutton(ventana_principal, text="FFT: Vandermonde en Imaginarios", variable=VandermondeI_v)
chkVandermondeI.place(x= 350, y= 210)
chkIterativo = ttk.Checkbutton(ventana_principal, text="FFt: Iterativo con bit reverso", variable=Iterativo_v)
chkIterativo.place(x= 350, y= 230)

# Parte de respuesta
lblRespuesta = ttk.Label(ventana_principal, text="Respuesta: ", font=("Calibri 14"))
lblRespuesta.place(x=20, y=280)
texto_respuesta = tk.Text(ventana_principal, width=68, height=2, font=("Calibri", 12))
texto_respuesta.place(x=10, y=320)

# Crear un botón para calcular la respuesta
boton_abrir = ttk.Button(ventana_principal, text="Calcular", command= lambda: Calcular(Lagrange_v, Iterativo_v, VandermondeI_v, VandermondeR_v))
boton_abrir.place(x=200, y=200)

# Crear un botón para borrar todo
boton_borrarTodo = ttk.Button(ventana_principal, text="Borrar", command= lambda: click_borrarTodo())
boton_borrarTodo.place(x=200, y=230)

ventana_principal.mainloop()
