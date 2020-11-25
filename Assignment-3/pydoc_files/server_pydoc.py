"""


   This server script is always available. It provides information on the functions
   defined in server.py file.
"""
def connect_clients():
    '''This listens for any incomming messages on the line and establishes a
	   connection with the client'''


def manage_client(client_connection, client):
	'''|Arguement 1 - client_connection - is the connection that to the respective
	   |              client that allows to send messages to that client.
	   |Arguement 2 - client - is the clients username to be displayed on screen.

	   This deals with all the incomming client messages and response according
	   to the message. If the message is the exit key it will close the client
	   connection otherwise it will broadcast the message.'''


def add_to_groupchat(server_name, client_connection, client):
	'''|Arguement 1 - server_name - This is the name of the server the client
	   |              would like to join.
	   |Arguement 2 - client_connection - is the connection that to the respective
   	   |              client that allows to send messages to that client.

	   This adds the client name and client connections to their respective
	   groupchat dictionaries.'''


def remove_client(client_connection):
	'''|Arguement 1 - client_connection - is the connection that to the respective
	   |             client that allows to send messages to that client.

	   This removes the client from the groupchat when the client presses the exit key q.'''


def broadcast(client_connection, message, client):
    '''|Arguement 1 - client_connection - is the connection that to the respective
	   |              client that allows to send messages to that client.
	   |Arguement 2 - messge - is the message send to the server by the client.
	   |Arguement 3 - client - this is the name of the respective client.

	    Broadcasts to all clients except the sender.'''
