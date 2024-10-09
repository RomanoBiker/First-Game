import pygame
#-Formato del personaje enemigo tomando las referencias de nuestro personaje
class Villian:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.widgh = 58
        self.height = 58
        self.speed = 4  #Velocidad de desplazamiento de nuestros enemigos
        self.color = "red"
        #-Dimensiones del objeto
        self.rect = pygame.Rect(self.x,self.y,self.widgh,self.height)
        self.vida = 2
        # Imagenes
        self.imagen = pygame.image.load("VillianPy.jpeg")
        self.imagen = pygame.transform.scale(self.imagen, (self.widgh, self.height))   
    def dibujar(self,ventana):
        self.rect = pygame.Rect(self.x,self.y,self.widgh,self.height)
        pygame.draw.rect(ventana, self.color, self.rect)
        ventana.blit(self.imagen, (self.x,self.y))
    #-Los enemigos se desplazan de manera descendente
    def movement(self):
        self.y += self.speed
       
        