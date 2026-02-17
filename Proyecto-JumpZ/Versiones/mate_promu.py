import pandas as pd
from scipy.integrate import cumulative_trapezoid
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter
import time
import os


def importar_datos(archivo):
    df = pd.read_excel(f'Excels/{archivo}.xlsx')
    t = df.values[:, 0].astype(float)
    a_abs = df.values[:, 4].astype(float)
    a = a_abs * np.sign(df.values[:, 2].astype(float)) - 9.81
    return t, a

def filtros(a, t):
    diferencias = np.diff(a)
    dispersion = 2 * diferencias.std()
    a_gauss = gaussian_filter(a, sigma=dispersion)
    v_gaus = cumulative_trapezoid(a_gauss, t, initial=0)
    return a_gauss, v_gaus

def calcular_datos(archivo, m):
    t, a = importar_datos(archivo)
    a_gauss, v_gauss = filtros(a, t)
    t0_x, t0_y = tiempo_min(a_gauss, t)
    t1_x, t1_y = tiempo_max(a_gauss, t)
    tia = tiempo_vuelo(a_gauss, t)
    altura = altura_max(tia)
    a_salto, maximos = acel_max(a_gauss, t0_y, t1_y)
    F = fuerza_max(a_gauss, m)
    P_t0 = potencia(F, v_gauss, t0_y)
    P = potencia_en_salto(F, v_gauss)
    grafica_velocidad_mostrar(t, v_gauss)
    grafica_aceleracion_mostrar(t, a_gauss, t0_x, t1_x, t0_y, t1_y, maximos, a_salto)
    grafica_fuerza_mostrar(t, F)
    grafica_potencia_mostrar(t, P)
    return t, a_gauss, v_gauss, t0_x, t0_y, t1_x, t1_y, tia, altura, a_salto, maximos, F, P_t0, P

def tiempo_min(a, tiempo):
    minimo = np.argmin(a)
    return tiempo[minimo], minimo

def tiempo_max(a, tiempo):
    maximo = np.argmax(a)
    return tiempo[maximo], maximo

def tiempo_vuelo(a, tiempo):
    return tiempo_max(a, tiempo)[0] - tiempo_min(a, tiempo)[0]

def altura_max(t):
    return (1/8) * 9.81 * t**2 * 1000

def acel_max(a_gauss, t0_y, t1_y):
    punto_max = t0_y + (t1_y - t0_y) // 2
    maximos = np.argmax(a_gauss[:punto_max])
    aceleracion_max = a_gauss[maximos]
    return aceleracion_max, maximos

def fuerza_max(a_gauss, m):
    return m * a_gauss

def potencia(F, v_gauss):
    return F * v_gauss

def potencia_en_salto(F, v_gauss, t0_y):
    return F * v_gauss[t0_y]

def grafica_velocidad_mostrar(t, v_filtrado):
    fig, ax = plt.subplots()
    ax.plot(t, v_filtrado, label='Velocidad')
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    rect = plt.Rectangle((xlim[0], ylim[0]), xlim[1]-xlim[0], ylim[1]-ylim[0], color='lightgray', zorder=0)
    ax.add_patch(rect)
    ax.set_facecolor('lightgray')
    ax.grid(True)
    ax.legend()
    plt.savefig(f'Archivos/Saltos Guardados (NO TOCAR)/{nombre_global}/velocidad.png', transparent=True)
    plt.close(fig)

def grafica_aceleracion_mostrar(t, a_gauss, t0_x, t1_x, t0_y, t1_y, maximos, aceleracion_max):
    fig, ax = plt.subplots()
    ax.plot(t, a_gauss, label='Aceleración')
    ax.plot(t0_x, a_gauss[t0_y], 'x', label='T0', color='Blue')
    ax.plot(t1_x, a_gauss[t1_y], 'x', label='T1', color='Blue')
    ax.plot(t[maximos], aceleracion_max, "x", label="Aceleración máx", color="Red")
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    rect = plt.Rectangle((xlim[0], ylim[0]), xlim[1]-xlim[0], ylim[1]-ylim[0], color='lightgray', zorder=0)
    ax.add_patch(rect)
    ax.set_facecolor('lightgray')
    ax.grid(True)
    ax.legend()
    plt.savefig(f'Archivos/Saltos Guardados (NO TOCAR)/{nombre_global}/aceleracion.png', transparent=True)
    plt.close(fig)

def grafica_fuerza_mostrar(t, F):
    fig, ax = plt.subplots()
    ax.plot(t, F, label='Fuerza')
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    rect = plt.Rectangle((xlim[0], ylim[0]), xlim[1]-xlim[0], ylim[1]-ylim[0], color='lightgray', zorder=0)
    ax.add_patch(rect)
    ax.set_facecolor('lightgray')
    ax.grid(True)
    ax.legend()
    plt.savefig(f'Archivos/Saltos Guardados (NO TOCAR)/{nombre_global}/fuerza.png', transparent=True)
    plt.close(fig)

def grafica_potencia_mostrar(t, P):
    fig, ax = plt.subplots()
    ax.plot(t, P, label='Potencia')
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    rect = plt.Rectangle((xlim[0], ylim[0]), xlim[1]-xlim[0], ylim[1]-ylim[0], color='lightgray', zorder=0)
    ax.add_patch(rect)
    ax.set_facecolor('lightgray')
    ax.grid(True)
    ax.legend()
    plt.savefig(f'Archivos/Saltos Guardados (NO TOCAR)/{nombre_global}/potencia.png', transparent=True)
    plt.close(fig)

def crear_carpeta(nombre):
    global nombre_global
    fecha = time.localtime()
    fecha_str = time.strftime(f'%Y-%m-%d %H-%M-%S', fecha)
    nombre_global = f'{nombre} {fecha_str}'
    os.makedirs(f'Archivos/Saltos Guardados (NO TOCAR)/{nombre_global}', exist_ok=True)
