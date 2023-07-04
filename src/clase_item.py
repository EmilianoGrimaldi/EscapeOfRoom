import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, path_imagen, tam):
        super().__init__()
        self.image = pygame.image.load(path_imagen)
        self.image = pygame.transform.scale(self.image, tam)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    

class Trampa(pygame.sprite.Sprite):
    def __init__(self, x, y, animaciones, tam, pantalla):
        super().__init__()
        self.pantalla = pantalla
        self.animaciones = animaciones
        self.tam = tam
        self.reescalar_animaciones()
        self.que_hacer = "movimiento"
        self.contador_pasos = 0
        self.image = self.animaciones[self.que_hacer][self.contador_pasos]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
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
    
    def update(self):
        self.animar("movimiento")
        