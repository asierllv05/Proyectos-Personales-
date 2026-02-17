from funciones_arqred import *
from funciones import *
from cambiartemas import *
from mate_promu2 import *
import mate_promu2
import pygame as pg

pg.init()
'''-----------------------------INICIO-----------------------------'''
inicio_app = crear_app(title='Inicio / JumpZ',width=1920,height=1080,bg=(233,124,21),layout='grid',visible=True,columnas=51,filas=21,full_screen=True)
inicio_app.icon = 'Archivos/Temas/icon.png'
fondo_iniciar_juego = Picture(inicio_app, image='Archivos/Temas/Goku/imagen.png',grid=[0,0,51,21])

#Inicio
'''-----------------------------MENU PRINCIPAL-----------------------------'''
menuprincipal_ventana = crear_window(inicio_app, 'Menú Principal / JumpZ', 1920, 1080, 'grid', (233,124,21), visible=False, columnas=51, filas=21, full_screen=True)
fondo_menu_principal = Picture(menuprincipal_ventana, image='Archivos/Temas/Goku/goku_fondo.png', grid=[0,0,51,21])
fondo_menu_principal.resize(width=1920, height=1080)

#Menu Principal
'''-----------------------------INICAR SESION-----------------------------'''
iniciarsesion_ventana = crear_window(menuprincipal_ventana, 'Iniciar Sesión / JumpZ', 350, 460, 'grid', (233,124,21), visible=False, columnas=11, filas=15, full_screen=False)

#Menu Principal
'''-----------------------------LEADERBOARD-----------------------------'''
leaderboard_ventana = crear_window(menuprincipal_ventana, 'LeaderBoard / JumpZ',1920, 1080, 'grid', (233,124,21), visible=False, columnas=51, filas=21, full_screen=True)

#Menu Principal
'''-----------------------------MAIN MENU-----------------------------'''
mainmenu_ventana = crear_window(menuprincipal_ventana, 'MainMenu / JumpZ', 1920, 1080, 'grid', (233,124,21), visible=False, columnas=51, filas=21, full_screen=True)

#Menu Principal
'''---------------------------CARGAR SALTO---------------------------'''
cargarsalto_ventana = crear_window(menuprincipal_ventana, 'Cargar Salto / JumpZ', 1920, 1080, 'grid', (233,124,21), visible=False, columnas=51, filas=21, full_screen=True)
mainmenu_cs_ventana = crear_window(menuprincipal_ventana, 'MainMenu Cs / JumpZ', 1920, 1080, 'grid', (233,124,21), visible=False, columnas=51, filas=21, full_screen=True)


'''---------------------------CONFIGURACION---------------------------'''
configuracion = crear_window(menuprincipal_ventana, 'Configuracion / JumpZ', 460, 460, 'grid', (233,124,21), visible=False, columnas=5, filas=3, full_screen=False)

#Configuracion
'''-----------------------------CREDITOS-----------------------------'''
creditos_ventana = crear_window(configuracion, 'Créditos / JumpZ', 1280, 720, 'grid', (233,124,21), visible=False, columnas=2, filas=4, full_screen=False)
creditos_foto = Picture(creditos_ventana,image='Archivos/Temas/creditos.jpg',grid=[0,0])
#Configuracion
'''-----------------------------TEMAS-----------------------------'''
temas_ventana = crear_window(configuracion, 'Temas / JumpZ', 400, 300, 'grid', (100, 100, 100), visible=False, columnas=2, filas=4, full_screen=False)

#Configuracion
'''-----------------------------VOLUMENES-----------------------------'''
volumenes_ventana = crear_window(configuracion, 'Volumenes / JumpZ', 700, 200, 'grid', (233,124,21), visible=False, columnas=3, filas=2, full_screen=False)











'''-----------------------------WIDGETS-----------------------------'''
'''-----------------------------INICIO-----------------------------'''
boton_iniciar_juego = crear_button(inicio_app,image='Archivos/Temas/Goku/iniciar_juego.png',command=lambda:[sonido_click(),mover(1,inicio_app,menuprincipal_ventana),cambiar_boton_volver_config(boton_volver_configuracion_p,configuracion,menuprincipal_ventana)],grid=[25, 20],borde=True)


'''-----------------------------CONFIGURACION-----------------------------'''
boton_temas_configuracion = crear_button(configuracion,image='Archivos/Temas/Goku/temas.png',command=lambda:[sonido_click(),mover(0,configuracion,temas_ventana)],grid=[1, 0])
boton_creditos_configuracion = crear_button(configuracion,image='Archivos/Temas/Goku/creditos.png',command=lambda:[sonido_click(),mover(0,configuracion,creditos_ventana)],grid=[3, 0])
boton_volumen_configuracion = crear_button(configuracion,image='Archivos/Temas/Goku/volumenes.png',command=lambda:[sonido_click(),mover(0,configuracion,volumenes_ventana)],grid=[1, 1])
boton_cerrar_sesion_configuracion = crear_button(configuracion,image='Archivos/Temas/Goku/cerrar_sesion.png',command=lambda:[sonido_click(),cerrar_sesion(s,boton_iniciar_sesion_menuprincipal,boton_jugar_online_menuprincipal,boton_leaderboard_menuprincipal,boton_cerrar_sesion_configuracion),mover(1,mainmenu_ventana,menuprincipal_ventana)],grid=[3, 1])
boton_cerrar_sesion_configuracion.disable()
boton_volver_configuracion_p = crear_button(configuracion,image='Archivos/Temas/flecha_p.png',command=lambda:[sonido_click(),mover(1,configuracion,menuprincipal_ventana)],grid=[2,2])


'''-----------------------------TEMAS-----------------------------'''
boton_goku_temas = crear_button(temas_ventana,image='Archivos/Temas/Goku/goku.png',command=lambda:[cambiar_tema('Goku',lista_text_box,lista_labels_cambiar_blanconegro,lista_botones_texto_cambiar_blanconegro,lista_botones_cambiar_blanconegro,lista_botones_imagen_cambiar_temas,lista_ventanas,mate_promu2.lista_nodestacados_cargar_salto,mate_promu2.lista_textos_cargar_salto,mate_promu2.lista_destacados_cargar_salto),cerrar_ventana(temas_ventana),voces('Archivos/Audios/Voces/frase_goku.mp3'),musica('Archivos/Audios/Musicas/GOKU_CANCION.mp3')],grid=[0, 0])
boton_goku_temas.bg = (233,124,21)
boton_feezer_temas = crear_button(temas_ventana,image='Archivos/Temas/Freezer/freezer.png',command=lambda:[cambiar_tema('Freezer',lista_text_box,lista_labels_cambiar_blanconegro,lista_botones_texto_cambiar_blanconegro,lista_botones_cambiar_blanconegro,lista_botones_imagen_cambiar_temas,lista_ventanas,mate_promu2.lista_nodestacados_cargar_salto,mate_promu2.lista_textos_cargar_salto,mate_promu2.lista_destacados_cargar_salto),cerrar_ventana(temas_ventana),voces('Archivos/Audios/Voces/frase_freezer.mp3'),musica('Archivos/Audios/Musicas/FREEZER_CANCION.mp3')],grid=[1, 0])
boton_feezer_temas.bg = (200, 180, 230)
boton_piccolo_temas = crear_button(temas_ventana,image='Archivos/Temas/Piccolo/piccolo.png',command=lambda:[cambiar_tema('Piccolo',lista_text_box,lista_labels_cambiar_blanconegro,lista_botones_texto_cambiar_blanconegro,lista_botones_cambiar_blanconegro,lista_botones_imagen_cambiar_temas,lista_ventanas,mate_promu2.lista_nodestacados_cargar_salto,mate_promu2.lista_textos_cargar_salto,mate_promu2.lista_destacados_cargar_salto),cerrar_ventana(temas_ventana),voces('Archivos/Audios/Voces/frase_piccolo.mp3'),musica('Archivos/Audios/Musicas/PICCOLO_CANCION.mp3')],grid=[0, 1])
boton_piccolo_temas.bg = (119,221,119)
boton_boo_temas = crear_button(temas_ventana,image='Archivos/Temas/Boo/boo.png',command=lambda:[cambiar_tema('Boo',lista_text_box,lista_labels_cambiar_blanconegro,lista_botones_texto_cambiar_blanconegro,lista_botones_cambiar_blanconegro,lista_botones_imagen_cambiar_temas,lista_ventanas,mate_promu2.lista_nodestacados_cargar_salto,mate_promu2.lista_textos_cargar_salto,mate_promu2.lista_destacados_cargar_salto),cerrar_ventana(temas_ventana),voces('Archivos/Audios/Voces/frase_buu.mp3'),musica('Archivos/Audios/Musicas/BUU_CANCION.mp3')],grid=[1, 1])
boton_boo_temas.bg = (255, 200, 228)
boton_vegeta_temas = crear_button(temas_ventana,image='Archivos/Temas/Vegeta/vegeta.png',command=lambda:[cambiar_tema('Vegeta',lista_text_box,lista_labels_cambiar_blanconegro,lista_botones_texto_cambiar_blanconegro,lista_botones_cambiar_blanconegro,lista_botones_imagen_cambiar_temas,lista_ventanas,mate_promu2.lista_nodestacados_cargar_salto,mate_promu2.lista_textos_cargar_salto,mate_promu2.lista_destacados_cargar_salto),cerrar_ventana(temas_ventana),voces('Archivos/Audios/Voces/frase_vegeta.mp3'),musica('Archivos/Audios/Musicas/VEGETA_CANCION.mp3')],grid=[0, 2])
boton_vegeta_temas.bg = (25, 68, 131)
boton_bulma_temas = crear_button(temas_ventana,image='Archivos/Temas/Bulma/bulma.png',command=lambda:[cambiar_tema('Bulma',lista_text_box,lista_labels_cambiar_blanconegro,lista_botones_texto_cambiar_blanconegro,lista_botones_cambiar_blanconegro,lista_botones_imagen_cambiar_temas,lista_ventanas,mate_promu2.lista_nodestacados_cargar_salto,mate_promu2.lista_textos_cargar_salto,mate_promu2.lista_destacados_cargar_salto),cerrar_ventana(temas_ventana),voces('Archivos/Audios/Voces/frase_bulma.mp3'),musica('Archivos/Audios/Musicas/BULMA_CANCION.mp3')],grid=[1, 2])
boton_bulma_temas.bg = (126,197,172)
boton_claro_temas = crear_button(temas_ventana,image='Archivos/Temas/Claro/claro.png',command=lambda:[cambiar_tema('Claro',lista_text_box,lista_labels_cambiar_blanconegro,lista_botones_texto_cambiar_blanconegro,lista_botones_cambiar_blanconegro,lista_botones_imagen_cambiar_temas,lista_ventanas,mate_promu2.lista_nodestacados_cargar_salto,mate_promu2.lista_textos_cargar_salto,mate_promu2.lista_destacados_cargar_salto),cerrar_ventana(temas_ventana),musica('Archivos/Audios/Musicas/CLARO_CANCION.mp3')],grid=[0, 3])
boton_claro_temas.bg = (188, 188, 188)
boton_oscuro_temas = crear_button(temas_ventana,image='Archivos/Temas/Oscuro/oscuro.png',command=lambda:[cambiar_tema('Oscuro',lista_text_box,lista_labels_cambiar_blanconegro,lista_botones_texto_cambiar_blanconegro,lista_botones_cambiar_blanconegro,lista_botones_imagen_cambiar_temas,lista_ventanas,mate_promu2.lista_nodestacados_cargar_salto,mate_promu2.lista_textos_cargar_salto,mate_promu2.lista_destacados_cargar_salto),cerrar_ventana(temas_ventana),musica('Archivos/Audios/Musicas/OSCURO_CANCION.mp3')],grid=[1, 3])
boton_oscuro_temas.bg = (25, 25, 25)


'''-----------------------------MENU PRINCIPAL-----------------------------'''
box_options_menuprincipal = Box(menuprincipal_ventana,layout='grid',grid=[0,21,51,1])
boton_configuracion_menuprincipal = crear_button(box_options_menuprincipal,image='Archivos/Temas/config.png',command=lambda:[sonido_click(),abrir_ventana(configuracion)],grid=[0,21])
boton_casa_menuprincipal = crear_button(box_options_menuprincipal,image='Archivos/Temas/home.png',grid=[6,21])
boton_volver_menuprincipal = crear_button(box_options_menuprincipal,image='Archivos/Temas/flecha.png',command=lambda:[sonido_click(),mover(1,menuprincipal_ventana,inicio_app)],grid=[12,21])
boton_cerrar_menuprincipal = crear_button(box_options_menuprincipal,image='Archivos/Temas/x.png',command=lambda:[sonido_click(),cerrar(inicio_app)],grid=[19,21])

logo_menu_principal = Picture(menuprincipal_ventana, image='Archivos/Temas/Goku/logo.png', grid=[4,2])
boton_iniciar_sesion_menuprincipal = crear_button(menuprincipal_ventana,image='Archivos/Temas/Goku/iniciar_sesion_pj.png',command=lambda:[sonido_click(),mover(0,menuprincipal_ventana,iniciarsesion_ventana)],grid=[4, 7])
boton_jugar_online_menuprincipal = crear_button(menuprincipal_ventana,image='Archivos/Temas/Goku/jugar_online.png',command=lambda:[sonido_click(),restablecer_valores_iniciales(argumentos_restablecer_main_menu),mover(1,menuprincipal_ventana,mainmenu_ventana),registrar_boton('online'),cambiar_boton_volver_config(boton_volver_configuracion_p, configuracion, mainmenu_ventana)],grid=[4, 7])
boton_jugar_online_menuprincipal.hide()
boton_jugar_offline_menuprincipal = crear_button(menuprincipal_ventana,image='Archivos/Temas/Goku/jugar_offline.png',command=lambda:[sonido_click(),restablecer_valores_iniciales(argumentos_restablecer_main_menu),mover(1,menuprincipal_ventana,mainmenu_ventana),registrar_boton('offline'),cambiar_boton_volver_config(boton_volver_configuracion_p, configuracion, mainmenu_ventana)],grid=[4, 9])
boton_cargar_salto_menuprincipal = crear_button(menuprincipal_ventana,image='Archivos/Temas/Goku/cargar_salto.png',command=lambda:[sonido_click(),crear_botones('Archivos/Saltos Guardados (NO TOCAR)',inicio_app,cargarsalto_ventana,mainmenu_cs_ventana,configuracion,menuprincipal_ventana,boton_temas_configuracion,boton_volver_configuracion_p),mover(1,menuprincipal_ventana,cargarsalto_ventana),registrar_boton('cargar'),cambiar_boton_volver_config(boton_volver_configuracion_p, configuracion, cargarsalto_ventana)],grid=[4, 11])
boton_leaderboard_menuprincipal = crear_button(menuprincipal_ventana,image='Archivos/Temas/Goku/leaderboard.png',command=lambda:[sonido_click(),crear_leaderboard(s, leaderboard_ventana),mover(1,menuprincipal_ventana,leaderboard_ventana),cambiar_boton_volver_config(boton_volver_configuracion_p,configuracion,leaderboard_ventana)],grid=[4, 13])
boton_leaderboard_menuprincipal.disable()

'''-----------------------------INICAR SESION-----------------------------'''
label_iniciar_sesion = crear_text(iniciarsesion_ventana,text='Inicio de sesion',size=20,color='black',grid=[5,1])
label_user_iniciarsesion = crear_text(iniciarsesion_ventana,text='Ingrese su nombre de usuario',color='black',grid=[5,3])
tb_user_iniciarsesion = crear_textbox(iniciarsesion_ventana,grid=[5,4],width=20)
label_password_iniciarsesion = crear_text(iniciarsesion_ventana,text='Ingrese su contraseña',color='black',grid=[5,7])
tb_password_iniciarsesion = crear_textbox(iniciarsesion_ventana,grid=[5,8],width=20,hide_text=True)
boton_showpassword_iniciarsesion = crear_button(iniciarsesion_ventana,image='Archivos/Temas/ojo.png',command=lambda:[sonido_click(),mostrar_contraseña(tb_password_iniciarsesion)],grid=[6,8])
espacio_iniciarsesion = crear_text(iniciarsesion_ventana,'yyyy',color=(233,124,21),grid=[1,8])
label_status_iniciarsesion = crear_text(iniciarsesion_ventana,text = "",color = "red",grid=[5,9])
boton_iniciarsesion = crear_button(iniciarsesion_ventana,image='Archivos/Temas/Goku/iniciar_sesion.png',command=lambda:[sonido_click(),log_in(s,tb_user_iniciarsesion, tb_password_iniciarsesion, label_status_iniciarsesion, menuprincipal_ventana, iniciarsesion_ventana,boton_leaderboard_menuprincipal,boton_jugar_online_menuprincipal,boton_cerrar_sesion_configuracion,boton_iniciar_sesion_menuprincipal)],grid=[5, 10])


'''-----------------------------LEADERBOARD-----------------------------'''
leaderboard = Picture(leaderboard_ventana, image='Archivos/Temas/Goku/leaderboard.png',grid=[25,1])

box_leaderboard_options = Box(leaderboard_ventana,layout='grid',grid=[0,21,50,1])
boton_configuracion_mainmenu = crear_button(box_leaderboard_options,image='Archivos/Temas/config.png',command=lambda:[sonido_click(),abrir_ventana(configuracion)],grid=[0,21])
boton_casa_mainmenu = crear_button(box_leaderboard_options,image='Archivos/Temas/home.png',command=lambda:[sonido_click(),mover(1,mainmenu_ventana,menuprincipal_ventana),cambiar_boton_volver_config(boton_volver_configuracion_p,configuracion,menuprincipal_ventana)],grid=[6,21])
boton_volver_mainmenu = crear_button(box_leaderboard_options,image='Archivos/Temas/flecha.png',command=lambda:[sonido_click(),mover(1,mainmenu_ventana,menuprincipal_ventana),cambiar_boton_volver_config(boton_volver_configuracion_p,configuracion,menuprincipal_ventana)],grid=[12,21])
boton_cerrar_mainmenu = crear_button(box_leaderboard_options,image='Archivos/Temas/x.png',command=lambda:[sonido_click(),cerrar(inicio_app)],grid=[19,21])


'''-----------------------------MAIN MENU-----------------------------'''
box_grafico_mainmenu = Box(mainmenu_ventana,layout='grid',grid=[10,5,40,14])
grafico_mainmenu = Picture(box_grafico_mainmenu, image='Archivos/Temas/grafico_pred.png', grid=[0,0])
grafico_mainmenu.resize(960,720)

label_excel_mainmenu = crear_text(mainmenu_ventana,text='Ingrese el nombre del archivo Excel (sin la extensión):',color='black',grid=[10,0])
tb_excel_mainmenu = crear_textbox(mainmenu_ventana,width=70,grid=[10,1])
boton_comprobar_archivo_mainmenu = crear_button(mainmenu_ventana,text='Comprobar',command=lambda:[sonido_click(),comprobar_archivo(argumentos_comprobar_archivo)],grid=[10,2],borde=True)
label_masa_mainmenu = crear_text(mainmenu_ventana,text='Ingrese la masa:',color='black',grid=[10,3])
tb_masa_mainmenu = crear_textbox(mainmenu_ventana,width=30,grid=[10,4])
boton_cargar_masa_mainmenu = crear_button(mainmenu_ventana,text='Cargar',command=lambda:[sonido_click(),comprobar_masa(argumentos_comprobar_masa)],grid=[10,5],borde=True)
boton_representar_mainmenu = crear_button(mainmenu_ventana,text='Representar',command=lambda:[sonido_click(),representar(mainmenu_ventana,argumentos_representar,tb_calculos),mostrar_garfica('aceleracion',grafico_mainmenu)],grid=[20,5],borde=True)
boton_representar_mainmenu.text_size = 15
boton_enviardatos_mainmenu = crear_button(mainmenu_ventana,text='Enviar Datos',command=lambda:[sonido_click(),SEND_DATA(s,mainmenu_ventana,argumentos_send_data)],grid=[5,5],borde=True)
boton_enviardatos_mainmenu.text_size = 15
label_info_mainmenu = crear_text(mainmenu_ventana,text='xxxxxxx',color='black',grid=[10,6])
label_datosenviados_mainmenu = crear_text(mainmenu_ventana,text='xxxxxxx',color='black',grid=[1,15,9,1])
label_datosenviados_mainmenu.size = 10

box_options_mainmenu = Box(mainmenu_ventana,layout='grid',grid=[0,21,50,1])
boton_configuracion_mainmenu = crear_button(box_options_mainmenu,image='Archivos/Temas/config.png',command=lambda:[sonido_click(),abrir_ventana(configuracion)],grid=[0,21])
boton_casa_mainmenu = crear_button(box_options_mainmenu,image='Archivos/Temas/home.png',command=lambda:[sonido_click(),mover(1,mainmenu_ventana,menuprincipal_ventana),cambiar_boton_volver_config(boton_volver_configuracion_p,configuracion,menuprincipal_ventana),borrar_carpeta_offline()],grid=[6,21])
boton_volver_mainmenu = crear_button(box_options_mainmenu,image='Archivos/Temas/flecha.png',command=lambda:[sonido_click(),mover(1,mainmenu_ventana,menuprincipal_ventana),cambiar_boton_volver_config(boton_volver_configuracion_p,configuracion,menuprincipal_ventana),borrar_carpeta_offline()],grid=[12,21])
boton_cerrar_mainmenu = crear_button(box_options_mainmenu,image='Archivos/Temas/x.png',command=lambda:[sonido_click(),cerrar(inicio_app),borrar_carpeta_offline()],grid=[19,21])

boton_aceleracion_mainmenu = crear_button(mainmenu_ventana,image='Archivos/Temas/aceleracion.png',command=lambda:[sonido_click(),mostrar_garfica('aceleracion',grafico_mainmenu),cambiar_boton_guardar(boton_guardargrafico_mainmenu,'aceleracion')],grid=[1,8],borde=True)
boton_velocidad_mainmenu = crear_button(mainmenu_ventana,image='Archivos/Temas/velocidad.png',command=lambda:[sonido_click(),mostrar_garfica('velocidad',grafico_mainmenu),cambiar_boton_guardar(boton_guardargrafico_mainmenu,'velocidad')],grid=[1,10],borde=True)
boton_fuerza_mainmenu = crear_button(mainmenu_ventana,image='Archivos/Temas/fuerza.png',command=lambda:[sonido_click(),mostrar_garfica('fuerza',grafico_mainmenu),cambiar_boton_guardar(boton_guardargrafico_mainmenu,'fuerza')],grid=[1,12],borde=True)
boton_potencia_mainmenu = crear_button(mainmenu_ventana,image='Archivos/Temas/potencia.png',command=lambda:[sonido_click(),mostrar_garfica('potencia',grafico_mainmenu),cambiar_boton_guardar(boton_guardargrafico_mainmenu,'potencia')],grid=[1,14],borde=True)
boton_guardargrafico_mainmenu = crear_button(mainmenu_ventana,text='Guardar',command=lambda:[sonido_click(),guardar_imagen('aceleracion')],grid=[7,11],borde=True)
boton_guardargrafico_mainmenu._command
label_t0_mainmenu = crear_text(mainmenu_ventana,text='Inicio del vuelo:',color='black',grid=[3,8])
label_t1_mainmenu = crear_text(mainmenu_ventana,text='Final del vuelo:',color='black',grid=[3,9])
label_tia_mainmenu = crear_text(mainmenu_ventana,text='Tiempo de vuelo:',color='black',grid=[3,10])
label_altmax_mainmenu = crear_text(mainmenu_ventana,text='Altura maxima:',color='black',grid=[3,11])
label_acelmax_mainmenu = crear_text(mainmenu_ventana,text='Aceleracion en el salto:',color='black',grid=[3,12])
label_f_mainmenu = crear_text(mainmenu_ventana,text='Fuerza del salto:',color='black',grid=[3,13])
label_p_mainmenu = crear_text(mainmenu_ventana,text='Potencia del salto:',color='black',grid=[3,14])
tb_t0_mainmenu = crear_textbox(mainmenu_ventana,grid=[5,8],bloquear=True)
tb_t0_mainmenu.tk.config(disabledbackground='#D27014')
tb_t1_mainmenu = crear_textbox(mainmenu_ventana,grid=[5,9],bloquear=True)
tb_t1_mainmenu.tk.config(disabledbackground='#D27014')
tb_tia_mainmenu = crear_textbox(mainmenu_ventana,grid=[5,10],bloquear=True)
tb_tia_mainmenu.tk.config(disabledbackground='#D27014')
tb_altmax_mainmenu = crear_textbox(mainmenu_ventana,grid=[5,11],bloquear=True)
tb_altmax_mainmenu.tk.config(disabledbackground='#D27014')
tb_acelmax_mainmenu = crear_textbox(mainmenu_ventana,grid=[5,12],bloquear=True)
tb_acelmax_mainmenu.tk.config(disabledbackground='#D27014')
tb_f_mainmenu = crear_textbox(mainmenu_ventana,grid=[5,13],bloquear=True)
tb_f_mainmenu.tk.config(disabledbackground='#D27014')
tb_p_mainmenu = crear_textbox(mainmenu_ventana,grid=[5,14],bloquear=True)
tb_p_mainmenu.tk.config(disabledbackground='#D27014')

'''-----------------------------CARGAR SALTO-----------------------------'''
box_options_cargarsalto = Box(cargarsalto_ventana,layout='grid',grid=[0,21,50,1])
boton_configuracion_cargarsalto = crear_button(box_options_cargarsalto,image='Archivos/Temas/config.png',command=lambda:[sonido_click(),abrir_ventana(configuracion)],grid=[0,21])
boton_casa_cargarsalto = crear_button(box_options_cargarsalto,image='Archivos/Temas/home.png',command=lambda:[sonido_click(),mover(1,mainmenu_ventana,menuprincipal_ventana),cambiar_boton_volver_config(boton_volver_configuracion_p,configuracion,menuprincipal_ventana),boton_temas_configuracion.enable()],grid=[6,21])
boton_volver_cargarsalto = crear_button(box_options_cargarsalto,image='Archivos/Temas/flecha.png',command=lambda:[sonido_click(),mover(1,mainmenu_ventana,menuprincipal_ventana),cambiar_boton_volver_config(boton_volver_configuracion_p,configuracion,menuprincipal_ventana),boton_temas_configuracion.enable()],grid=[12,21])
boton_cerrar_cargarsalto = crear_button(box_options_cargarsalto,image='Archivos/Temas/x.png',command=lambda:[sonido_click(),cerrar(inicio_app),boton_temas_configuracion.enable()],grid=[19,21])


'''-----------------------------VOLUMENES-----------------------------'''
label_music_volumenes = crear_text(volumenes_ventana,text='Música:',size=15,color='black',grid=[0,0])
slider_music_volumenes = Slider(volumenes_ventana, command=ajustar_volumen_music, start=0, end=100, width=200, height=30, grid=[0,1])
slider_music_volumenes.value = 50
label_voice_volumenes = crear_text(volumenes_ventana,text='Voces:',size=15,color='black',grid=[1,0])
slider_voice_volumenes = Slider(volumenes_ventana, command=ajustar_volumen_voice, start=0, end=100, width=200, height=30, grid=[1,1])
slider_voice_volumenes.value = 20
label_soundefect_volumenes = crear_text(volumenes_ventana,text='Efectos de sonido:',size=15,color='black',grid=[2,0])
slider_soundefect_volumenes = Slider(volumenes_ventana, command=ajustar_volumen_se, start=0, end=100, width=200, height=30, grid=[2,1])
slider_soundefect_volumenes.value = 50
boton_volver_volumenes_p = crear_button(volumenes_ventana,image='Archivos/Temas/flecha_p.png',command=lambda:[sonido_click(),mover(1,volumenes_ventana,configuracion)],grid=[1,3])


s = comprobar_conexion(boton_iniciar_sesion_menuprincipal)
musica('Archivos/Audios/Musicas/GOKU_CANCION.mp3')

lista_text_box = [tb_user_iniciarsesion,tb_password_iniciarsesion, tb_excel_mainmenu,tb_masa_mainmenu,tb_t0_mainmenu,tb_t1_mainmenu,tb_tia_mainmenu,tb_altmax_mainmenu,tb_acelmax_mainmenu,tb_f_mainmenu,tb_p_mainmenu]
lista_labels_cambiar_blanconegro = [label_iniciar_sesion,label_user_iniciarsesion,label_password_iniciarsesion,label_status_iniciarsesion, label_excel_mainmenu,label_masa_mainmenu,label_info_mainmenu,label_datosenviados_mainmenu,label_t0_mainmenu,label_t1_mainmenu,label_tia_mainmenu,label_altmax_mainmenu,label_acelmax_mainmenu,label_f_mainmenu,label_p_mainmenu, label_music_volumenes, label_voice_volumenes, label_soundefect_volumenes]
lista_botones_texto_cambiar_blanconegro = [boton_comprobar_archivo_mainmenu,boton_cargar_masa_mainmenu,boton_representar_mainmenu,boton_enviardatos_mainmenu,boton_guardargrafico_mainmenu,slider_music_volumenes,slider_voice_volumenes,slider_soundefect_volumenes]
lista_botones_cambiar_blanconegro = [boton_volver_menuprincipal,boton_volver_mainmenu,boton_volver_cargarsalto, boton_volver_configuracion_p,boton_volver_volumenes_p, boton_casa_menuprincipal,boton_casa_mainmenu,boton_casa_cargarsalto, boton_cerrar_menuprincipal,boton_cerrar_mainmenu,boton_cerrar_cargarsalto, boton_configuracion_menuprincipal,boton_configuracion_mainmenu,boton_configuracion_cargarsalto, boton_showpassword_iniciarsesion, boton_aceleracion_mainmenu,boton_velocidad_mainmenu,boton_fuerza_mainmenu,boton_potencia_mainmenu]
lista_botones_imagen_cambiar_temas = [boton_iniciar_juego, boton_temas_configuracion,boton_creditos_configuracion,boton_volumen_configuracion, boton_goku_temas,boton_feezer_temas,boton_piccolo_temas,boton_boo_temas,boton_vegeta_temas,boton_bulma_temas,boton_claro_temas,boton_oscuro_temas, logo_menu_principal,boton_iniciar_sesion_menuprincipal,boton_jugar_offline_menuprincipal,boton_cargar_salto_menuprincipal,boton_leaderboard_menuprincipal, boton_iniciarsesion, leaderboard, fondo_iniciar_juego, fondo_menu_principal,boton_cerrar_sesion_configuracion,boton_jugar_online_menuprincipal]
lista_ventanas = [inicio_app,temas_ventana, mainmenu_cs_ventana]

argumentos_send_data = [label_info_mainmenu,label_datosenviados_mainmenu,boton_enviardatos_mainmenu]
argumentos_restablecer_main_menu = [tb_t0_mainmenu, tb_t1_mainmenu, tb_tia_mainmenu, tb_altmax_mainmenu, tb_acelmax_mainmenu, tb_f_mainmenu, tb_p_mainmenu, tb_excel_mainmenu, tb_masa_mainmenu, label_masa_mainmenu, label_info_mainmenu, boton_comprobar_archivo_mainmenu, boton_cargar_masa_mainmenu, boton_representar_mainmenu, boton_enviardatos_mainmenu, grafico_mainmenu, label_datosenviados_mainmenu,boton_guardargrafico_mainmenu,boton_aceleracion_mainmenu,boton_velocidad_mainmenu,boton_fuerza_mainmenu,boton_potencia_mainmenu]
argumentos_representar = [tb_excel_mainmenu, tb_masa_mainmenu,boton_enviardatos_mainmenu,boton_representar_mainmenu,label_info_mainmenu,boton_guardargrafico_mainmenu,boton_aceleracion_mainmenu,boton_velocidad_mainmenu,boton_fuerza_mainmenu,boton_potencia_mainmenu]
argumentos_comprobar_masa = [tb_masa_mainmenu,boton_representar_mainmenu,boton_cargar_masa_mainmenu,label_info_mainmenu]
argumentos_comprobar_archivo = [tb_excel_mainmenu,label_masa_mainmenu,tb_masa_mainmenu,boton_comprobar_archivo_mainmenu,boton_cargar_masa_mainmenu, grafico_mainmenu,label_info_mainmenu]
tb_calculos = [tb_t0_mainmenu, tb_t1_mainmenu, tb_tia_mainmenu, tb_altmax_mainmenu, tb_acelmax_mainmenu, tb_f_mainmenu, tb_p_mainmenu]

inicio_app.display()