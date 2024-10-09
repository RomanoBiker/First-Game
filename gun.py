import pygame
#-Formato del los disparos de nuestro personaje para eliminar enemigos
class Gun:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.widgh = 8
        self.height = 8
        self.speed = 16  #Velocidad de disparo
        self.color = "orange"
        #-Dimensiones 
        self.rect = pygame.Rect(self.x,self.y,self.widgh,self.height) 
    def dibujar(self,ventana):
        self.rect = pygame.Rect(self.x,self.y,self.widgh,self.height)
        pygame.draw.rect(ventana, self.color, self.rect)
    #-Los disparos se desplazan de manera ascendente a la posicion del personaje
    def movement(self):
        self.y -= self.speed
        