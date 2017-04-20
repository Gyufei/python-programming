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

def fib(x):
    time.sleep(0.005)
    if x<2:return 1
    else:return fib(x-2)+fib(x-1)

def fac(x):
    time.sleep(1)
    if x==0 or x==1:return 1
    else:return x*fac(x-1)

def sum(x):
    time.sleep(0.1)
    if x==1:return 1
    else:return x+sum(x-1)

func=[fib,fac,sum]
n=12

def main():

    nfunc=range(len(func))

    print 'single'+'-'*20
    for i in nfunc:
        print 'starting',func[i].__name__,'at',ctime()
        print func[i](n)
        print 'end',func[i].__name__,'at',ctime()

    print '\nmul'+'-'*20
    threads=[]
    nloops=randint(2,6)
    q=Queue(32)
    for i in nfunc:
        t=lf(func[i],(n,),func[i].__name__)
        threads.append(t)

    for i in nfunc:
        threads[i].start()

    for i in nfunc:
        threads[i].join()
        print '%s result:'%func[i].__name__,threads[i].getres()

    print 'done'
if __name__ == '__main__':
    main()
