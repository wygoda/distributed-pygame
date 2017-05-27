#! /usr/bin/python3

import pygame, sys, pickle, random, socket
# from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, timeout
from pygame.locals import *
from player import Player
from threading import Thread, Lock, currentThread
from gamestate import Gamestate
from bullet import Bullet

#server loop: check for incoming connections -> pygame computations -> send updates to clients -> repeat

class Server:
    def __init__(self, host, port, buf):
        self.host = host
        self.port = port
        self.buf = buf
        self.addr = (host, port)

        self.tcp_server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcp_server_sock.bind(self.addr)
        self.tcp_server_sock.listen(5)
        self.tcp_server_sock.settimeout(1) #this makes socket.accept() non-blocking

        self.clients = {}
        self.clients_mutex = Lock()

        self.gamestate = Gamestate()

    def accept_connections(self):
        player_counter = 0
        t = currentThread()
        #thanks to getattr we can stop a thread that is in an infinite loop https://stackoverflow.com/a/36499538/7804248
        while getattr(t, "do_run", True):
            connected = False
            try:
                client_sock, addr = self.tcp_server_sock.accept()
                connected = True
            except socket.timeout:
                pass

            if connected:
                # print("asd")
                player_counter += 1
                player = Player(player_counter, pygame.Rect(300,300,50,50)) #TODO: randomize spawn place
                with self.clients_mutex:
                    clients[player.id] = Client(client_sock, addr)
                #send this info to the client
                self.gamestate.addPlayer(player)
                bin_player = pickle.dumps(player)
                client_sock.send(bin_player)
                bin_gamestate = pickle.dumps(self.gamestate)
                client_sock.send(bin_gamestate)
                print("accepted: playerid {}, addr {}".format(player.id, addr))

    #SERVER LOOP
    def run(self):
        accept_conn_thread = Thread(target=self.accept_connections)
        accept_conn_thread.start()
        while 1:
            # print("in the loop")
            #receiving data from clients, client have to send their player object,
            #bullets are stored in players to make it easier to transmit
            for player_id, client in self.clients:
                bin_data = client.sock.recv(buf)
                #TODO: close() and remove from clients if no data
                updated_player_data = pickle.loads(bin_data)
                self.gamestate.updatePlayer(player_id, updated_player_data)

            #pygame computations (players positions, bullets, winning condition etc)
            gamestate.update()

            #sending updates to clients
            bin_gamestate = pickle.dumps(self.gamestate)
            for player_id, client in self.clients:
                client.sock.send(bin_gamestate)

        # print("koniec")
        accept_conn_thread.do_run = False
        accept_conn_thread.join()

class Client:
    def __init__(self, sock, addr):
        self.sock = sock
        self.addr = addr

host, port = 'localhost', 7777

#MAIN
buf = 1024
s = Server(host, port, buf)
s.run()
