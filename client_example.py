import time, socket, sys, threading

if len(sys.argv) == 4:
	name = sys.argv[1]
	server_host = sys.argv[2]
	sport = int(sys.argv[3])

else:
	print("Please input an active server and port number on the command line.\n")
	exit()

socket_server = socket.socket()
#server_host = socket.gethostname()
#ip = socket.gethostbyname(server_host)
#sport = 5000

#print('This is your IP address: ',ip)
#server_host = input('Enter friend\'s IP address:')
#name = input('Enter Friend\'s name: ')


socket_server.connect((server_host, sport))

socket_server.send(name.encode())
#server_name = socket_server.recv(1024)
#server_name = server_name.decode()

#print(server_name,' has joined...')
def recieve():
	while True:
		try:
			message = (socket_server.recv(2048)).decode()
			if message:
				print(message)
		except:
			print("Error")
			socket_server.close()

def write():
	while True:
		message = input("Me: ")
		socket_server.send(message.encode())

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
