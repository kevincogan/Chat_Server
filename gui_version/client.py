import socket
import sys
import threading
from tkinter import *

#This function receives information inputed by the login GUI such as server name, client name, ip address, port number.
def mySetUp():
	try:
		global server_name #Makes the variable available to all functions.
		server_name = (server_name.get()).split(":")[1].strip() #This strips parses the information that we need.
		global client_name #Makes the variable available to all functions.
		client_name = (client_name.get()).split(":")[1].strip() #This strips parses the information that we need.
		global ip_address #Makes the variable available to all functions.
		ip_address = (ip_address.get()).split(":")[1].strip() #This strips parses the information that we need.
		global port #Makes the variable available to all functions.
		port = int((port.get()).split(":")[1].strip()) #This strips parses the information that we need.
		set_up.destroy() #This closes the login GUI.

	except: #If an exception occurs we will print the statement below, close the login GUI and exit the program.
		print("Please input the correct information.")
		set_up.destroy()
		exit()

	global server_socket #Makes the variable available to all functions.
	server_socket = socket.socket() # this creates a socket.
	server_socket.connect((ip_address, port)) #This links the ip_address to the port so when messages are received it will go to both ip_address and port.

	server_socket.send(server_name.encode()) # sends server name.
	print(server_socket.recv(1024).decode()) # receives server name.

	server_socket.send(client_name.encode()) # sends username.

i = 3
#This deals with incomming messages and prints them if they or valid or else prints and error and closes.
def incomming_message():
	global i #Makes the variable available to all functions.
	message = (server_socket.recv(2048)).decode() #Message is recieved here.
	if message and message != "q":
		print(message) #Printed to the user.
		chat = Label(chatbox, text=message) #Outputes messages on the chatbox GUI.
		chat['font']=("Comic Sans MS",19) #Allows us to modify the font size and style.
		chat['fg']= '#340669'#Changes the font colour of the text in the chatbox.
		chat['width'] = 50 #Makes the width of the chat box.
		chat.grid(columnspan=2,column=0,row=i,padx=0) #Formats the layout of the messages.
		i += 1 #Increments the row so messages do not overlap.

	elif message == "q": #If the exit key is pressed the client leave the chat room.
		print("You have left the chat.")
		server_socket.close() #closes the socket.
		return

#Send messages to the server.
def send_message():
	global i #Makes the variable available to all functions.
	message = chat.get() #Gets the input from the user.
	chat1 = Label(chatbox, text=message) #displays the input on the chatbox GUI.
	chat1['font']  = ("Comic Sans MS",19) #Changes the style of the font.
	chat1['fg'] = '#340669' #The colour of the font.
	chat1['width'] = 50 #With of the GUI.
	chat1.grid(columnspan = 2, column = 0, row = i) #Formats the layout of the GUI.
	i += 1
	server_socket.send(message.encode()) #The message is encoded into byte and sent to the server.
	if message == "q": #If the user inputes q we will stop the while loop by returning the thread.
		chatbox.destroy()
		return #Thread is returned

#This function lets the client leave .
def leave():
	try:
		server_socket.send("q".encode())#The exit key is sent to the server to remove the user from the server.
		chatbox.destroy() #The GUI window is then closed.
		server_socket.close() #The connection is then closed.
		return #The program is finished.

	except: #If there are any exceptions then close the GUI and end the connection.
		chatbox.destroy()
		server_socket.close()
		return



###################################################################################################

set_up = Tk() #Call an instance of Tkinter.
set_up.title('Login') #Name the title of the login window.
set_up['bg'] = '#fc0345' #The background colour.

server_name = Entry(set_up, font=('Comic Sans MS', 24)) #Creates an entry box for input on the GUI.S
server_name.insert(0, "Enter Sever Name: ") #User inputs required details to log into a chatroom.
server_name['width'] = 25 #This adjust the with to the GUI element.
server_name['relief'] = GROOVE # This adds a groove around the GUI features to enhance the style.
server_name['bg']='#ffffff' #Adjusts the background colour.
server_name['fg']='#340669' #Adjusts the font colour.
server_name.grid(column=0,row=1,padx=5,pady=5)

client_name = Entry(set_up, font=('Comic Sans MS', 24)) #Creates an entry box for input on the GUI.S
client_name.insert(1, "Enter Your Username: ") #User inputs required details to log into a chatroom.
client_name.grid(column=0,row=2,padx=5,pady=5) #Fomates the layout of the GUI.
client_name['width'] = 25 #This adjust the with to the GUI element.
client_name['relief'] = GROOVE # This adds a groove around the GUI features to enhance the style.
client_name['bg']='#ffffff' #Adjusts the background colour.
client_name['fg']='#340669' #Adjusts the font colour.

ip_address = Entry(set_up, font=('Comic Sans MS', 24)) #Creates an entry box for input on the GUI.S
ip_address.insert(2, "Enter Sever IP Address: ") #User inputs required details to log into a chatroom.
ip_address.grid(column=0,row=3,padx=5,pady=5) #Fomates the layout of the GUI.
ip_address['width'] = 25 #This adjust the with to the GUI element.
ip_address['relief'] = GROOVE # This adds a groove around the GUI features to enhance the style.
ip_address['bg']='#ffffff' #Adjusts the background colour.
ip_address['fg']='#340669' #Adjusts the font colour.

port = Entry(set_up, font=('Comic Sans MS', 24)) #Creates an entry box for input on the GUI.S
port.insert(3, "Enter Server Port: ") #User inputs required details to log into a chatroom.
port.grid(column=0,row=4,padx=5,pady=5) #Fomates the layout of the GUI.
port['width'] = 25 #This adjust the with to the GUI element.
port['relief'] = GROOVE # This adds a groove around the GUI features to enhance the style.
port['bg']='#ffffff' #Adjusts the background colour.
port['fg']='#340669' #Adjusts the font colour.


myButton = Button(set_up, text="Enter Chatroom", command=mySetUp)
myButton['relief']= GROOVE # This adds a groove around the GUI features to enhance the style.
myButton['bg']='#ffae00' #Adjusts the background colour.
myButton['fg']='white' #Adjusts the font colour.
myButton['activebackground']='#a691fa'
myButton['padx']=3 # adds padding,
myButton['font']=("Comic Sans MS",19) #Changes the font and size/
myButton.grid(column=0,row=5,padx=5,pady=5) #Fomates the layout of the GUI.

set_up.mainloop()

#This  thread is created so the client is always ready to recieve a message.
incomming_message = threading.Thread(target=incomming_message) # Thread is created and sent to incomming_message.
incomming_message.start() #Thread is created.

#This thread is created so the client is always ready to send a meeage.
#send_message = threading.Thread(target=send_message) # Thrad is created and sent to the send_message method.
#send_message.start() #Thread is created.

chatbox = Tk() #Creates an instance of Tkinter.
chatbox.title('Chatbox') #Creates a chatboc tittle.
chatbox['bg']='#fc0345' #Adjusts the background colour.

chat = Entry(chatbox, font=('Comic Sans MS', 24)) #Creates an entry box for input on the GUI.S
chat['width'] = 50 #This adjust the with to the GUI element.
chat['relief'] = GROOVE # This adds a groove around the GUI features to enhance the style.
chat['bg']='#ffffff' #Adjusts the background colour.
chat['fg']='#340669' #Adjusts the font colour.
chat.grid(column=0,row=1,padx=5,pady=5) #Fomates the layout of the GUI.

myButton = Button(chatbox, text="Enter", command=send_message)
myButton['relief']= GROOVE # This adds a groove around the GUI features to enhance the style.
myButton['bg']='#ffae00' #Adjusts the background colour.
myButton['fg']='white' #Adjusts the font colour.
myButton['activebackground']='#a691fa' #Changes colour when hovered on.
myButton['padx']=3 # adds padding,
myButton['font']=("Comic Sans MS",19) #font style/
myButton.grid(column=1,row=1,padx=5,pady=0) #Fomates the layout of the GUI.

myButton1 = Button(chatbox, text="Leave", command=leave)
myButton1['relief']= GROOVE # This adds a groove around the GUI features to enhance the style.
myButton1['bg']='#ffae00' #Adjusts the background colour.
myButton1['fg']='white' #Adjusts the font colour.
myButton1['activebackground']='#a691fa' #Changes colour when hovered on by the mouse.
myButton1['padx']=3 #Adds a buffer around the elements.
myButton1['font']=("Comic Sans MS",17) #Font style.
myButton1.grid(column=1,row=2,padx=5,pady=5) #Fomates the layout of the GUI.


chatbox.mainloop()
