from datetime import datetime
import socket
host='localhost'
port=5012
addr=(host,port)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
time = datetime.ctime(datetime.now()).encode()
while True:
    msg,addr=s.recvfrom(8192)
    print("got data from",addr)
    s.sendto(time,addr)
