from socket import *

HOST='afei-cmp'
PORT=21567
BUFSIZE=1024
ADDR=(HOST,PORT)

tcpcli=socket(AF_INET,SOCK_STREAM)
tcpcli.connect(ADDR)

while True:
    data=raw_input('input---->')
    if not data:
        break
    tcpcli.send(data)
    data=tcpcli.recv(BUFSIZE)
    if not data:
        break
    print data

tcpcli.close()
