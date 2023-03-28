import socket
from datetime import datetime 
network= input("Enter your IP Address::")
net2=network.split('.')
a='.'

netsp=net2[0]+a+net2[1]+a+net2[2]+a
st1=int(input("Enter the Start number IP::"))  # กำหนดหมายเลขเริ่ม
st2=int(input("enter your the last number IP::"))   #กำหนดหมายเลขสุดท้าย
st2=st2+1
t1=datetime.now()
# สร้างว func scan เพื่อนำค่าที่ได้มาทำการค้นหาหมายเลข ip
def scan(addr):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result=s.connect_ex((addr,135))
    if result==0:
        return 1
    else:
        return 0

#func หาเวลาในการทำงานของระบบบ
def run1():
    for ip in range(st1,st2):
        addr=netsp+str(ip)
        if(scan(addr)):
            print(addr,"is live")

run1()
t2=datetime.now()
total=t2-t1
print('Scaning completed in:',total)  