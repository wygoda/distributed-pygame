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
rect = pygame.Rect((WIDTH-1)*TILESIZE,0,TILESIZE,TILESIZE)
windowSurface.blit(image,rect)

#draw left wall sand and right wall

for col in range(0,WIDTH):
	for row in range(1,HEIGHT-1):
		if col == 0:
			image = pygame.image.load("sprites/wall4.png")
			rect = pygame.Rect(col*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE)
			windowSurface.blit(image,rect)
		elif col == WIDTH-1:
			image = pygame.image.load("sprites/wall5.png")
			rect = pygame.Rect(col*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE)
			windowSurface.blit(image,rect)
		else:
			image = pygame.image.load("sprites/sand.png")
			rect = pygame.Rect(col*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE)
			windowSurface.blit(image,rect)
#draw lower wall
image = pygame.image.load("sprites/wall6.png")
rect = pygame.Rect(0,(HEIGHT-1)*TILESIZE,TILESIZE,TILESIZE)
windowSurface.blit(image,rect)


image = pygame.image.load("sprites/wall7.png")
for col in range(1,WIDTH-1):
	rect = pygame.Rect(col*TILESIZE,(HEIGHT-1)*TILESIZE,TILESIZE,TILESIZE)
	windowSurface.blit(image,rect)


image = pygame.image.load("sprites/wall8.png")
rect = pygame.Rect((WIDTH-1)*TILESIZE,(HEIGHT-1)*TILESIZE,TILESIZE,TILESIZE)
windowSurface.blit(image,rect)
	
# Draw the window onto the screen.
pygame.display.update()

# Run the game loop.
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
