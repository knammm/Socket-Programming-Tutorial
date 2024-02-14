import socket

serverName = socket.gethostname()
serverPort = 12000

# Initialize client socket and connect to server socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Send message to server
sentence = input("Enter your input: ")
clientSocket.send(sentence.encode())

# Receive message from server
modifiedMessage = clientSocket.recv(1024)
print(f'Server message: {modifiedMessage.decode()}')

# Close the socket
clientSocket.close()
