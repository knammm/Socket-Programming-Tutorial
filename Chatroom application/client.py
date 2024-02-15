import socket
import select
import errno
import sys

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 12345

# Sending username info
my_username = input("Enter your username: ")
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((IP, PORT))
clientSocket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
clientSocket.send(username_header + username)

# Sending messages and Receiving messages of client
while True:
	# Sending message
	message = input(f"{my_username} > ")
	# message = ""
	if message:
		message = message.encode("utf-8")
		message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8")
		clientSocket.send(message_header + message)

	# Receiving message
	try:
		while True:
			# Process username
			username_header = clientSocket.recv(HEADER_LENGTH)
			if not len(username_header):
				print("Connection closed by the server")
				sys.exit()

			username_length = int(username_header.decode("utf-8").strip())
			username = clientSocket.recv(username_length).decode("utf-8")
			# Process message
			message_header = clientSocket.recv(HEADER_LENGTH)
			message_length = int(message_header.decode("utf-8").strip())
			message = clientSocket.recv(message_length).decode("utf-8")
			# Print out other client's username and message
			print(f"{username} > {message}")
	
	except IOError as e:
		if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
			print('Reading error', str(e))
			sys.exit()
		continue

	except Exception as e:
		print('General error', str(e))
		sys.exit()