import pygame
from pygame.locals import *

class Player:
    def __init__(self, id, rect):
        self.id = id
        self.rect = rect
        self.image = pygame.image.load("cross.png")
        
