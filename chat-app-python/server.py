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
def broadcast(message):
    for client in clients:
        client.send(message)

#recieve function- accepts new connection, listens


#handle function- individual connection to client