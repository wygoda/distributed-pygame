import pygame
from pygame.locals import *
from bullet import Bullet

class Player:
    def __init__(self, id, rect):
        self.id = id
        self.rect = rect
        self.image = pygame.image.load("cross.png")
        self.angle = 90

    def shoot(self):
        print("strzelam")
        b = Bullet(1, self)
        return b
