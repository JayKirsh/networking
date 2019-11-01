from socket import *
import time

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Input host and port
print("Enter host: ", end = "")
HOST = input()
print("Enter port: ", end = "")
PORT = int(input())

s = socket(AF_INET, SOCK_DGRAM)

i = 1

while i <= 10:
    try:
        t_i = time.time()
        s.sendto(b"ping", ((HOST, PORT)))
        
        s.settimeout(1)
        data, addr = s.recvfrom(1024)
        t_f = time.time()
        t_e = t_f - t_i
        print(data + " " + i + " " + t_e)
    
    except:
        print("Request timed out")
    i += 1
