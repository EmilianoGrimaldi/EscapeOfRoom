import pygame
import sys
from class_nivel import *
# from debug import *
# from configs import *
# from clase_personaje import Personaje
# from clase_enemigo import Enemigo
# from clase_item import *
# from clase_boton import *

class Juego():
    def __init__(self,):
        pygame.init()
        self.menu_principal = True
        self.sub_menu = False
        self.corriendo = True
        self.reloj = pygame.time.Clock()
        self.fps = FPS
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption(TITULO)
        self.nivel_actual = None
        self.boton_iniciar = Boton(ANCHO // 2 - 250, ALTO // 2 - 100,PATH_BOTON_INICIAR,TAM_BOTONES, self.pantalla)
        self.boton_cerrar = Boton(ANCHO // 2 + 100, ALTO // 2 - 100,PATH_BOTON_CERRAR,TAM_BOTONES, self.pantalla)
        self.boton_nivel_1 = Boton(ANCHO // 2 + 100, ALTO // 2 - 100,PATH_BOTON_CERRAR,TAM_BOTONES, self.pantalla)
        
    def comenzar(self,):
        while self.corriendo:
            self.reloj.tick(self.fps)
            self.manejar_eventos()
            self.actualizar_pantalla()
            self.renderizar_pantalla()
        
    def manejar_eventos(self,):
        self.eventos = pygame.event.get()
        for evento in self.eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def subMenu(self):
        self.pantalla_sub_menu = pygame.transform.scale(pygame.image.load(PATH_FONDO_SUB_MENU), TAM_PANTALLA)
        self.img_level =  pygame.transform.scale(pygame.image.load(PATH_IMG_LEVEL), TAM_ENCABEZADO)
        self.level_rect = self.img_level.get_rect()
        self.level_rect.center = (ANCHO // 2, 200)
        self.boton_nivel_1 = Boton(ANCHO // 2 - 150, ALTO // 2, PATH_IMG_NIVEL_1, TAM_IMG_NUM_NIVEL, self.pantalla)
        self.boton_nivel_2 = Boton(ANCHO // 2 - 50, ALTO // 2, PATH_IMG_NIVEL_2, TAM_IMG_NUM_NIVEL, self.pantalla)
        self.pantalla.blit(self.pantalla_sub_menu, ORIGEN_PANTALLA)
        self.pantalla.blit(self.img_level, self.level_rect)  
        if self.boton_nivel_1.dibujar():
            self.sub_menu = False
            self.nivel_actual = Nivel_Uno(self.pantalla)
        elif self.boton_nivel_2.dibujar():
            self.sub_menu = False
            self.nivel_actual = Nivel_Dos(self.pantalla)
            
    def actualizar_pantalla(self,):
        
        if self.menu_principal:
            self.fondo_menu = pygame.image.load(PATH_MENU_IMG)
            self.fondo_menu = pygame.transform.scale(self.fondo_menu, TAM_PANTALLA)
            self.pantalla.blit(self.fondo_menu, ORIGEN_PANTALLA)
            if self.boton_iniciar.dibujar():
                self.menu_principal = False
                self.sub_menu = True 
            if self.boton_cerrar.dibujar():
                self.corriendo = False
        elif self.sub_menu:
            self.subMenu()
        else:
            self.nivel_actual.update(self.eventos)
            if self.nivel_actual.game_over == 2:
                self.menu_principal = True
                

    def renderizar_pantalla(self,):
        pygame.display.flip()

