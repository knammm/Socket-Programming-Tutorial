import socket
import os

serverName = socket.gethostname()
serverPort = 12000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((serverName, serverPort))

# Open file in mode read byte
myFile = open("D:\\My projects\\Socket Programming Tutorial\\Files Transfer Application\\Random Files\\randomFile.txt", "rb")
fileSize = os.path.getsize("D:\\My projects\\Socket Programming Tutorial\\Files Transfer Application\\Random Files\\randomFile.txt")

print(fileSize)

# Sending newFile name and its size
client.send("ReceiveText.txt".encode())
# client.send(str(fileSize).encode())

# Read the data of the file and send all those data
data = myFile.read()
client.sendall(data)
client.send(b"<END>")

myFile.close()
client.close()