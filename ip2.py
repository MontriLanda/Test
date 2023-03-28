import socket
while True:
    sitname=input("Enter Your Websit Url : ")
    ip=socket.gethostbyname(sitname)
    print(ip)