import socket
import sys
import threading

#Checks if four command line arguements are taken such as group name, the clients name, the ip address of the desired server, and the port number of the desired server.
if len(sys.argv) == 5:
	server_name = sys.argv[1] #Name of the server the user wants to join.
	client_name = sys.argv[2] #Name of the client that will be displayed
	ip_address = sys.argv[3] #The IP address of the server they want to connect to.
	port = int(sys.argv[4]) #The port that the server they wish to connect to is using.

#If no command line arguements output message and exit.
else:
	print("Please input an active server and port number on the command line.\n")
	exit()

server_socket = socket.socket() # this creates a socket.
server_socket.connect((ip_address, port)) #This links the ip_address to the port so when messages are received it will go to both ip_address and port.

server_socket.send(server_name.encode()) # sends server name.
print(server_socket.recv(1024).decode()) # receives server name.

server_socket.send(client_name.encode()) # sends username.

#This deals with incomming messages and prints them if they or valid or else prints and error and closes.
def incomming_message():
	while True:
		try:
			message = (server_socket.recv(2048)).decode() #Message is recieved here.
			if message != "q":
				print(message) #Printed to the user.
			elif message == "q":
				print("You have left the chat.")
				server_socket.close()
				return

		except:
			print("Error") #Error message if anything goes wrong.
			server_socket.close() #Closes the client server_socket.

#Send messages to the server.
def send_message():
	while True: #Loop to consistantly waiting for input.
		message = input() #Message is taken from the user.
		server_socket.send(message.encode()) #The message is encoded into byte and sent to the server.
		if message == "q": #If the user inputes q we will stop the while loop by returning the thread.
			return #Thread is returned

#This  thread is created so the client is always ready to recieve a message.
incomming_message = threading.Thread(target=incomming_message) # Thread is created and sent to incomming_message.
incomming_message.start() #Thread is created.

#This thread is created so the client is always ready to send a meeage.
send_message = threading.Thread(target=send_message) # Thrad is created and sent to the send_message method.
send_message.start() #Thread is created.
