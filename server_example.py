import time, socket, sys, threading

if len(sys.argv) == 3:
    host_name = sys.argv[1]
    port = int(sys.argv[2])

else:
    host_name = "0.0.0.0"
    port = 5001

new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host_name = socket.gethostname()

#port = 6021

new_socket.bind((host_name, port))
print( "Binding successful!")

#name = input('Enter name: ')

###############################################################################

client_name_list = []
connections = []

def start():
	new_socket.listen(100)
	print("LISTENING...")
	while True:
		conn, add = new_socket.accept()
		connections.append(conn)

		print("Received connection from ", add[0])
		print('Connection Established. Connected From: ',add[0])

		client = (conn.recv(1024)).decode() #Name of the client
		client_name_list.append(client)
		print(client + ' has connected.')
		#conn.send(name.encode())

		thread = threading.Thread(target=handle_client, args=(conn, add, client))
		thread.start()
		print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
		print(client_name_list)

def handle_client(conn, add, client):
	print(f"[NEW CONNECTION] {add} connected.")
	#crap = "hello"################################
	#conn.send(crap.encode())######################

	connected = True
	while connected:
		message = conn.recv(2048)
		message = message.decode()
		print(client, ":", message)
		#########conn.send(message.encode())
		broadcast(conn, message)

def broadcast(conn, message):
	for client_connection in connections:
		if client_connection != conn:
			broadcast_message = client_name_list[connections.index(conn)] + ": " + message
			client_connection.send(broadcast_message.encode())





start()
