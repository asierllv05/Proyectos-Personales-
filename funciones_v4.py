from guizero import App,PushButton,Text,Window,TextBox
import cambiartemas
import pygame
import os
import time
import logging
music_vol = 0.5
voice_vol = 0.025
se_vol = 0.03
volumenes = [music_vol,voice_vol,se_vol]
# Funciones de creacion de witgets y ventanas
def crear_button(master, text=None, command=None, image=None, grid=[0,0], visible=True, borde=False, text_color=None):
    button = PushButton(master, text=text, command=command, image=image, grid=grid, visible=visible)
    if not borde:
        button.tk.config(border=0)
    button.tk.lift()
    if text_color is not None:
        button.text_color = text_color
    return button

def crear_text(master, text=None, size=None, color=None, grid=[0,0], visible=True):
    argumentos = {'text': text, 'grid': grid, 'visible': visible}
    if size:
        argumentos['size'] = size
    if color:
        argumentos['color'] = color
    text = Text(master, **argumentos)
    return text

def crear_textbox(master, width=None, grid=[0,0], visible=True, hide_text=False, bloquear=False, blq_color=None):
    textbox = TextBox(master, width=width, grid=grid, visible=visible, hide_text=hide_text)
    textbox.bg = (210, 112, 20)
    if bloquear:
        textbox.disable()
        if blq_color is not None:
            textbox.tk.config(disabledbackground=blq_color)
    else:
        textbox.enable()
    return textbox

def generar_columnas_filas(ventana,columnas,filas):
    if columnas is not None and filas is not None:
        try:
            columnas=int(columnas)
            filas=int(filas)
            if columnas and filas:
                for i in range(filas):
                    ventana.tk.rowconfigure(i, weight=1)
                for u in range(columnas):
                    ventana.tk.columnconfigure(u, weight=1)
        except:
            ventana.tk.rowconfigure(1, weight=1)
            ventana.tk.columnconfigure(1, weight=1)

    else:
        ventana.tk.rowconfigure(1, weight=1)
        ventana.tk.columnconfigure(1, weight=1)    

def crear_window(master, title=None, width=None, height=None, layout=None, bg=None, visible=False, columnas=None, filas=None, full_screen=False):
    window_kwargs = {'master': master, 'title': title, 'layout': layout, 'bg': bg, 'visible': visible}
    if width is not None and height is not None:
        window_kwargs.update({'width': width, 'height': height})
    window = Window(**window_kwargs)
    window.full_screen = full_screen
    window.tk.attributes('-toolwindow', True)
    generar_columnas_filas(window, columnas, filas)
    return window

def crear_app(title=None, width=None, height=None, layout=None, bg=None, visible=False, columnas=None, filas=None, full_screen=False):
    app_kwargs = {'title': title, 'layout': layout, 'bg': bg, 'visible': visible}
    if width is not None and height is not None:
        app_kwargs.update({'width': width, 'height': height})
    app = App(**app_kwargs)
    app.full_screen = full_screen
    app.tk.attributes('-toolwindow', True)
    generar_columnas_filas(app, columnas, filas)
    return app


#Manejo musica, voces y efectos de sonido
def ajustar_volumen_music(valor):
    global music_vol
    try:
        valor = float(valor)
        volumen = valor / 100
    except ValueError:
        crear_log('El valor proporcionado no es un número válido.','ERROR')
        volumen=music_vol
    try:
        pygame.mixer.Channel(2).set_volume(volumen)
    except IndexError:
        crear_log('El canal 2 no está disponible en el mezclador.','ERROR')
    music_vol = volumen
    crear_log(f'Se estableció el volumen de la musica en: {music_vol}','INFO')
    return music_vol

def ajustar_volumen_voice(valor):
    global voice_vol
    try:
        valor = float(valor)
        volumen = valor / 500
    except ValueError:
        crear_log('El valor proporcionado no es un número válido.','ERROR')
        volumen=voice_vol
    try:
        pygame.mixer.Channel(1).set_volume(volumen)
    except IndexError:
        crear_log('El canal 1 no está disponible en el mezclador.','ERROR')
    voice_vol = volumen
    crear_log(f'Se estableció el volumen de las voces en: {voice_vol}','INFO')
    return voice_vol

def ajustar_volumen_se(valor):
    global se_vol
    try:
        valor=float(valor)
        volumen = valor / 600
    except ValueError:
        crear_log('El valor proporcionado no es un número válido.','ERROR')
        volumen=se_vol
    try:
        pygame.mixer.Channel(3).set_volume(volumen)
    except IndexError:
        crear_log('El canal 3 no está disponible en el mezclador.','ERROR')
    se_vol = volumen
    crear_log(f'Se estableció el volumen de los efectos de sonido en: {se_vol}','INFO')
    return se_vol

def musica(cancion=None):
    global volumenes
    try:
        if cancion:
            pygame.mixer.music.load(cancion)
            crear_log(f'Reproduciendo: {cancion}','INFO')
        else:
            pygame.mixer.Channel(2).stop()
    except pygame.error:
        crear_log(f'No se pudo cargar la canción: {cancion}','ERROR')
    try:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound(cancion), loops=-1)
    except pygame.error:
        crear_log(f'No se pudo reproducir la canción: {cancion}','ERROR')
    pygame.mixer.Channel(2).set_volume(volumenes[0])

def voces(nombre=None):
    global volumenes
    try:
        if nombre:
            pygame.mixer.music.load(nombre)
            crear_log(f'Reproduciendo: {nombre}','INFO')
        else:
            pygame.mixer.Channel(1).stop()
    except pygame.error:
        crear_log(f'No se pudo cargar el archivo de sonido: {nombre}','ERROR')
    try:
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(nombre))
    except pygame.error:
        crear_log(f'No se pudo reproducir el archivo de sonido: {nombre}','ERROR')
    pygame.mixer.Channel(1).set_volume(volumenes[1])

def efectos(nombre=None):
    global volumenes
    try:
        if nombre:
            pygame.mixer.music.load(nombre)
            crear_log(f'Reproduciendo: {nombre}','INFO')
        else:
            pygame.mixer.Channel(3).stop()
    except pygame.error:
        crear_log(f'No se pudo cargar el archivo de sonido: {nombre}','ERROR')
    try:
        pygame.mixer.Channel(3).play(pygame.mixer.Sound(nombre))
    except pygame.error:
        crear_log(f'No se pudo reproducir el archivo de sonido: {nombre}','ERROR')
    pygame.mixer.Channel(3).set_volume(volumenes[2])
#Movimientos entre ventanas
def cambiar_ventanas(ocultar_ventana, ventana_a_mostrar, ventana_a_ocultar=None):
    if ocultar_ventana:
        ventana_a_mostrar.show()
        if ventana_a_ocultar:
            ventana_a_ocultar.hide()
    else:
        if ventana_a_ocultar:
            ventana_a_ocultar.show()
        ventana_a_mostrar.show()

def cerrar(app):
    try:
        pygame.quit()
    except pygame.error as e:
        crear_log(f'Error al cerrar Pygame: {e}','ERROR')
    time.sleep(0.5)
    app.destroy()

# Funciones iniciar sesion
def alternar_visibilidad_contraseña(tb1):
    tb1.hide_text = not tb1.hide_text

#Funciones main menu
def comprobar_archivo(witgets):
    n_excel = witgets[0].value
    ruta = f'Excels/{n_excel}.xlsx'
    if os.path.isfile(ruta):
        witgets[0].disable()
        witgets[0].tk.config(disabledbackground=cambiartemas.colores[0])
        witgets[3].visible = False
        witgets[2].visible = True
        witgets[1].visible = True
        witgets[4].visible = True
        witgets[5].image = 'Archivos/Temas/grafico_pred.png'
        witgets[6].value = 'Archivo encontrado'
        witgets[6].text_color = 'green'
        witgets[6].grid = [10, 2]
        witgets[6].visible = True
    else:
        witgets[6].value = 'Archivo no encontrado'
        witgets[6].text_color = 'red'
        witgets[6].grid = [10, 3]
        witgets[6].visible = True

def es_numero(numero):
    numero = str(numero)
    if len(numero) <= 3:
        try:
            int(numero)
            return True
        except (ValueError, TypeError):
            return False
    else:
        return False

def comprobar_masa(witgets):
    num = witgets[0].value
    if es_numero(num):
        witgets[0].disable()
        witgets[0].tk.config(disabledbackground=cambiartemas.colores[0])
        witgets[2].visible = False
        witgets[3].value = 'Listo para representar'
        witgets[3].text_color = cambiartemas.colores[1]
        witgets[3].grid = [10, 5]
        witgets[3].visible = True
        witgets[1].enable()
        witgets[1].visible = True
    else:
        witgets[3].value = 'Masa ingresada incorrecta'
        witgets[3].text_color = 'red'
        witgets[3].grid = [10, 6]
        witgets[3].visible = True

def cambiar_boton_volver_config(boton, ocultar_ventana, ventana_a_mostrar, ventana_a_ocultar):
    boton.update_command(cambiar_ventanas, (ocultar_ventana, ventana_a_mostrar, ventana_a_ocultar))

def setup_logging(nombre):
    fecha = time.localtime()
    fecha_str = time.strftime(f'%Y-%m-%d %H-%M-%S', fecha)
    log_file = f'Archivos/Logs/log_{nombre}_{fecha_str}.log'
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler(log_file),
                                  logging.StreamHandler()])
    
def crear_log(message,level):
    if level == 'INFO':
        logging.info(message)
    elif level == 'DEBUG':
        logging.debug(message)
    elif level == 'WARNING':
        logging.warning(message)
    elif level == 'ERROR':
        logging.error(message)
    elif level == 'CRITICAL':
        logging.critical(message)

def activar_desactivar_boton(boton,modo):
    if modo == True:
        boton.enable()
    elif modo == False:
        boton.disable()