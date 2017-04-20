class Ns(object):

    def __init__(self,num=0,st=''):
        self.num=num
        self.st=st

    def __str__(self):
        return '[%d::%r]'%(self.num,self.st)
    __repr__=__str__

    def __add__(self, other):
        if isinstance(other,Ns):
            return self.__class__(self.num+other.num,self.st+other.st)
        else:
            raise TypeError,'cant add this'

    def __mul__(self, other):
        return self.__class__(self.num*other,self.st*other)

    def __nonzero__(self):
        if self.num==0 and self.st=='':
            return False
        else:
            return True

    def __cmp__(self, other):
        a=cmp(self.num,other.num)
        b=cmp(self.st,other.st)
        if a+b==0:
            return 0
        elif a+b>0:
            return 1
        else:
            return -1

a=Ns(3,'foo')
b=Ns(3,'goo')
c=Ns(2,'foo')
d=Ns()
e=Ns(st='boo')
f=Ns(1)
print a
print b
print c
print d
print e
print f
print a<b
print b<c
print a==a
print b*2
print a*3
print b+e
print e+b
print bool(d)
print bool(e)
print cmp(a,b)
print cmp(a,c)
print cmp(a,a)