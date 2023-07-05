import pygame
from configs import *
from debug import *
from clase_personaje import *
from clase_enemigo import *
from clase_item import *
from clase_boton import *

class Nivel:
    def __init__(self, pantalla, personaje_principal, mapa, imagen_fondo):
        self.pantalla = pantalla
        self.jugador = personaje_principal
        self.mapa = mapa
        self.img_fondo = imagen_fondo
        self.boton_reinicio = Boton(ANCHO // 2 - 80, ALTO // 2 - 50,PATH_BOTON_REINICIAR,TAM_BOTONES, self.pantalla)
        self.animaciones_proyectil = []
        self.sonidos = {
            "gameplay" : pygame.mixer.Sound(SONIDO_GAMEPLAY),
            "personaje" : {
                            "salto" : pygame.mixer.Sound("Sonidos/Jump.wav"),
                            "moneda" : pygame.mixer.Sound("Sonidos/Coin.wav"),
                            "murio" : pygame.mixer.Sound("Sonidos/Die.wav"),
                            "mato"  : pygame.mixer.Sound("assets_level_2/Sonidos/Thwomp.wav"),
                            "disparo": pygame.mixer.Sound("assets_level_2/Sonidos/Fire Ball.wav")
                       },
            "final_nivel": pygame.mixer.Sound("Sonidos/06. Level Complete.mp3"),
        }
        
        for num in range(0, 3):
            self.animaciones_proyectil.append(pygame.image.load(f"assets_level_2/Balas/{num}.png"))
        self.sprites_proyectiles = pygame.sprite.Group()
            
    def update(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_TAB:
                cambiar_modo()
                
        self.teclas_presionadas()
        self.actualizar_pantalla()
        
    def actualizar_pantalla(self,):
        
        self.pantalla.blit(self.img_fondo, ORIGEN_PANTALLA)
        self.dibujar()
        # self.dibujar_cuadricula()
        self.game_over = self.jugador.actualizar(self.game_over)
        self.verificar_game_over()
        
    def teclas_presionadas(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:   
            self.jugador.que_hacer = "camina_izq"
        elif keys[pygame.K_d]:
            self.jugador.que_hacer = "camina_der"
        elif keys[pygame.K_SPACE]:
            self.jugador.que_hacer = "salta"
        elif keys[pygame.K_f] and self.jugador.puede_disparar:
            self.jugador.que_hacer = "quieto"     
            self.jugador.disparar(10, self.sprites_proyectiles, self.animaciones_proyectil, (10,10))
            self.sonidos["personaje"]["disparo"].play()
        else:
            self.jugador.que_hacer = "quieto"
  
class Nivel_Uno(Nivel):
    def __init__(self, pantalla: pygame.surface.Surface):
        
        self.pantalla = pantalla
        W = pantalla.get_width()
        H = pantalla.get_height()
        self.tam_bloque = 40
        imagen_fondo = pygame.image.load(PATH_FONDO)
        imagen_fondo = pygame.transform.scale(imagen_fondo, (W, H))
        self.game_over = 0
        self.sonidos = {
            "gameplay" : pygame.mixer.Sound(SONIDO_GAMEPLAY),
            "personaje" : {
                            "salto" : pygame.mixer.Sound("Sonidos/Jump.wav"),
                            "moneda" : pygame.mixer.Sound("Sonidos/Coin.wav"),
                            "murio" : pygame.mixer.Sound("Sonidos/Die.wav")
                       },
            "final_nivel": pygame.mixer.Sound("Sonidos/06. Level Complete.mp3"),
        }
        #ANIMACIONES
        parado_der = [pygame.image.load("Animaciones/Parado/0.png")]
        camina_der = [
            pygame.image.load("Animaciones/Caminando/0.png"),
            pygame.image.load("Animaciones/Caminando/1.png"),
            pygame.image.load("Animaciones/Caminando/2.png")
        ]
        salta_der = [pygame.image.load("Animaciones/Saltando/0.png")]


        self.animaciones_personaje = {
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
        self.animaciones_enemigo = {
            "camina_izq" : camina_izq_enemigo,
            "camina_der" : camina_der_enemigo,
        }
       
        self.sprites_enemigos = pygame.sprite.Group()
        self.sprites_trampas = pygame.sprite.Group()
        self.sprites_recompensas = pygame.sprite.Group()
        self.sprites_meta = pygame.sprite.Group()
        mapa = MAPA_NIVEL_1
        self.mundo(mapa)
        
        personaje_principal = Personaje(self.pantalla, self.animaciones_personaje, 50, ALTO-50, TAM_PERSONAJE, self.lista_bloques,self.sprites_enemigos, self.sprites_recompensas,self.sonidos, self.sprites_meta, self.sprites_trampas)
        self.personaje = personaje_principal
        self.sonidos["gameplay"].play(-1)
        self.boton_volver = Boton(ANCHO // 2 - 80 ,ALTO // 2 + 100, PATH_BOTON_MENU,TAM_BOTONES,self.pantalla)
        super().__init__(pantalla, personaje_principal, mapa, imagen_fondo)
    
    def dibujar_cuadricula(self,):
        for line in range(0, 25):
            pygame.draw.line(self.pantalla, (255, 255, 255), (0, line * self.tam_bloque), (ANCHO, line * self.tam_bloque))
            pygame.draw.line(self.pantalla, (255, 255, 255), (line * self.tam_bloque, 0), (line * self.tam_bloque, ALTO))
        
    def mundo(self, mundo):
        self.lista_bloques = []
        #load images
        self.pasto = pygame.image.load('Terrenos/0.png')
        self.pared = pygame.image.load('Terrenos/1.png')
        self.techo = pygame.image.load('Terrenos/2.png')
        self.piso = pygame.image.load("Plataformas/0.png")
        
        self.numero_filas = 0
        for fila in mundo:
            self.columna = 0
            for bloque in fila:
                if bloque == 1:
                    img = pygame.transform.scale(self.pasto, TAM_BLOQUE)
                    img_rect = img.get_rect()
                    img_rect.x = self.columna * self.tam_bloque
                    img_rect.y = self.numero_filas * self.tam_bloque
                    bloque = (img, img_rect)
                    self.lista_bloques.append(bloque)
                if bloque == 2:
                    img = pygame.transform.scale(self.pared, TAM_BLOQUE)
                    img_rect = img.get_rect()
                    img_rect.x = self.columna * self.tam_bloque
                    img_rect.y = self.numero_filas * self.tam_bloque
                    bloque = (img, img_rect)
                    self.lista_bloques.append(bloque)
                if bloque == 3:
                    img = pygame.transform.scale(self.techo, TAM_TECHO)
                    img_rect = img.get_rect()
                    img_rect.x = self.columna * self.tam_bloque
                    img_rect.y = self.numero_filas * self.tam_bloque
                    bloque = (img, img_rect)
                    self.lista_bloques.append(bloque)
                if bloque == 4:
                    img = pygame.transform.scale(self.piso, TAM_TECHO)
                    img_rect = img.get_rect()
                    img_rect.x = self.columna * self.tam_bloque
                    img_rect.y = self.numero_filas * self.tam_bloque
                    bloque = (img, img_rect)
                    self.lista_bloques.append(bloque)
                if bloque == 5:
                    enemigo = Enemigo(self.columna * self.tam_bloque, self.numero_filas * self.tam_bloque + 10, TAM_ENEMIGO, animaciones_enemigo,self.pantalla)
                    self.sprites_enemigos.add(enemigo)
                if bloque == 6:
                    moneda = Item(self.columna * self.tam_bloque, self.numero_filas * self.tam_bloque,PATH_MONEDA ,TAM_MONEDA)
                    self.sprites_recompensas.add(moneda)
                if bloque == 7:
                    meta = Item(self.columna * self.tam_bloque, self.numero_filas * self.tam_bloque - 40,PATH_META ,TAM_META)
                    self.sprites_meta.add(meta)
                    
                self.columna += 1
            self.numero_filas += 1
        
    def dibujar(self,):
        for bloque in self.lista_bloques:
            self.pantalla.blit(bloque[0], bloque[1])
    
    def verificar_game_over(self):
        if self.game_over == 0:
            self.sprites_enemigos.update()
            self.sprites_recompensas.draw(self.pantalla)
            self.sprites_meta.draw(self.pantalla)
        elif self.game_over == -1:
                self.pantalla_perdio()
        elif self.game_over == 1:
            self.pantalla_win()
    
    def pantalla_perdio(self):
        self.image_lose = pygame.transform.scale(pygame.image.load("Gui\lose.png"),TAM_ENCABEZADO)
        self.rect_lose = self.image_lose.get_rect()
        self.rect_lose.center = ANCHO // 2, ALTO // 2 - 200
        self.pantalla.blit(self.image_lose, self.rect_lose)
        if self.boton_reinicio.dibujar():
            self.jugador.sonidos["personaje"]["murio"].stop()
            self.sonidos["gameplay"].play(-1)
            self.game_over = 0
            self.sprites_enemigos = pygame.sprite.Group()
            self.sprites_trampas = pygame.sprite.Group()
            self.sprites_recompensas = pygame.sprite.Group()
            self.sprites_meta = pygame.sprite.Group() 
            self.coord_mundo = MAPA_NIVEL_1
            self.mundo(self.coord_mundo)
            self.personaje.reiniciar(self.pantalla, animaciones_personaje, 50, ALTO-50, TAM_PERSONAJE, self.lista_bloques,self.sprites_enemigos, self.sprites_recompensas,self.sonidos, self.sprites_meta, self.sprites_trampas)
        elif self.boton_volver.dibujar():
            self.sonidos["personaje"]["murio"].stop()
            self.game_over = 2
       
    def pantalla_win(self):
        
        self.image_win = pygame.transform.scale(pygame.image.load("Gui/win.png"),TAM_ENCABEZADO)
        self.rect_win = self.image_win.get_rect()
        self.rect_win.center = ANCHO // 2, ALTO // 2 - 200
        
        if self.personaje.score >= 30:
            self.image_estrellas = pygame.transform.scale(pygame.image.load("Gui/star_1.png"),TAM_ESTRELLAS)
            self.rect_estrellas = self.image_estrellas.get_rect()
            self.rect_estrellas.center = POS_ESTRELLAS
        elif self.personaje.score >= 20:
            self.image_estrellas = pygame.transform.scale(pygame.image.load("Gui/star_2.png"),TAM_ESTRELLAS)
            self.rect_estrellas = self.image_estrellas.get_rect()
            self.rect_estrellas.center = POS_ESTRELLAS
        elif self.personaje.score >= 10:
            self.image_estrellas = pygame.transform.scale(pygame.image.load("Gui/star_3.png"),TAM_ESTRELLAS)
            self.rect_estrellas = self.image_estrellas.get_rect()
            self.rect_estrellas.center = POS_ESTRELLAS
        else:
            self.image_estrellas = pygame.transform.scale(pygame.image.load("Gui/star_4.png"),TAM_ESTRELLAS)
            self.rect_estrellas = self.image_estrellas.get_rect()
            self.rect_estrellas.center = POS_ESTRELLAS
        
        
        self.pantalla.blit(self.image_win, self.rect_win)
        self.pantalla.blit(self.image_estrellas, self.rect_estrellas)
        
        if self.boton_volver.dibujar():
            self.sonidos["final_nivel"].stop()
            self.game_over = 2
        
class Nivel_Dos(Nivel):
    def __init__(self, pantalla: pygame.surface.Surface):
        
        self.pantalla = pantalla
        W = pantalla.get_width()
        H = pantalla.get_height()
        self.tam_bloque = 40
        imagen_fondo = pygame.image.load("Background/backgroundColorGrass.png")
        imagen_fondo = pygame.transform.scale(imagen_fondo, (W, H))
        self.game_over = 0
        
        self.sonidos = {
            "gameplay" : pygame.mixer.Sound(SONIDO_GAMEPLAY),
            "personaje" : {
                            "salto" : pygame.mixer.Sound("Sonidos/Jump.wav"),
                            "moneda" : pygame.mixer.Sound("Sonidos/Coin.wav"),
                            "murio" : pygame.mixer.Sound("Sonidos/Die.wav"),
                            "mato"  : pygame.mixer.Sound("assets_level_2/Sonidos/Thwomp.wav"),
                            "disparo": pygame.mixer.Sound("assets_level_2/Sonidos/Fire Ball.wav")
                       },
            "final_nivel": pygame.mixer.Sound("Sonidos/06. Level Complete.mp3"),
        }
        #ANIMACIONES
        parado_der = [pygame.image.load("Animaciones/Parado/0.png")]
        camina_der = [
            pygame.image.load("Animaciones/Caminando/0.png"),
            pygame.image.load("Animaciones/Caminando/1.png"),
            pygame.image.load("Animaciones/Caminando/2.png")
        ]
        salta_der = [pygame.image.load("Animaciones/Saltando/0.png")]

        self.animaciones_personaje = {
                "quieto_der" : parado_der,
                "quieto_izq" : rotar_imagenes(parado_der, True, False),
                "camina_der" : camina_der,
                "camina_izq" : rotar_imagenes(camina_der, True, False),
                "salta_der" : salta_der,
                "salta_izq" : rotar_imagenes(salta_der, True, False),
            }
        #ENEMIGO
        izq_gallina = []
        for num_img in range(0,13):
            izq_gallina.append(pygame.image.load(f"assets_level_2/Enemigo/{num_img}.png"))

        der_gallina = rotar_imagenes(izq_gallina, True, False)
        self.animaciones_enemigo = {
            "camina_izq" : izq_gallina,
            "camina_der" : der_gallina,
        }

        self.moneda = []
        for num_img in range(0,6):
            self.moneda.append(pygame.image.load(f"assets_level_2/Coin/{num_img}.png"))
            
        #sprites
        self.sprites_enemigos = pygame.sprite.Group()
        self.sprites_trampas = pygame.sprite.Group()
        self.sprites_recompensas = pygame.sprite.Group()
        self.sprites_meta = pygame.sprite.Group()

        #cargar mapa nivel 2
        mapa = MAPA_NIVEL_2
        self.mundo(mapa)
 
        #crear personaje
        personaje_principal = Personaje(self.pantalla, self.animaciones_personaje, 50, ALTO-50, TAM_PERSONAJE, self.lista_bloques,self.sprites_enemigos, self.sprites_recompensas,self.sonidos, self.sprites_meta, self.sprites_trampas)
        self.personaje = personaje_principal
        self.personaje.puede_disparar = True
        #sonido gameplay
        self.sonidos["gameplay"].play(-1)
       
        self.boton_volver = Boton(ANCHO // 2 - 80 ,ALTO // 2 + 100, PATH_BOTON_MENU,TAM_BOTONES,self.pantalla)
        super().__init__(pantalla, personaje_principal, mapa, imagen_fondo)
    
    def dibujar_cuadricula(self,):
        for line in range(0, 25):
            pygame.draw.line(self.pantalla, (255, 255, 255), (0, line * self.tam_bloque), (ANCHO, line * self.tam_bloque))
            pygame.draw.line(self.pantalla, (255, 255, 255), (line * self.tam_bloque, 0), (line * self.tam_bloque, ALTO))
        
    def mundo(self, mundo):
        self.lista_bloques = []
        #load images
        self.piso = pygame.image.load('assets_level_2/Terreno/0.png')
        self.pared = pygame.image.load('Terrenos/1.png')
        self.techo = pygame.image.load('assets_level_2/Terreno/1.png')
        self.pisos = pygame.image.load("assets_level_2/Plataformas/2.png")
        
        self.numero_filas = 0
        for fila in mundo:
            self.columna = 0
            for bloque in fila:
                if bloque == 1:
                    img = pygame.transform.scale(self.piso, TAM_BLOQUE)
                    img_rect = img.get_rect()
                    img_rect.x = self.columna * self.tam_bloque
                    img_rect.y = self.numero_filas * self.tam_bloque
                    bloque = (img, img_rect)
                    self.lista_bloques.append(bloque)
                if bloque == 2:
                    img = pygame.transform.scale(self.pared, TAM_BLOQUE)
                    img_rect = img.get_rect()
                    img_rect.x = self.columna * self.tam_bloque
                    img_rect.y = self.numero_filas * self.tam_bloque
                    bloque = (img, img_rect)
                    self.lista_bloques.append(bloque)
                if bloque == 3:
                    img = pygame.transform.scale(self.techo, TAM_TECHO)
                    img_rect = img.get_rect()
                    img_rect.x = self.columna * self.tam_bloque
                    img_rect.y = self.numero_filas * self.tam_bloque
                    bloque = (img, img_rect)
                    self.lista_bloques.append(bloque)
                if bloque == 4:
                    img = pygame.transform.scale(self.pisos, TAM_TECHO)
                    img_rect = img.get_rect()
                    img_rect.x = self.columna * self.tam_bloque
                    img_rect.y = self.numero_filas * self.tam_bloque
                    bloque = (img, img_rect)
                    self.lista_bloques.append(bloque)
                if bloque == 5:
                    moneda = Item_Animado(self.columna * self.tam_bloque + 5, self.numero_filas * self.tam_bloque, self.moneda, (30,30), self.pantalla)
                    self.sprites_recompensas.add(moneda)
                if bloque == 6:
                    gallina = Enemigo(self.columna * self.tam_bloque, self.numero_filas * self.tam_bloque, (40,40), self.animaciones_enemigo, self.pantalla)
                    self.sprites_enemigos.add(gallina)
                if bloque == 7:
                    trampa = Item(self.columna * self.tam_bloque - 10, self.numero_filas * self.tam_bloque,"assets_level_2/Trampas/Spike Head/Idle.png",(60,60))
                    self.sprites_trampas.add(trampa)
                if bloque == 8:
                    trampa = Item(self.columna * self.tam_bloque - 10, self.numero_filas * self.tam_bloque,"assets_level_2/Trampas/Spikes/Idle.png",(40,40))
                    self.sprites_trampas.add(trampa)
                if bloque == 9:
                    meta = Item(self.columna * self.tam_bloque, self.numero_filas * self.tam_bloque - 40,PATH_META ,TAM_META)
                    self.sprites_meta.add(meta)
                self.columna += 1
            self.numero_filas += 1
        
    def dibujar(self,):
        for bloque in self.lista_bloques:
            self.pantalla.blit(bloque[0], bloque[1])
    
    def verificar_game_over(self):
        if self.game_over == 0:
            for proyectil in self.sprites_proyectiles:
                lista = pygame.sprite.spritecollide(proyectil, self.sprites_enemigos, True)
                if len(lista):
                    self.personaje.score += 1
                    self.sonidos["personaje"]["mato"].play()
                    proyectil.kill()
                    
            self.sprites_recompensas.update()
            self.sprites_enemigos.update()
            self.sprites_proyectiles.update()
            self.sprites_trampas.draw(self.pantalla)
            self.sprites_proyectiles.draw(self.pantalla)
            self.sprites_meta.draw(self.pantalla)
        elif self.game_over == -1:
                self.pantalla_perdio()
        elif self.game_over == 1:
            self.pantalla_win()
    
    def pantalla_perdio(self):
        self.image_lose = pygame.transform.scale(pygame.image.load("Gui\lose.png"),TAM_ENCABEZADO)
        self.rect_lose = self.image_lose.get_rect()
        self.rect_lose.center = ANCHO // 2, ALTO // 2 - 200
        self.pantalla.blit(self.image_lose, self.rect_lose)
        if self.boton_reinicio.dibujar():
            self.jugador.sonidos["personaje"]["murio"].stop()
            self.sonidos["gameplay"].play(-1)
            self.game_over = 0
            self.sprites_enemigos = pygame.sprite.Group()
            self.sprites_trampas = pygame.sprite.Group()
            self.sprites_recompensas = pygame.sprite.Group()
            self.sprites_meta = pygame.sprite.Group() 
            self.coord_mundo = MAPA_NIVEL_2
            self.mundo(self.coord_mundo)
            self.personaje.reiniciar(self.pantalla, animaciones_personaje, 50, ALTO-50, TAM_PERSONAJE, self.lista_bloques,self.sprites_enemigos, self.sprites_recompensas,self.sonidos, self.sprites_meta, self.sprites_trampas)
            self.personaje.puede_disparar = True
        elif self.boton_volver.dibujar():
            self.sonidos["personaje"]["murio"].stop()
            self.game_over = 2
            
    def pantalla_win(self):
        self.image_win = pygame.transform.scale(pygame.image.load("Gui/win.png"),TAM_ENCABEZADO)
        self.rect_win = self.image_win.get_rect()
        self.rect_win.center = ANCHO // 2, ALTO // 2 - 200
        
        if self.personaje.score >= 40:
            self.image_estrellas = pygame.transform.scale(pygame.image.load("Gui/star_1.png"),TAM_ESTRELLAS)
            self.rect_estrellas = self.image_estrellas.get_rect()
            self.rect_estrellas.center = POS_ESTRELLAS
        elif self.personaje.score >= 30:
            self.image_estrellas = pygame.transform.scale(pygame.image.load("Gui/star_2.png"),TAM_ESTRELLAS)
            self.rect_estrellas = self.image_estrellas.get_rect()
            self.rect_estrellas.center = POS_ESTRELLAS
        elif self.personaje.score >= 15:
            self.image_estrellas = pygame.transform.scale(pygame.image.load("Gui/star_3.png"),TAM_ESTRELLAS)
            self.rect_estrellas = self.image_estrellas.get_rect()
            self.rect_estrellas.center = POS_ESTRELLAS
        else:
            self.image_estrellas = pygame.transform.scale(pygame.image.load("Gui/star_4.png"),TAM_ESTRELLAS)
            self.rect_estrellas = self.image_estrellas.get_rect()
            self.rect_estrellas.center = POS_ESTRELLAS
        
        
        self.pantalla.blit(self.image_win, self.rect_win)
        self.pantalla.blit(self.image_estrellas, self.rect_estrellas)
        
        if self.boton_volver.dibujar():
            self.sonidos["final_nivel"].stop()
            self.game_over = 2
  
        
        