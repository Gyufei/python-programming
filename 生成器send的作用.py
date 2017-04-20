def g1():
    value=0
    while True:
        r=yield value
        if not r:
            return
        else:
            value = 'value change to %s'%r


def s1(c):
    print c.send(None)
    n=1
    while True:
        if n<5:
            print 'will be sended---->%s'%n
            print c.send(n)
            print 'has been sended---->%s'%n
            n+=1
        else:
            c.close()
            break


g=g1()
s1(g)

