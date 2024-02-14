import socket

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Binding
serverSocket.bind((socket.gethostname(), serverPort))

print(f"The server is ready !")

while True:
	# Receive message and client address
	message, clientAddress = serverSocket.recvfrom(2048)
	print(f"Receive request from {clientAddress}")
	modifiedMessage = message.decode().upper() # Decode the message then uppercase it
	serverSocket.sendto(modifiedMessage.encode(), clientAddress)