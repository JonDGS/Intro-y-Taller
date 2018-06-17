import pygame
from pygame.locals import *
from math import *
import main
import json

WIDTH  = 800
HEIGHT = 600


pressed = pygame.KEYDOWN

# Colores
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
green = (0, 255, 0)
darkgreen = (0, 100, 0)
light_green = (127, 255, 212)

ffx = 'freesansbold.ttf'

#globals
G_exit = False

# Teclas

K_2 = pygame.K_w
K_0 = pygame.K_s
K_1 = pygame.K_a
K_3 = pygame.K_d
arriba = pygame.K_UP
abajo = pygame.K_DOWN
derecha = pygame.K_RIGHT
izquierda = pygame.K_LEFT
test_x = pygame.K_s

# abreviaciones

pressed = pygame.KEYDOWN
ffx = 'freesansbold.ttf'

# Imagenes y configuracion de pantalla
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Road to Cartaguito")
clock = pygame.time.Clock()
Timage1 = pygame.image.load('TitleCar.png')
PauseBack = pygame.image.load('pause_background.png')
pause_background = pygame.transform.scale(PauseBack, (800, 600))
Timage = pygame.transform.scale(Timage1, (int(800 * 0.6), int(600 * 0.3)))
ScoresImg = pygame.image.load('Scores.png')
scorepng = pygame.transform.scale(ScoresImg, (800, 600))
IngresoBack = pygame.image.load('cr.png')
InBack = pygame.transform.scale(IngresoBack, (800, 600))


#music_menu = pygame.mixer.music.load('Stuff.wav')

# Define la superficie y font para el texto
def text_in_menu(text, color, font):
    textS = font.render(text, True, color)
    return textS, textS.get_rect()


# Define donde se mostrara el texto y con que color y tamaño
def mostrarTexto(text, x, y, size, color):
    TitleText = pygame.font.Font(ffx, size)
    TSurface, Trect = text_in_menu(text, color, TitleText)
    Trect.center = ((x, y))
    main.SCREEN.blit(TSurface, Trect)
#Recibe los inputs del usernames
def recover_input2(user1):
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    font = pygame.font.Font(None, 32)
    active = False
    text = ''
    done = False
    user2 = ''
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.pause()
                        user2 = text
                        return main.main(user1, user2)
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        pantalla.fill((30, 30, 30))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        pantalla.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(pantalla, color, input_box, 2)
        mostrarTexto("Insert player2's name, click the textbox to input", 200, 70, 15, white)

        pygame.display.flip()
        clock.tick(30)

#Recibe los inputs del usernames
def recover_input1jugador(player2):
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    font = pygame.font.Font(None, 32)
    active = False
    text = ''
    done = False
    user1 = ''
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        user1 = text
                        if not player2:
                            #pygame.mixer.music.pause()
                            return main.main(user1, False)
                        else:
                            recover_input2(user1)
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        pantalla.fill((30, 30, 30))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        pantalla.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(pantalla, color, input_box, 2)
        mostrarTexto("Insert player1's name, click the textbox to input", 200, 70, 15, white)

        pygame.display.flip()
        clock.tick(30)

def loopdejuego(player2):
    return recover_input1jugador(player2)


def ingreso(player2):
    Ingreso = True
    while Ingreso:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return loopdejuego(player2)
        pantalla.fill(white)
        pantalla.blit(InBack, (0, 0))
        mostrarTexto('Presione enter para continuar', (800 * 0.50), (600 * 0.40), 40, light_green)
        mostrarTexto('Player 1 control are the W,A,S,D keys and x for shooting', (800 * 0.50), (600 * 0.55),
                     20, light_green)
        if player2:
            mostrarTexto('Player 2 control are the arrow keys and space for shooting', (800 * 0.50),
                         (600 * 0.70), 20, light_green)
        mostrarTexto('Beta release v.0.3', (800 * 0.10), (600 * 0.95), 15, light_green)
        clock.tick(20)
        pygame.display.flip()

# Loop del menu de scores
def menu1():
    with open("SaveFile.json", "r") as f:
        datos = json.load(f)
    m1 = True
    s = pygame.Surface((780,580)) 
    s.set_alpha(240)                
    s.fill((255,255,255)) 
    while m1:
        for event in pygame.event.get():
            if event.type == pressed:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == test_x:
                    m1 = False
                    #menu_principal()
        main.SCREEN.blit(scorepng, (0, 0))
        #pygame.draw.rect(main.SCREEN, (245, 245, 245, 128), (10, 10, 780, 580))
        main.SCREEN.blit(s, (0,0))
        mostrarTexto('Username:', 66, 100, 18, black)
        mostrarTexto('Score:', 66, 200, 18, black) 
        mostrarTexto('Laps:', 66, 300, 18, black)
        mostrarTexto('Hits:', 66, 400, 18, black)
        for i in range(5):
            mostrarTexto(str((i*1)+1) + '#', 199 + (110*i), 50, 18, black)
        for i in range(5):
            mostrarTexto(datos['players'][i]['username'], 199 + (110*i), 100, 18, black)
        for i in range(5):
            mostrarTexto(str(datos['players'][i]['total']), 199 + (110*i), 200, 18, black)
        for i in range(5):
            mostrarTexto(str(datos['players'][i]['laps']), 199 + (110*i), 300, 18, black)
        for i in range(5):
            mostrarTexto(str(datos['players'][i]['hits']), 199 + (110*i), 400, 18, black)
        mostrarTexto('Beta release v.0.3', (800 * 0.10), (600 * 0.95), 15, light_green)
        main.FPS.tick(20)
        pygame.display.flip()

#Menu principal
def menu_principal():
    #pygame.mixer.music.play(-1)
    menu_principal = True
    while menu_principal:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                quit()
            elif event.type == pressed:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == test_x:
                    menu1()
                elif event.key == pygame.K_1:
                    menu_principal = False
                    player2 = False
                    return ingreso(player2)
                elif event.key == pygame.K_2:
                    menu_principal = False
                    player2 = True
                    return ingreso(player2)
        main.SCREEN.fill(yellow)
        mostrarTexto("Road to Cartaguito", (800 * 0.5), (600 * 1 / (72 / 20)), 58, black)
        mostrarTexto('Press 1 for solo or 2 for multiplayer', (800 * 0.5), (600 * 0.7 // 1), 28, darkgreen)
        mostrarTexto('Press R to reload previous game', (800 * 0.5), (600 * 0.75), 26, darkgreen)
        mostrarTexto('Press S to view scores', (800 * 0.5), (600 * 0.85), 24, darkgreen)
        main.SCREEN.blit(Timage, (int(800 * 0.20), int(600 * 0.35)))
        mostrarTexto('Beta release v.0.3', (800 * 0.10), (600 * 0.95), 15, darkgreen)
        main.FPS.tick(20)
        pygame.display.flip()

#Pausa del juego
def pause_menu():
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = False
                if event.key == pygame.K_m:
                    return menu_principal()
                if event.key == pygame.K_r:
                    return menu_principal()
                else:
                    mostrarTexto('Please press either enter escape to get back to game or m to go to the menu_principal',
                                 (800 * 0.50), (600 * 0.20), 30, red)
        main.SCREEN.fill(white)
        main.SCREEN.blit(pause_background, (0, 0))
        mostrarTexto('Pause', (800 * 0.50), (600 * 0.10), 50, black)
        mostrarTexto('Press m to got back to the menu_principal', (800 * 0.50), (600 * 0.20), 25, darkgreen)
        mostrarTexto("Press r to restart the game in it's current mode", (800 * 0.50), (600 * 0.25), 25,
                     darkgreen)
        mostrarTexto("Press escape to get back into game", (800 * 0.50), (600 * 0.30), 28, green)
        mostrarTexto('Beta release v.0.3', (800 * 0.10), (600 * 0.95), 15, light_green)
        main.FPS.tick(20)
        pygame.display.update()
