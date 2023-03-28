import socket
while True:
    try:
        sitname=input("Enter Your Websit Url : ")
        ip=socket.gethostbyname(sitname)
        print(ip)
    except:
        print("ข้อมูลผิดพลาดในการกรอก!!!")
        exit()