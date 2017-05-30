import pygame, math
from pygame.locals import *
# from player import Player

bullet_size = 10

class Bullet:
	def __init__(self, id, player):
		self.id = id
		self.rect = pygame.Rect(player.rect.centerx - bullet_size/2, player.rect.centery - bullet_size/2, bullet_size, bullet_size)
		self.speed = 10

		#components of bullet velocity vector
		self.velocityX = -math.cos(player.angleRad)*self.speed
		self.velocityY = -math.sin(player.angleRad)*self.speed

		self.image = pygame.image.load("sprites/bullet.png")
		self.image = pygame.transform.rotate(self.image,90 - player.angle)
		self.rect.move_ip(self.velocityX*5,self.velocityY*5)
	def update(self):
		self.rect.move_ip(self.velocityX,self.velocityY)#move rect in place by the velocity
