import socket
import tqdm
import os

serverName = socket.gethostname()
serverPort = 12000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((serverName, serverPort))

server.listen()

client, addr = server.accept()

# Receiving file name and file size
fileName = client.recv(1024).decode()
fileSize = client.recv(1024).decode()
print("File size:" + fileSize)

receiveFile = open(fileName, "wb")
file_bytes = b""

done = False
progress = tqdm.tqdm(unit = "B", unit_scale = True, unit_divisor = 1000, total = int(fileSize))


while not done:
	data = client.recv(1024)
	if file_bytes[-5:] == b"<END>": # Check end message
		done = True
	else:
		file_bytes += data
	progress.update(1024)

# Remove <END>
endIndex = file_bytes.find(b"<END>")
new_file_bytes = file_bytes[0:endIndex]

# Write the content to the file
receiveFile.write(new_file_bytes)
receiveFile.close()

# Move file to the appropriate directory
# os.replace(fileName, "D:\\My projects\\Socket Programming Tutorial\\Files Transfer Application\\Files Destination\\")

client.close()
server.close()