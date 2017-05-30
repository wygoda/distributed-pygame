import pygame, sys
from pygame.locals import *

# Set up pygame.
pygame.init()

TILESIZE = 64
WIDTH = 16
HEIGHT = 10
# Set up the window.
windowSurface = pygame.display.set_mode((TILESIZE*WIDTH,TILESIZE*HEIGHT), 0, 32)
pygame.display.set_caption('SHOOTER')

WHITE = (255, 255, 255)


#draw uppper left corner
sandimage = pygame.image.load("sprites/sand.png")
lwallimage = pygame.image.load("sprites/leftwall.png")
rwallimage = pygame.image.load("sprites/rightwall.png")
topwallimage = pygame.image.load("sprites/upperwall.png")
botwallimage = pygame.image.load("sprites/lowerwall.png")


sandrect = pygame.Rect(0,0,TILESIZE*WIDTH,TILESIZE*HEIGHT)
lwallrect = pygame.Rect(0,0,TILESIZE,TILESIZE*HEIGHT)
rwallrect = pygame.Rect(TILESIZE*(WIDTH-1),0,TILESIZE,TILESIZE*HEIGHT)
topwallrect = pygame.Rect(TILESIZE,0,TILESIZE*(WIDTH-2),TILESIZE)
botwallrect = pygame.Rect(TILESIZE,TILESIZE*(HEIGHT-1),TILESIZE*(WIDTH-2),TILESIZE)


windowSurface.blit(sandimage,sandrect)
windowSurface.blit(lwallimage,lwallrect)
windowSurface.blit(rwallimage,rwallrect)
windowSurface.blit(topwallimage,topwallrect)
windowSurface.blit(botwallimage,botwallrect)


	
# Draw the window onto the screen.
pygame.display.update()

# Run the game loop.
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
