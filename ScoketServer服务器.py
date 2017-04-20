from SocketServer import *
from time import ctime

host=''
port=5000
addr=(host,port)

class mq(StreamRequestHandler):
    def handle(self):
        print 'connect from:',self.client_address
        return self.wfile.write('[%s] %s'%(ctime(),self.rfile.readline()))

ser=TCPServer(addr,mq)
print 'wait conncet'
ser.serve_forever()

