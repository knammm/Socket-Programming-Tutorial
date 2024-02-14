import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server. In real life, we will connect to specified IP address instead our host machine 
s.connect((socket.gethostname(), 12000))

# This is a buffer. How big of chunks of data do we want to receive at a time
msg = s.recv(1024)
print(msg.decode("utf-8"))
