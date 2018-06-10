import pygame
from time import sleep as wait_x_secs
#parametros iniciales
pygame.init()

#Colores
white = (255,255,255)
red = (255,0,0)

P_width = 640
P_height = 480
x_player = P_width * 0.50
y_player = P_height * 0.50

#x_player_change = 0
#y_player_change = 0

#Teclas que se pueden presionar para moverse

K_2 = pygame.K_UP
K_0 = pygame.K_DOWN
K_1 = pygame.K_LEFT
K_3 = pygame.K_RIGHT

#Imagenes y configuracion de pantalla
pantalla = pygame.display.set_mode((P_width,P_height))
pygame.display.set_caption('Death Race')
clock = pygame.time.Clock()
pistaImg = pygame.image.load('pista.png')

#funcion que se encarga de salir del juego
G_exit = False

#DeathRace's gameloop
while not G_exit:
    #Loop para mover al jugador(es)
    for event in pygame.event.get():
        print (event)
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                G_exit = True
                pygame.quit()
                quit()
            elif event.key == K_2:
                if event.key == K_3:
                    y_player -=10
                    x_player += 10
                elif event.key == K_1:
                    y_player -=10
                    x_player -=10
                else:
                    y_player -=10
                    x_player += 0
            elif event.key == K_0:
                if event.key == K_3:
                    y_player += 10
                    x_player -= 10
                elif event.key == K_1:
                    y_player += 10
                    x_player -=10
                else:
                    y_player += 10
                    x_player += 0
            elif event.key == K_3:
                if event.key == K_2:
                    x_player += 10
                    y_player -= 10
                elif event.key == K_0:
                    x_player += 10
                    y_player += 10
                else:
                    x_player += 10
                    y_player += 0
            elif event.key == K_1:
                if event.key == K_2:
                    x_player -=10
                    y_player -=10
                elif event.key == K_0:
                    x_player -=10
                    y_player += 10
                else:
                    x_player -=10
                    y_player += 0
        elif event.type == pygame.KEYUP:
            if event.key == K_2:
                y_player += 0
                x_player += 0
            elif event.key == K_0:
                y_player += 0
                x_player += 0
            elif event.key == K_3:
                x_player += 0
                y_player += 0
            elif event.key == K_1:
                x_player += 0
                y_player += 0
                
    
    #x_player += x_player_change
    #y_player += y_player_change
    pantalla.fill(white)
    pantalla.blit(pistaImg,(0,0))
    pygame.draw.rect(pantalla, red, (x_player,y_player,25,25),0)
    pygame.display.flip()
    clock.tick(60)






