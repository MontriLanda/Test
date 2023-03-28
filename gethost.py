import socket

host_name=socket.gethostname()
ip_address=socket.gethostbyname(host_name)
print("Host %s"% host_name)
print("IP %s"% ip_address)
