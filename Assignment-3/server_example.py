import socket
import sys
import threading

#Takes in two command line arguements the ip address and a port to communicate on.
if len(sys.argv) == 3:
    ip_address = sys.argv[1]
    port = int(sys.argv[2])

#If no command line arguements set the ip address and port to value below.
else:
    ip_address = "0.0.0.0"
    port = 5001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # This creates a socket. The first arguement sets the type value it will recieve such as IPV4 and the second arguement tells us how the data will be send in this case our data will be streamed(TCP data)
server_socket.bind((ip_address, port)) #This links the ip_address to the port so whrn messages are received it will go to both ip_address and port.
print("Server is on...")

groupchat = {} #contains all the the server names and the clients in the respective server.
groupchat_connections = {} #contains all the server names and their respective client connections.

#This listens for any incomming messages on the line and establishes a connection with the client and passes them onto manage_client as a new thread.
def connect_clients():
	server_socket.listen() #listens for connection on the line.
	print("LISTENING...")
	while True:
		client_connection, add = server_socket.accept() # waits untill a new connection occurs. When a connection happens the cliens connection and ip address will be stored as separate variables.


		server_name = (client_connection.recv(1024)).decode() #Receives server name from clients server.
		client_connection.send(("You have entered " + server_name).encode()) # Update to client that the user has entered the desired server.

		client = (client_connection.recv(1024)).decode() #Receives the name of the client.
		print(client + ' has connected.')#####delete############

		add_to_groupchat(server_name, client_connection, client) # adds the clients and client connections to the respective dictionaries.

		thread = threading.Thread(target=manage_client, args=(client_connection, add, client)) #Creates a thread for each client and sends it to manage_client.
		thread.start() #Thread is initiated.
		print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") ####delete#####
		print(groupchat) ####delete#####

#This adds the client name and client connections to their respective groupchat.
def add_to_groupchat(server_name, client_connection, client):
	#If groupchat is empty add groupchat name and map it to client name and client connection.
	if groupchat == {}:
		groupchat[server_name] = [client]
		groupchat_connections[server_name] = [client_connection]

	#If the group name inputed by the client is not in the dictionary create the group name and map it to a list with the client in it.
	elif server_name not in groupchat:
		groupchat[server_name] = [client]
		groupchat_connections[server_name] = [client_connection]

	#If the group name is already in the dictionary just add the client name and client connection to the dictionary.
	else:
		for name in groupchat:
			if name == server_name:
				groupchat[name].append(client)
				groupchat_connections[name].append(client_connection)

#This deals with all the incomming client messages and broadcast them to all other clients in the same groupchat but does not broadcast to the client who sent the message.
def manage_client(client_connection, add, client):
	print(f"[NEW CONNECTION] {add} connected.") ####delete####


	connected = True
	while connected:
		message = client_connection.recv(2048) #Messages from clients are received here.
		message = message.decode() #The encoded message is decoded from bytes to a string message.
		print(client, ":", message) ###delete###

		broadcast(client_connection, message, client) #broadcasts to all clients except the sender.


#Broadcasts to all clients except the sender.
def broadcast(client_connection, message, client):

	#Locates what groupchat the client is in.
	for name in groupchat:
		if client in groupchat[name]:
			client_server = name

	#Iterates through the dictionary to locate the client list of the associated group name.
	for connection in groupchat_connections[client_server]:
		if connection != client_connection: #If the client name is not the sender.
			broadcast_message = groupchat[client_server][groupchat_connections[client_server].index(client_connection)] + ": " + message #Adds the sender name to the top of the message.
			connection.send(broadcast_message.encode()) # sends the message to the other clients in the groupchat.


connect_clients() #Initiates by going to the connect_clients method.
