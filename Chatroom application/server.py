import socket
import select

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 12345

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((IP, PORT))

serverSocket.listen()
print(f"The server is ready !")

socketLists = [serverSocket]
clients = {}

# Return the 2 elements dictionary of header and data of the message
def receive_message(clientsSocket):
	try:
		# Receive message with decode
		messageHeader = clientsSocket.recv(HEADER_LENGTH)
		if(not len(messageHeader)): # No message -> false
			return False
		# Calculate message length
		messageLength = int(messageHeader.decode("utf-8").strip())
		return {"header": messageHeader, "data": clientsSocket.recv(messageLength)}
	except:
		return False


while True:
	readSockets, _, exceptionSockets = select.select(socketLists, [], socketLists)

	for notified_socket in readSockets:
		if notified_socket == serverSocket:
			# Server socket => accept conenction
			clientsSocket, clientAddress = serverSocket.accept()
			user = receive_message(clientsSocket)

			if user is False:
				continue

			socketLists.append(clientsSocket)
			clients[clientsSocket] = user # A dictionary inside a dictionary {clientSocket: {header: messHead, data: messData},...}
			print(f"Accept conenction from {clientAddress[0]}:{clientAddress[1]} username: {user['data'].decode('utf-8')}")
		
		else:
			message = receive_message(notified_socket)

			if message is False:
				print(f"Closed conenction from {clients[notified_socket]['data'].decode('utf-8')}")
				socketLists.remove(notified_socket)
				del clients[notified_socket]
				continue

			user = clients[notified_socket]
			print(f"Receive message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

			# Send message to other users
			for client_socket in clients:
				if client_socket != notified_socket:
					client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

	for notified_socket in exceptionSockets:
		print("Debugging...")
		socketLists.remove(notified_socket)
		del	clients[notified_socket]

	try:
		pass

	except IOError as e:
		if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
			print('Reading error', str(e))
			sys.exit()
		continue

	except Exception as e:
		print('General error', str(e))
		sys.exit()












