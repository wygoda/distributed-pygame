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
buf = 3072
server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_connection.connect(addr)

pygame.init()

WINDOWWIDTH = 1024
WINDOWHEIGHT = 640
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

mainClock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# p1 = Player(1, pygame.Rect(300,300,50,50))
bin_recvd_player = server_connection.recv(buf)
p1 = pickle.loads(bin_recvd_player)
print(p1.rect)
player_image = pygame.image.load("sprites/player.png")
bullet_image = pygame.image.load("sprites/bullet.png")

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

#stany do mowiace z ktorej strony jest kolizja
fromLeft = False
fromRight = False
fromTop = False
fromBottom = False

MOVESPEED = 6

#GAME LOOP
while True:
	bin_gamestate = server_connection.recv(buf)
	gamestate = pickle.loads(bin_gamestate)
	print("liczba graczy: {}".format(len(gamestate.players)))

	for p in gamestate.players:
		if p.id == p1.id:
			p1 = p
			break
	print(p1)

	mouse_pos = pygame.mouse.get_pos()
	p1.angleRad = math.atan2(p1.rect.centery - mouse_pos[1], p1.rect.centerx - mouse_pos[0])
	p1.angle = math.degrees(p1.angleRad)
	# print(str(mouse_pos) + " " + str(p1.angleRad))

	windowSurface.fill(WHITE)

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
				p1.shoot()
	if not p1.dead:
		#sprawdzanie kolizji gracza p1 z innymi graczami z listy players
		possible_collisions = [p for p in gamestate.players if p.id != p1.id and not p.dead]#players.remove(p1)#trzeba usunac bo inaczej wykrywa zderzenie z samym soba
		indexOfOpponent = p1.rect.collidelist(possible_collisions)#zwraca index zioma z ktorym sie zderza
		if indexOfOpponent != -1:
			opponent_id = possible_collisions[indexOfOpponent].id
			for p in gamestate.players:
				if p.id == opponent_id:
					opponent = p.rect
					break
			if p1.rect.bottom >= opponent.top and p1.rect.top <= opponent.top:
				fromBottom = True
			else:
				fromTop = True;
			if p1.rect.left <= opponent.right and p1.rect.left >=  opponent.left:
				fromLeft = True;
			else:
				fromRight = True
		# players.append(p1)#dodajemy do listy wczesniej skasowanego gracza
		# Move the player.
		if moveDown and p1.rect.bottom < WINDOWHEIGHT and not fromBottom:
			p1.rect.top += MOVESPEED
		if moveUp and p1.rect.top > 0 and not fromTop:
			p1.rect.top -= MOVESPEED
		if moveLeft and p1.rect.left > 0 and not fromLeft:
			p1.rect.left -= MOVESPEED
		if moveRight and p1.rect.right < WINDOWWIDTH and not fromRight:
			p1.rect.right += MOVESPEED
		fromTop=False;
		fromBottom=False;
		fromLeft=False;
		fromRight=False;

		#Draw local player
		rotatedPlayerImage = rot_center(player_image, 90-p1.angle)
		windowSurface.blit(rotatedPlayerImage, p1.rect)
		for b in p1.bullets:
			rotated_bullet_image = pygame.transform.rotate(bullet_image,90 - b.owner.angle)
			windowSurface.blit(rotated_bullet_image, b.rect)

	bin_player = pickle.dumps(p1)
	sent_bytes_count = server_connection.send(bin_player)
	if sent_bytes_count:
		print("bin_player size: {}; sent_bytes_count: {}".format(len(bin_player), sent_bytes_count))


	#Draw players from the server
	for p in gamestate.players:
		if p.id != p1.id and not p.dead:
			rotatedPlayerImage = rot_center(player_image, 90-p.angle)
			# Draw the player onto the surface.
			windowSurface.blit(rotatedPlayerImage, p.rect)

			# Draw bullets
			for b in p.bullets:
				rotated_bullet_image = pygame.transform.rotate(bullet_image,90 - b.owner.angle)
				windowSurface.blit(rotated_bullet_image, b.rect)


	pygame.display.update()
	mainClock.tick(60)
