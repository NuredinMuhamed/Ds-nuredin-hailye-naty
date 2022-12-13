iimport socket

host = input("host:")
port = int(input("port:"))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(6)


