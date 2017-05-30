#! /usr/bin/python3

import pygame, sys, math, bullet, random, socket, pickle
from pygame.locals import *
from player import Player
from gamestate import Gamestate

def rot_center(image, angle):
	"""rotate an image while keeping its center and size"""
	orig_rect = image.get_rect()
	rot_image = pygame.transform.rotate(image, angle)
	rot_rect = orig_rect.copy()
	rot_rect.center = rot_image.get_rect().center
	rot_image = rot_image.subsurface(rot_rect).copy()
	return rot_image

host, port = 'localhost', 7777
addr = (host, port)
buf = 2048
server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_connection.connect(addr)

pygame.init()

WINDOWWIDTH = 700
WINDOWHEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

mainClock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# p1 = Player(1, pygame.Rect(300,300,50,50))
bin_recvd_player = server_connection.recv(buf)
p1 = pickle.loads(bin_recvd_player)
print(p1.rect)
tmp_player_image = pygame.image.load("sprites/cross.png")
tmp_bullet_image = pygame.image.load("sprites/bullet.png")



#bullety beda na serwerze
# bullets = []

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

print("przed petla")
#GAME LOOP
while True:
	bin_gamestate = server_connection.recv(buf)
	gamestate = pickle.loads(bin_gamestate)
	print("asd")
	print("liczba graczy: {}".format(len(gamestate.players)))

	for p in gamestate.players:
		if p.id == p1.id:
			p1 = p
			break

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
			if event.key == K_x:
				p1.shoot()
				print(p1)

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

	print(p1)
	bin_player = pickle.dumps(p1)
	sent_bytes_count = server_connection.send(bin_player)
	if sent_bytes_count:
		print("bin_player size: {}; sent_bytes_count: {}".format(len(bin_player), sent_bytes_count))


	#Draw local player
	rotatedPlayerImage = rot_center(tmp_player_image, 90-p1.angle)
	windowSurface.blit(rotatedPlayerImage, p1.rect)
	for b in p1.bullets:
		rotated_tmp_bullet_image = pygame.transform.rotate(tmp_bullet_image,90 - b.owner.angle)
		windowSurface.blit(rotated_tmp_bullet_image, b.rect)

	#Draw players from the server
	for p in gamestate.players:
		if p.id != p1.id:
			rotatedPlayerImage = rot_center(tmp_player_image, 90-p.angle)
			# Draw the player onto the surface.
			windowSurface.blit(rotatedPlayerImage, p.rect)

			# Draw bullets
			for b in p.bullets:
				rotated_tmp_bullet_image = pygame.transform.rotate(tmp_bullet_image,90 - b.owner.angle)
				windowSurface.blit(rotated_tmp_bullet_image, b.rect)


	pygame.display.update()
	mainClock.tick(60)
