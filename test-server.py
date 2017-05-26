#! /usr/bin/python3

import pygame, sys, pickle
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from pygame.locals import *
from player import Player

#server loop: check for incoming connections -> pygame computations -> send updates to clients -> repeat

class SampleClass:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.list = [123, 'asd']

host, port = 'localhost', 7777
addr = (host, port)
buf = 1024

tcp_server_sock = socket(AF_INET, SOCK_STREAM)
tcp_server_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcp_server_sock.bind(addr)
tcp_server_sock.listen(5)

client_sock, addr = tcp_server_sock.accept()

print("accepted: {}".format(addr))

while 1:
    (bin_data, address) = client_sock.recv(buf)
    # str_data = bin_data.decode()
    # if (str_data == "\quit"):
    #     print("Quiting!")
    #     break
    # else:
    print("unpickling from: {}".format(address))
    data = pickle.loads(bin_data)
    print("id: {}, {}".format(data.id, data.rect))

TCPSock.close()
