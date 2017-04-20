def bp(net):
    try:
        if isinstance(net,str):
            raise TypeError
        for zlb in net:
            for ys in bp(zlb):
                print 'get %s'%ys
    except TypeError:
        yield   net


l=[[1,2,3],'fear',[4,5,[7,3,4,[2,2,2]]],'aliswa',]
i=bp(l)
for l in i:
    print l
