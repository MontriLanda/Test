import socket
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
traget=input('Enter ip address ::')
traget_ip=socket.gethostbyname(traget)

#func scan ports
def port_scan(port):
    try:
        s.connect((traget_ip,port))
        return True
    except:
        return False
start=time.time()
#loop port scaning
for port in range(100): #กำหนดจำนวนหมายเลขท่จะทำการ Scan
    if port_scan(port):
        print(f'port {port} is open')
    else:
        print(f'port {port} is Closed')
end=time.time()
print(f'Time Taken {end-start:.2f} sec ')