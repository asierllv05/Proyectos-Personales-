
from calculos_fisica_v4 import *
import calculos_fisica_v4
import cambiartemas
from guizero import *
from funciones import sonido_click,crear_textbox,crear_button,crear_text,mover,cerrar,cambiar_boton_volver_config
import time
import os
import json
import re
import shutil
import tkinter as tk
from tkinter import filedialog
from PIL import Image
global altura, nombre
altura = ''
nombre = ''

def mostrar_garfica(garfica,ventana):
    try:
        ventana.image = f'Archivos/Saltos Guardados (NO TOCAR)/{calculos_fisica_v4.carpeta_g}/{garfica}.png'
    except:
        ventana.image = 'Archivos/Temas/grafico_pred.png'

def mostrar_garfica_cs(carpeta,garfica,ventana):
    try:
        ventana.image = f'Archivos/Saltos Guardados (NO TOCAR)/{carpeta}/{garfica}.png'
    except:
        ventana.image = 'Archivos/Temas/grafico_pred.png'

def mostrar_datos(tb):
    with open(f'Archivos/Saltos Guardados (NO TOCAR)/{calculos_fisica_v4.carpeta_g}/datos.json', 'r') as file:
        datos = json.load(file)
    n = 0
    for valor in datos.items():
        tb[n].value = valor[1]
        n +=1




def get_name(ventana):
    nombre = question('Nombre', 'Indique su nombre: ', master=ventana)
    if nombre:
        nombre_limpio = re.sub(r'\s|\d', '', nombre)
        datos_cargar_salto.append(nombre_limpio)
        return nombre_limpio

def principal(ventana,archivo, m):
    global altura, nombre
    nombre = get_name(ventana)
    if nombre:
        t, a = importar_datos(archivo)
        a_gauss, v_gauss = filtros(a,t)
        t0_x, t0_y = tiempo_min(a_gauss, t)
        t1_x, t1_y = tiempo_max(a_gauss, t)
        tia = tiempo_vuelo(a_gauss, t)
        altura = altura_max(tia)
        a_salto, maximos = acel_max(a_gauss, t0_y, t1_y)
        F = fuerza(a_gauss, m)
        f_max = fuerza_max(a_salto, m)
        P = potencia(F, v_gauss)
        p_max = potencia_en_salto(f_max, v_gauss, maximos)
        crear_carpeta(nombre)
        grafica_velocidad_mostrar(t, v_gauss)
        grafica_aceleracion_mostrar(t, a_gauss, t0_x, t1_x, t0_y, t1_y, maximos, a_salto)
        grafica_fuerza_mostrar(t, F, maximos, f_max)
        grafica_potencia_mostrar(t, P, maximos, p_max)
        datos = {
        "t0": f'{t0_x:.2f} s',
        "t1": f'{t1_x:.2f} s',
        "tia": f'{tia:.2f} s',
        "alt_max": f'{altura:.2f} mm',
        "amax": f'{a_salto:.2f} m/s²',
        "f_max": f'{f_max:.2f} N',
        "p_max": f'{p_max:.2f} W'
        }
        datos_cargar_salto.append(m)
        datos_cargar_salto.append(t0_x)
        datos_cargar_salto.append(t1_x)
        datos_cargar_salto.append(tia)
        datos_cargar_salto.append(altura)
        datos_cargar_salto.append(a_salto)
        datos_cargar_salto.append(f_max)
        datos_cargar_salto.append(p_max)
        ruta_datos = f'Archivos/Saltos Guardados (NO TOCAR)/{calculos_fisica_v4.carpeta_g}/datos.json'
        if not os.path.exists(ruta_datos):
            with open(ruta_datos, "w") as archivo:
                json.dump({}, archivo)
        with open(ruta_datos, "r") as archivo:
            datos_exist = json.load(archivo)
        datos_exist.update(datos)
        with open(ruta_datos, "w") as archivo:
            json.dump(datos_exist, archivo)

        ruta_cargar = f'Archivos/Saltos Guardados (NO TOCAR)/{calculos_fisica_v4.carpeta_g}/datos_cargar.txt'
        cadena = ','.join(str(elemento) for elemento in datos_cargar_salto)
        if not os.path.exists(ruta_cargar):
            with open(ruta_cargar, "w") as archivo:
                archivo.write(cadena)
        return t, a_gauss, v_gauss, t0_x, t0_y, t1_x, t1_y, tia, altura, a_salto, maximos, F, P, f_max,p_max,nombre
        # Crear carpeta y calcular datos
    else:
        warn('Error','No se proporcionó un nombre.',ventana)




def get_group(ventana):
    return question('Grupo', 'Indique su grupo: ',master=ventana)

def SEND_DATA(s,ventana,argumentos_send_data):
    global nombre,alt
    local_time = time.localtime()
    fecha = time.strftime(f'%d-%m-%Y', local_time)
    grupo = get_group(ventana)
    datos = {
        "nombre": nombre,
        "grupo_ProMu": grupo,
        "altura": altura,
        "fecha": fecha
    }
    try:
        datos_json = '{"nombre":"' + datos["nombre"] + '","grupo_ProMu":"' + datos["grupo_ProMu"] + '","altura":' + str(datos["altura"]) + ',"fecha":"' + datos["fecha"] + '"}'
        datos_cargar_salto.append(datos_json) 
        s.send(("SEND_DATA " + datos_json + "\r\n").encode())
        recieve = s.recv(2048).decode()
        argumentos_send_data[0].value = 'Se han enviado los datos correctamente'
        argumentos_send_data[1].value = f'Datos enviados: {datos_json}'
        argumentos_send_data[1].visible = True
        argumentos_send_data[2].disable()
        return recieve
    except:
        argumentos_send_data[0].value = 'No se han enviado los datos correctamente'

boton_pulsado = ''
def registrar_boton(boton_nombre):
    global boton_pulsado
    boton_pulsado = boton_nombre
    return boton_pulsado

def borrar_carpeta_offline():
    if boton_pulsado == 'offline':
        if len(calculos_fisica_v4.carpeta_g)>0:
            ruta_carpeta = f'Archivos/Saltos Guardados (NO TOCAR)/{calculos_fisica_v4.carpeta_g}'
            try:
                if os.path.exists(ruta_carpeta):
                    shutil.rmtree(ruta_carpeta)
            except Exception as e:
                print(f"Error al borrar la carpeta: {e}")


def representar(ventana,argumento_representar,tb):
    global boton_pulsado
    archivo = argumento_representar[0].value
    m = int(argumento_representar[1].value)
    principal(ventana,archivo,m)
    mostrar_datos(tb)
    argumento_representar[3].disable()
    argumento_representar[4].visible = False
    argumento_representar[5].enable()
    argumento_representar[6].enable()
    argumento_representar[7].enable()
    argumento_representar[8].enable()
    argumento_representar[9].enable()
    if boton_pulsado != 'offline':
        argumento_representar[4].value = 'Listo para enviar'
        argumento_representar[4].visible = True
        argumento_representar[2].enable()
        argumento_representar[2].visible = True
        argumento_representar[6].enable()
        argumento_representar[7].enable()
        argumento_representar[8].enable()
        argumento_representar[9].enable()

def obtener_carpetas(directorio):
    # Obtener todas las carpetas en el directorio
    carpetas = [nombre for nombre in os.listdir(directorio) if os.path.isdir(os.path.join(directorio, nombre))]
    
    # Obtener las fechas de creación de las carpetas
    carpetas_con_fechas = [(carpeta, os.path.getctime(os.path.join(directorio, carpeta))) for carpeta in carpetas]
    
    # Ordenar las carpetas por fecha de creación, de más reciente a más antigua
    carpetas_ordenadas = sorted(carpetas_con_fechas, key=lambda x: x[1], reverse=True)
        
    return carpetas_ordenadas

lista_nodestacados_cargar_salto = []
lista_textos_cargar_salto = []
lista_destacados_cargar_salto = []
def crear_botones(directorio, app, ventana_hide, ventana, config, menuprincipal,boton_temas_configuracion,boton):
    carpetas_ordenadas = obtener_carpetas(directorio)
    
    if len(carpetas_ordenadas) == 0:
        label_no_hay_saltos = Text(ventana_hide, text="No hay saltos disponibles", size=30, grid=[25,10])
        label_no_hay_saltos.text_color = cambiartemas.colores[1]
        lista_textos_cargar_salto.append(label_no_hay_saltos)
    
    if len(carpetas_ordenadas) > 0:
        seccion_destacados = Box(ventana_hide, layout="grid", grid=[0, 0, 51, 2])
        label_destacados = Text(seccion_destacados, text="Últimos 3 destacados", grid=[0, 0, 3, 1])
        label_destacados.text_color = cambiartemas.colores[1]
        lista_textos_cargar_salto.append(label_destacados)
        
        for i in range(min(3, len(carpetas_ordenadas))):
            carpeta, _ = carpetas_ordenadas[i]
            destacados = PushButton(seccion_destacados, text=carpeta, command=lambda c=carpeta: [sonido_click(), cargar_salto(c, ventana, app, ventana_hide, config, menuprincipal,boton_temas_configuracion,boton), mover(1, ventana_hide, ventana),cambiar_boton_volver_config(boton,config,ventana),boton_temas_configuracion.disable()], grid=[i, 1], width=25)
            destacados.bg = "lightyellow"
            destacados.text_size = 14
            lista_destacados_cargar_salto.append(destacados)
        Box(ventana_hide, width="fill", height=20, grid=[0, 2])
    
    if len(carpetas_ordenadas) > 3:
        seccion_otros = Box(ventana_hide, layout="grid", grid=[0, 1, 51, 20])
        label_otras_carpetas = Text(seccion_otros, text="Otras carpetas", grid=[0, 0, 3, 1])
        label_otras_carpetas.text_color = cambiartemas.colores[1]
        lista_textos_cargar_salto.append(label_otras_carpetas)
        
        for u in range(3, len(carpetas_ordenadas)):
            carpeta, _ = carpetas_ordenadas[u]
            no_destacados = PushButton(seccion_otros, text=carpeta, command=lambda c=carpeta: [sonido_click(), cargar_salto(c, ventana, app, ventana_hide, config, menuprincipal,boton_temas_configuracion,boton), mover(1, ventana_hide, ventana),cambiar_boton_volver_config(boton,config,ventana),boton_temas_configuracion.disable()], grid=[(u-3) % 3, (u-3) // 3 + 1], width=25)
            no_destacados.text_size = 14
            no_destacados.text_color = cambiartemas.colores[1]
            lista_nodestacados_cargar_salto.append(no_destacados)
    return lista_nodestacados_cargar_salto,lista_textos_cargar_salto, lista_destacados_cargar_salto

def cargar_salto(carpeta,ventana,app,volver,config,menuprincipal,boton_temas_configuracion,boton):
    with open(f'Archivos/Saltos Guardados (NO TOCAR)/{carpeta}/datos_cargar.txt', 'r') as archivo:
        lineas = archivo.readlines()
    datos = []
    for linea in lineas:
        valores = linea.strip().split(',')
        datos.extend(valores)

    box_mainmenu_grafico_cs = Box(ventana,layout='grid',grid=[10,5,40,14])
    grafico_cs = Picture(box_mainmenu_grafico_cs, image=f'Archivos/Saltos Guardados (NO TOCAR)/{carpeta}/aceleracion.png', grid=[0,0])
    grafico_cs.resize(960,720)

    label_excel_mainmenu_cs = crear_text(ventana,text='Nombre del archivo ingrasado:',grid=[13,0],color = cambiartemas.colores[1])
    tb_excel_mainmenu_cs = crear_textbox(ventana,width=70,grid=[13,1],bloquear=True,blq_color=cambiartemas.colores[0])
    label_masa_mainmenu_cs = crear_text(ventana,text='Masa ingresada:',grid=[13,2],color = cambiartemas.colores[1])
    tb_masa_mainmenu_cs = crear_textbox(ventana,width=30,grid=[13,3],bloquear=True,blq_color=cambiartemas.colores[0])

    box_mainmenu_options_cs = Box(ventana,layout='grid',grid=[0,21,50,1])
    boton_configuracion_mainmenu_cs = crear_button(box_mainmenu_options_cs,image=cambiartemas.botones[4],command=lambda:[sonido_click(),mover(0,ventana,config)],grid=[0,21])
    boton_casa_mainmenu_cs = crear_button(box_mainmenu_options_cs,image=cambiartemas.botones[5],command=lambda:[sonido_click(),mover(1,ventana,menuprincipal),boton_temas_configuracion.enable(),cambiar_boton_volver_config(boton,config,menuprincipal)],grid=[6,21])
    boton_volver_mainmenu_cs = crear_button(box_mainmenu_options_cs,image=cambiartemas.botones[6],command=lambda:[sonido_click(),mover(1,ventana,volver),boton_temas_configuracion.enable(),cambiar_boton_volver_config(boton,config,volver)],grid=[12,21])
    boton_cerrar_mainmenu_cs = crear_button(box_mainmenu_options_cs,image=cambiartemas.botones[7],command=lambda:[sonido_click(),cerrar(app),boton_temas_configuracion.enable()],grid=[19,21])
    
    boton_aceleracion_cs = crear_button(ventana,image=cambiartemas.botones[0],command=lambda:[sonido_click(),mostrar_garfica_cs(carpeta,'aceleracion',grafico_cs)],grid=[1,8],borde=True)
    boton_velocidad_cs = crear_button(ventana,image=cambiartemas.botones[1],command=lambda:[sonido_click(),mostrar_garfica_cs(carpeta,'velocidad',grafico_cs)],grid=[1,10],borde=True)
    boton_fuerza_cs = crear_button(ventana,image=cambiartemas.botones[2],command=lambda:[sonido_click(),mostrar_garfica_cs(carpeta,'fuerza',grafico_cs)],grid=[1,12],borde=True)
    boton_potencia_cs = crear_button(ventana,image=cambiartemas.botones[3],command=lambda:[sonido_click(),mostrar_garfica_cs(carpeta,'potencia',grafico_cs)],grid=[1,14],borde=True)
    texto_t0_cs = crear_text(ventana,text='Inicio del vuelo:',grid=[3,8],color = cambiartemas.colores[1])
    texto_t1_cs = crear_text(ventana,text='Final del vuelo:',grid=[3,9],color = cambiartemas.colores[1])
    texto_tia_cs = crear_text(ventana,text='Tiempo de vuelo:',grid=[3,10],color = cambiartemas.colores[1])
    texto_altmax_cs = crear_text(ventana,text='Altura maxima:',grid=[3,11],color = cambiartemas.colores[1])
    texto_acelmax_cs = crear_text(ventana,text='Aceleracion en el salto:',grid=[3,12],color = cambiartemas.colores[1])
    texto_f_cs = crear_text(ventana,text='Fuerza del salto:',grid=[3,13],color = cambiartemas.colores[1])
    texto_p_cs = crear_text(ventana,text='Potencia del salto:',grid=[3,14],color = cambiartemas.colores[1])
    tb_t0_cs = crear_textbox(ventana,grid=[5,8],bloquear=True,blq_color=cambiartemas.colores[0])
    tb_t1_cs = crear_textbox(ventana,grid=[5,9],bloquear=True,blq_color=cambiartemas.colores[0])
    tb_tia_cs = crear_textbox(ventana,grid=[5,10],bloquear=True,blq_color=cambiartemas.colores[0])
    tb_altmax_cs = crear_textbox(ventana,grid=[5,11],bloquear=True,blq_color=cambiartemas.colores[0])
    tb_acelmax_cs = crear_textbox(ventana,grid=[5,12],bloquear=True,blq_color=cambiartemas.colores[0])
    tb_f_cs = crear_textbox(ventana,grid=[5,13],bloquear=True,blq_color=cambiartemas.colores[0])
    tb_p_cs = crear_textbox(ventana,grid=[5,14],bloquear=True,blq_color=cambiartemas.colores[0])

    tb_excel_mainmenu_cs.value = valores[1]+'.xlsx'
    tb_masa_mainmenu_cs.value = valores[2]+' Kg'
    tb_t0_cs.value = "{:.2f}".format(float(valores[3]))+' s'
    tb_t1_cs.value = "{:.2f}".format(float(valores[4]))+' s'
    tb_tia_cs.value = "{:.2f}".format(float(valores[5]))+' s'
    tb_altmax_cs.value = "{:.2f}".format(float(valores[6]))+' mm'
    tb_acelmax_cs.value = "{:.2f}".format(float(valores[7]))+' m/s²'
    tb_f_cs.value = "{:.2f}".format(float(valores[8]))+' N'
    tb_p_cs.value = "{:.2f}".format(float(valores[9]))+' W'

def guardar_imagen(imagen):
    global carpeta_g
    ruta = Image.open(f'Archivos/Saltos Guardados (NO TOCAR)/{calculos_fisica_v4.carpeta_g}/{imagen}.png')
    guardar_grafica_sel = tk.Tk()
    guardar_grafica_sel.withdraw()

    archivo_guardar = filedialog.asksaveasfilename(
        defaultextension=f'{imagen}.png',
        filetypes=[('PNG files', '*.png'), ('All files', '*.*')],
        title='Guardar imagen como',
        initialfile=f'{imagen}'
    )

    if archivo_guardar:
        ruta.save(archivo_guardar, "PNG")
        guardar_grafica_sel.destroy()

def cambiar_boton_guardar(boton,grafic):
        boton.update_command(command=lambda: guardar_imagen(grafic))