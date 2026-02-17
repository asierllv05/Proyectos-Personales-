from socket import *

def CONNECTION():
    dir_IP_servidor = '158.42.188.200'
    puerto_servidor = 64010
    dir_socket_servidor = (dir_IP_servidor,puerto_servidor)
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(dir_socket_servidor)
    return s

def HELLO(s):
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
    mensaje= 'GET_LEADERBOARD\r\n'
    s.send(mensaje.encode())
    respuesta = ''
    for i in range(10):
        i = s.recv(2048)
        respuesta=i.decode()
    return respuesta

