from time import time
def mult(x,y):
    return x*y

def timeit(func):
    def warp(*args):
        now=time()
        try:
            ret=func(*args)
            end=time()
            return ret
        finally:
            print '%s use time %.8f s'%(func.__name__,(end-now))
    return warp

@timeit
def dy(q):
    return reduce(mult,range(q)[:1:-1])

@timeit
def rd(x):
    return reduce(lambda z,y:z*y,range(x)[:1:-1])

@timeit
def fn(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fn(n-1)


dy(15)

rd(15)

fn(15)