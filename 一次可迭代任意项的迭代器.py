#coding=utf-8
class It(object):

    def __init__(self,seq,safe=False):
        #将序列转化为一个迭代器对象
        self.seq=iter(seq)
        self.safe=safe

    def __iter__(self):
        return self

    def next(self,n=1):
        res=[]
        for i in range(n):
            try:
                res.append(self.seq.next())#调用迭代器的next方法
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return res

s=range(100)
l=It(s,True)
for j in range(1,10):
    print j,':',l.next(j)






