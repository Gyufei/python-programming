#coding=utf-8
from weakref import WeakKeyDictionary
class Sc(object):
    save={}     #Sc.save和self.data一样作用，两者选一即可
    def __init__(self):
        self.data=WeakKeyDictionary()

    def __get__(self, instance, owner):
        return Sc.save.get(instance)

    def __set__(self, instance, value):
        assert isinstance(value,int),'score is number'
        if value<0 or value>100:
            raise TypeError,'impassable score'
        Sc.save[instance]=value

class Scc(object):
    score=Sc()
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def __str__(self):
        return '%s : %s'%(self.name,self.score)


wang=Scc('wang',92)
li=Scc('li',67)
guo=Scc('wudi',99)
print wang.score
print li.score
print guo.score
wang.score=78
print wang.score


