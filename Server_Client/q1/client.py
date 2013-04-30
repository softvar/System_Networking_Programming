import socket
host=('localhost',5011)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.sendto(b'Hello lnll',host)
while True:
    (buf,addr)=s.recvfrom(2048)
    if not len(buf):
        break
    print("Receive from %s:%s" %(addr,buf))
