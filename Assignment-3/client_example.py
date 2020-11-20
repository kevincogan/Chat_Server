import socket
import sys
import threading

#Checks if four command line arguements are taken such as group name, the clients name, the ip address of the desired server, and the port number of the desired server.
if len(sys.argv) == 5:
	server_name = sys.argv[1]
	client_name = sys.argv[2]
	ip_address = sys.argv[3]
	port = int(sys.argv[4])

#If no command line arguements output message and exit.
else:
	print("Please input an active server and port number on the command line.\n")
	exit()

server_socket = socket.socket() # this creates a socket.
server_socket.connect((ip_address, port)) #This links the ip_address to the port so when messages are received it will go to both ip_address and port.

server_socket.send(server_name.encode()) # sends server name.
print(server_socket.recv(2048).decode()) # receives server name.

server_socket.send(client_name.encode()) # sends username.

def incomming_message():
	while True:
		try:
			message = (server_socket.recv(2048)).decode()
			if message:
				print(message)
		except:
			print("Error")
			server_socket.close()

def send_message():
	while True:
		message = input()
		server_socket.send(message.encode())

incomming_message = threading.Thread(target=incomming_message)
incomming_message.start()

send_message = threading.Thread(target=send_message)
send_message.start()
