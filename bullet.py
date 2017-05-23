import pygame, math
from pygame.locals import *
# from player import Player

class Bullet:
    def __init__(self, id, player):
        self.id = id
        self.rect = pygame.Rect(player.rect.centerx, player.rect.centery, 10, 10)
        self.angle = -player.angle + 90
        self.velocity = 2
        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.rotate(self.image, -self.angle + 90)

    def update(self):
        self.rect.centerx += math.sin(self.angle) * self.velocity
        self.rect.centery += math.cos(self.angle) * self.velocity
