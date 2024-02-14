import socket

serverName = socket.gethostname()
serverPort = 12000

# Connect UDP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input('Input lowercase sentence: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Buffer of 2048
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())
clientSocket.close()