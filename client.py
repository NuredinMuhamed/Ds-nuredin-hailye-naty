import socket

host = input("host:")
port = int(input("port:"))

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))

socket.send(input('please enter your message:').encode('utf-8'))
print(socket.recv(1024))