import pygame

class Boton():
    def __init__(self, x, y, path_imagen,tam, pantalla):
        self.pantalla = pantalla
        self.image = pygame.image.load(path_imagen)
        self.image = pygame.transform.scale(self.image, tam)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.click = False

    def dibujar(self):
        accion = False
        
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.click:
                accion = True
                self.click = True
            else:
                self.click = False

        #draw button
        self.pantalla.blit(self.image, self.rect)

        return accion