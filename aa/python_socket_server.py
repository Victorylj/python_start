import socket
import sys

#creat Socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 9090

server_socket.bind((host, port))

server_socket.listen(10)

while True:
    clent_socket,addr = server_socket.accept()

    clent_msg = clent_socket.recv(1024)

    print("address:%s" % str(addr))
    print("msg: "+str(clent_msg))
    msg = "you are Welcome !"
    clent_socket.send(msg.encode("utf-8"))
    clent_socket.close()