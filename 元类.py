#coding=UTF-8
"""定义了一个元类mete，使用元类创建的类属性都为大写."""
class mete(type):
    def __new__(cls, cname,cbase,class_atr):
        attr=((name,value) for name,value in class_atr.items() if not name.startswith('_'))
        upat=dict((name.upper(),value) for name,value in attr)
        return type(cls,cname,cbase,upat)
        # return type.__new__(cls,cname,cbase,upat)
        # return super(mete,cls).__new__(cls,cname,cbase,upat)

class sub():
    __metaclass__ = mete
    foo=123


t=sub()
print hasattr(t,'foo')

print hasattr(t,'FOO')

print t.FOO

