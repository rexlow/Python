import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'socket created'
except socket.error, message:
    print 'Failed to create socket. Error code: ' + str(message[0]) + ' , Error message : ' + message[1]
    sys.exit()

host = 'www.google.com'
port = 80

try:
    remote_ip = socket.gethostbyname(host)
    print 'IP address of ' + host + ' is ' + remote_ip
except socket.gaierror:  # could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

# connect to remote server
s.connect((remote_ip, port))
print 'Socket Connected to ' + host + ' on ip ' + remote_ip
