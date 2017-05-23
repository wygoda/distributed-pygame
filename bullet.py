import pygame, math
from pygame.locals import *
# from player import Player

class Bullet:
	def __init__(self, id, player):
		self.id = id
		self.rect = pygame.Rect(player.rect.centerx, player.rect.centery, 10, 10)
		self.angle = player.angle
		self.speed = 10
		
		#components of bullet velocity vector
		self.velocityX = -math.cos(player.angleRad)
		self.velocityY = -math.sin(player.angleRad)
		
		#got to normalize velocity so the bullet won't be faster when fired diagonally
		euclid_dist = math.sqrt(math.pow(self.velocityX,2)+math.pow(self.velocityY,2))
		self.velocityX = self.velocityX*self.speed*euclid_dist
		self.velocityY = self.velocityY*self.speed*euclid_dist
		
		self.image = pygame.image.load("bullet.png")
		self.image = pygame.transform.rotate(self.image,90 - self.angle)
		
	def update(self):
		self.rect.move_ip(self.velocityX,self.velocityY)#move rect in place by the velocity