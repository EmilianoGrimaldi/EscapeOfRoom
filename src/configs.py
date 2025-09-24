import pygame

def rotar_imagenes(lista:list, flip_x:bool, flip_y:bool):
    
    lista_aux = []
    
    for imagen in lista:
        lista_aux.append(pygame.transform.flip(imagen, flip_x, flip_y))
    
    return lista_aux

#PANTALLA
ANCHO = 800
ALTO = 600
TAM_PANTALLA = (ANCHO, ALTO)
ORIGEN_PANTALLA = (0, 0)
FPS = 30

#JUEGO
TITULO = "Escape Of Room"
FUENTE = "Fuente/Super Funky.ttf"

#ICONO
PATH_ICONO = "icon/0.png"
TAM_ICONO = (10,10)

#FONDO
PATH_FONDO = "Background/Blue.png"
TAM_FONDO = ANCHO, ALTO

#SONIDO
SONIDO_GAMEPLAY = "Sonidos/Fondo.mp3"

#MAPA
TAM_BLOQUE = 32
PATH_SUELO = "Terrenos/0.png"
MAPA_NIVEL_1 = [
        [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2], 
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 2], 
        [2, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2], 
        [2, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 2], 
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 2], 
        [2, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 2], 
        [2, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [2, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2], 
        [2, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 2], 
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 2], 
        [2, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 2], 
        [2, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 5, 6, 0, 0, 0, 0, 0, 2], 
        [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
        ]

#PERSONAJE
TAM_PERSONAJE = (30,30)
POS_PERSONAJE = (50, ALTO-40)
#ANIMACIONES
parado_der = [pygame.image.load("Animaciones/Parado/0.png")]
camina_der = [
    pygame.image.load("Animaciones/Caminando/0.png"),
    pygame.image.load("Animaciones/Caminando/1.png"),
    pygame.image.load("Animaciones/Caminando/2.png")
]
salta_der = [pygame.image.load("Animaciones/Saltando/0.png")]


animaciones_personaje = {
    "quieto_der" : parado_der,
    "quieto_izq" : rotar_imagenes(parado_der, True, False),
    "camina_der" : camina_der,
    "camina_izq" : rotar_imagenes(camina_der, True, False),
    "salta_der" : salta_der,
    "salta_izq" : rotar_imagenes(salta_der, True, False),
}
#ENEMIGO
camina_izq_enemigo = [pygame.image.load("Enemigo/0.png"),
              pygame.image.load("Enemigo/1.png"),
              pygame.image.load("Enemigo/2.png"),
              pygame.image.load("Enemigo/3.png"),
              pygame.image.load("Enemigo/4.png"),
              pygame.image.load("Enemigo/5.png"),
              pygame.image.load("Enemigo/6.png"),
              pygame.image.load("Enemigo/7.png"),
              pygame.image.load("Enemigo/8.png"),
              pygame.image.load("Enemigo/9.png"),
              pygame.image.load("Enemigo/10.png"),
              pygame.image.load("Enemigo/11.png"),
              pygame.image.load("Enemigo/12.png"),
              pygame.image.load("Enemigo/13.png"),
              pygame.image.load("Enemigo/14.png"),
              pygame.image.load("Enemigo/15.png"),
              ]

camina_der_enemigo = rotar_imagenes(camina_izq_enemigo, True, False)
animaciones_enemigo = {
    "camina_izq" : camina_izq_enemigo,
    "camina_der" : rotar_imagenes(camina_izq_enemigo, True, False),
}

TAM_ENEMIGO = (30,30)
#TAM BLOQUES
TAM_TECHO = (40, 20)
TAM_BLOQUE = (40,40)

#META
PATH_META = "Objetos\End (Idle).png"
TAM_META = (80,80)
#INICIO
PATH_INICIO = "Objetos\Start (Idle).png"
TAM_INICIO = (80,80)

#TRAMPA
TAM_TRAMPA = (30,50)

#MONEDA
PATH_MONEDA = "Objetos/coin.png"
TAM_MONEDA = (30,30)

#MENU
PATH_BOTON_REINICIAR = "Gui/restart.png"
PATH_BOTON_INICIAR = "Gui/play.png"
PATH_BOTON_CERRAR = "Gui/close.png"
PATH_BOTON_MENU = "Gui/menu.png"
PATH_BOTON_PAUSA = "Gui/pause.png"
TAM_BOTONES = (150, 150)
PATH_MENU_IMG = "Background/Gray.png"

#SUBMENU
PATH_FONDO_SUB_MENU = "Background/Green.png"
PATH_IMG_LEVEL = "Gui/bubble/header.png"
PATH_IMG_NIVEL_1 = "Gui/bubble/1.png"
PATH_IMG_NIVEL_2 = "Gui/bubble/2.png"
TAM_ENCABEZADO = (300,200)
TAM_IMG_NUM_NIVEL = (50,100)
#WIN
TAM_ESTRELLAS = (300,200)
POS_ESTRELLAS = ANCHO // 2, ALTO // 2 - 50

#MAPA NIVEL 2
MAPA_NIVEL_2 = [
                [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2], 
                [2, 0, 0, 0, 0, 0, 5, 5, 0, 6, 9, 0, 5, 5, 0, 0, 0, 0, 0, 2], 
                [2, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 2], 
                [2, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 2], 
                [2, 0, 0, 6, 0, 0, 0, 5, 7, 0, 7, 5, 0, 0, 0, 0, 6, 0, 0, 2], 
                [2, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 2], 
                [2, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 2], 
                [2, 0, 0, 7, 5, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 5, 7, 0, 0, 2], 
                [2, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 2], 
                [2, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 2], 
                [2, 0, 0, 0, 6, 0, 0, 5, 7, 5, 7, 5, 0, 0, 0, 0, 6, 0, 0, 2], 
                [2, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 2], 
                [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 2], 
                [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 5, 5, 2], 
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
                ]

#MAPA ORIGINAL
# MAPA_ORIGINAL = [
#         [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2], 
#         [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 2], 
#         [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
#         [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
#         [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
#         [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
#         [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
#         [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
#         [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
#         [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
#         [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
#         [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
#         [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
#         [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
#         [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
# ]
