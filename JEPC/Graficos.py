import matplotlib.pyplot as plt
import numpy as np
import time
import sys
import os
proyecto_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(proyecto_dir)

from fft_lagrange import multiplicar_polinomios as fftLagrange
from fft_imaginario import multiplicar_polinomios as FFTImaginario
from fft_iterativo import multiplicar_polinomios as FFTIterativo
from fft_reales import multiplicar_polinomios as FFTReales

tiempos = [[],[],[],[]]
tamanios = [2**x for x in range(1,11)]

def JEPC_G_ML():
    for tamn in tamanios:
        A = [np.random.rand() for _ in range(tamn)]
        B = [np.random.rand() for _ in range(tamn)]
    
        inicio = time.perf_counter()
        fftLagrange(A, B)
        fin = time.perf_counter()
      

        tiempos[0].append((float(fin) - float(inicio))*1000)
def JEPC_G_FFT_Reales():
    for tamn in tamanios:
        A = [np.random.rand() for _ in range(tamn)]
        B = [np.random.rand() for _ in range(tamn)]
    
        inicio = time.perf_counter()
        FFTReales(A, B)
        fin = time.perf_counter()

        tiempos[1].append((float(fin) - float(inicio))*1000)
def JEPC_G_FFT_Imaginarios():
    for tamn in tamanios:
        A = [np.random.rand() for _ in range(tamn)]
        B = [np.random.rand() for _ in range(tamn)]

        inicio = time.perf_counter()
        C = FFTImaginario(A, B)
        fin = time.perf_counter()

        tiempos[2].append((float(fin) - float(inicio))*1000)
def JEPC_G_FFT_Iterarivo_bitReverso():
    for tamn in tamanios:
        A = [np.random.rand() for _ in range(tamn)]
        B = [np.random.rand() for _ in range(tamn)]
 
        inicio = time.perf_counter()
        C = FFTIterativo(A, B)
        fin = time.perf_counter()


        tiempos[3].append((float(fin) - float(inicio))*1000)

# Pruba de tiempos de ejecucion con valores aletorios
def FC_GraficarPruebaEstres(langrange, vandermonderR, vandermonderI,iterativo, tamanioPolinomio = 0,times = [],respuestas = []):
    JEPC_G_ML()
    JEPC_G_FFT_Reales()
    JEPC_G_FFT_Imaginarios()
    JEPC_G_FFT_Iterarivo_bitReverso()
    # Crear el gráfico de dispersión con puntos de diferentes colores
    plt.scatter( tamanios,tiempos[0], color='red', label='Multiplicadores de Lagrange', marker='o',s=20)
    plt.scatter( tamanios,tiempos[1], color='blue', label='FFT Reales', marker='o',s=20)
    plt.scatter( tamanios,tiempos[2], color='green', label='FFT Imaginarios', marker='o',s=20)
    plt.scatter( tamanios,tiempos[3], color='black', label='Iterativo bit reverso', marker='o',s=20)

    # Agregar etiquetas y título
    plt.xlabel('Tamaño de polinomio')
    plt.ylabel('Tiempo de ejecucion')
    plt.title('Multiplicacion de polinomios')

    # Agregar leyenda
    plt.legend()

    plt.xscale('log')
    plt.yscale('log')
    # Mostrar el gráfico
    plt.show()
    
def FC_Graficar(Lagrange_v,VandermondeR_v,VandermondeI_v,Iterativo_v, tamanioPolinomio = 0,times = [],respuestas = []):
  
    # Crear el gráfico de dispersión con puntos de diferentes colores
    if(Lagrange_v):
        plt.scatter( tamanioPolinomio,times[0], color='red', label='FFT: Multiplicadores de Lagrange', marker='o',s=20)
    if(VandermondeR_v):
        plt.scatter( tamanioPolinomio,times[1], color='blue', label='FFT: Vandemonde en Reales', marker='o',s=20)
    if(VandermondeI_v):
        plt.scatter( tamanioPolinomio,times[2], color='green', label='FFT: Vandemonde en Imaginarios', marker='o',s=20)
    if(Iterativo_v):
        plt.scatter( tamanioPolinomio,times[3], color='black', label='FFT: Iterativo con bit reverso', marker='o',s=20)

    # Agregar etiquetas y título
    plt.xlabel('Tamaño de polinomio')
    plt.ylabel('Tiempo de ejecucion')
    plt.title('Multiplicacion de polinomios')

    # Agregar leyenda
    plt.legend()

    plt.xscale('log')
    plt.yscale('log')
    # Mostrar el gráfico
    plt.show()