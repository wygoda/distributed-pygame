import pygame, math
from pygame.locals import *
# from player import Player

class Bullet:
	def __init__(self, id, player,mousePos):
		self.id = id
		self.rect = pygame.Rect(player.rect.centerx, player.rect.centery, 10, 10)
		self.angle = player.angle
		self.velocityX = -math.cos(player.angleRad)
		self.velocityY = -math.sin(player.angleRad)
		self.image = pygame.image.load("bullet.png")
		self.image = pygame.transform.rotate(self.image, self.angle)
		print('kat gracza    '+str(player.angle))
		print('kat graczarad '+str(player.angleRad))
		print('velocityX     '+str(self.velocityX))
		print('velocityY     '+str(self.velocityY))

	def update(self):
	
		self.rect.centerx += self.velocityX
		self.rect.centery += self.velocityY
