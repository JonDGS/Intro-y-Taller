import pygame
import tkinter as tk
import threading
import json
from time import sleep as wait_x_secs

# Inicializacion de python
pygame.init()

# Colores
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
green = (0, 255, 0)
darkgreen = (0, 100, 0)
light_green = (127, 255, 212)

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
P_width = int((screen_width * 0.65))
P_height = int((screen_height * 0.65))

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
pantalla = pygame.display.set_mode((P_width, P_height))
pygame.display.set_caption("Road to Cartaguito")
clock = pygame.time.Clock()
carImg1 = pygame.image.load('Batest.png')
carImg = pygame.transform.scale(carImg1, (int(P_width * 0.0114583333), int(P_height * 0.0305555555)))
car2Img1 = pygame.image.load('f1car.png')
car2Img = pygame.transform.scale(car2Img1, (int(P_width * 0.0114583333), int(P_height * 0.0305555555)))
pistaImg1 = pygame.image.load('pistaResized.png')
bullet = pygame.image.load('bullet.png')
bullet1 = pygame.transform.scale(bullet, (int(P_width * (13 / 1366)), int(P_height * (15 / 768))))
Timage1 = pygame.image.load('TitleCar.png')
PauseBack = pygame.image.load('pause_background.png')
pause_background = pygame.transform.scale(PauseBack, (P_width, P_height))
Timage = pygame.transform.scale(Timage1, (int(P_width * 0.6), int(P_height * 0.3)))
pistaImg = pygame.transform.scale(pistaImg1, (P_width, P_height))
ScoresImg = pygame.image.load('Scores.png')
scorepng = pygame.transform.scale(ScoresImg, (P_width, P_height))
IngresoBack = pygame.image.load('cr.png')
InBack = pygame.transform.scale(IngresoBack, (P_width, P_height))
pista2i = pygame.image.load('1erapista.png')
pista2 = pygame.transform.scale(pista2i, (P_width, P_height))
pista3i = pygame.image.load('pista2.png')
pista3 = pygame.transform.scale(pista3i, (P_width, P_height))

#Archivos de musica
music_menu = pygame.mixer.music.load('Stuff.wav')

# Funciones

with open('test.json') as f:
    data = json.load(f)


# Funcion encargada de los choques
def crash(who, player2):
    crash = True
    while crash:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    crash = False
                    return loopdejuego(player2)
                if event.key == pygame.K_ESCAPE:
                    crash = False
                    return menus()
                if event.key == pygame.K_SPACE:
                    crash = False
                    return loopdejuego(player2)
        pantalla.fill(white)
        mostrarTexto(who, P_width * 0.50, P_height * 0.50, 100, black)
        mostrarTexto('Press spacebar to restart or Escape to go back to the menu', P_width * 0.50, P_height * 0.70, 30,
                     green)
        mostrarTexto('Beta release v.0.3', (P_width * 0.10), (P_height * 0.95), 15, light_green)
        clock.tick(20)
        pygame.display.flip()


# Define las x y y para los autos
#def car(carImg, x_player, y_player):
    #pantalla.blit(carImg, (x, y))


# Define como se debe rotar el objeto en cada movimiento
def rotation(pantalla, image, x, y, angle):
    rotImg = pygame.transform.rotate(image, angle)
    center = rotImg.get_rect()
    # print (center)
    # print(x-center[0],y-center[1])
    pantalla.blit(rotImg, (x - center[0], y - center[1]))


# Define la superficie y font para el texto
def text_in_menu(text, color, font):
    textS = font.render(text, True, color)
    return textS, textS.get_rect()


# Define donde se mostrara el texto y con que color y tamaño
def mostrarTexto(text, x, y, size, color):
    TitleText = pygame.font.Font(ffx, size)
    TSurface, Trect = text_in_menu(text, color, TitleText)
    Trect.center = ((x, y))
    pantalla.blit(TSurface, Trect)


# Loop del menu de scores
def menu1():
    m1 = True
    while m1:
        for event in pygame.event.get():
            if event.type == pressed:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == test_x:
                    m1 = False
                    #menus()
        pantalla.blit(scorepng, (0, 0))
        mostrarTexto('Beta release v.0.3', (P_width * 0.10), (P_height * 0.95), 15, light_green)
        clock.tick(20)
        pygame.display.flip()


def ingreso(player2):
    Ingreso = True
    while Ingreso:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return loopdejuego(player2)
        pantalla.fill(white)
        pantalla.blit(InBack, (0, 0))
        mostrarTexto('Presione enter para continuar', (P_width * 0.50), (P_height * 0.40), 40, light_green)
        mostrarTexto('Player 1 control are the W,A,S,D keys and x for shooting', (P_width * 0.50), (P_height * 0.55),
                     20, light_green)
        if player2:
            mostrarTexto('Player 2 control are the arrow keys and space for shooting', (P_width * 0.50),
                         (P_height * 0.70), 20, light_green)
        mostrarTexto('Beta release v.0.3', (P_width * 0.10), (P_height * 0.95), 15, light_green)
        clock.tick(20)
        pygame.display.flip()


# Loop de los menus
def menus():
    pygame.mixer.music.play(-1)
    Menus = True
    while Menus:
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
                    Menus = False
                    player2 = False
                    return ingreso(player2)
                elif event.key == pygame.K_2:
                    Menus = False
                    player2 = True
                    return ingreso(player2)
        pantalla.fill(yellow)
        mostrarTexto("Road to Cartaguito", (P_width * 0.5), (P_height * 1 / (72 / 20)), 58, black)
        mostrarTexto('Press 1 for solo or 2 for multiplayer', (P_width * 0.5), (P_height * 0.7 // 1), 28, darkgreen)
        mostrarTexto('Press S to view scores', (P_width * 0.5), (P_height * 0.75), 24, darkgreen)
        pantalla.blit(Timage, (int(P_width * 0.20), int(P_height * 0.35)))
        mostrarTexto('Beta release v.0.3', (P_width * 0.10), (P_height * 0.95), 15, darkgreen)
        clock.tick(20)
        pygame.display.flip()


# Menu para cuando el juego este pausado
def pause_menu(player2):
    pygame.mixer.music.pause()
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = False
                if event.key == pygame.K_m:
                    return menus()
                if event.key == pygame.K_r:
                    return menus()
                else:
                    mostrarTexto('Please press either enter escape to get back to game or m to go to the menus',
                                 (P_width * 0.50), (P_height * 0.20), 30, red)
                    wait_x_secs(5)
        pantalla.fill(white)
        pantalla.blit(pause_background, (0, 0))
        mostrarTexto('Pause', (P_width * 0.50), (P_height * 0.10), 50, black)
        mostrarTexto('Press m to got back to the menus', (P_width * 0.50), (P_height * 0.20), 25, darkgreen)
        mostrarTexto("Press r to restart the game in it's current mode", (P_width * 0.50), (P_height * 0.25), 25,
                     darkgreen)
        mostrarTexto("Press escape to get back into game", (P_width * 0.50), (P_height * 0.30), 28, green)
        mostrarTexto('Beta release v.0.3', (P_width * 0.10), (P_height * 0.95), 15, light_green)
        clock.tick(20)
        pygame.display.update()

def recover_input2( player_name, x_player, y_player, speed, speed_change, x_player_change, y_player_change,
                                          Angle, UP, DP, RP, LP,
                                          score, c, player2_name, x_player2, y_player2, speed2, speed_change2, x_player_change2,
                                          y_player_change2, Angle2,
                                          UP2, DP2, RP2, LP2, score2, c2, player2):
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    font = pygame.font.Font(None, 32)
    active = False
    text = ''
    done = False
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
                        player2_name = text
                        return loop_juego(player_name, x_player, y_player, speed, speed_change, x_player_change, y_player_change,
                                          Angle, UP, DP, RP, LP,
                                          score, c,player2_name,  x_player2, y_player2, speed2, speed_change2, x_player_change2,
                                          y_player_change2, Angle2,
                                          UP2, DP2, RP2, LP2, score2, c2, player2)
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

def recover_input( player_name, x_player, y_player, speed, speed_change, x_player_change, y_player_change,
                                          Angle, UP, DP, RP, LP,
                                          score, c, player2_name, x_player2, y_player2, speed2, speed_change2, x_player_change2,
                                          y_player_change2, Angle2,
                                          UP2, DP2, RP2, LP2, score2, c2, player2):
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    font = pygame.font.Font(None, 32)
    active = False
    text = ''
    done = False
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
                        player_name = text
                        if not player2:
                            pygame.mixer.music.pause()
                            return loop_juego(player_name, x_player, y_player, speed, speed_change, x_player_change, y_player_change,
                                              Angle, UP, DP, RP, LP,
                                              score, c,player2_name,  x_player2, y_player2, speed2, speed_change2, x_player_change2,
                                              y_player_change2, Angle2,
                                              UP2, DP2, RP2, LP2, score2, c2, player2)
                        else:
                            recover_input2(player_name, x_player, y_player, speed, speed_change, x_player_change, y_player_change, Angle, UP, DP, RP, LP, score, c, '',  x_player2, y_player2, speed2, speed_change2, x_player_change2, y_player_change2, Angle2, UP2, DP2, RP2, LP2, score2, c2, player2)
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



def mapa3(player_name, x_player, y_player, speed, speed_change, x_player_change, y_player_change, Angle, UP, DP, RP, LP, score, c, player2_name,
             x_player2, y_player2, speed2, speed_change2, x_player_change2, y_player_change2, Angle2, UP2, DP2, RP2,
             LP2, score2, c2, player2):
    #global G_exit
    t = pygame.time.get_ticks()
    G_exit3 = False
    while not G_exit3:
        seconds = (pygame.time.get_ticks() - t) / 1000
        if seconds > 180:
            G_exit3 = True
        for event in pygame.event.get():
           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_menu(player2)
                if event.key == pygame.K_SPACE:
                    shot = True
                if event.key == K_2:
                    UP = True
                    Angle = 0
                    y_player_change = -speed
                if event.key == K_0:
                    Angle = 180
                    DP = True
                    y_player_change = speed
                if event.key == K_3:
                    Angle = 270
                    RP = True
                    x_player_change = speed
                if event.key == K_1:
                    Angle = 90
                    LP = True
                    x_player_change = -speed
                if event.key == arriba:
                    UP2 = True
                    Angle2 = 0
                    y_player_change2 = -speed2
                if event.key == abajo:
                    Angle2 = 180
                    DP2 = True
                    y_player_change2 = speed2
                if event.key == derecha:
                    Angle2 = 270
                    RP2 = True
                    x_player_change2 = speed2
                if event.key == izquierda:
                    Angle2 = 90
                    LP2 = True
                    x_player_change2 = -speed2

            if event.type == pygame.KEYUP:
                if event.key == K_2:
                    UP = False
                    if UP:
                        Angle = 0
                        y_player_change = -speed
                    else:
                        y_player_change = 0
                if event.key == K_0:
                    DP = False
                    if DP:
                        Angle = 180
                        y_player_change = speed
                    else:
                        y_player_change = 0
                if event.key == K_3:
                    RP = False
                    if RP:
                        Angle = 270
                        x_player_change = speed
                    else:
                        x_player_change = 0
                if event.key == K_1:
                    LP = False
                    if LP:
                        Angle = 90
                        x_player_change = -speed
                    else:
                        x_player_change = 0
                if event.key == arriba:
                    UP2 = False
                    if UP2:
                        Angle2 = 0
                        y_player_change2 = -speed2
                    else:
                        y_player_change2 = 0
                if event.key == abajo:
                    DP2 = False
                    if DP2:
                        Angle2 = 180
                        y_player_change2 = speed2
                    else:
                        y_player_change2 = 0
                if event.key == derecha:
                    RP2 = False
                    if RP2:
                        Angle2 = 270
                        x_player_change2 = speed2
                    else:
                        x_player_change2 = 0
                if event.key == izquierda:
                    LP2 = False
                    if LP2:
                        Angle2 = 90
                        x_player_change2 = -speed2
                    else:
                        x_player_change2 = 0

        if UP:
            Angle = 0
        if DP:
            Angle = 180
        if RP:
            Angle = 270
        if LP:
            Angle = 90
        if UP and RP:
            Angle = 315
        if UP and LP:
            Angle = 45
        if DP and LP:
            Angle = 135
        if DP and RP:
            Angle = 225
        x_player += x_player_change
        y_player += y_player_change
        if x_player > (P_width * (496/1248)) and y_player < (P_height * (165/702)):
            if c + 1 == score and (Angle == 225 or Angle == 270 or Angle == 315):
                c += 1
            if c == score and (Angle == 90 or Angle == 45 or Angle == 135):
                c -= 1
        if x_player < (P_width*(272/1248)) and y_player < (P_height * (675/702)) and y_player > (P_height * (517/702)):
            if c == score and (Angle == 90 or Angle == 45 or Angle == 135):
                score += 1
            if c == score - 1 and (Angle == 225 or Angle == 270 or Angle == 315):
                score -= 1
        if x_player > P_width or x_player < 0 or y_player > P_height or y_player < 0:
            return crash('Player 1 has crashed', player2)
        if x_player < (P_width * 0.3382187148) and y_player > (P_height * (215 / 510)) and y_player < (
                P_height * (245 / 510)):
            if Angle == 180 or Angle == 135 or Angle == 225:
                y_player = P_height * (215 / 510)
            if Angle == 0 or Angle == 45 or Angle == 315:
                y_player = P_height * (245 / 510)
            if Angle == 90:
                x_player = P_width * 0.3382187148
        if x_player > (P_width * (104 / 887)) and x_player < (P_width * (684 / 887)) and y_player > (
                P_height * (100 / 510)) and y_player < (P_height * (126 / 510)):
            if Angle == 180 or Angle == 135 or Angle == 225:
                y_player = P_height * (100 / 510)
            if Angle == 0 or Angle == 45 or Angle == 315:
                y_player = P_height * (126 / 510)
            if Angle == 90:
                x_player = P_width * (684 / 887)
            if Angle == 270:
                x_player = P_width * (104 / 887)
        if x_player > (P_width * (641 / 887)) and y_player > (P_height * (192 / 510)) and y_player < (
                P_height * (216 / 510)):
            if Angle == 180 or Angle == 135 or Angle == 225:
                y_player = P_height * (192 / 510)
            if Angle == 0 or Angle == 45 or Angle == 315:
                y_player = P_height * (216 / 510)
            if Angle == 270:
                x_player = P_width * (641 / 887)
        if x_player > (P_width * (105 / 887)) and x_player < (P_width * (423 / 887)) and y_player > (
                P_height * (344 / 510)) and y_player < (P_height * (372 / 510)):
            if Angle == 180 or Angle == 135 or Angle == 225:
                y_player = P_height * (344 / 510)
            if Angle == 0 or Angle == 45 or Angle == 315:
                y_player = P_height * (372 / 510)
            if Angle == 90:
                x_player = P_width * (423 / 887)
            if Angle == 270:
                x_player = P_width * (105 / 887)
        if x_player > (P_width * (402 / 887)) and x_player < (P_width * (744 / 887)) and y_player > (
                P_height * (356 / 510)) and y_player < (P_height * (382 / 510)):
            if Angle == 180 or Angle == 135 or Angle == 225:
                y_player = P_height * (356 / 510)
            if Angle == 0 or Angle == 45 or Angle == 315:
                y_player = P_height * (382 / 510)
            if Angle == 90:
                x_player = P_width * (744 / 887)
            if Angle == 270:
                x_player = P_width * (402 / 887)
        if x_player > (P_width * (405 / 877)) and x_player < (P_width * (431 / 887)) and y_player > (
                P_height * (121 / 510)) and y_player < (P_height * (350 / 510)):
            if Angle == 90 or Angle == 45 or Angle == 135:
                x_player = P_width * (431 / 887)
            if Angle == 270 or Angle == 315 or Angle == 225:
                x_player = P_width * (405 / 887)
        if x_player > (P_width * (736 / 887)) and x_player < (P_width * (744 / 887)) and y_player > (
                P_height * (291 / 510)) and y_player < (P_height * (380 / 510)):
            if Angle == 90 or Angle == 45 or Angle == 135:
                x_player = P_width * (744 / 887)
            if Angle == 180:
                y_player = P_height * (291 / 510)
        ###########################################
        # diagonal
        if (int((0.7367 * x_player) - 699.61) < y_player + 2 and int((0.7367 * x_player) - 699.61) < y_player - 2) and (
                int((y_player + 699.61) / 0.7362) < x_player + 2 and int((y_player + 699.61) / 0.7362) < x_player - 2):
            if Angle == 90 or Angle == 45 or Angle == 135:
                x_player = P_width * 0.22
                y_player = P_height * 0.81
            if Angle == 270 or Angle == 225 or Angle == 315:
                x_player = P_width * 0.22
                y_player = P_height * 0.81
        ############################################
        if UP2:
            Angle2 = 0
        if DP2:
            Angle2 = 180
        if RP2:
            Angle2 = 270
        if LP2:
            Angle2 = 90
        if UP2 and RP2:
            Angle2 = 315
        if UP2 and LP2:
            Angle2 = 45
        if DP2 and LP2:
            Angle2 = 135
        if DP2 and RP2:
            Angle2 = 225
        if x_player2 > P_width or x_player2 < 0 or y_player2 > P_height or y_player2 < 0:
            return crash('Player 1 has crashed', player2)
        if x_player2 < (P_width * 0.3382187148) and y_player2 > (P_height * (215 / 510)) and y_player2 < (
                P_height * (245 / 510)):
            if Angle2 == 180 or Angle2 == 135 or Angle2 == 225:
                y_player2 = P_height * (215 / 510)
            if Angle2 == 0 or Angle2 == 45 or Angle2 == 315:
                y_player2 = P_height * (245 / 510)
            if Angle2 == 90:
                x_player2 = P_width * 0.3382187148
        if x_player2 > (P_width * (104 / 887)) and x_player2 < (P_width * (684 / 887)) and y_player2 > (
                P_height * (100 / 510)) and y_player2 < (P_height * (126 / 510)):
            if Angle2 == 180 or Angle2 == 135 or Angle2 == 225:
                y_player2 = P_height * (100 / 510)
            if Angle2 == 0 or Angle2 == 45 or Angle2 == 315:
                y_player2 = P_height * (126 / 510)
            if Angle2 == 90:
                x_player2 = P_width * (684 / 887)
            if Angle2 == 270:
                x_player2 = P_width * (104 / 887)
        if x_player2 > (P_width * (641 / 887)) and y_player2 > (P_height * (192 / 510)) and y_player2 < (
                P_height * (216 / 510)):
            if Angle2 == 180 or Angle2 == 135 or Angle2 == 225:
                y_player2 = P_height * (192 / 510)
            if Angle2 == 0 or Angle2 == 45 or Angle2 == 315:
                y_player2 = P_height * (216 / 510)
            if Angle2 == 270:
                x_player2 = P_width * (641 / 887)
        if x_player2 > (P_width * (105 / 887)) and x_player2 < (P_width * (423 / 887)) and y_player2 > (
                P_height * (344 / 510)) and y_player2 < (P_height * (372 / 510)):
            if Angle == 180 or Angle == 135 or Angle == 225:
                y_player2 = P_height * (344 / 510)
            if Angle == 0 or Angle == 45 or Angle == 315:
                y_player2 = P_height * (372 / 510)
            if Angle2 == 90:
                x_player2 = P_width * (423 / 887)
            if Angle2 == 270:
                x_player2 = P_width * (105 / 887)
        if x_player2 > (P_width * (402 / 887)) and x_player2 < (P_width * (744 / 887)) and y_player2 > (
                P_height * (356 / 510)) and y_player2 < (P_height * (382 / 510)):
            if Angle == 180 or Angle == 135 or Angle == 225:
                y_player2 = P_height * (356 / 510)
            if Angle2 == 0 or Angle2 == 45 or Angle2 == 315:
                y_player2 = P_height * (382 / 510)
            if Angle2 == 90:
                x_player2 = P_width * (744 / 887)
            if Angle2 == 270:
                x_player2 = P_width * (402 / 887)
        if x_player2 > (P_width * (405 / 877)) and x_player2 < (P_width * (431 / 887)) and y_player2 > (
                P_height * (121 / 510)) and y_player2 < (P_height * (350 / 510)):
            if Angle2 == 90 or Angle2 == 45 or Angle2 == 135:
                x_player2 = P_width * (431 / 887)
            if Angle2 == 270 or Angle2 == 315 or Angle2 == 225:
                x_player2 = P_width * (405 / 887)
        if x_player2 > (P_width * (736 / 887)) and x_player2 < (P_width * (744 / 887)) and y_player2 > (
                P_height * (291 / 510)) and y_player2 < (P_height * (380 / 510)):
            if Angle2 == 90 or Angle2 == 45 or Angle2 == 135:
                x_player2 = P_width * (744 / 887)
            if Angle2 == 180:
                y_player2 = P_height * (291 / 510)
        ###########################################
        # diagonal
        if (int((0.7367 * x_player2) - 699.61) < y_player2 + 2 and int((0.7367 * x_player2) - 699.61) < y_player2 - 2) and (
                int((y_player2 + 699.61) / 0.7362) < x_player2 + 2 and int((y_player2 + 699.61) / 0.7362) < x_player2 - 2):
            if Angle2 == 90 or Angle2 == 45 or Angle2 == 135:
                x_player2 = P_width * 0.22
                y_player2 = P_height * 0.84
            if Angle2 == 270 or Angle2 == 225 or Angle2 == 315:
                x_player2 = P_width * 0.22
                y_player2 = P_height * 0.84
        ############################################
        x_player2 += x_player_change2
        y_player2 += y_player_change2
        if x_player2 > (P_width * (496/1248)) and y_player2 < (P_height * (165/702)):
            if c2 + 1 == score2 and (Angle2 == 225 or Angle2 == 270 or Angle2 == 315):
                c2 += 1
            if c2 == score2 and (Angle2 == 90 or Angle2 == 45 or Angle2 == 135):
                c2 -= 1
        if x_player2 < (P_width*(272/1248)) and y_player2 < (P_height * (675/702)) and y_player2 > (P_height * (517/702)):
            if c2 == score2 and (Angle2 == 90 or Angle2 == 45 or Angle2 == 135):
                score2 += 1
            if c2 == score2 - 1 and (Angle2 == 225 or Angle2 == 270 or Angle2 == 315):
                score2 -= 1
        if x_player > P_width or x_player < 0 or y_player > P_height or y_player < 0:
            return crash('Player 1 has crashed', player2)
        if x_player2 > P_width or x_player2 < 0 or y_player2 > P_height or y_player2 < 0:
            return crash('Player 2 has crashed', player2)
        # Obstaculo 1
        if x_player2 < (P_width * 0.3382187148) and y_player2 > (P_height * (230 / 510)) and y_player2 < (
                P_height * (239 / 510)):
            score2 += -1
            x_player2 = P_width * 0.19
            y_player2 = P_height * 0.84
            Angle2 = 90
        pantalla.fill(white)
        pantalla.blit(pistaImg, (0, 0, 93, 40))
        pygame.draw.rect(pantalla, blue ,[int(P_width * 624/1248),int(P_height * 201/702),int(P_width * 114/1248),int(P_height * 69/702)])
        mostrarTexto(player_name + "'s" + ' score: ' + str(score - 1), int(P_width*680/1248), int(P_height * 220/702), 15 , light_green )
        mostrarTexto('Time: ' + str(int(180 - seconds)) + 's', (P_width * 100/1248), (P_height * 44/702), 15, blue)
        rotation(pantalla, carImg, x_player, y_player, Angle)
        if player2:
            rotation(pantalla, car2Img, x_player2, y_player2, Angle2)
            mostrarTexto(player2_name + "'s" + ' score: ' + str(score2 - 1), int(P_width * 680 / 1248), int(P_height * 240 / 702), 15, light_green)
        if x_player == x_player2 + 22 and x_player == x_player2 - 22 and y_player == y_player2 + 11 and y_player == y_player2 - 11:
            crash('Players crashed into each other', player2)
        mostrarTexto('Beta release v.0.3', (P_width * 0.10), (P_height * 0.95), 15, light_green)
        clock.tick(60)
        pygame.display.flip()

def mapa2(player_name, x_player, y_player, speed, speed_change, x_player_change, y_player_change, Angle, UP, DP, RP, LP, score, c, player2_name,
             x_player2, y_player2, speed2, speed_change2, x_player_change2, y_player_change2, Angle2, UP2, DP2, RP2,
             LP2, score2, c2, player2):
    #global G_exit
    t = pygame.time.get_ticks()
    G_exit2 = False
    while not G_exit2:
        seconds = (pygame.time.get_ticks() - t) / 1000
        if seconds > 180:
            G_exit2 = True
            x_player = P_width * 0.28
            y_player = P_height * 0.81

            speed = 5
            speed_change = 0

            x_player_change = 0
            y_player_change = 0

            Angle = 90

            score = 0
            c = 0

            UP, DP, RP, LP = False, False, False, False
            x_player2 = P_width * 0.28
            y_player2 = P_height * 0.84

            speed2 = 5
            speed_change2 = 0

            x_player_change2 = 0
            y_player_change2 = 0

            Angle2 = 90

            score2 = 0
            c2 = 0

            UP2, DP2, RP2, LP2 = False, False, False, False

            mapa3(player_name, x_player, y_player, speed, speed_change, x_player_change, y_player_change, Angle, UP, DP,
                  RP, LP,
                  score, c, player2_name, x_player2, y_player2, speed2, speed_change2, x_player_change2,
                  y_player_change2,
                  Angle2, UP2, DP2, RP2, LP2, score2, c2, player2)
        for event in pygame.event.get():
            print()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_menu(player2)
                if event.key == pygame.K_SPACE:
                    shot = True
                if event.key == K_2:
                    UP = True
                    Angle = 0
                    y_player_change = -speed
                if event.key == K_0:
                    Angle = 180
                    DP = True
                    y_player_change = speed
                if event.key == K_3:
                    Angle = 270
                    RP = True
                    x_player_change = speed
                if event.key == K_1:
                    Angle = 90
                    LP = True
                    x_player_change = -speed
                if event.key == arriba:
                    UP2 = True
                    Angle2 = 0
                    y_player_change2 = -speed2
                if event.key == abajo:
                    Angle2 = 180
                    DP2 = True
                    y_player_change2 = speed2
                if event.key == derecha:
                    Angle2 = 270
                    RP2 = True
                    x_player_change2 = speed2
                if event.key == izquierda:
                    Angle2 = 90
                    LP2 = True
                    x_player_change2 = -speed2

            if event.type == pygame.KEYUP:
                if event.key == K_2:
                    UP = False
                    if UP:
                        Angle = 0
                        y_player_change = -speed
                    else:
                        y_player_change = 0
                if event.key == K_0:
                    DP = False
                    if DP:
                        Angle = 180
                        y_player_change = speed
                    else:
                        y_player_change = 0
                if event.key == K_3:
                    RP = False
                    if RP:
                        Angle = 270
                        x_player_change = speed
                    else:
                        x_player_change = 0
                if event.key == K_1:
                    LP = False
                    if LP:
                        Angle = 90
                        x_player_change = -speed
                    else:
                        x_player_change = 0
                if event.key == arriba:
                    UP2 = False
                    if UP2:
                        Angle2 = 0
                        y_player_change2 = -speed2
                    else:
                        y_player_change2 = 0
                if event.key == abajo:
                    DP2 = False
                    if DP2:
                        Angle2 = 180
                        y_player_change2 = speed2
                    else:
                        y_player_change2 = 0
                if event.key == derecha:
                    RP2 = False
                    if RP2:
                        Angle2 = 270
                        x_player_change2 = speed2
                    else:
                        x_player_change2 = 0
                if event.key == izquierda:
                    LP2 = False
                    if LP2:
                        Angle2 = 90
                        x_player_change2 = -speed2
                    else:
                        x_player_change2 = 0

        if UP:
            Angle = 0
        if DP:
            Angle = 180
        if RP:
            Angle = 270
        if LP:
            Angle = 90
        if UP and RP:
            Angle = 315
        if UP and LP:
            Angle = 45
        if DP and LP:
            Angle = 135
        if DP and RP:
            Angle = 225
        x_player += x_player_change
        y_player += y_player_change
        ############################################
        if UP2:
            Angle2 = 0
        if DP2:
            Angle2 = 180
        if RP2:
            Angle2 = 270
        if LP2:
            Angle2 = 90
        if UP2 and RP2:
            Angle2 = 315
        if UP2 and LP2:
            Angle2 = 45
        if DP2 and LP2:
            Angle2 = 135
        if DP2 and RP2:
            Angle2 = 225
        ############################################
        x_player2 += x_player_change2
        y_player2 += y_player_change2
        pantalla.fill(white)
        pantalla.blit(pista3, (0, 0, 93, 40))
        pygame.draw.rect(pantalla, blue ,[int(P_width * 624/1248),int(P_height * 201/702),int(P_width * 114/1248),int(P_height * 69/702)])
        mostrarTexto(player_name + "'s" + ' score: ' + str(score - 1), int(P_width*680/1248), int(P_height * 220/702), 15 , light_green )
        mostrarTexto('Time: ' + str(int(180 - seconds)) + 's', (P_width * 100/1248), (P_height * 44/702), 15, blue)
        rotation(pantalla, carImg, x_player, y_player, Angle)
        if player2:
            rotation(pantalla, car2Img, x_player2, y_player2, Angle2)
            mostrarTexto(player2_name + "'s" + ' score: ' + str(score2 - 1), int(P_width * 680 / 1248), int(P_height * 240 / 702), 15, light_green)
        if x_player == x_player2 + 22 and x_player == x_player2 - 22 and y_player == y_player2 + 11 and y_player == y_player2 - 11:
            crash('Players crashed into each other', player2)
        mostrarTexto('Beta release v.0.3', (P_width * 0.10), (P_height * 0.95), 15, light_green)
        clock.tick(60)
        pygame.display.flip()

def mapa1(player_name, x_player, y_player, speed, speed_change, x_player_change, y_player_change, Angle, UP, DP, RP, LP, score, c, player2_name,
             x_player2, y_player2, speed2, speed_change2, x_player_change2, y_player_change2, Angle2, UP2, DP2, RP2,
             LP2, score2, c2, player2):
    #global G_exit
    G_exit1 = False
    t = pygame.time.get_ticks()
    while not G_exit1:
        seconds = (pygame.time.get_ticks() - t) / 1000
        if seconds > 180:
            G_exit1 = True
            x_player = P_width * 0.28
            y_player = P_height * 0.87

            speed = 5
            speed_change = 0

            x_player_change = 0
            y_player_change = 0

            Angle = 90

            score = 0
            c = 0

            UP, DP, RP, LP = False, False, False, False
            x_player2 = P_width * 0.28
            y_player2 = P_height * 0.90

            speed2 = 5
            speed_change2 = 0

            x_player_change2 = 0
            y_player_change2 = 0

            Angle2 = 90

            score2 = 0
            c2 = 0
            mapa2(player_name, x_player, y_player, speed, speed_change, x_player_change, y_player_change, Angle, UP, DP,
                  RP, LP,
                  score, c, player2_name, x_player2, y_player2, speed2, speed_change2, x_player_change2,
                  y_player_change2,
                  Angle2, UP2, DP2, RP2, LP2, score2, c2, player2)
        for event in pygame.event.get():
           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_menu(player2)
                if event.key == pygame.K_SPACE:
                    shot = True
                if event.key == K_2:
                    UP = True
                    Angle = 0
                    y_player_change = -speed
                if event.key == K_0:
                    Angle = 180
                    DP = True
                    y_player_change = speed
                if event.key == K_3:
                    Angle = 270
                    RP = True
                    x_player_change = speed
                if event.key == K_1:
                    Angle = 90
                    LP = True
                    x_player_change = -speed
                if event.key == arriba:
                    UP2 = True
                    Angle2 = 0
                    y_player_change2 = -speed2
                if event.key == abajo:
                    Angle2 = 180
                    DP2 = True
                    y_player_change2 = speed2
                if event.key == derecha:
                    Angle2 = 270
                    RP2 = True
                    x_player_change2 = speed2
                if event.key == izquierda:
                    Angle2 = 90
                    LP2 = True
                    x_player_change2 = -speed2

            if event.type == pygame.KEYUP:
                if event.key == K_2:
                    UP = False
                    if UP:
                        Angle = 0
                        y_player_change = -speed
                    else:
                        y_player_change = 0
                if event.key == K_0:
                    DP = False
                    if DP:
                        Angle = 180
                        y_player_change = speed
                    else:
                        y_player_change = 0
                if event.key == K_3:
                    RP = False
                    if RP:
                        Angle = 270
                        x_player_change = speed
                    else:
                        x_player_change = 0
                if event.key == K_1:
                    LP = False
                    if LP:
                        Angle = 90
                        x_player_change = -speed
                    else:
                        x_player_change = 0
                if event.key == arriba:
                    UP2 = False
                    if UP2:
                        Angle2 = 0
                        y_player_change2 = -speed2
                    else:
                        y_player_change2 = 0
                if event.key == abajo:
                    DP2 = False
                    if DP2:
                        Angle2 = 180
                        y_player_change2 = speed2
                    else:
                        y_player_change2 = 0
                if event.key == derecha:
                    RP2 = False
                    if RP2:
                        Angle2 = 270
                        x_player_change2 = speed2
                    else:
                        x_player_change2 = 0
                if event.key == izquierda:
                    LP2 = False
                    if LP2:
                        Angle2 = 90
                        x_player_change2 = -speed2
                    else:
                        x_player_change2 = 0

        if UP:
            Angle = 0
        if DP:
            Angle = 180
        if RP:
            Angle = 270
        if LP:
            Angle = 90
        if UP and RP:
            Angle = 315
        if UP and LP:
            Angle = 45
        if DP and LP:
            Angle = 135
        if DP and RP:
            Angle = 225
        x_player += x_player_change
        y_player += y_player_change
        ############################################
        if UP2:
            Angle2 = 0
        if DP2:
            Angle2 = 180
        if RP2:
            Angle2 = 270
        if LP2:
            Angle2 = 90
        if UP2 and RP2:
            Angle2 = 315
        if UP2 and LP2:
            Angle2 = 45
        if DP2 and LP2:
            Angle2 = 135
        if DP2 and RP2:
            Angle2 = 225
        ############################################
        x_player2 += x_player_change2
        y_player2 += y_player_change2
        pantalla.fill(white)
        pantalla.blit(pista2, (0, 0, 93, 40))
        pygame.draw.rect(pantalla, blue ,[int(P_width * 624/1248),int(P_height * 201/702),int(P_width * 114/1248),int(P_height * 69/702)])
        mostrarTexto(player_name + "'s" + ' score: ' + str(score - 1), int(P_width*680/1248), int(P_height * 220/702), 15 , light_green )
        mostrarTexto('Time: ' + str(int(180 - seconds)) + 's', (P_width * 100/1248), (P_height * 44/702), 15, blue)
        rotation(pantalla, carImg, x_player, y_player, Angle)
        if player2:
            rotation(pantalla, car2Img, x_player2, y_player2, Angle2)
            mostrarTexto(player2_name + "'s" + ' score: ' + str(score2 - 1), int(P_width * 680 / 1248), int(P_height * 240 / 702), 15, light_green)
        if x_player == x_player2 + 22 and x_player == x_player2 - 22 and y_player == y_player2 + 11 and y_player == y_player2 - 11:
            crash('Players crashed into each other', player2)
        mostrarTexto('Beta release v.0.3', (P_width * 0.10), (P_height * 0.95), 15, light_green)
        clock.tick(60)
        pygame.display.flip()


# Se encarga de cargar el juego y la pista , asi como sus jugadores
def loop_juego(player_name, x_player, y_player, speed, speed_change, x_player_change, y_player_change, Angle, UP, DP, RP, LP, score, c, player2_name,
               x_player2, y_player2, speed2, speed_change2, x_player_change2, y_player_change2, Angle2, UP2, DP2, RP2,
               LP2, score2, c2, player2 ):
        # Loop para mover al jugador(es)
    mapa1(player_name, x_player, y_player, speed, speed_change, x_player_change, y_player_change, Angle, UP, DP, RP, LP, score, c,player2_name, x_player2, y_player2, speed2, speed_change2, x_player_change2, y_player_change2, Angle2, UP2, DP2, RP2, LP2, score2, c2, player2)



    # Loop que carga los parametros iniciales del juego
def loopdejuego(player2):
    x_bot = P_width * 0.24
    y_bot = P_height * 0.82

    x_player = P_width * 0.28
    y_player = P_height * 0.81

    speed = 5
    speed_change = 0

    x_player_change = 0
    y_player_change = 0

    Angle = 90

    score = 0
    c = 0

    UP, DP, RP, LP = False, False, False, False
    x_player2 = P_width * 0.28
    y_player2 = P_height * 0.84

    speed2 = 5
    speed_change2 = 0

    x_player_change2 = 0
    y_player_change2 = 0

    Angle2 = 90

    score2 = 0
    c2 = 0

    UP2, DP2, RP2, LP2 = False, False, False, False

    recover_input('', x_player, y_player, speed, speed_change, x_player_change, y_player_change, Angle, UP, DP, RP, LP, score, c, '',  x_player2, y_player2, speed2, speed_change2, x_player_change2, y_player_change2, Angle2, UP2, DP2, RP2, LP2, score2, c2, player2)


menus()
