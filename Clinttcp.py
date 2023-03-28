import socket
#Socket Obj Socket
s=socket.socket()
#creat port ให้ตรง Server
port = 12345
# สร้างการเชื่อมต่อกับเครื่องแม่ ต้องการหมายเลข ip และ port
s.connect(('192.168.36.126',port))
print(s.recv(1024))
s.close #ปิดการเชื่อมต่อ
