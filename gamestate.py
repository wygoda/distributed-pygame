#!/usr/bin/python3
import pygame
from pygame.locals import *
from bullet import Bullet
from player import Player

class Gamestate:
    def __init__(self):
        self.players = []
        # self.bullets = [] #i wrote it before i decided that bullets would be stored in players
        self.is_playing = False

    def addPlayer(self, player):
        self.players.append(player)
        return

    def removePlayer(self, player_id):
        for p in self.players:
            if p.id == player_id:
                self.players.remove(p)
            break
        return

    def updatePlayer(self, id, new_data):
        for p in self.players:
            if p.id == new_data.id:
                p = new_data
                print(p)
                break
        return

    #i wrote it before i decided that bullets would be stored in players
    # def addBullet(self, bullet):
    #     self.bullets.append(bullet)
    #     return

    def update(self):
        #GAME LOGIC: for each player{ bla bla for each bullet{} bla bla}
        pass
