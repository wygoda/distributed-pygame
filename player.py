import pygame
from pygame.locals import *
from bullet import Bullet

class Player:
    def __init__(self, id, rect):
        self.id = id
        self.rect = rect
        self.image = pygame.image.load("sprites/player.png")
        self.angle = 0
        self.angleRad = 0

    def shoot(self):
        b = Bullet(1, self)
        return b
