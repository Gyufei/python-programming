#coding=utf-8
class Point(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return str((self.x,self.y))

from math import sqrt
class zx(Point):

    def __init__(self,a1=(0,0),b1=(0,0)):
        self.a1=a1
        self.b1=b1
        self.__l=None   #给描述符返回值一个初始值，从而定义它
        self.__s=None
        self.a1x=a1[0]
        self.a1y=a1[1]
        self.b1x=b1[0]
        self.b1y=b1[1]
        self.length=None   #给属性一个初始值，从而能够启动set
        self.slope=None

    @property
    def length(self):
        return self.__l

    @length.setter
    def length(self,value):
        if self.a1==self.b1 or self.a1x==self.b1x:
            self.__l=0
        else:
            self.__l=sqrt((self.a1x-self.b1x)**2+(self.a1y-self.b1y)**2)
        return self.__l

    @property
    def slope(self):
        return self.__s

    @slope.setter
    def slope(self,value):
        if self.a1==self.b1 or self.a1x==self.b1x:
            self.__s=None
        else:
            self.__s=float(self.b1y-self.a1y)/(self.b1x-self.a1x)
        return self.__s

    def __str__(self):
        return str(((self.a1x,self.a1y),(self.b1x,self.b1y)))


z=zx((2,8),(3,17))
print z
print z.length
print z.slope
