# coding=utf-8
import sys
from collections import deque
from time import sleep

lamp=deque('>---------------') #deque是双端队列
while True:
    print '\r%s'%''.join(lamp)
    lamp.rotate(1)  #队列旋转1个位置
    sys.stdout.flush() #缓存全部输出，防止卡死
    sleep(0.5)    #暂停0.5秒

