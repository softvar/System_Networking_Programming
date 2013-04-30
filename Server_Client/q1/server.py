import socket
host='localhost'
port=5011
addr=(host,port)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
while True:
    msg,addr=s.recvfrom(4)
    print("got data from",addr,msg)
    s.sendto(msg,addr)
