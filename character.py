import pygame
#-Formato de nuestro personaje
class Cubo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.widgh = 55
        self.height = 55
        self.speed = 11 #Velocidad de desplazamiento de nuestro personaje
        self.color = "blue"
        #-Dimensiones del objeto
        self.rect = pygame.Rect(self.x,self.y,self.widgh,self.height)
        # Imagenes
        self.imagen = pygame.image.load("CuboPy.jpeg")
        self.imagen = pygame.transform.scale(self.imagen, (self.widgh, self.height))
    def dibujar(self,ventana):
        #-Movimiento
        self.rect = pygame.Rect(self.x,self.y,self.widgh,self.height)
        pygame.draw.rect(ventana, self.color, self.rect)
        ventana.blit(self.imagen, (self.x,self.y))
        