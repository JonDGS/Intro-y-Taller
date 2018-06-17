import pygame
from pygame.locals import *
from math import *
import main

class Car(pygame.sprite.Sprite):
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
        self.initial_score = initial_score
        self.initial_laps = initial_laps
        self.initial_hits = initial_hits
        self.goal = 0
        self.check = 0

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
        if main.on_track(self): self.speed *= 0.95
        else: self.speed *= 0.75

        #Change the position of the car
        self.x += self.speed * cos(radians(self.angle))
        self.y -= self.speed * sin(radians(self.angle))

    def wrap(self):
        '''Wrap the car around the edges of the screen'''
        self.wrap_around = False

        if self.x <  0 :
            self.x += main.WIDTH
            self.wrap_around = True

        if self.x  + self.rotcar.get_width() > main.WIDTH:
            self.x -= main.WIDTH
            self.wrap_around = True

        if self.y  < 0:
            self.y += main.HEIGHT
            self.wrap_around = True

        if self.y + self.rotcar.get_height() > main.HEIGHT:
            self.y -= main.HEIGHT
            self.wrap_around = True

        if self.wrap_around:
            main.SCREEN.blit(self.rotcar, self.rotcar.get_rect(center = (self.x, self.y)))

        self.x %= main.WIDTH
        self.y %= main.HEIGHT

    def render(self):
        '''Renders the car on the screen'''
        self.rotcar   = pygame.transform.rotate(self.image, self.angle)

        main.SCREEN.blit(self.rotcar, self.rotcar.get_rect(center = (self.x, self.y)))