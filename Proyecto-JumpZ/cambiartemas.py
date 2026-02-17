colores = ['#D27014','black']
botones = ['Archivos/Temas/aceleracion.png','Archivos/Temas/velocidad.png','Archivos/Temas/fuerza.png','Archivos/Temas/potencia.png','Archivos/Temas/config.png','Archivos/Temas/home.png','Archivos/Temas/flecha.png','Archivos/Temas/x.png']
def cambiar_tema(tema, text_boxs, labels_blanconegro, botones_texto_blanconegro, botones_imagen_blanconegro,botones_imagen_cambiartemas,ventanas,nodestacados_cargarsalto,textos_cargarsalto,destacados_cargarsalto):
    global colores,botones
    
    tema_lower = tema.lower()

    cambiar_logo = f'Archivos/Temas/{tema}/logo.png'
    cambiarfondo_inicio_juego = f'Archivos/Temas/{tema}/imagen.png'
    cambiarfondo_menu_principal = f'Archivos/Temas/{tema}/{tema_lower}_fondo.png'

    cambiarboton_tema = f'Archivos/Temas/{tema}/temas.png'
    cambiarboton_creditos = f'Archivos/Temas/{tema}/creditos.png'
    cambiarboton_volumen = f'Archivos/Temas/{tema}/volumenes.png'
    cambiarboton_cerrar_sesion = f'Archivos/Temas/{tema}/cerrar_sesion.png'
    cambiarboton_cargar_salto = f'Archivos/Temas/{tema}/cargar_salto.png'
    cambiarboton_leaderboard = f'Archivos/Temas/{tema}/leaderboard.png'
    cambiarboton_jugaroffline = f'Archivos/Temas/{tema}/jugar_offline.png'
    cambiarboton_jugaronline = f'Archivos/Temas/{tema}/jugar_online.png'
    cambiarboton_iniciarsesion1 = f'Archivos/Temas/{tema}/iniciar_sesion_pj.png'
    cambiarboton_iniciarsesion2 = f'Archivos/Temas/{tema}/iniciar_sesion.png'
    cambiarboton_iniciarjuego = f'Archivos/Temas/{tema}/iniciar_juego.png'
    if tema == 'Goku':
        bg_color = (233,124,21)
        tb_color = '#d27014'
    elif tema == 'Freezer':
        bg_color = (200, 180, 230)
        tb_color = '#b99fdf'
    elif tema == 'Piccolo':
        bg_color = (119,221,119)
        tb_color = '#5cd65c'
    elif tema == 'Boo':
        bg_color = (255, 200, 228)
        tb_color = '#ff80c1'
    elif tema == 'Vegeta':
        bg_color = (25, 68, 131)
        tb_color = '#14376c'
    elif tema == 'Bulma':
        bg_color = (126,197,172)
        tb_color = '#4fb08f'
    elif tema == 'Claro':
        bg_color = (216, 216, 216)
        tb_color = '#bfbfbf'
    elif tema == 'Oscuro':
        bg_color = (25, 25, 25)
        tb_color = '#0d0d0d'

    if tema == 'Oscuro':
        txt_color = 'white'
        cambiarboton_back_color = 'Archivos/Temas/flecha_clara.png'
        cambiarboton_back_p_color = 'Archivos/Temas/flecha_clara_p.png'
        cambiarboton_cerrar_color = 'Archivos/Temas/x_clara.png'
        cambiarboton_home_color = 'Archivos/Temas/home_clara.png'
        cambiarboton_config_color = 'Archivos/Temas/config_clara.png'
        cambiarboton_showpassword_color = 'Archivos/Temas/ojo_clara.png'
        cambiarboton_aceleracion = 'Archivos/Temas/aceleracion_clara.png'
        cambiarboton_velocidad = 'Archivos/Temas/velocidad_clara.png'
        cambiarboton_fuerza = 'Archivos/Temas/fuerza_clara.png'
        cambiarboton_potencia = 'Archivos/Temas/potencia_clara.png'

    else:
        txt_color = 'black'
        cambiarboton_back_color = 'Archivos/Temas/flecha.png'
        cambiarboton_back_p_color = 'Archivos/Temas/flecha_p.png'
        cambiarboton_cerrar_color = 'Archivos/Temas/x.png'
        cambiarboton_home_color = 'Archivos/Temas/home.png'
        cambiarboton_config_color = 'Archivos/Temas/config.png'
        cambiarboton_showpassword_color = 'Archivos/Temas/ojo.png'
        cambiarboton_aceleracion = 'Archivos/Temas/aceleracion.png'
        cambiarboton_velocidad = 'Archivos/Temas/velocidad.png'
        cambiarboton_fuerza = 'Archivos/Temas/fuerza.png'
        cambiarboton_potencia = 'Archivos/Temas/potencia.png'
    
    ventanas[0].bg = bg_color
    ventanas[1].bg = (100, 100, 100)

    for textbox in text_boxs:
        textbox.bg = tb_color
        textbox.tk.config(disabledbackground=tb_color)
        textbox.text_color = txt_color

    for label in labels_blanconegro:
        label.text_color = txt_color

    for boton_texto in botones_texto_blanconegro:
        boton_texto.text_color = txt_color

    for nodestacado_cargarsalto in nodestacados_cargarsalto:
        nodestacado_cargarsalto.text_color = txt_color

    for destacado_cargarsalto in destacados_cargarsalto:
        destacado_cargarsalto.bg = 'lightyellow'
    
    for label_cargarsalto in textos_cargarsalto:
        label_cargarsalto.text_color = txt_color

    botones_imagen_blanconegro[0].image = cambiarboton_back_color
    botones_imagen_blanconegro[1].image = cambiarboton_back_color
    botones_imagen_blanconegro[2].image = cambiarboton_back_color

    botones_imagen_blanconegro[3].image = cambiarboton_back_p_color
    botones_imagen_blanconegro[4].image = cambiarboton_back_p_color
    
    botones_imagen_blanconegro[5].image = cambiarboton_home_color
    botones_imagen_blanconegro[6].image = cambiarboton_home_color
    botones_imagen_blanconegro[7].image = cambiarboton_home_color

    botones_imagen_blanconegro[8].image = cambiarboton_cerrar_color
    botones_imagen_blanconegro[9].image = cambiarboton_cerrar_color
    botones_imagen_blanconegro[10].image = cambiarboton_cerrar_color

    botones_imagen_blanconegro[11].image = cambiarboton_config_color
    botones_imagen_blanconegro[12].image = cambiarboton_config_color
    botones_imagen_blanconegro[13].image = cambiarboton_config_color

    botones_imagen_blanconegro[14].image = cambiarboton_showpassword_color
    botones_imagen_blanconegro[15].image = cambiarboton_aceleracion
    botones_imagen_blanconegro[16].image = cambiarboton_velocidad
    botones_imagen_blanconegro[17].image = cambiarboton_fuerza
    botones_imagen_blanconegro[18].image = cambiarboton_potencia

    botones_imagen_cambiartemas[0].image = cambiarboton_iniciarjuego
    botones_imagen_cambiartemas[1].image = cambiarboton_tema
    botones_imagen_cambiartemas[2].image = cambiarboton_creditos
    botones_imagen_cambiartemas[3].image = cambiarboton_volumen
    botones_imagen_cambiartemas[4].bg = '#d27014'
    botones_imagen_cambiartemas[5].bg = '#b99fdf'
    botones_imagen_cambiartemas[6].bg = '#5cd65c'
    botones_imagen_cambiartemas[7].bg = '#ff80c1'
    botones_imagen_cambiartemas[8].bg = '#14376c'
    botones_imagen_cambiartemas[9].bg = '#4fb08f'
    botones_imagen_cambiartemas[10].bg = '#bfbfbf'
    botones_imagen_cambiartemas[11].bg = '#0d0d0d'
    botones_imagen_cambiartemas[12].image = cambiar_logo
    botones_imagen_cambiartemas[13].image = cambiarboton_iniciarsesion1
    botones_imagen_cambiartemas[14].image = cambiarboton_jugaroffline
    botones_imagen_cambiartemas[15].image = cambiarboton_cargar_salto
    botones_imagen_cambiartemas[16].image = cambiarboton_leaderboard
    botones_imagen_cambiartemas[17].image = cambiarboton_iniciarsesion2
    botones_imagen_cambiartemas[18].image = cambiarboton_leaderboard
    botones_imagen_cambiartemas[19].image = cambiarfondo_inicio_juego
    botones_imagen_cambiartemas[20].image = cambiarfondo_menu_principal
    botones_imagen_cambiartemas[21].image = cambiarboton_cerrar_sesion
    botones_imagen_cambiartemas[22].image = cambiarboton_jugaronline

    colores = [tb_color,txt_color]
    botones = [
            cambiarboton_aceleracion, cambiarboton_velocidad, cambiarboton_fuerza, 
            cambiarboton_potencia, cambiarboton_config_color, cambiarboton_home_color, 
            cambiarboton_back_color, cambiarboton_cerrar_color
    ]    
    return colores, botones
    
def  restablecer_valores_iniciales(argumentos_restablecer_main_menu):
    argumentos_restablecer_main_menu[0].value = '0.00s'
    argumentos_restablecer_main_menu[1].value = '0.00s'
    argumentos_restablecer_main_menu[2].value = '0.00s'
    argumentos_restablecer_main_menu[3].value = '000mm'
    argumentos_restablecer_main_menu[4].value = '0.00m/s²'
    argumentos_restablecer_main_menu[5].value = '0.00N'
    argumentos_restablecer_main_menu[6].value = '0.00W'
    argumentos_restablecer_main_menu[7].value = ''
    argumentos_restablecer_main_menu[7].enable()
    argumentos_restablecer_main_menu[7].bg = colores[0]
    argumentos_restablecer_main_menu[7].text_color = colores[1]
    argumentos_restablecer_main_menu[8].value = ''
    argumentos_restablecer_main_menu[8].enable()
    argumentos_restablecer_main_menu[8].bg = colores[0]
    argumentos_restablecer_main_menu[8].text_color = colores[1]
    argumentos_restablecer_main_menu[8].visible = False
    argumentos_restablecer_main_menu[9].visible = False
    argumentos_restablecer_main_menu[10].visible = False
    argumentos_restablecer_main_menu[11].enable()
    argumentos_restablecer_main_menu[11].visible = True
    argumentos_restablecer_main_menu[12].enable()
    argumentos_restablecer_main_menu[12].visible = False
    argumentos_restablecer_main_menu[13].disable()
    argumentos_restablecer_main_menu[13].visible = False
    argumentos_restablecer_main_menu[14].disable()
    argumentos_restablecer_main_menu[14].visible = False
    argumentos_restablecer_main_menu[15].image = 'Archivos/Temas/grafico_pred.png'
    argumentos_restablecer_main_menu[16].visible = False
    argumentos_restablecer_main_menu[17].disable()
    argumentos_restablecer_main_menu[17].visible = True
    argumentos_restablecer_main_menu[18].disable()
    argumentos_restablecer_main_menu[19].disable()
    argumentos_restablecer_main_menu[20].disable()
    argumentos_restablecer_main_menu[21].disable()