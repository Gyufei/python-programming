class Moneyfmt(object):

    def __init__(self,x,j=1):
        assert isinstance(x,float),'must be float'
        self.x=x
        self.j=j

    def __str__(self):
        a=(str(round(self.x,2))).partition('.')
        c=a[0][::-1]
        flag = c.endswith('-') and '-' or ''
        c = flag and c[:len(c)-1] or c
        b=''
        for i,j in enumerate(c):
            if i%3==0 and i!=0:
                b=','.join((b,j))
            else:
                b+=j
        if self.j==1:
            self.__a='%s$%s'%(flag,('.'.join((b[::-1],a[2]))))
        elif self.j==2:
            self.__a='<$%s>'%('.'.join((b[::-1],a[2])))
        else:
            raise TypeError,'just two type-->1:"-" or 2:"<>"'

        return self.__a

    __repr__=__str__

    def __nonzero__(self):
        if self.x==0:
            return False
        else:
            return True

    def update(self,c):
        Moneyfmt.__init__(self,c)

foo=Moneyfmt(-0.25)
print foo










