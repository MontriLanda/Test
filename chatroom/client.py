import time
import socket
import sys

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 1234
print("This Is Your IP address :: ",ip)
server_host = input("Enter Frind\s IP Address :: ")
name=input("Enter Friend \s IP Name :: ")

socket_server.connect((server_host,sport))
socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()
print(server_name,"Has Joined Success ...... ")

while True:
    message = (socket_server.recv(1024).decode())
    print(server_name,":::",message)
    message=input("ME :: ")
    socket_server.send(message.encode())
    