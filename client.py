import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 3007
s.bind(('127.0.0.1',port))
print("Waiting for server to come online")
data, a = s.recvfrom(1024)
print(data)
s.close()