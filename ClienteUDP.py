import socket
import sys

arglen = len(sys.argv)
if arglen < 3:
    print('Por favor correrlo con los siguientes parametros ClienteUDP.py <ip_address> <numbers>')
    exit()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 222
addr = sys.argv[1]
data = str()
data = data + sys.argv[2]
for i in range(3, len(sys.argv)):
    data = data + ':' + sys.argv[i]
s.sendto(data, (addr, port))
data, addr = s.recvfrom(1024)
print data