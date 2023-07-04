import pygame
from configs import *

class Personaje():
    def __init__(self,pantalla ,animaciones, x, y, tam_per, lista_bloques,grupo_enemigos,grupo_items, sonidos, meta):
        
        self.reiniciar(pantalla ,animaciones, x, y, tam_per, lista_bloques,grupo_enemigos,grupo_items, sonidos, meta)
        # self.pantalla = pantalla
        # self.grupo_enemigos = grupo_enemigos
        # self.grupo_items = grupo_items
        # self.meta = meta
        # self.izquierda = False
        # self.esta_saltando = False
        # self.score = 0
        # self.fuente = pygame.font.Font(FUENTE, 20)
        # self.lista_bloques = lista_bloques
        # self.animaciones = animaciones
        # self.sonidos_pj = sonidos_pj
        # self.tam = tam_per
        # self.reescalar_animaciones()
             
        # self.que_hacer = "quieto_der"
        # self.contador_pasos = 0
        # self.image = self.animaciones[self.que_hacer][self.contador_pasos]
        # self.rect = self.image.get_rect()
        # self.rect.bottomleft = x,y
        
        # self.vel_x = 5
        # self.vel_y = 0
        
        # # self.gravedad = 0 
        # self.limite_salto = 16
        # self.potencia_salto = -16 
        # # self.sonidos = sonidos
        # self.vidas = 3
        
        # self.ancho = self.image.get_width()
        # self.alto = self.image.get_height()

        

    def reescalar_animaciones(self):
        for clave, valores in self.animaciones.items():
            for valor in range(len(valores)):
                image = pygame.transform.scale(valores[valor], self.tam)
                valores[valor] = image

    def animar(self,que_animacion):
        
        animacion = self.animaciones[que_animacion]
        largo = len(self.animaciones[que_animacion])

        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        
        self.pantalla.blit(animacion[self.contador_pasos], self.rect)
        self.contador_pasos += 1
    
    # def teclas_presionadas(self):
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_a]:   
    #         self.que_hacer = "camina_izq"
    #     elif keys[pygame.K_d]:
    #         self.que_hacer = "camina_der"
    #     elif keys[pygame.K_SPACE]:
    #         self.que_hacer = "salta"
    #     else:
    #         self.que_hacer = "quieto"
    
    def actualizar(self, game_over):
        self.dx = 0
        self.dy = 0
        self.game_over = game_over
        
        if self.game_over == 0:
            # self.teclas_presionadas()

            if self.que_hacer == "camina_der":
                if not self.esta_saltando:
                    self.animar("camina_der")   
                
                self.dx += self.vel_x
                self.izquierda = False
                
            elif self.que_hacer == "camina_izq":
                if not self.esta_saltando:
                    self.animar("camina_izq")

                self.dx -= self.vel_x
                self.izquierda = True
                
            elif self.que_hacer == "salta" and not self.esta_saltando:
                
                if self.izquierda:
                    self.que_hacer = "salta_izq"
                else:
                    self.que_hacer = "salta_der"

                self.animar(self.que_hacer)
                self.vel_y = self.potencia_salto
                self.esta_saltando = True 
                self.sonidos["personaje"]["salto"].play()
                
            elif self.que_hacer == "quieto":
                if self.izquierda:
                    self.que_hacer = "quieto_izq"
                else:
                    self.que_hacer = "quieto_der" 
                    
                if not self.esta_saltando:
                    self.animar(self.que_hacer)
            
            if self.esta_saltando:
                if self.izquierda:
                    self.que_hacer = "salta_izq"
                else:
                    self.que_hacer = "salta_der"
                    
                self.animar(self.que_hacer) 

                
            self.pantalla.blit(self.fuente.render(f"Puntos: {self.score}", True, "Black"), (ANCHO // 2 - 80,ALTO-40))
            self.aplicar_gravedad()
            self.chequear_colisiones()
            self.rect.x += self.dx
            self.rect.y += self.dy
          
        return self.game_over
    
    def aplicar_gravedad(self):
        self.vel_y += 1
        if self.vel_y > self.limite_salto:
            self.vel_y = self.limite_salto
        self.dy += self.vel_y

    
    def chequear_colisiones(self):
          
        for bloque in self.lista_bloques:
            
            if bloque[1].colliderect(self.rect.x + self.dx, self.rect.y, self.ancho, self.alto):
                self.dx = 0
            
            if bloque[1].colliderect(self.rect.x, self.rect.y + self.dy, self.ancho, self.alto):
                
                if self.vel_y < 0:
                    self.dy = bloque[1].bottom - self.rect.top
                    self.vel_y = 0

                elif self.vel_y >= 0:
                    self.dy = bloque[1].top - self.rect.bottom
                    self.vel_y = 0
                    self.esta_saltando = False
        
        if pygame.sprite.spritecollide(self, self.grupo_enemigos, False):
            self.sonidos["gameplay"].stop()  
            self.sonidos["personaje"]["murio"].play()
            self.game_over = -1
  
        if pygame.sprite.spritecollide(self, self.grupo_items, True):
            self.score += 1
            self.sonidos["personaje"]["moneda"].play()
            
        if pygame.sprite.spritecollide(self, self.meta, True):
            self.game_over = 1
            self.sonidos["gameplay"].stop()
            self.sonidos["final_nivel"].play()
            

    def reiniciar(self, pantalla ,animaciones, x, y, tam_per, lista_bloques,grupo_enemigos,grupo_items, sonidos, meta):
        
        self.pantalla = pantalla
        self.grupo_enemigos = grupo_enemigos
        self.grupo_items = grupo_items
        self.meta = meta
        self.izquierda = False
        self.esta_saltando = False
        self.score = 0
        self.fuente = pygame.font.Font(FUENTE, 20)
        self.lista_bloques = lista_bloques
        self.animaciones = animaciones
        self.sonidos = sonidos
        self.tam = tam_per
        self.reescalar_animaciones()
                
        self.que_hacer = "quieto_der"
        self.contador_pasos = 0
        self.image = self.animaciones[self.que_hacer][self.contador_pasos]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = x,y
        
        self.vel_x = 5
        self.vel_y = 0

        self.limite_salto = 16
        self.potencia_salto = -16 
        self.vidas = 3
        
        self.ancho = self.image.get_width()
        self.alto = self.image.get_height()
