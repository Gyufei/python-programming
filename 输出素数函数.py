#coding=utf-8
def prime(num):
    n=num/2
    while n>1:
        if num%n==0:
            break
        else:
            n-=1
    else:
        return num

print filter(prime,range(2,100))
