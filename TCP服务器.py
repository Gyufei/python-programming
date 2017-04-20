from socket import *
from time import ctime

HOST=''
PORT=21567
BUFSIZE=1024
ADDR=(HOST,PORT)

tcpser=socket(AF_INET,SOCK_STREAM)
tcpser.bind(ADDR)
tcpser.listen(6)

while True:
    print 'wait connect'
    a,addr=tcpser.accept()
    print 'connect from',addr

    while True:
        data=a.recv(BUFSIZE)
        if not data:
            break
        a.send(('[%s] %s'%(ctime(),data)))

    a.close()
tcpser.close()


