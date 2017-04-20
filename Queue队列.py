# coding=utf-8
import time
import threading
from random import randint
from Queue import Queue

def ctime():
    return time.strftime('%M:%S',time.localtime())

class lf(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func=func
        self.args=args
        self.name=name
        self.res=None

    def run(self):
        print 'starting',self.func.__name__,'at',ctime()
        self.res=apply(self.func,self.args)
        print 'end',self.func.__name__,'at',ctime()

    def getres(self):
        return self.res
def wq(queue):
    print 'for queue'
    queue.put('aaa',1)
    print 'queue size：%s'%queue.qsize()

def rq(queue):
    print 'from queue'
    queue.get(1)
    print 'queue size:%s'%queue.qsize()

def write(queue,loop):
    for i in range(loop):
        wq(queue)
        time.sleep(randint(1,3))

def read(queue,loop):
    for i in range(loop):
        rq(queue)
        time.sleep(randint(2,5))
func=[write,read]
nfunc=range(len(func))

def main():
    threads=[]
    nloops=randint(2,6)
    q=Queue(32)
    for i in nfunc:
        t=lf(func[i],(q,nloops),func[i].__name__)
        threads.append(t)

    for i in nfunc:
        threads[i].start()

    for i in nfunc:
        threads[i].join()

    print 'done'

if __name__ == '__main__':
    main()
