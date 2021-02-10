# Client-Server-Model
For my class EECE2540, Fundamentals of Networks, I used Python 3 to create  the  client  side  of  the  communication  model to interact with a server on a remote machine. I used sockets  for  communication, and a TCP/IP connection.

My client contacts the server with an  introductory  message. The client sends their unique ID. Then,  the  server  asks  my  client  to  evaluate hundreds of simple mathematical expressions.  Each of these expressions will be sent as a separate message.  For each expression message, the server expects a response that contains the correctly determined result of the expression.  New messages  from  the  server  will  be  sent  only  if  the  client  has  responded  to  the previous message correctly.  When the program is able to successfully and correctly evaluate all of the expressions and send the results to the server, then the server will return a “secret flag”, unique to each student's ID. Then, the client will terminate.

I was able to successfully get my unique flag "66d3116cf0604813dc64a4d41bd3a5160dbd68649b34cb50ad4f356b3ad63247"
