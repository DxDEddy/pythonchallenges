import sys
import socket

ip = sys.argv[1]

port = sys.argv[2]

s = socket.socket()

try:
    s.connect((ip, port))
    print("Port is open: "+ip+" : "+port)
    s.settimeout = 1
    s.close
except:
    print("Port is closed: "+ip+" : "+port)