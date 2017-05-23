import pygame, math
from pygame.locals import *
# from player import Player

bullet_size = 10

class Bullet:
    def __init__(self, id, player):
        self.id = id
        self.rect = pygame.Rect(player.rect.centerx - bullet_size/2, player.rect.centery - bullet_size/2, bullet_size, bullet_size)
        self.angle = player.angle
        self.speed = 10

		#components of bullet velocity vector
        self.velocityX = -math.cos(player.angleRad)
        self.velocityY = -math.sin(player.angleRad)

        #got to normalize velocity so the bullet won't be faster when fired diagonally
        velocityMagnitude = math.sqrt(math.pow(self.velocityX,2)+math.pow(self.velocityY,2))
        # print(velocityMagnitude)
        self.velocityX = self.velocityX*self.speed*velocityMagnitude
        self.velocityY = self.velocityY*self.speed*velocityMagnitude

        #maćkowe pieprzenie
        # self.velocityX = math.cos(player.angleRad)
        # self.velocityY = math.sin(player.angleRad)

        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.rotate(self.image,90 - self.angle)

    def update(self):
        self.rect.move_ip(self.velocityX,self.velocityY)#move rect in place by the velocity

        #maćkowe pieprzenie
        # self.rect.centerx -= self.velocityX * self.speed
        # self.rect.centery -= self.velocityY * self.speed
