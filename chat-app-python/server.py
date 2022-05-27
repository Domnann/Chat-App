import socket
import threading


HOST ='127.0.0.1'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients=[]
nicknames=[]

#broadcast function- sends one message to all clients
def broadcast(msg):
    for client in clients:
        client.send(msg)
#handle function- individual connection to client
def recieve(client):
    pass

#recieve function- accepts new connection, listens
def recieve():
    while true:
        client, address =server.accept()
        print(f"Connected with {str(address)}!")

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024)
        nickname.append (nickname)

        client.append(client)

        print(f"Client's nickname is {nickname}")
        broadcast(f"{nickname} connected to the server!".encode('utf-8'))
        client.send('Connected to the server '.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start


#please help me update code
#thanks


from socket import *
from time import ctime

CLIENT_IP = '192.168.1.109'
PORT = 23567
BUFSIZE = 1024
ADDR = (CLIENT_IP, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    sendData = input("> ")
    if sendData is None:
        break
    udpCliSock.sendto(sendData.encode(), ADDR)

udpCliSock.close()