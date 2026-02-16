import pandas as pd
import numpy as np
import time
import os
from scipy.integrate import cumulative_trapezoid
from scipy.ndimage import gaussian_filter
from funciones_v4 import *
import matplotlib.pyplot as plt
datos_cargar_salto = []

def importar_datos(archivo):
    crear_log(f'importando los datos del archivo: {archivo}...','INFO')
    try:
        datos_cargar_salto.append(archivo)
        df = pd.read_excel(f'Excels/{archivo}.xlsx')
        t = df.values[:, 0].astype(float)
        aceleracion_abs = df.values[:, 1].astype(float)
        aceleracion = aceleracion_abs * np.sign(df.values[:, 3].astype(float))-9.81
        crear_log('Datos importados correctamente','INFO')
        return t, aceleracion
    except Exception as e:
        crear_log(f'No se han podido importar los datos correctamente: {e}','ERROR')


def filtros(a,t):
    diferencias = np.diff(a)
    dispersion = 2 * diferencias.std()
    a_gauss = gaussian_filter(a, sigma=dispersion)
    v_gauss = cumulative_trapezoid(a, t, initial=0)
    return a_gauss, v_gauss


def tiempo_min(a_gauss, t):
    minimo = np.argmin(a_gauss)
    return t[minimo], minimo

def tiempo_max(a_gauss, t):
    maximo = np.argmax(a_gauss)
    return t[maximo], maximo

def tiempo_vuelo(a, tiempo):
    return tiempo_max(a, tiempo)[0] - tiempo_min(a, tiempo)[0]

def altura_max(t):
    return int((1/8) * 9.81 * t**2 * 1000)

def acel_max(a_gauss, t0_y, t1_y):
    punto_max = t0_y + (t1_y - t0_y) // 2
    maximos = np.argmax(a_gauss[:punto_max])
    aceleracion_max = a_gauss[maximos]
    return aceleracion_max, maximos

def fuerza(aceleracion, m):
    fuerza_empleada = (aceleracion+9.81)*m
    return fuerza_empleada

def potencia(fuerza_empleada, v_gauss):
    potencia_empleada = fuerza_empleada*v_gauss
    return potencia_empleada

def potencia_en_salto(f_max, v_gauss, maximos):
    p_max = f_max * v_gauss[maximos]
    return p_max

def fuerza_max(aceleracion_max, m):
    f_max  = m * (aceleracion_max+9.81)
    return f_max


def grafica_velocidad_mostrar(t, v_gauss):
    fig, ax = plt.subplots()
    ax.plot(t, v_gauss, label='Velocidad', color='blue')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad (m/s)')
    agregar_fondo(ax)
    ax.grid(True)
    ax.legend()
    try:
        crear_log(f'Guardando las garficas de velocidad en {carpeta_g}...','INFO')
        plt.savefig(f'Archivos/Saltos Guardados (NO TOCAR)/{carpeta_g}/velocidad.png', transparent=True)
        cambiar_ejes(ax)
        plt.savefig(f'Archivos/Saltos Guardados (NO TOCAR)/{carpeta_g}/velocidad_blanco.png', transparent=True)
        crear_log('Graficas de velocidad guardadas correctamente','INFO')
        plt.close(fig)
    except Exception as e:
        crear_log(f'Error al crear o guardar las graficas de velocidad: {e}','ERROR')

def grafica_aceleracion_mostrar(t, a_gauss, t0_x, t1_x, t0_y, t1_y, maximos, aceleracion_max):
    fig, ax = plt.subplots()
    ax.plot(t, a_gauss, label='Aceleración', color='green')
    ax.plot(t0_x, a_gauss[t0_y], 'x', label='T0', color='Blue')
    ax.plot(t1_x, a_gauss[t1_y], 'x', label='T1', color='Purple')
    ax.plot(t[maximos], aceleracion_max, 'x', label='Aceleración máx', color='Red')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Aceleracion (m/s²)')
    agregar_fondo(ax)
    ax.grid(True)
    ax.legend()
    try:
        crear_log(f'Guardando las garficas de aceleracion en {carpeta_g}...','INFO')
        plt.savefig(f'Archivos/Saltos Guardados (NO TOCAR)/{carpeta_g}/aceleracion.png', transparent=True)
        cambiar_ejes(ax)
        plt.savefig(f'Archivos/Saltos Guardados (NO TOCAR)/{carpeta_g}/aceleracion_blanco.png', transparent=True)
        crear_log('Graficas de aceleracion guardadas correctamente','INFO')
        plt.close(fig)
    except Exception as e:
        crear_log(f'Error al guardar las graficas de aceleracion: {e}','ERROR')

def grafica_fuerza_mostrar(t, F, maximos, f_max):
    fig, ax = plt.subplots()
    ax.plot(t, F, label='Fuerza', color='purple')
    ax.plot(t[maximos], f_max, 'x', label='Fuerza Máxima', color='Green')
    agregar_fondo(ax)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Fuerza (N)')
    ax.grid(True)
    ax.legend()
    try:
        crear_log(f'Guardando las garficas de fuerza en {carpeta_g}...','INFO')
        plt.savefig(f'Archivos/Saltos Guardados (NO TOCAR)/{carpeta_g}/fuerza.png', transparent=True)
        cambiar_ejes(ax)
        plt.savefig(f'Archivos/Saltos Guardados (NO TOCAR)/{carpeta_g}/fuerza_blanco.png', transparent=True)
        crear_log('Graficas de fuerza guardadas correctamente','INFO')
        plt.close(fig)
    except Exception as e:
        crear_log(f'Error al guardar las graficas de fuerza: {e}','ERROR')

def grafica_potencia_mostrar(t, P, maximos, p_max):
    fig, ax = plt.subplots()
    ax.plot(t, P, label='Potencia', color='orange')
    ax.plot(t[maximos], p_max, 'x', label='Potencia Máxima', color='Green')
    agregar_fondo(ax)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Potencia (W)')
    ax.grid(True)
    ax.legend()
    try:
        crear_log(f'Guardando las garficas de potencia en {carpeta_g}...','INFO')
        plt.savefig(f'Archivos/Saltos Guardados (NO TOCAR)/{carpeta_g}/potencia.png', transparent=True)
        cambiar_ejes(ax)
        plt.savefig(f'Archivos/Saltos Guardados (NO TOCAR)/{carpeta_g}/potencia_blanco.png', transparent=True)
        crear_log('Graficas de potencia guardadas correctamente','INFO')
        plt.close(fig)
    except Exception as e:
        crear_log(f'Error al guardar las graficas de potencia: {e}','ERROR')

def cambiar_ejes(ax):
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')

def agregar_fondo(ax):
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    rect = plt.Rectangle((xlim[0], ylim[0]), xlim[1] - xlim[0], ylim[1] - ylim[0], color='lightgray', zorder=0)
    ax.add_patch(rect)
    ax.set_facecolor('lightgray')

def crear_carpeta(carpeta):
    global carpeta_g
    fecha = time.localtime()
    fecha_str = time.strftime(f'%Y-%m-%d %H-%M-%S', fecha)
    carpeta_g = f'{carpeta} {fecha_str}'
    os.makedirs(f'Archivos/Saltos Guardados (NO TOCAR)/{carpeta_g}', exist_ok=True)
    crear_log(f'Creando la carpeta {carpeta_g}...','INFO')
    return carpeta_g