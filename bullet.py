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
		#do tego momentu sa dobrze wyliczone skladowe x i y predkosci pocisku
		#pokrec sie i postrzelaj sobie 
		#pamietaj ze tu lewy gorny rog to (0,0) i x rosna w prawo a y w dol
		#jak patrzy w prawo to x rosnie o 1 a y jest 0
		#jak patrzy w gore to x jest 0 a y maleje o 1
		#jak patrzy w lewo to x maleje o 1 a y = 0
		#jak w dol to x = 0 a y = 1
		#wiec ta trygonometria jest juz dobrze tylko trzeba znormalizowac bo inaczej 
		#na skosy bedzie leciec z v = sqrt(2) a po osiach z v=1
		#nie mam tylko pojecia czemu to nadal lata jak chce
		print('kat gracza    '+str(player.angle))
		print('kat graczarad '+str(player.angleRad))
		print('velocityX     '+str(self.velocityX))
		print('velocityY     '+str(self.velocityY))

	def update(self):
	
		self.rect.centerx += self.velocityX
		self.rect.centery += self.velocityY
