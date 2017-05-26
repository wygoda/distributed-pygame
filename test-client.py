#! /usr/bin/python3

import pygame, sys, math, bullet, random, pickle
from socket import socket, AF_INET, SOCK_STREAM
from pygame.locals import *
from player import Player

# player = Player(1234, pygame.Rect(300,300,50,50))

class SampleClass:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.list = [123, 'asd']

host, port = 'localhost', 7777
addr = (host, port)

tcp_sock = socket(AF_INET, SOCK_STREAM)
tcp_sock.connect(addr)

while (1):
    id_number = input('>> ')
    player = Player(id_number, pygame.Rect(300,300,50,50))
    # sample_object = SampleClass(id_number, "dupa")
    bin_data = pickle.dumps(player)
    if(tcp_sock.send(bin_data)):
        print("Sending message '" + str(bin_data) + "'...")

TCPSock.close()
