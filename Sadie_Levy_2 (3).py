#description:my program imports the socket package, creates a TCP
#connection with the server and creates and connects a client socket,
#then sends introductory NUID info to the server, gets an expression back, calculates the result and sends the server the result until it's wrong and gets a fail message, or right and gets a success message and a flag. Then, the socket closes. While it is communicating with the server it is converting strings to messages and messages to strings, and it uses eval() and a while loop to calculate the result.
#testing summary: I ran the program using a local host and the sample_server_py and typed in EECE2540 INTR 001327578 and ran it and that part worked as it answered with an expression. I gave the wrong result and it said EECE2540 fail so I knew that it recognizes wrong expressions. Then, I ran it again, and this time put the correct results using EECE2540 RSLT result while loop until I got the flag.
#NUID:001327578
#flag:66d3116cf0604813dc64a4d41bd3a5160dbd68649b34cb50ad4f356b3ad63247
import math
# Import socket package.
from socket import *
# Create a TCP/IP socket

#TCP connection with the server.
server_address = 'phase.coe.neu.edu'
server_port_number = 12000
identifier = ( server_address , server_port_number )
# Create and connect client socket.
client_socket = socket( AF_INET , SOCK_STREAM )
client_socket.connect( identifier )

#send info  
#Then, the client must send theintroductorymessage to the server. 
# Get input string.
input_string = input( 'EECE2540 INTR nuid:' )
# Convert input string to message.
message_to_server = input_string.encode()
# Send message to server.
client_socket.send( message_to_server )
# Receive message from server.
message_from_server = client_socket.recv( 2048 )
# Convert message to output string and get expr
output_string = message_from_server.decode()
#calcualte and send results back to server
while 'EECE2540 EXPR' in output_string:
  #while it gives expression print it 
  print(output_string)
  #take out those words
  express_string=output_string.replace('EECE2540 EXPR ','')
  #evaluate the expression
  input_string=eval(express_string)
  #convert back to string and add begining phrase
  input_string='EECE2540 RSLT ' + str(input_string)
  #convert input string to msg
  message_to_server = input_string.encode()

# Send message to server.
  client_socket.send( message_to_server )
# Receive message from server.
  message_from_server = client_socket.recv( 2048 )
  output_string = message_from_server.decode()
  print(output_string) #print success or fail msg

client_socket.close()#close socket