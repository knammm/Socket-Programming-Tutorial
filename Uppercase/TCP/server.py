import socket

# Create TCP welcoming socket
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((socket.gethostname(), serverPort))

# Listen for incoming request -> queue 1
serverSocket.listen(1)
print(f'Server is ready !')

while True:
	connectionSocket, addr = serverSocket.accept()	# wait on accept for incomming requests
	print(f'Receive request from {addr}')
	# Receive client msg and proceed
	sentence = connectionSocket.recv(1024).decode()
	capital_msg = sentence.upper()
	connectionSocket.send(capital_msg.encode())
	connectionSocket.close()