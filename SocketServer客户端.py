from socket import *

host='afei-cmp'
port=5000
addr=(host,port)

while True:
    cli=socket(AF_INET,SOCK_STREAM)
    cli.connect(addr)
    data=raw_input('---->')
    if not data:
        break
    cli.send('%s\t\n'%data)
    data=cli.recv(1024)
    print data.strip()
    cli.close()
