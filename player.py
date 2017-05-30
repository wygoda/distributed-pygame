import pygame
from pygame.locals import *
from bullet import Bullet

class Player:
    def __init__(self, id, rect):
        self.id = id
        self.rect = rect

        #it generates a pickling issue on windows
        # self.image = pygame.image.load("sprites/cross.png")
        self.angle = 0
        self.angleRad = 0
        self.bullets = []
        self.dead = False

    def shoot(self):
        b = Bullet(-1, self)
        self.bullets.append(b)
        return b

    def __str__(self):
        bullets = ",".join(str(b) for b in self.bullets)
        return "PLAYER: id:{}, {}, bullets:{}".format(self.id, self.rect, bullets)
