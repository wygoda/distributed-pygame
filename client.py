#! /usr/bin/python3

import pygame, sys, math
from pygame.locals import *

class player:
    def __init__(self):
        #constructor - id, rect, hp, bullets?
        pass

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

player = pygame.Rect(300, 100, 70, 70)
playerImage = pygame.image.load('cross.png')

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6



while True:
    # Check for events.
    mouse_pos = pygame.mouse.get_pos()
    player_direction = math.atan2(player.centery - mouse_pos[1], player.centerx - mouse_pos[0])
    player_direction = math.degrees(player_direction)
    print(str(mouse_pos) + " " + str(player_direction))
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
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)

    windowSurface.fill(WHITE)

    # Move the player.
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    # rotatedPlayerImage = pygame.transform.rotate(playerImage, -player_direction + 90)
    rotatedPlayerImage = rot_center(playerImage, -player_direction + 90)
    # Draw the player onto the surface.
    # pygame.draw.rect(windowSurface, BLACK, player)
    windowSurface.blit(rotatedPlayerImage, player)

    pygame.display.update()
    mainClock.tick(60)
