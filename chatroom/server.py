import time
import socket
import sys
# ทำการสร้าง การเชื่อมต่อด้วย Socket

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 1234
new_socket.bind((host_name,port))
print("Create Successfull!!!!!!!!!")
print("This Is Your IP :: ",s_ip)
name=input("Enter Your Name Avatar :: ")
new_socket.listen(1)
conn,add = new_socket.accept()
print ("Receiced Connection fron",add[0])
print ("Connnection esti ...... from : ",add[0])

#สร้าง Client สำหรับรับคำมาจากลูก
client = (conn.recv(1024)).decode()
print(client+"Has Conbbected")
conn.send(name.encode())
while True:
    message=input("ME :: ")
    conn.send(message.encode())
    message=conn.recv(1024)
    message = message.decode()
    print(client,"::",message)
    