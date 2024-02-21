import socket
import os
import sys

serverName = socket.gethostname()
serverPort = 12000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((serverName, serverPort))

path = "D:\\My projects\\Socket Programming Tutorial\\Files Transfer Application\\Random Files\\"
file_names = os.listdir(path)

print(f"Existing files: " + str(file_names))

fileName = input("Enter the file's name: ")

# Handling unexisting file
if fileName not in file_names:
	print("\nThe file does not exist !")
	client.close()
	sys.exit()

# Open file in mode read byte
myFile = open(path + fileName, "rb")
fileSize = os.path.getsize(path + fileName)

# print(fileSize)
dotIndex = fileName.find(".")
tail = fileName[dotIndex:]

# Sending newFile name and its size
newFileName = "Receive_File" + tail
# print(newFileName)

client.send(newFileName.encode())
client.send(str(fileSize).encode())

# Read the data of the file and send all those data
data = myFile.read()
client.sendall(data)
client.send(b"<END>")

myFile.close()
client.close()