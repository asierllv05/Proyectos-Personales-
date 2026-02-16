from guizero import App,PushButton,Text,Window,TextBox,warn,Picture
import cambiartemas
from funciones_arqred import *
from requests.exceptions import Timeout
import pygame
import os
import time
import json
import logging
music_vol = 0.05
voice_vol = 0.025
se_vol = 0.03
volumenes = [music_vol,voice_vol,se_vol]
# Funciones de creacion de witgets y ventanas
def crear_button(master, text=None, command=None, image=None, grid=[0,0], visible=True, borde=False, text_color=None):
    '''
    Crea un botón con las opciones especificadas y lo devuelve.

    Parámetros:
    - master: El widget maestro al que pertenecerá el botón.
    - text: El texto que se mostrará en el botón (por defecto, None).
    - command: La función que se ejecutará al hacer clic en el botón (por defecto, None).
    - image: La imagen que se mostrará en el botón (por defecto, None).
    - grid: La posición en la cuadrícula del master donde se colocará el botón (por defecto, [0,0]).
    - visible: Indica si el botón será visible al crearse (por defecto, True).
    - borde: Indica si el botón tendrá borde o no (por defecto, False).
    - text_color: El color del texto del botón (por defecto, None).

    Retorna:
    - button: El botón creado con las opciones especificadas.
    '''

    button = PushButton(master, text=text, command=command, image=image, grid=grid, visible=visible)
    if not borde:
        button.tk.config(border=0)
    button.tk.lift()
    if text_color is not None:
        button.text_color = text_color
    return button

def crear_text(master, text=None, size=None, color=None, grid=[0,0], visible=True):
    '''
    Crea un widget de texto con las opciones especificadas y lo devuelve.

    Parámetros:
    - master: El widget maestro al que pertenecerá el widget de texto.
    - text: El texto que se mostrará en el widget (por defecto, None).
    - size: El tamaño del texto (por defecto, None).
    - color: El color del texto (por defecto, None).
    - grid: La posición en la cuadrícula del master donde se colocará el widget de texto (por defecto, [0,0]).
    - visible: Indica si el widget de texto será visible al crearse (por defecto, True).

    Retorna:
    - text: El widget de texto creado con las opciones especificadas.
    '''

    argumentos = {'text': text, 'grid': grid, 'visible': visible}
    if size:
        argumentos['size'] = size
    if color:
        argumentos['color'] = color
    text = Text(master, **argumentos)
    return text

def crear_textbox(master, width=None, grid=[0,0], visible=True, hide_text=False, bloquear=False, blq_color=None):
    '''
    Crea un TextBox con las opciones especificadas y lo devuelve.

    Parámetros:
    - master: El widget maestro al que pertenecerá el TextBox.
    - width: La anchura del TextBox (por defecto, None).
    - grid: La posición en la cuadrícula del master donde se colocará el TextBox (por defecto, [0,0]).
    - visible: Indica si el TextBox será visible al crearse (por defecto, True).
    - hide_text: Indica si el texto dentro del TextBox será ocultado (por defecto, False).
    - bloquear: Indica si el TextBox estará bloqueado o no (por defecto, False).
    - blq_color: El color de fondo cuando el TextBox está bloqueado (por defecto, None).

    Retorna:
    - textbox: El TextBox creado con las opciones especificadas.
    '''

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
    '''
    Genera configuraciones de columnas y filas en una ventana dada.

    Parámetros:
    - ventana: La ventana a la que se aplicarán las configuraciones.
    - columnas: El número de columnas que se configurarán.
    - filas: El número de filas que se configurarán.
    '''
    for i in range(filas):
        ventana.tk.rowconfigure(i, weight=1)
    for u in range(columnas):
        ventana.tk.columnconfigure(u, weight=1)

def crear_window(master, title=None, width=None, height=None, layout=None, bg=None, visible=False, columnas=None, filas=None, full_screen=False):
    '''
    Crea una ventana con las opciones especificadas y la devuelve.

    Parámetros:
    - master: El widget maestro al que pertenecerá la ventana.
    - title: El título de la ventana (por defecto, None).
    - width: La anchura de la ventana (por defecto, None).
    - height: La altura de la ventana (por defecto, None).
    - layout: El diseño de la ventana (por defecto, None).
    - bg: El color de fondo de la ventana (por defecto, None).
    - visible: Indica si la ventana será visible al crearse (por defecto, False).
    - columnas: El número de columnas a configurar en la ventana (por defecto, None).
    - filas: El número de filas a configurar en la ventana (por defecto, None).
    - full_screen: Indica si la ventana se mostrará en pantalla completa o no (por defecto, False).

    Retorna:
    - window: La ventana creada con las opciones especificadas.
    '''
    
    window_kwargs = {'master': master, 'title': title, 'layout': layout, 'bg': bg, 'visible': visible}
    if width is not None and height is not None:
        window_kwargs.update({'width': width, 'height': height})
    window = Window(**window_kwargs)
    window.full_screen = full_screen
    window.tk.attributes('-toolwindow', True)
    generar_columnas_filas(window, columnas, filas)
    return window

def crear_app(title=None, width=None, height=None, layout=None, bg=None, visible=False, columnas=None, filas=None, full_screen=False):
    '''
    Crea una aplicación con las opciones especificadas y la devuelve.

    Parámetros:
    - title: El título de la aplicación (por defecto, None).
    - width: La anchura de la aplicación (por defecto, None).
    - height: La altura de la aplicación (por defecto, None).
    - layout: El diseño de la aplicación (por defecto, None).
    - bg: El color de fondo de la aplicación (por defecto, None).
    - visible: Indica si la aplicación será visible al crearse (por defecto, False).
    - columnas: El número de columnas a configurar en la aplicación (por defecto, None).
    - filas: El número de filas a configurar en la aplicación (por defecto, None).
    - full_screen: Indica si la aplicación se mostrará en pantalla completa o no (por defecto, False).

    Retorna:
    - app: La aplicación creada con las opciones especificadas.
    '''

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
    '''
    Ajusta el volumen de la música y devuelve el nuevo valor del volumen.

    Parámetros:
    - valor: El valor del volumen a ajustar.
    - music_vol: El valor actual del volumen de la música.

    Retorna:
    - music_vol: El nuevo valor del volumen de la música.
    '''

    global music_vol
    try:
        volumen = int(valor) / 1000
    except ValueError:
        crear_log('El valor proporcionado no es un número válido.','ERROR')
    try:
        pygame.mixer.Channel(2).set_volume(volumen)
    except IndexError:
        crear_log('El canal 2 no está disponible en el mezclador.','ERROR')
    music_vol = volumen
    crear_log(f'Se estableció el volumen de la musica en: {music_vol}','INFO')
    return music_vol

def ajustar_volumen_voice(valor):
    '''
    Ajusta el volumen de la voz y devuelve el nuevo valor del volumen.

    Parámetros:
    - valor: El valor del volumen a ajustar.
    - voice_vol: El valor actual del volumen de la voz.

    Retorna:
    - voice_vol: El nuevo valor del volumen de la voz.
    '''

    global voice_vol
    try:
        volumen = int(valor) / 500
    except ValueError:
        crear_log('El valor proporcionado no es un número válido.','ERROR')
    try:
        pygame.mixer.Channel(1).set_volume(volumen)
    except IndexError:
        crear_log('El canal 1 no está disponible en el mezclador.','ERROR')
    voice_vol = volumen
    crear_log(f'Se estableció el volumen de las voces en: {voice_vol}','INFO')
    return voice_vol

def ajustar_volumen_se(valor):
    '''
    Ajusta el volumen de los efectos de sonido y devuelve el nuevo valor del volumen.

    Parámetros:
    - valor: El valor del volumen a ajustar.
    - se_vol: El valor actual del volumen de los efectos de sonido.

    Retorna:
    - se_vol: El nuevo valor del volumen de los efectos de sonido.
    '''

    global se_vol
    try:
        volumen = int(valor) / 600
    except ValueError:
        crear_log('El valor proporcionado no es un número válido.','ERROR')
    try:
        pygame.mixer.Channel(3).set_volume(volumen)
    except IndexError:
        crear_log('El canal 3 no está disponible en el mezclador.','ERROR')
    se_vol = volumen
    crear_log(f'Se estableció el volumen de los efectos de sonido en: {se_vol}','INFO')
    return se_vol

def musica(cancion):
    '''
    Reproduce una canción de música con los volúmenes proporcionados.

    Parámetros:
    - cancion: La ruta de la canción a reproducir.
    - volumenes: Una lista de volúmenes para la música, la voz y los efectos de sonido, respectivamente.

    Notas:
    - La música se reproduce en el canal 2 del mezclador de sonido.
    - El primer elemento de la lista de volúmenes se utiliza para ajustar el volumen de la música.
    '''
    global volumenes
    try:
        pygame.mixer.music.load(cancion)
        crear_log(f'Reproduciendo: {cancion}','INFO')
    except pygame.error:
        crear_log(f'No se pudo cargar la canción: {cancion}','ERROR')
    try:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound(cancion), loops=-1)
    except pygame.error:
        crear_log(f'No se pudo reproducir la canción: {cancion}','ERROR')
    pygame.mixer.Channel(2).set_volume(volumenes[0])

def voces(nombre):
    '''
    Reproduce un archivo de sonido de voz con los volúmenes proporcionados.

    Parámetros:
    - nombre: La ruta del archivo de sonido de voz a reproducir.
    - volumenes: Una lista de volúmenes para la música, la voz y los efectos de sonido, respectivamente.

    Notas:
    - El archivo de sonido de voz se reproduce en el canal 1 del mezclador de sonido.
    - El segundo elemento de la lista de volúmenes se utiliza para ajustar el volumen de la voz.
    '''

    global volumenes
    try:
        pygame.mixer.music.load(nombre)
        crear_log(f'Reproduciendo: {nombre}','INFO')
    except pygame.error:
        crear_log(f'No se pudo cargar el archivo de sonido: {nombre}','ERROR')
    try:
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(nombre))
    except pygame.error:
        crear_log(f'No se pudo reproducir el archivo de sonido: {nombre}','ERROR')
    pygame.mixer.Channel(1).set_volume(volumenes[1])

def efectos(nombre):
    '''
    Reproduce un archivo de sonido de efectos con los volúmenes proporcionados.

    Parámetros:
    - nombre: La ruta del archivo de sonido de efectos a reproducir.
    - volumenes: Una lista de volúmenes para la música, la voz y los efectos de sonido, respectivamente.

    Notas:
    - El archivo de sonido de efectos se reproduce en el canal 3 del mezclador de sonido.
    - El tercer elemento de la lista de volúmenes se utiliza para ajustar el volumen de los efectos de sonido.
    '''

    global volumenes
    try:
        pygame.mixer.music.load(nombre)
        crear_log(f'Reproduciendo: {nombre}','INFO')
    except pygame.error:
        crear_log(f'No se pudo cargar el archivo de sonido: {nombre}','ERROR')
    try:
        pygame.mixer.Channel(3).play(pygame.mixer.Sound(nombre))
    except pygame.error:
        crear_log(f'No se pudo reproducir el archivo de sonido: {nombre}','ERROR')
    pygame.mixer.Channel(3).set_volume(volumenes[2])

#Movimientos entre ventanas
def cambiar_ventanas(ocultar_ventana, ventana_a_mostrar, ventana_a_ocultar=None):
    '''
    Cambia la visibilidad de las ventanas especificadas.

    Parámetros:
    - ocultar_ventana: Booleano que indica si se debe mostrar o no la ventana especificada.
    - ventana_a_mostrar: La ventana que se debe mostrar u ocultar dependiendo del valor de mostrar_ventana.
    - ventana_a_ocultar: La ventana que se debe ocultar si mostrar_ventana es True (por defecto, None).

    Notas:
    - Si mostrar_ventana es True, ventana_a_mostrar se mostrará y ventana_a_ocultar, si está especificada, se ocultará.
    - Si mostrar_ventana es False, ventana_a_mostrar se mostrará y ventana_a_ocultar, si está especificada, se mostrará por debajo.
    '''

    if ocultar_ventana:
        ventana_a_mostrar.show()
        if ventana_a_ocultar:
            ventana_a_ocultar.hide()
    else:
        if ventana_a_ocultar:
            ventana_a_ocultar.show()
        ventana_a_mostrar.show()

def cerrar(app):
    '''
    Cierra la aplicación y finaliza el uso de Pygame.

    Parámetros:
    - app: La aplicación que se va a cerrar.

    Notas:
    - Intenta finalizar Pygame y captura cualquier error que ocurra, imprimiendo un mensaje si es necesario.
    - Espera 0.5 segundos antes de destruir la aplicación.
    '''

    try:
        pygame.quit()
    except pygame.error as e:
        crear_log(f'Error al cerrar Pygame: {e}','ERROR')
    time.sleep(0.5)
    app.destroy()

# Funciones iniciar sesion
def alternar_visibilidad_contraseña(tb1):
    '''
    Alterna la visibilidad del texto en un TextBox.

    Parámetros:
    - tb1: El TextBox cuyo texto se va a alternar entre visible y oculto.

    Notas:
    - Si el texto está actualmente visible, se ocultará. Si está oculto, se hará visible.
    '''

    tb1.hide_text = not tb1.hide_text

#Funciones main menu
def comprobar_archivo(witgets):
    '''
    Comprueba la existencia de un archivo de Excel y actualiza los widgets proporcionados en consecuencia.

    Parámetros:
    - widgets: Los widgets que se actualizarán según el resultado de la comprobación.

    Notas:
    - Si el archivo se encuentra, se actualizan los widgets para indicar que el archivo fue encontrado:
        - Se deshabilitan los widgets que tienen el método `disable`.
        - Se cambia el fondo de los widgets que tienen el atributo `tk` y se usa `config`.
        - Se hace visible cualquier widget con el atributo `visible`.
        - Se cambia la imagen de los widgets que tienen el atributo `image`.
        - Se establece el valor de los widgets que tienen el atributo `value` a 'Archivo encontrado'.
        - Se cambia el color del texto de los widgets que tienen el atributo `text_color` a verde.
        - Se establece la posición en la cuadrícula de los widgets que tienen el atributo `grid` a [10, 2].

    - Si el archivo no se encuentra, se actualizan los widgets para indicar que el archivo no fue encontrado:
        - Se establece el valor de los widgets que tienen el atributo `value` a 'Archivo no encontrado'.
        - Se cambia el color del texto de los widgets que tienen el atributo `text_color` a rojo.
        - Se establece la posición en la cuadrícula de los widgets que tienen el atributo `grid` a [10, 3].
        - Se hace visible cualquier widget con el atributo `visible`.
    '''

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
    '''
    Verifica si un valor dado es un número entero y si tiene una longitud de hasta 3 caracteres.

    Parámetros:
    - numero: El valor a verificar.

    Retorna:
    - True si el valor es un número entero y su longitud es de 3 caracteres o menos.
    - False en caso contrario.
    '''

    if len(numero) <= 3:
        try:
            int(numero)
            return True
        except (ValueError, TypeError):
            return False
    else:
        return False

def comprobar_masa(witgets):
    '''
    Comprueba la validez de la masa ingresada y actualiza los widgets proporcionados en consecuencia.

    Parámetros:
    - argumentos_comprobar_masa: Una lista de widgets a actualizar basada en la validez de la masa ingresada.
    - argumentos_comprobar_masa[0]: El widget que contiene el valor de la masa a verificar.
    - argumentos_comprobar_masa[1]: El widget a habilitar si la masa es válida.
    - argumentos_comprobar_masa[3]: El widget que muestra el mensaje de resultado.

    Notas:
    - Si la masa ingresada es válida (es un número entero de hasta 3 caracteres):
        - Deshabilita los widgets que tienen el método `disable`.
        - Cambia el fondo de los widgets que tienen el atributo `tk` y se usa `config`.
        - Hace visibles los widgets que tienen el atributo `visible`.
        - Establece el valor de `argumentos_comprobar_masa[3]` a 'Listo para representar'.
        - Cambia el color del texto de `argumentos_comprobar_masa[3]` a un color especificado en `cambiartemas.colores[1]`.
        - Establece la posición en la cuadrícula de `argumentos_comprobar_masa[3]` a [10, 5].
        - Habilita y hace visible `argumentos_comprobar_masa[1]`.

    - Si la masa ingresada no es válida:
        - Establece el valor de `argumentos_comprobar_masa[3]` a 'Masa ingresada incorrecta'.
        - Cambia el color del texto de `argumentos_comprobar_masa[3]` a rojo.
        - Establece la posición en la cuadrícula de `argumentos_comprobar_masa[3]` a [10, 6].
        - Hace visible `argumentos_comprobar_masa[3]`.
    '''

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

def log_in(user_input, password_input, label, ventana_inicio, ventana_principal, leaderboard, jugar_online, cerrar_sesion, iniciar_sesion, s):
    '''
    Realiza el proceso de inicio de sesión y actualiza los widgets según el resultado.

    Parámetros:
    - user_input: El widget de entrada que contiene el nombre de usuario.
    - password_input: El widget de entrada que contiene la contraseña.
    - label: El widget de etiqueta que muestra mensajes de estado.
    - ventana_inicio: La ventana de inicio que se muestra al iniciar sesión correctamente.
    - ventana_principal: La ventana principal que se oculta al iniciar sesión correctamente.
    - leaderboard: El widget de la tabla de clasificación que se habilita al iniciar sesión correctamente.
    - jugar_online: El widget que permite jugar en línea y se muestra al iniciar sesión correctamente.
    - cerrar_sesion: El widget del botón de cerrar sesión que se habilita al iniciar sesión correctamente.
    - iniciar_sesion: El widget del botón de iniciar sesión que se oculta al iniciar sesión correctamente.
    - s: La sesión actual del usuario.

    Notas:
    - Intenta autenticar al usuario usando las funciones `USER` y `PASS` con la sesión proporcionada.
    - Si la autenticación falla, muestra un mensaje de error en `label`.
    - Si la autenticación es exitosa:
        - Muestra `ventana_inicio` y oculta `ventana_principal`.
        - Habilita `leaderboard` y `cerrar_sesion`.
        - Muestra `jugar_online` y oculta `iniciar_sesion`.
        - Limpia los valores de `user_input` y `password_input`.
    - Si ocurre un error de tiempo de espera, muestra una advertencia indicando que no se pudo establecer la conexión con el servidor.
    '''

    user = user_input.value
    password = password_input.value
    try:
        response_user = USER(user, s)
        response_password = PASS(password, s)
        
        if response_user != '200 ESPERANDO PASS\r\n' or response_password != '200 ESPERANDO COMANDO\r\n':
            label.value = 'Usuario o contraseña incorrecto'
        else:
            ventana_inicio.show()
            ventana_principal.hide()
            leaderboard.enable()
            iniciar_sesion.hide()
            jugar_online.show()
            cerrar_sesion.enable()
            user_input.value = ''
            password_input.value = ''
    except Timeout:
        warn('Fallo de conexión', 'No se pudo establecer conexión con el servidor.\nInténtelo de nuevo más tarde.')

def crear_leaderboard(s, ventana):
    '''
    Crea y muestra el leaderboard en la ventana proporcionada.

    Parámetros:
    - s: La sesión utilizada para obtener los datos del leaderboard.
    - ventana: La ventana en la que se mostrará el leaderboard.

    Notas:
    - Utiliza la función `GET_LEADERBOARD` para obtener los datos del leaderboard.
    - Si no hay datos, muestra un mensaje indicando que no hay datos en el leaderboard.
    - Si se encuentran datos válidos, los procesa y muestra en la ventana:
        - Descodifica los datos JSON y verifica que contienen las claves esperadas ('ranking', 'nombre', 'altura', 'fecha').
        - Crea una imagen y un texto para cada entrada en el leaderboard.
        - Distribuye los datos en columnas y filas, cambiando de columna después de cinco entradas.
    - Maneja y muestra errores de decodificación JSON y otros posibles errores en el proceso.
    '''

    try:
        linea = ''
        fila = 2
        contador_botones = 1

        while linea != '202 NO MORE RECORDS\r\n':
            linea = GET_LEADERBOARD(s)

            if linea.startswith('201'):
                no_hay_leaderboard = Text(ventana, text='No hay datos en el leaderboard', size=20, grid=[25, 10])
            elif linea.startswith('202'):
                break
            elif linea.startswith('200'):
                continue
            elif linea.startswith('{'):
                try:
                    dic = json.loads(linea)
                    crear_log(f'Decodificado JSON: {dic}','INFO')
                except json.JSONDecodeError as e:
                    crear_log(f'Error de decodificación JSON: {e}','ERROR')
                # Verificar si las claves existen en el diccionario
                if all(k in dic for k in ("ranking", "nombre", "altura", "fecha")):
                    columna = 10 if contador_botones <= 5 else 30
                    if contador_botones == 6:
                        fila = 2
                    try:
                        foto = Picture(ventana, image=f'Archivos/Temas/{contador_botones}.png', grid=[columna, fila,])
                        text = crear_text(ventana, text=f'{dic["ranking"]}. {dic["nombre"]} | {dic["altura"]} | {dic["fecha"]}', grid=[columna + 1, fila])
                        crear_log(f'Creado botón y texto para {dic["nombre"]} en columna {columna}, fila {fila}','INFO')
                        fila += 2
                        contador_botones += 1
                    except Exception as e:
                        crear_log(f'Error creando botones/texto: {e}','ERROR')
                else:
                    crear_log('El JSON no contiene las claves esperadas','ERROR')
    except Exception as e:
        crear_log(f'Error obteniendo leaderboard: {e}','ERROR')

def comprobar_conexion(boton_iniciar_sesion):
    '''
    Comprueba la conexión con el servidor y actualiza el estado del botón de inicio de sesión.

    Parámetros:
    - boton_iniciar_sesion: El botón de inicio de sesión que se habilita o deshabilita en función del estado de la conexión.

    Retorna:
    - conexion: El objeto de conexión si se establece con éxito.

    Notas:
    - Intenta establecer una conexión utilizando la función `CONNECTION` y establece un tiempo de espera de 1 segundo.
    - Envía un mensaje `HELLO` para verificar la conexión.
    - Si la conexión es exitosa:
        - Habilita `boton_iniciar_sesion` y elimina su borde.
    - Si se produce un `TimeoutError`:
        - Muestra una advertencia indicando el fallo de conexión y desactiva `boton_iniciar_sesion`, añadiendo un borde.
    - Si ocurre cualquier otra excepción:
        - Muestra una advertencia con el mensaje de error inesperado y desactiva `boton_iniciar_sesion`, añadiendo un borde.
    '''

    try:
        conexion = CONNECTION()
        conexion.settimeout(1)
        HELLO(conexion)
        boton_iniciar_sesion.enable()
        boton_iniciar_sesion.tk.config(border=0)
        return conexion
    except TimeoutError:
        warn('Fallo de conexión', 'No se pudo establecer conexión con el servidor.\nSe han desactivado todas las funcionalidades que requieren de este.')
        boton_iniciar_sesion.disable()
        boton_iniciar_sesion.tk.config(border=1)
    except Exception as e:
        warn('Error inesperado', f'Ha ocurrido un error inesperado: {e}')
        boton_iniciar_sesion.disable()
        boton_iniciar_sesion.tk.config(border=1)

def cambiar_boton_volver_config(boton, ocultar_ventana, ventana_a_mostrar, ventana_a_ocultar):
    '''
    Cambia el comando del botón para volver a la ventana de configuración.

    Parámetros:
    - boton: El botón cuyo comando se va a actualizar.
    - ventana_config: La ventana de configuración a la que se debe volver.
    - ventana: La ventana actual que se debe ocultar.

    Notas:
    - Actualiza el comando del botón para que, al ser presionado, oculte `ventana` y muestre `ventana_config` usando la función `cambiar_ventanas`.
    '''

    boton.update_command(cambiar_ventanas, (ocultar_ventana, ventana_a_mostrar, ventana_a_ocultar))

def cerrar_sesion(s, boton_iniciar_sesion, boton_jugar_online, boton_leaderboard, boton_cerrar_sesion):
    '''
    Cierra la sesión del usuario y actualiza el estado de los botones relacionados con la sesión.

    Parámetros:
    - s: La conexión del servidor que se cerrará.
    - boton_iniciar_sesion: El botón de inicio de sesión que se mostrará.
    - boton_jugar_online: El botón de jugar en línea que se ocultará.
    - boton_leaderboard: El botón de la tabla de clasificación que se deshabilitará.
    - boton_cerrar_sesion: El botón de cerrar sesión que se deshabilitará.

    Notas:
    - Cierra la conexión con el servidor utilizando la función `QUIT`.
    - Muestra `boton_iniciar_sesion` y oculta `boton_jugar_online`.
    - Deshabilita `boton_leaderboard` y `boton_cerrar_sesion`.
    '''

    QUIT(s)
    boton_iniciar_sesion.show()
    boton_jugar_online.hide()
    boton_leaderboard.disable()
    boton_cerrar_sesion.disable()

def setup_logging():
    fecha = time.localtime()
    fecha_str = time.strftime(f'%Y-%m-%d %H-%M-%S', fecha)
    log_file = f'Archivos/Logs/log_jumpz_{fecha_str}.log'
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

        