from socket import *
from time import ctime

host=''
port=21957
buffsize=1024
addr=(host,port)

ser=socket(AF_INET,SOCK_DGRAM)
ser.bind(addr)

while True:
    print 'wait message'
    data,addr=ser.recvfrom(buffsize)
    ser.sendto(('[%s]%s'%(ctime(),data)),addr)
    print 'receive'



