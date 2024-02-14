import socket
import select

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 12345

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
