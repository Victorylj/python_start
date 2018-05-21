import socket
import sys

clent_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9090

clent_socket.connect((host, port))

send_msg = "Hello Server Socket by Python..."
clent_socket.send(send_msg.encode("utf-8"))

msg = clent_socket.recv(1024)
print(msg)

clent_socket.close()
