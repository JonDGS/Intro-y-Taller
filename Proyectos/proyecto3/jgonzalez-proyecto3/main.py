import sys, pygame
from pygame.locals import *
from math import *
import Car_Class
import SavesManager
import menus

pygame.init()

WIDTH  = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS    = pygame.time.Clock()
track_time = 15

pygame.display.set_caption('road to cartaguito')

track = pygame.image.load('track2.png').convert()
track2 = pygame.image.load('track3.png').convert()
track3 = pygame.image.load('track.png').convert()

#Check if car is on track
def on_track(sprite, pista):
    #Color beneath the car
    if sprite.x > 1 and sprite.x < WIDTH - 1 and sprite.y > 1 and sprite.y < HEIGHT - 1:
        if pista.get_at((int(sprite.x), int(sprite.y))).r == 163 or pista.get_at((int(sprite.x), int(sprite.y))).r == 0 or pista.get_at((int(sprite.x), int(sprite.y))).r == 255:
            print(True)
            return True
        else:
            print(False)
            return False
    else:
        pass
#Loop del nivel 3
def level_three(car1, car2):
    car1.x, car1.y = (334, 524)
    if car2 != False:
        car2.x, car2.y = (334, 484)
        car2.angle = 180
        car2.third = True
    car1.angle = 180
    car1.third = True
    running = True
    t = pygame.time.get_ticks()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menus.pause_menu()
        seconds = (pygame.time.get_ticks() - t) / 1000
        if seconds > track_time:
            running = False
        #Blit the track to the background
        SCREEN.blit(track3, (0, 0))
        #print(car1.self)

        #Test if the game has been quit
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        car1.move()
        car1.wrap()
        car1.render()
        menus.mostrarTexto(car1.username + ' score: ' + str(car1.initial_score), 400, 300,15, menus.black)
        if car2 != False:
            car2.move()
            car2.wrap()
            car2.render()
            menus.mostrarTexto(car2.username + ' score: ' + str(car2.initial_score), 400, 325,15, menus.black)
        menus.mostrarTexto('Time: ' + str(int(180-seconds)), 50, 25,15, menus.red)

        pygame.display.update()
        FPS.tick(30)
    SavesManager.leaderboard(car1.username, car1.initial_score, car1.initial_laps, car1.initial_hits)
    if car2 != False:
        SavesManager.leaderboard(car2.username, car2.initial_score, car2.initial_laps, car2.initial_hits)
    running = False
    menus.menu_principal()
#Loop del nivel 2
def level_two(car1, car2):
    car1.x, car1.y = (370, 47)
    if car2 != False:
        car2.x, car2.y = (370, 77)
        car2.angle = 0
        car2.second = True
    else:
        car2 = False
    car1.angle = 0
    car1.second = True
    running = True
    t = pygame.time.get_ticks()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menus.pause_menu()
        seconds = (pygame.time.get_ticks() - t) / 1000
        if seconds > track_time:
            running = False
            level_three(car1, car2)
        #Blit the track to the background
        SCREEN.blit(track2, (0, 0))
        #print(car1.self)

        #Test if the game has been quit
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        car1.move()
        car1.wrap()
        car1.render()
        menus.mostrarTexto(car1.username + ' score: ' + str(car1.initial_score), 400, 300,15, menus.black)
        if car2 != False:
            car2.move()
            car2.wrap()
            car2.render()
            menus.mostrarTexto(car2.username + ' score: ' + str(car2.initial_score), 400, 325,15, menus.black)
        menus.mostrarTexto('Time: ' + str(int(180-seconds)), 50, 25,15, menus.red)
        pygame.display.update()
        FPS.tick(30)
    level_three(car1, car2)
#Loop del nivel 1
def level_one(car1, car2):
    car1.x, car1.y = (53, 370)
    if car2 != False:
        car2.x, car2.y = (83, 370)
        car2.angle = 90
        car2.first = True
    car1.angle = 90
    car1.first = True
    running = True
    t = pygame.time.get_ticks()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menus.pause_menu()
        seconds = (pygame.time.get_ticks() - t) / 1000
        if seconds > track_time:
            running = False
            level_two(car1, car2)
        #Blit the track to the background
        SCREEN.blit(track, (0, 0))
        #print(car1.self)

        #Test if the game has been quit
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        mouse = pygame.mouse.get_pos()
        car1.move()
        car1.wrap()
        car1.render()
        menus.mostrarTexto(car1.username + ' score: ' + str(car1.initial_score), 400, 300,15, menus.black)
        if car2 != False:
            car2.move()
            car2.wrap()
            car2.render()
            menus.mostrarTexto(car2.username + ' score: ' + str(car2.initial_score), 400, 325,15, menus.black)
        menus.mostrarTexto('Time: ' + str(int(180-seconds)), 50, 25,15, menus.black)
        pygame.display.update()
        FPS.tick(30)
    level_two(car1, car2)

#Class Car
class Car(pygame.sprite.Sprite):
    #Constructor car
    def __init__(self, start_pos, start_angle, image, keys, username, initial_score, initial_laps, initial_hits):
        '''Initialises the Car object'''
        super().__init__()
        self.x     = start_pos[0]
        self.y     = start_pos[1]
        self.angle = start_angle
        self.speed = 0

        self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), (48, 48))

        self.rotcar   = pygame.transform.rotate(self.image, self.angle)

        self.keys = keys
        self.username = username
        self.initial_score = initial_score
        self.initial_laps = initial_laps
        self.initial_hits = initial_hits
        self.check = 0
        self.first = False
        self.second = False
        self.third = False

    #Checks checkpoints
    def validar_check(self, x, x2, y, angle_range1):
        if self.x > x and self.x < x2 and self.y == y:
            if self.check + 1 == self.goal and (self.angle > angle_range1[0] and self.angle < angle_range1[1]):
                self.check += 1
            else:
                self.check -= 1

    #Checks laps
    def validar_laps(self, x, x2, y, angle_range1):
        if self.x > x and self.x < x2 and self.y == y:
            if self.check == self.goal and (self.angle > angle_range1[0] and self.angle < angle_range1[1]):
                self.goal += 1
            else:
                self.goal -= 1

    #Move car
    def move(self, forward_speed = 1, rearward_speed = 0.2):
        '''Moves the car when the arrow keys are pressed'''
        keys = pygame.key.get_pressed()

        #Move the car depending on which keys have been pressed
        if keys[self.keys[0]]:
            self.angle += self.speed
        if keys[self.keys[1]]:
            self.angle -= self.speed
        if keys[self.keys[2]]:
            self.speed += forward_speed
        if keys[self.keys[3]]:
            self.speed -= rearward_speed

        #Keep the angle between 0 and 359 degrees
        self.angle %= 359

        #Apply friction
        if self.first and not self.second and not self.third:
            if on_track(self, track2): self.speed *= 0.95
        elif self.first and self.second and not self.third:
            if on_track(self, track3): self.speed *= 0.95
        elif self.first and self.second and self.third:
            if on_track(self, track): self.speed *= 0.95
        else: self.speed *= 0.75

        #Change the position of the car
        self.x += self.speed * cos(radians(self.angle))
        self.y -= self.speed * sin(radians(self.angle))

    def wrap(self):
        '''Wrap the car around the edges of the screen'''
        self.wrap_around = False

        if self.x <  0 :
            self.x += WIDTH
            self.wrap_around = True

        if self.x  + self.rotcar.get_width() > WIDTH:
            self.x -= WIDTH
            self.wrap_around = True

        if self.y  < 0:
            self.y += HEIGHT
            self.wrap_around = True

        if self.y + self.rotcar.get_height() > HEIGHT:
            self.y -= HEIGHT
            self.wrap_around = True

        if self.wrap_around:
            SCREEN.blit(self.rotcar, self.rotcar.get_rect(center = (self.x, self.y)))

        self.x %= WIDTH
        self.y %= HEIGHT

    def render(self):
        '''Renders the car on the screen'''
        self.rotcar   = pygame.transform.rotate(self.image, self.angle)

        SCREEN.blit(self.rotcar, self.rotcar.get_rect(center = (self.x, self.y)))

#Loop princioal del juego
def main(user1, user2):
    car1  = Car((0, 0), 0, 'Car1.png', [K_LEFT, K_RIGHT, K_UP, K_DOWN], user1, 20, 8, 12)
    if user2 != False:
        car2  = Car((0, 0), 0, 'Car.png', [K_a, K_d, K_w, K_s], user2, 12, 6, 6)
    else:
        car2 = user2
    level_one(car1, car2)

menus.menu_principal()

