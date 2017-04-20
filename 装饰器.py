from time import ctime,sleep
from functools import wraps
def logg(args1):
    def log(func):
        @wraps(func)
        def warp(*args):
            print func.__name__
            print warp.__name__
            print ctime()
            print 'begin call:%s---->%s'%(func.__name__,args1)
            func(*args)
            print ctime()
            print 'end call:%s---->%s'%(func.__name__,args1)
            return func(*args)
        return warp
    return log
@logg('nice!!!')
def foo(a,b):
    print a*b

@logg('rua')
def foo2(a,b,c):
    print a*b*c

foo(5,3)
print '-----'
sleep(3)
foo(7,2)
print '-----'
sleep(3)
print '-----'
foo2(88,99,77)
