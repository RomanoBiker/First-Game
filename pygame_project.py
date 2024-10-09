import pygame
from character import Cubo  #-Personaje principal
from enemy import Villian   #-Enemigos
from gun import Gun         #-Arma
import random               

pygame.init()

#Sonido
pygame.mixer.init()

# Dimensiones de la ventana de juego
ANCHO = 1200
ALTO = 800
#-Creamos la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
FPS = 60
#Fuente
fuente = pygame.font.SysFont("Comic Sans", 40)
#Sonido disparo
Sonido_shot = pygame.mixer.Sound('sonido\Efecto-de-sonido-fusil-de-asalto-fortnite.mp3')
#Sonido muerte
deathsound = pygame.mixer.Sound('sonido\SOUND OFF ROBLOX SONIDO OFF MUERTE DE ROBLOX.mp3')

#-Variables de tiempo para el bucle principal
playgame = True
reloj = pygame.time.Clock()
tiempo_transcurrido = 0 #Contador de tiempo 
tiempo_oleada = 500      #Tiempo de transcurso para cada oleada

#-Nuestro personaje en la ventana de juego
cubo = Cubo(ANCHO/2,ALTO-75)

'''ATRIBUTOS'''
vida = 6
puntos = 0

#-Creamos una variable para añadir la informacio de nuestro enemigo
enemies = []
enemies.append(Villian(ANCHO/2,100))

#-Teclas de movimiento
shots = []
last_shot = 0
shot_time = 200
def shotgun():
    global last_shot
    if pygame.time.get_ticks() - last_shot > shot_time:
        shots.append(Gun(cubo.rect.centerx, cubo.rect.centery)) #Coordenadas de nuestro cubo para disparar 
        last_shot = pygame.time.get_ticks()
        Sonido_shot.play()

def gestionar_teclas(teclas):
    if teclas[pygame.K_w]:
        cubo.y -= cubo.speed
    if teclas[pygame.K_s]:
        cubo.y += cubo.speed
    if teclas[pygame.K_a]:
        cubo.x -= cubo.speed
    if teclas[pygame.K_d]:
        cubo.x += cubo.speed
    if teclas[pygame.K_SPACE]:
        shotgun()


#-Bucle para mantener el juego abierto
while playgame and vida > 0:
    tiempo_transcurrido += reloj.tick(FPS)
    if tiempo_transcurrido > tiempo_oleada:
        enemies.append(Villian(random.randint(0,ANCHO),-100))
        tiempo_transcurrido = 0
    #1
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            playgame = False
    #2
    teclas = pygame.key.get_pressed()
    #3
    texto_vida = fuente.render(f"Vida: {vida}", True, "White")
    texto_puntos = fuente.render(f"Puntos: {puntos}", True, "Green")
    #4
    gestionar_teclas(teclas)
    ventana.fill("black")
    cubo.dibujar(ventana)
    #5
    #Enemigos
    for enemy in enemies:
        enemy.dibujar(ventana)
        enemy.movement()
        # IMPACTOS
        if pygame.Rect.colliderect(cubo.rect,enemy.rect):
            vida -= 1
            print(f"Te quedan {vida} vidas")
            enemies.remove(enemy)
            '''quit()  #Si nos chocan se cierra el juego'''
        # Puntos por no chocar
        if enemy.y > ALTO:
            puntos += 1
            enemies.remove(enemy)

        for shot in shots:
            if pygame.Rect.colliderect(enemy.rect, shot.rect):
                enemy.vida -= 1
                #enemies.remove(enemy)
                shots.remove(shot)
                puntos += 1        
        if enemy.vida <= 0:
            deathsound.play()   #Sonido muerte  
            enemies.remove(enemy)


    #6
    #Shots
    for shot in shots:
        shot.dibujar(ventana)
        shot.movement()
    #7
    #Texto en pantalla
    ventana.blit(texto_vida, (20,30))
    ventana.blit(texto_puntos, (20,70))

    pygame.display.update()
deathsound.play()   #Sonido muerte

# Guardar las puntuaciones de los usuarios al finalizar la partida
pygame.quit()
name = input("Introduce tu nombre: ")
with open('points.txt', "a") as file:
    #a  --> Append
    #w  --> Write
    #r  --> Read
    file.write(f"{name} - {puntos}\n")
quit()

        