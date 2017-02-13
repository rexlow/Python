import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, message:
    print 'Failed to create socket. Error code: ' + str(message[0]) + ', Error message: ' + str(message[1])
    sys.exit()

print 'socket created'
