from guizero import App,Picture,PushButton,Text,Window,TextBox
import random as rd
import pygame as pg

def generar_columnas_filas(ventana,columnas,filas):
    for i in range(filas):
        #crear_text(ventana,text=f'{i}',color='black',grid=[0,i])
        ventana.tk.rowconfigure(i, weight=1)
    for u in range(columnas):
        ventana.tk.columnconfigure(u, weight=1)
        #crear_text(ventana,text=f'{i}',color='black',grid=[i,0])

def crear_button(master,text=None,command=None,image=None,grid=[0,0],visible=True, borde=False):
    if borde == True:
        button = PushButton(master, text=text, command=command, image=image, grid=grid, visible=visible)
    elif borde == False:
        button = PushButton(master, text=text, command=command, image=image, grid=grid, visible=visible)
        button.tk.config(border=0)
    button.tk.lift()

    return button
def crear_text(master,text=None,size=None,color=None,font=None,grid=[0,0],visible=True):
    kwargs = {"text": text, "grid": grid, "visible": visible}
    if size:
        kwargs["size"] = size
    if color:
        kwargs["color"] = color
    if font:
        kwargs["font"] = font
    text = Text(master, **kwargs)
    return text

def crear_textbox(master, width=None, grid=[0,0], visible=True, hide_text=False):
    textbox = TextBox(master, width=width, grid=grid, visible=visible, hide_text=hide_text)
    return textbox

def crear_window(master, title=None, width=None, height=None, layout=None, bg=None, visible=False, columnas=None, filas=None, full_screen=False):
    if width is not None and height is not None:
        window = Window(master, title=title, width=width, height=height, layout=layout, bg=bg, visible=visible)
    else:
        window = Window(master, title=title, layout=layout, bg=bg, visible=visible)
    if full_screen == True:
        window.full_screen = True
    elif full_screen == False:
        window.full_screen = False
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
    generar_columnas_filas(app,columnas,filas)
    return app

def musica(nombre, volumen):
    sound_file = nombre
    pg.mixer.music.set_volume(volumen)
    pg.mixer.music.load(sound_file)
    pg.mixer.music.Channel(0).play()

def sonido_click():
    pg.mixer.music.load('click.mp3')
    pg.mixer.music.set_volume(0.1)
    pg.mixer.music.play()