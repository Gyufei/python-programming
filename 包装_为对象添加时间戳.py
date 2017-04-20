from time import time,ctime,sleep

class Ft(object):

    def __init__(self,obj):
        self.__this=obj
        self.__ctime=self.__atime=self.__mtime=time()

    def get(self):
        self.__atime=time()
        return self.__this

    def getime(self,tp):
        if isinstance(tp,str) and tp[0] in 'cma':
            return getattr(self,'_%s__%stime'%(self.__class__.__name__,tp[0]))
        else:
            raise TypeError,'object no such attribute'

    def gectime(self,tp):
        return ctime(self.getime(tp))

    def set(self,obj):
        self.__this=obj
        self.__mtime=self.__atime=time()

    def __str__(self):
        self.__atime=time()
        return str(self.__this)

    def __getattr__(self, item):
        self.__atime=time()
        return getattr(self.__this,item)

    def dl(self):
        l = {'-': '-' * 20, 'c': 'create', 'a': 'access', 'm': 'modify'}
        for i in l.keys():
            if i == '-':
                print l[i]
            else:
                print '%s: %s' % (l[i], self.gectime(i))


f=Ft(998)
print f
sleep(2)
f.dl()

print f.get()
f.dl()
sleep(2)

f.set([1,2,3,4,5,6])
print f
f.dl()
sleep(2)

f.append('+')
print f
f.dl()
sleep(2)

f.remove(2)
print f
f.dl()
