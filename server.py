#! /usr/bin/python3

import pygame, sys, pickle
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from pygame.locals import *
from player import Player

#server loop: check for incoming connections -> pygame computations -> send updates to clients -> repeat

class Client:
    def __init__(self, sock, addr):
        self.sock = sock
        self.addr = addr

host, port = 'localhost', 7777
addr = (host, port)
buf = 1024

tcp_server_sock = socket(AF_INET, SOCK_STREAM)
tcp_server_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcp_server_sock.bind(addr)
tcp_server_sock.listen(5)

clients = []

#SERVER LOOP STARTS HERE
while 1:
    client_sock, addr = tcp_server_sock.accept()
    clients.append(Client(client_sock, addr))
    print("accepted: {}".format(addr))

    #receiving data from clients
    for client in clients:
        bin_data = client_sock.recv(buf)
        #TODO: close() and remove from clients if no data
        print("unpickling from: {}".format(address))
        data = pickle.loads(bin_data)
        print("id: {}, {}".format(data.id, data.rect))

    #pygame computations (players positions, bullets, winning condition etc)
    #...


    #sending updates to clients
    #...
