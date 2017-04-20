#coding=utf-8
def testit(func,*args,**kwargs):
    try:
        rv=func(*args,**kwargs)
        rs=(True,rv)
    except Exception as diag:
        rs=(False,diag)
    return rs

def test():
    func=(int,float,long)
    val=(1234,12.34,'1234','12.34')

    for efunc in func:
        for eva in val:
            rv=testit(efunc,eva)
            if rv[0]:
                print '%s(%s)='%(efunc.__name__,eva),rv[1]
            else:
                print '%s(%s) failed'%(efunc.__name__,eva),rv[1]


test()