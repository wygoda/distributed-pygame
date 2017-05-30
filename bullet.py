import pygame, math
from pygame.locals import *
# from player import Player

bullet_size = 10

class Bullet:
	def __init__(self, id, player):
		self.id = id
		self.owner = player
		self.rect = pygame.Rect(player.rect.centerx - bullet_size/2, player.rect.centery - bullet_size/2, bullet_size, bullet_size)
		self.speed = 10
		self.ttl = 600 #time to live

		#components of bullet velocity vector
		self.velocityX = -math.cos(player.angleRad)*self.speed
		self.velocityY = -math.sin(player.angleRad)*self.speed

		#it generates a pickling issue on windows
		# self.image = pygame.image.load("sprites/bullet.png")
		# self.image = pygame.transform.rotate(self.image,90 - player.angle)

	def update(self):
		print("bullet.update called")
		self.rect.move_ip(self.velocityX,self.velocityY)#move rect in place by the velocity
		self.ttl -= 1

	def __str__(self):
		return "{} ttl:{}".format(self.rect, self.ttl)
