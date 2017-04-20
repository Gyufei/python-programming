class fib(object):

    def __init__(self):
        self.a,self.b=0,1

    def __iter__(self):
        return self

    def next(self):
            self.a,self.b=self.b,self.b+self.a
            if self.a>100000000:
               raise StopIteration
            return  self.a
for i in fib():
    print i
