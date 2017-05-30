#! /usr/bin/python3

import pygame, sys, math, bullet, random
from pygame.locals import *
from player import Player

def rot_center(image, angle):
	"""rotate an image while keeping its center and size"""
	orig_rect = image.get_rect()
	rot_image = pygame.transform.rotate(image, angle)
	rot_rect = orig_rect.copy()
	rot_rect.center = rot_image.get_rect().center
	rot_image = rot_image.subsurface(rot_rect).copy()
	return rot_image

pygame.init()

WINDOWWIDTH = 700
WINDOWHEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

mainClock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

p1 = Player(1, pygame.Rect(300,300,50,50))
p1Image = p1.image

#bullety beda na serwerze
bullets = []

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

#GAME LOOP
while True:
	mouse_pos = pygame.mouse.get_pos()
	p1.angleRad = math.atan2(p1.rect.centery - mouse_pos[1], p1.rect.centerx - mouse_pos[0])
	p1.angle = math.degrees(p1.angleRad)
	# print(str(mouse_pos) + " " + str(p1.angleRad))

	# Check for events.
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			# Change the keyboard variables.
			if event.key == K_LEFT or event.key == K_a:
				moveRight = False
				moveLeft = True
			if event.key == K_RIGHT or event.key == K_d:
				moveLeft = False
				moveRight = True
			if event.key == K_UP or event.key == K_w:
				moveDown = False
				moveUp = True
			if event.key == K_DOWN or event.key == K_s:
				moveUp = False
				moveDown = True
		if event.type == KEYUP:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
			if event.key == K_LEFT or event.key == K_a:
				moveLeft = False
			if event.key == K_RIGHT or event.key == K_d:
				moveRight = False
			if event.key == K_UP or event.key == K_w:
				moveUp = False
			if event.key == K_DOWN or event.key == K_s:
				moveDown = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0]:
				bullets.append(p1.shoot())

	windowSurface.fill(WHITE)

	# Move the player.
	if moveDown and p1.rect.bottom < WINDOWHEIGHT:
		p1.rect.top += MOVESPEED
	if moveUp and p1.rect.top > 0:
		p1.rect.top -= MOVESPEED
	if moveLeft and p1.rect.left > 0:
		p1.rect.left -= MOVESPEED
	if moveRight and p1.rect.right < WINDOWWIDTH:
		p1.rect.right += MOVESPEED

	rotatedPlayerImage = rot_center(p1Image, 90-p1.angle)
	# Draw the player onto the surface.
	windowSurface.blit(rotatedPlayerImage, p1.rect)

	for b in bullets:
		b.update()
	for b in bullets:
		windowSurface.blit(b.image, b.rect)

	pygame.display.update()
	mainClock.tick(60)
