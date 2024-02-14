# TCP Connection
import socket

# AF_INET is IPv4, SOCK_STREAM corresponds to TCP
# AF_INET means Address Family InterNET for IPV4. IPV6 is AF_INET6, Bluetooth is AF_BLUETOOTH, unix sockets are AF_UNIX, etc.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to a tuple (IP, Port) => local host
s.bind((socket.gethostname(), 12000))

# Prepare for number of connection (queue)
s.listen(5)

while True:
	clientSocket, address = s.accept()
	print(f"Connection from {address} has been establish!")
	clientSocket.send(bytes("Welcome to the server!", "utf-8"))