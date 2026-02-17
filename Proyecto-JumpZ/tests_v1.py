from funciones_v4 import *
from cambiartemas import *
from funciones2_v4 import *
from funciones_arqred import *
import pytest

setup_logging('tests')
pygame.init()
def test_es_numero():
    assert es_numero('12') == True
    assert es_numero('67') == True
    assert es_numero('674643324') == False
    assert es_numero('hbdhs') == False
    assert es_numero('rydfhs') == False
    
def test_crear_columnas_filas():
    app_prueba = crear_app('Test Columnas y filas',1920,1080,'grid')
    generar_columnas_filas(app_prueba,20,10)
    app_prueba.tk.grid_size()[0] == 20
    app_prueba.tk.grid_size()[1] == 10
    generar_columnas_filas(app_prueba,60,80)
    app_prueba.tk.grid_size()[0] == 60
    app_prueba.tk.grid_size()[1] == 80
    generar_columnas_filas(app_prueba,4476,'hola')
    app_prueba.tk.grid_size()[0] != 20
    app_prueba.tk.grid_size()[1] == 1
    
    window_prueba = crear_window(app_prueba,'Test Columnas y filas 2',1920,1080,'grid')
    generar_columnas_filas(window_prueba,435,6798)
    window_prueba.tk.grid_size()[0] == 435
    window_prueba.tk.grid_size()[1] == 6798
    
    generar_columnas_filas(app_prueba,56,'40')
    window_prueba.tk.grid_size()[0] == 56
    window_prueba.tk.grid_size()[1] == 40
    
def test_ajustar_volumenes():
    global music_vol,voice_vol, se_vol
    assert music_vol==0.5
    music_vol=ajustar_volumen_music(90)
    assert music_vol==0.9
    music_vol=ajustar_volumen_music('27.7')
    assert round(music_vol,3)==0.277
    music_vol=ajustar_volumen_music('gfhf')
    assert round(music_vol,3)==0.277
    music_vol=ajustar_volumen_music(5467)
    assert music_vol==54.67
    
    assert voice_vol==0.025
    voice_vol=ajustar_volumen_voice(90)
    assert voice_vol==0.18
    voice_vol=ajustar_volumen_voice('27.7')
    assert round(voice_vol,3)==0.055
    voice_vol=ajustar_volumen_voice('gfhf')
    assert round(voice_vol,3)==0.055
    voice_vol=ajustar_volumen_voice(5467)
    assert round(voice_vol,3)==10.934
    
    assert se_vol==0.03
    se_vol=ajustar_volumen_se(90)
    assert se_vol==0.15
    se_vol=ajustar_volumen_se('27.7')
    assert round(se_vol,3)==0.046
    se_vol=ajustar_volumen_se('gfhf')
    assert round(se_vol,3)==0.046
    se_vol=ajustar_volumen_se(5467)
    assert round(se_vol,3)==9.112

def test_cambiar_ventana():
    app = App('App',visible=True)
    ventana1 = Window(app,'Ventana1',visible=True)
    ventana2 = Window(app,'Ventana2',visible=False)
    cambiar_ventanas(True,ventana2,ventana1)
    assert ventana1.visible == False
    assert ventana2.visible == True
    cambiar_ventanas(False,ventana1,ventana2)
    assert ventana1.visible == True 
    assert ventana2.visible == True
    cambiar_ventanas(True,ventana1,ventana2)
    assert ventana1.visible == True 
    assert ventana2.visible == False
    cambiar_ventanas(True,ventana2,ventana1)
    assert ventana1.visible == False
    assert ventana2.visible == True
    
    cambiar_ventanas(True,ventana2,app)
    assert app.visible == False
    assert ventana2.visible == True
    cambiar_ventanas(True,ventana1,ventana2)
    assert ventana1.visible == True 
    assert ventana2.visible == False 
    cambiar_ventanas(False,app,ventana1)
    assert ventana1.visible == True
    assert app.visible == True
    cambiar_ventanas(False,ventana2,app)
    assert ventana1.visible == True
    assert ventana2.visible == True
    assert app.visible == True
    
def test_es_numero():
    assert es_numero(1) == True 
    assert es_numero(4542) == False #Devuelve False porque tiene un limitador a 3 digitos
    assert es_numero('42') == True
    assert es_numero('erivn') == False
    assert es_numero(395) == True
    assert es_numero(7.90) == False #Devuelve False ya que es un float y solo acepta int porque se usa para comprobar la masa
    
def test_activar_desactivar_boton():
    app = App('App',visible=True,layout='grid')
    button = PushButton(app,text='Prueba',grid=[0,0])
    activar_desactivar_boton(button,False)
    assert button.enabled == False
    activar_desactivar_boton(button,True)
    assert button.enabled == True
    
def test_principal():
    app = crear_app('Test Principal',1920,1080,columnas=51,filas=21,layout='grid')
    registrar_boton('offline')
    t, a_gauss, v_gauss, t0_x, t0_y, t1_x, t1_y, tia, altura, a_salto, maximos, F, P, f_max,p_max,nombre = principal(app,'aceleracion1',90)
    assert t0_x == 2.418051562
    assert t1_x == 2.969954687
    assert tia == 0.5519031249999999
    assert altura == 373
    assert a_salto == 14.492623105316603
    assert f_max == 2187.2360794784945
    assert p_max == 5915.483150413017
    assert os.path.exists(f'Archivos/Saltos Guardados (NO TOCAR)/{calculos_fisica_v4.carpeta_g}')
    borrar_carpeta_offline()