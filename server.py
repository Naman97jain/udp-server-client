import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)       # Creation of socket object
print("Socket successfully created")
port = 3007

p = input("Enter Data you want to send to client")
print("Your data is sent to the client")

s.sendto(p.encode(),('127.0.0.1',port))