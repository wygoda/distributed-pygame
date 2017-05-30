import pygame, sys
from pygame.locals import *

# Set up pygame.
pygame.init()

TILESIZE = 64
WIDTH = 16
HEIGHT = 10
# Set up the window.
windowSurface = pygame.display.set_mode((TILESIZE*WIDTH,TILESIZE*HEIGHT), 0, 32)
pygame.display.set_caption('Hello world! - nazwa okna')

WHITE = (255, 255, 255)



windowSurface.fill(WHITE)
#draw uppper left corner
image = pygame.image.load("sprites/wall1.png")
rect = pygame.Rect(0,0,TILESIZE,TILESIZE)
windowSurface.blit(image,rect)

#draw upper wall
image = pygame.image.load("sprites/wall2.png")
for col in range(1,WIDTH-1):
	rect = pygame.Rect(col*TILESIZE,0,TILESIZE,TILESIZE)
	windowSurface.blit(image,rect)
	
#draw upper right corner
image = pygame.image.load("sprites/wall3.png")
	
	
	
# Draw the window onto the screen.
pygame.display.update()

# Run the game loop.
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
