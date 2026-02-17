from guizero import App,PushButton,Text,Window,TextBox,warn, Picture
import cambiartemas
from funciones_arqred import *
import pygame
import os
import time
import json
music_vol = 0.05
voice_vol = 0.025
se_vol = 0.03
volumenes = [music_vol,voice_vol,se_vol]
#Funciones de creacion de app, window, botones, textos y textboxs
def crear_button(master, text=None, command=None, image=None, grid=[0,0], visible=True, borde=False, text_color=None):
    button = PushButton(master, text=text, command=command, image=image, grid=grid, visible=visible)
    if not borde:
        button.tk.config(border=0)
    button.tk.lift()
    if text_color is not None:
        button.text_color = text_color
    return button

def crear_text(master,text=None,size=None,color=None,grid=[0,0],visible=True):
    argumentos = {"text": text, "grid": grid, "visible": visible}
    if size:
        argumentos["size"] = size
    if color:
        argumentos["color"] = color
    text = Text(master, **argumentos)
    return text

def crear_textbox(master, width=None, grid=[0,0], visible=True, hide_text=False, bloquear=False, blq_color=None):
    textbox = TextBox(master, width=width, grid=grid, visible=visible, hide_text=hide_text)
    textbox.bg = (210, 112, 20)
    if bloquear == False:
        textbox.enable()
    elif bloquear == True:
        textbox.disable()
        if blq_color is not None:
            textbox.tk.config(disabledbackground=blq_color)
        else:
            blq_color = None
    return textbox

def generar_columnas_filas(ventana,columnas,filas):
    for i in range(filas):
        ventana.tk.rowconfigure(i, weight=1)
    for u in range(columnas):
        ventana.tk.columnconfigure(u, weight=1)

def crear_window(master, title=None, width=None, height=None, layout=None, bg=None, visible=False, columnas=None, filas=None, full_screen=False):
    if width is not None and height is not None:
        window = Window(master, title=title, width=width, height=height, layout=layout, bg=bg, visible=visible)
    else:
        window = Window(master, title=title, layout=layout, bg=bg, visible=visible)
    if full_screen == True:
        window.full_screen = True
    elif full_screen == False:
        window.full_screen = False
    window.tk.attributes("-toolwindow", True)
    generar_columnas_filas(window,columnas,filas)
    return window

def crear_app(title=None, width=None, height=None, layout=None, bg=None, visible=False, columnas=None, filas=None, full_screen=False):
    if width is not None and height is not None:
        app = App(title=title, width=width, height=height, layout=layout, bg=bg, visible=visible)
    else:
        app = App(title=title, layout=layout, bg=bg, visible=visible)
    if full_screen == True:
        app.full_screen = True
    elif full_screen == False:
        app.full_screen = False
    app.tk.attributes("-toolwindow", True)
    generar_columnas_filas(app,columnas,filas)
    return app

#Manejo musica y voces
def ajustar_volumen_music(valor):
    global music_vol
    volumen = int(valor) / 1000
    pygame.mixer.Channel(2).set_volume(volumen)
    music_vol = volumen
    return music_vol

def ajustar_volumen_voice(valor):
    global voice_vol
    volumen = int(valor) / 500
    pygame.mixer.Channel(1).set_volume(volumen)
    voice_vol = volumen
    return voice_vol

def ajustar_volumen_se(valor):
    global se_vol
    volumen = int(valor) / 600
    pygame.mixer.Channel(3).set_volume(volumen)
    se_vol = volumen
    return se_vol

def musica(cancion):
    global volumenes
    sound_file = cancion
    pygame.mixer.music.load(sound_file)
    pygame.mixer.Channel(2).play(pygame.mixer.Sound(sound_file),loops=-1)
    pygame.mixer.Channel(2).set_volume(volumenes[0])

def voces(nombre):
    global volumenes
    sound_file = nombre
    pygame.mixer.music.load(sound_file)
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(sound_file))
    pygame.mixer.Channel(1).set_volume(volumenes[1])

def sonido_click():
    global volumenes
    sound_file = 'Archivos/Audios/Sonidos/click.mp3'
    pygame.mixer.music.load(sound_file)
    pygame.mixer.Channel(3).play(pygame.mixer.Sound(sound_file))
    pygame.mixer.Channel(3).set_volume(volumenes[2])


#Movimientos entre ventanas
def mover(hide, actual, ventana):
    if hide == 1:
        ventana.show()
        actual.hide()
    else:
        ventana.show()

def cerrar(app):
    pygame.quit()
    time.sleep(0.5)
    app.destroy()

def cerrar_ventana(ventana):
    ventana.hide()

def abrir_ventana(ventana):
    ventana.show()


# Funciones iniciar sesion
def mostrar_contraseña(tb1):
    if tb1.hide_text == True:
        tb1.hide_text=False
    else:
        tb1.hide_text=True

#Funciones main menu

def comprobar_archivo(argumentos_comprobar_archivo):
    n_excel = argumentos_comprobar_archivo[0].value
    ruta = f'Excels/{n_excel}.xlsx'
    if os.path.isfile(ruta):
        argumentos_comprobar_archivo[0].disable()
        argumentos_comprobar_archivo[0].tk.config(disabledbackground=cambiartemas.colores[0])
        argumentos_comprobar_archivo[3].visible = False
        argumentos_comprobar_archivo[2].visible = True
        argumentos_comprobar_archivo[1].visible = True
        argumentos_comprobar_archivo[4].visible = True
        argumentos_comprobar_archivo[5].image = 'Archivos/Temas/grafico_pred.png'
        argumentos_comprobar_archivo[6].value = 'Archivo encontrado'
        argumentos_comprobar_archivo[6].text_color = 'green'
        argumentos_comprobar_archivo[6].grid = [10, 2]
        argumentos_comprobar_archivo[6].visible = True
    else:
        argumentos_comprobar_archivo[6].value = 'Archivo no encontrado'
        argumentos_comprobar_archivo[6].text_color = 'red'
        argumentos_comprobar_archivo[6].grid = [10, 3]
        argumentos_comprobar_archivo[6].visible = True


def es_numero(numero):
    try:
        int(numero) 
        if len (numero)<= 3:
            return True
        else:
            return False
    except (ValueError, TypeError): 
        return False
    
def comprobar_masa(argumentos_comprobar_masa):
    num = argumentos_comprobar_masa[0].value
    if es_numero(num):
        argumentos_comprobar_masa[0].disable()
        argumentos_comprobar_masa[0].tk.config(disabledbackground=cambiartemas.colores[0])
        argumentos_comprobar_masa[2].visible = False
        argumentos_comprobar_masa[3].value = 'Listo para representar'
        argumentos_comprobar_masa[3].text_color = cambiartemas.colores[1]
        argumentos_comprobar_masa[3].grid = [10, 5]
        argumentos_comprobar_masa[3].visible = True
        argumentos_comprobar_masa[1].enable()
        argumentos_comprobar_masa[1].visible = True
    else:
        argumentos_comprobar_masa[3].value = 'Masa ingresada incorrecta'
        argumentos_comprobar_masa[3].text_color = 'red'
        argumentos_comprobar_masa[3].grid = [10, 6]
        argumentos_comprobar_masa[3].visible = True


def log_in(s,tb1,tb2,label1,ventana1,ventana2,leaderboard,jugar_online,cerrar_sesion,iniciar_sesion):
    user = tb1.value
    password = tb2.value
    
    try:
        responce_user = USER(user, s)
        response_password = PASS(password, s)
        
        if responce_user != '200 ESPERANDO PASS\r\n' or response_password != '200 ESPERANDO COMANDO\r\n':
            label1.value = 'Usuario o contraseña incorrecto'
        else:
            ventana1.show()
            ventana2.hide()
            leaderboard.enable()
            iniciar_sesion.hide()
            jugar_online.show()
            cerrar_sesion.enable()
            tb1.value = ''
            tb2.value = ''
    except timeout:
        warn('Fallo de conexión', 'No se pudo establecer conexión con el servidor.\nInténtelo de nuevo más tarde.')

import json
def crear_leaderboard(s, ventana):
    linea= ''
    fila = 2
    contador_botones = 1
    while linea != '202 NO MORE RECORDS\r\n':
        try:
            linea = GET_LEADERBOARD(s)
            if linea.startswith('201'):
                no_hay_leaderboard = Text(ventana, text="No hay datos en el leaderboard", size=20, grid=[25, 10])
            elif linea.startswith('202'):
                linea = '202 NO MORE RECORDS\r\n'
            elif linea.startswith('200'):
                continue
            elif linea.startswith('{'):
                try:
                    dic = json.loads(linea)
                    print(f"Decodificado JSON: {dic}")  # Añadir depuración para JSON decodificado
                except json.JSONDecodeError as e:
                    print(f"Error de decodificación JSON: {e}")
                    linea == '202 NO MORE RECORDS\r\n'
                
                # Verificar si las claves existen en el diccionario
                if all(k in dic for k in ('ranking', 'nombre', 'altura', 'fecha')):
                    columna = 10 if contador_botones <= 5 else 30
                    if contador_botones == 6:
                        fila = 2
                    
                    try:
                        foto = Picture(ventana, image=f'Archivos/Temas/{contador_botones}.png', grid=[columna, fila,])
                        text = crear_text(ventana, text=f"{dic['ranking']}. {dic['nombre']} | {dic['altura']} | {dic['fecha']}", grid=[columna + 1, fila])
                        print(f"Creado botón y texto para {dic['nombre']} en columna {columna}, fila {fila}")  # Depuración 
                        fila += 2
                        contador_botones += 1
                    except Exception as e:
                        print(f"Error creando botones/texto: {e}")

                else:
                    print("El JSON no contiene las claves esperadas")
                    linea == '202 NO MORE RECORDS\r\n'
        except Exception as e:
            # Manejo de errores en caso de fallo en la obtención del leaderboard
            print(f"Error obteniendo leaderboard: {e}")
            





def comprobar_conexion(iniciar_sesion):
    try:
        s = CONNECTION()
        s.settimeout(1)
        HELLO(s)
        iniciar_sesion.enable()
        iniciar_sesion.tk.config(border=0)
        return s
    except timeout:
        warn('Fallo de conexión', 'No se pudo establecer conexión con el servidor.\nSe han desactivado todas las funcionalidades que requieren de este mismo.')
        iniciar_sesion.disable()
        iniciar_sesion.tk.config(border=1)
    except Exception as e:
        warn('Error inesperado', f'Ha ocurrido un error inesperado: {e}')
        iniciar_sesion.disable()
        iniciar_sesion.tk.config(border=1)

def cambiar_boton_volver_config(boton,ventana_config,ventana):
    boton.update_command(mover, (1,ventana_config,ventana))

def cerrar_sesion(s,iniciar_sesion,jugar_online,leaderboard,cerrar_sesion):
    QUIT(s)
    iniciar_sesion.show()
    jugar_online.hide()
    leaderboard.disable()
    cerrar_sesion.disable()