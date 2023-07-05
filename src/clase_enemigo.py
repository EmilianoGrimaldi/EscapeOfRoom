import pygame

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, tam, animaciones, pantalla):
        super().__init__()
        self.pantalla = pantalla
        self.animaciones = animaciones
        self.tam = tam
        self.reescalar_animaciones()
        self.izq = False
        self.que_hacer = "camina_izq"
        self.contador_pasos = 0
        self.image = self.animaciones[self.que_hacer][self.contador_pasos]
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
        self.vel_x = 2

        self.movimiento = 0
        
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
        
    def update(self,):

        self.rect.x += self.vel_x
        # self.animar("camina_der")
        self.movimiento += 1
        if self.movimiento > 40:
            # self.animar("camina_izq")
            self.vel_x *= -1
            self.movimiento *= -1  
            self.izq = not self.izq
        
        if self.izq:
            self.animar("camina_izq")
        else:
            self.animar("camina_der")
        # self.animar(self.que_hacer)
