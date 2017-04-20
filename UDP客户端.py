from socket import *

host='afei-cmp'
port=21957
buffsize=1024
addr=(host,port)

cil=socket(AF_INET,SOCK_DGRAM)

while True:
    data=raw_input('input---->')
    if not data:
        break
    cil.sendto(data,addr)
    data,addr=cil.recvfrom(buffsize)
    if not data:
        break
    print data
