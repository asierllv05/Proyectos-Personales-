from socket import *
from funciones2_v4 import *
from funciones_v4 import *
from guizero import *
import time
import json
from requests.exceptions import Timeout
def CONNECTION():
    s = socket(AF_INET, SOCK_STREAM)
    return s

def HELLO(s):
    dir_IP_servidor = '158.42.188.200'
    puerto_servidor = 64010
    dir_socket_servidor = (dir_IP_servidor,puerto_servidor)
    s.connect(dir_socket_servidor)
    ip = s.getsockname()[0]
    mensaje = f'HELLO {ip}\r\n'
    s.send(mensaje.encode())
    recieve = s.recv(2048)

def USER(user,s):
    mensaje = f'USER {user}\r\n'
    s.send(mensaje.encode())
    recieve = (s.recv(2048)).decode()
    return recieve

def PASS(passw,s):
    mensaje = f'PASS {passw}\r\n'
    s.send(mensaje.encode())
    recieve = (s.recv(2048)).decode()
    return recieve

def GET_LEADERBOARD(s):
    s.settimeout(100)
    mensaje= 'GET_LEADERBOARD\r\n'
    s.send(mensaje.encode())
    rcv = str((s.recv(2048)).decode())
    return rcv

def SEND_DATA(s,ventana,argumentos_send_data):
    local_time = time.localtime()
    fecha = time.strftime(f'%d-%m-%Y', local_time)
    grupo = get_group(ventana)
    import funciones2_v4
    datos = {
        'nombre': funciones2_v4.nombre,
        'grupo_ProMu': grupo,
        'altura': funciones2_v4.altura,
        'fecha': fecha
    }
    try:
        datos_json = '{"nombre":"' + datos["nombre"] + '","grupo_ProMu":"' + datos["grupo_ProMu"] + '","altura":' + str(datos["altura"]) + ',"fecha":"' + datos["fecha"] + '"}'
        funciones2_v4.datos_cargar_salto.append(datos_json) 
        crear_log(f'Enviando los siguientes datos al servidor: {datos_json}...','INFO')
        s.send(('SEND_DATA ' + datos_json + '\r\n').encode())
        recieve = s.recv(2048).decode()
        argumentos_send_data[0].value = 'Se han enviado los datos correctamente'
        argumentos_send_data[1].value = f'Datos enviados: {datos_json}'
        argumentos_send_data[1].visible = True
        argumentos_send_data[2].disable()
        crear_log(f'Datos enviados correctamente','INFO')
        return recieve
    except Exception as e:
        argumentos_send_data[0].value = 'No se han enviado los datos correctamente'
        crear_log(f'Error al enviar los datos: {e}','ERROR')

def QUIT(s):
    msj= 'QUIT()\r\n'
    s.send(msj.encode())
    s.close()

def log_in(user_input, password_input, label, ventana_inicio, ventana_principal, leaderboard, jugar_online, cerrar_sesion, iniciar_sesion, s):
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

def cerrar_sesion(s, boton_iniciar_sesion, boton_jugar_online, boton_leaderboard, boton_cerrar_sesion):
    QUIT(s)
    boton_iniciar_sesion.show()
    boton_jugar_online.hide()
    boton_leaderboard.disable()
    boton_cerrar_sesion.disable()