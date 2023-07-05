import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, path_imagen, tam):
        super().__init__()
        self.image = pygame.image.load(path_imagen)
        self.image = pygame.transform.scale(self.image, tam)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Item_Animado(pygame.sprite.Sprite):
    def __init__(self, x, y, animaciones, tam, pantalla):
        super().__init__()
        self.pantalla = pantalla
        self.animaciones = animaciones
        self.tam = tam
        self.reescalar_animaciones()
        self.indice = 0
        self.image = self.animaciones[self.indice]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def reescalar_animaciones(self):
        for i in range(len(self.animaciones)):
            imagen = pygame.transform.scale(self.animaciones[i], self.tam)
            self.animaciones[i] = imagen
                
    def animar(self,):
        
        animacion = self.animaciones
        largo = len(self.animaciones)

        if self.indice >= largo:
            self.indice = 0

        self.pantalla.blit(animacion[self.indice], self.rect)
        self.indice += 1
    
    def update(self):
        self.animar()

class Proyectil(Item_Animado):
    def __init__(self,velocidad, x, y, animaciones, tam, pantalla, direccion):
        super().__init__(x, y, animaciones, tam, pantalla)
        self.rect.center = (x, y)
        self.velocidad = velocidad
        self.direccion = direccion

    def update(self):
        if not self.direccion:
            self.rect.x += self.velocidad
        else:
            self.rect.x -= self.velocidad
