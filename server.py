iimport socket

host = input("host:")
port = int(input("port:"))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(6)
while True:
    
    communication_socket, address=server.accept()
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client is: {message}")
    communication_socket.send(f"Got your message! thank you!".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} ended!")

