from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = input()
port = int(input())

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    
# Send STARTTLS command and print server response.
heloCommand = 'STARTTLS\r\n'
clientSocket.send(heloCommand.encode())
recvA = clientSocket.recv(1024).decode()
print(recvA)
if recvA[:3] != '220':
    print('220 reply not received from server.')
    
# Send MAIL FROM command and print server response.
mailfromCommand = 'MAIL FROM: jordankirchner@uvic.ca\r\n'
clientSocket.send(mailfromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcpttoCommand = 'RCPT TO: <jordankirchner04@hotmail.com>\r\n'
clientSocket.send(rcpttoCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')

# Send message data.
messagedata = input()
clientSocket.send(messagedata.encode())

# Message ends with a single period.
enddata = '\r\n.\r\n'
clientSocket.send(enddata.encode())

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '221':
    print('221 reply not received from server.')
